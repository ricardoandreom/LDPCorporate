import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import streamlit as st
from datetime import datetime
from config import *

def tab_defaults(defaults, df, df_macro, cols_sector):

    def_cols = [
        "dtref", "Date", "MODELO", "SEGMENTO", "# OBS", "# BONS", "# NPL", "# DEFAULTS 12M", "EXPOSIÇÃO", "EXPOSIÇÃO BONS",
        "EXPOSIÇÃO NPL", "NOVOS DEFAULTS", "DEFAULTS TÉCNICOS", "DEFAULTS REAIS", "DEFAULTS EXCLUSÕES", "#1º DEF"
            ]
    
    defaults['dtref'] = pd.to_datetime(defaults['dtref'], errors='coerce')  # Garante que é datetime
    defaults['Date'] = defaults['dtref'].dt.year  # Extrai apenas o ano

    df_def = defaults[
        (defaults['AMBITO_IRB'] == 1)
    ][def_cols]

    df_def['dtref'] = pd.to_datetime(df_def['dtref'], errors='coerce')  # Garante que é datetime
    df_def['Date'] = df_def['dtref'].dt.year  # Extrai apenas o ano

    with st.expander("Defaults Analysis", expanded=False):

        #st.dataframe(df_def)
        def_group = df_def.groupby('Date').agg(agg_cols).reset_index()
        #st.dataframe(def_group)


        st.title("Gráfico de Linhas com Normalização Min-Max")

        # Excluir 'Date' da seleção
        variables = [col for col in def_group.columns if col != 'Date']
        selected_vars = st.multiselect("Selecione as variáveis para o gráfico:", variables)

        # Botão para normalizar
        normalize = st.checkbox("Normalizar com Min-Max")

        # Filtrar e normalizar se necessário
        if selected_vars:
            df_plot = def_group[['Date'] + selected_vars].copy()

            if normalize:
                scaler = MinMaxScaler()
                df_plot[selected_vars] = scaler.fit_transform(df_plot[selected_vars])

            # Plot com Plotly
            df_melted = df_plot.melt(id_vars='Date', value_vars=selected_vars,
                                    var_name='Variável', value_name='Valor')

            fig = px.line(df_melted, x='Date', y='Valor', color='Variável',
                        title="Gráfico de Linhas das Variáveis Selecionadas")

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Selecione pelo menos uma variável para visualizar o gráfico.")
    #########################################################################

    with st.expander("📊 Economic variables vs defaults", expanded=True):

        col100, col101 = st.columns(2)
        with col100:
            # Add a selectbox for sector selection with a unique key
            sector = st.selectbox(
                "Select the business sector to analyze:",
                ldp_sectors, index=0, key="sector_selectbox_tab1x"
            )
            
        if sector == 'All':
            df_filtered = df[cols_sector]
        else:
            df_filtered = df.filter(like=sector)
            if 'Date' not in df_filtered.columns:
                df_filtered['Date'] = df['Date']
                df_filtered = df_filtered[['Date'] + [col for col in df_filtered.columns if col != 'Date']]
        
        df_filtered['Date'] = pd.to_datetime(df_filtered['Date'], errors='coerce')
        df_filtered = df_filtered[df_filtered['Date'].dt.month == 12]
        df_filtered['Date'] = df_filtered['Date'].dt.year

        df_total = df_filtered.merge(df_macro, on='Date', how='left')

        col2, col3 = st.columns(2)

        with col2:
            selected_macro = st.multiselect(
                    "Select which macroeconomics you want for the correlation analysis?",
                    options=df_total.columns[1:], default=df_total.columns[1:5], key="selected_macroxy"
                )
        with col3:
            selected_def_cols = st.multiselect(
                    "Select which default columns you want for the correlation analysis?",
                    options=def_group.columns[1:], default=def_group.columns[1:4], key="selected_macroxzy"
                )

        df_totalx = df_total[['Date'] + selected_macro].merge(def_group[["Date"] + selected_def_cols], on='Date', how='inner')


        # correlation matrix
        st.markdown(
            "<h2 style='color: #179297; text-align: center;'>Correlation Matrix</h2>",
            unsafe_allow_html=True
        )

        st.write("Visualize relationships between variables:")

        plot_cols = list(df_totalx.columns)[1:]

        if len(plot_cols) > 1:
            if plot_cols:
                df_corr = df_totalx[plot_cols]

                corr_matrix = df_corr.corr()

                mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

                corr_matrix_masked = corr_matrix.where(~mask)

                fig6 = px.imshow(
                    corr_matrix_masked,
                    color_continuous_scale='Greens',
                    aspect='auto',
                    labels=dict(x="", y="", color="Correlation"),
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    text_auto=".2f" 
                )

                fig6.update_layout(
                width=600,  
                height=600,  
                margin=dict(l=50, r=50, t=50, b=50)  
            )

                st.plotly_chart(fig6, use_container_width=True)
            else:
                st.warning("Please select at least one variable to calculate the correlation matrix.")

        # test granger entre 2 variaveis


        # correlação cruzada


        st.dataframe(df_totalx)
