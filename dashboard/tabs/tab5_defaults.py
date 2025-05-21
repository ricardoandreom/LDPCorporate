import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import streamlit as st
from datetime import datetime
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tools.sm_exceptions import InfeasibleTestError
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

    with st.expander("📊 Defaults Analysis", expanded=False):

        #st.dataframe(df_def)
        def_group = df_def.groupby('Date').agg(agg_cols).reset_index()
        #st.dataframe(def_group)

        #st.title("Defaults analysis over time")
        st.markdown(
            "<h2 style='color: #179297; text-align: center;'>Defaults analysis over time</h2>",
            unsafe_allow_html=True
        )

        # Excluir 'Date' da seleção
        variables = [col for col in def_group.columns if col != 'Date']
        selected_vars = st.multiselect("Select the variables for the plot:", variables, default=['EXPOSIÇÃO NPL', 'EXPOSIÇÃO BONS'])

        # Botão para normalizar
        normalize = st.checkbox("Min-Max Normalization", key="minmax_2")

        # Filtrar e normalizar se necessário
        if selected_vars:
            df_plot = def_group[['Date'] + selected_vars].copy()

            if normalize:
                scaler = MinMaxScaler()
                df_plot[selected_vars] = scaler.fit_transform(df_plot[selected_vars])

            # Plot com Plotly
            df_melted = df_plot.melt(id_vars='Date', value_vars=selected_vars,
                                    var_name='Variable', value_name='Value')

            fig = px.line(df_melted, x='Date', y='Value', color='Variable',
                        title="Selected variables over time")

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Select at one variable for the plot.")
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


        col5, col6 = st.columns(2)

        with col5:

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

            with col6:
                st.write("🔎 Preview data:")
                st.dataframe(df_totalx, hide_index=True)

        # test granger entre 2 variaveis à do df
        st.markdown(
                "<h2 style='color: #179297; text-align: center;'>Causality between variables - Granger test</h2>",
                unsafe_allow_html=True
            )
        
        df_granger = df_total.merge(def_group, on='Date', how='inner')
        
        variables_granger = [col for col in df_granger.columns if col != 'Date']

        col8, col9 = st.columns(2)

        with col8:
            # Seleção de variáveis
            var1 = st.selectbox("Choose the 'causable' variable (X):", variables_granger, index=variables_granger.index('Unemployment rate'))
            var2 = st.selectbox("Choose the variable affected (Y):", variables_granger, index=variables_granger.index('Gross domestic product at market prices'))

            # Seleção de número de lags
            max_lag = st.slider("Choose the max number of lags:", min_value=1, max_value=4, value=4)

        with col9:
            if var1 and var2 and var1 != var2:
                # Preparar os dados
                test_df = df_granger[[var2, var1]].dropna()

                # Converter para float e garantir que não há constantes
                test_df = test_df.astype(float)

                if test_df.nunique().min() <= 1:
                    st.warning("Uma das variáveis tem valores constantes. O teste de Granger requer variabilidade nas séries.")
                else:
                    try:
                        # Executar o teste de Granger
                        st.write(f"**Granger test: `{var1}` causes `{var2}`?**")
                        st.write("Raw test results:")
                        granger_result = grangercausalitytests(test_df, maxlag=max_lag, verbose=True)

                        # Extrair e exibir os p-valores
                        pvals = {
                            lag: res[0]['ssr_ftest'][1]
                            for lag, res in granger_result.items()
                        }

                        pval_df = pd.DataFrame.from_dict(pvals, orient='index', columns=['p-value'])
                        pval_df.index.name = 'Lag'
                        st.dataframe(pval_df.style.background_gradient(cmap='Greens', axis=0))

                        # Interpretação
                        significant = pval_df['p-value'] < 0.05
                        if significant.any():
                            best_lag = significant.idxmax()
                            st.success(f"There is significant evidence of Granger causality from `{var1}` to `{var2}` at lag {best_lag}.")
                        else:
                            st.warning(f"No significant Granger causality found from `{var1}` to `{var2}`.")

                    except InfeasibleTestError:
                        st.warning("Error: One of the variables has constant values or theres is dependent linearity, which is not  allowed in Granger test.")
                    except Exception as e:
                        st.error(f"Unexpected error: {e}")
            else:
                st.info("Select two different variables to apply the Granger causality test.")

        # correlação cruzada
        st.markdown(
                "<h2 style='color: #179297; text-align: center;'>Cross correlation plot</h2>",
                unsafe_allow_html=True
        )

        # Número de lags (defasagens)
        max_lag = st.slider("Select the maximum number of lags:", min_value=1, max_value=10, value=8)

        if var1 and var2 and var1 != var2:
            series_x = df_granger[var1].dropna().astype(float)
            series_y = df_granger[var2].dropna().astype(float)

            # Garantir que ambas as séries têm variabilidade
            if series_x.nunique() <= 1 or series_y.nunique() <= 1:
                st.warning("One of the variables has constant values. Cross correlation cannot be computed.")
            else:
                # Padronizar as séries (opcional, mas melhora o resultado da correlação)
                x = (series_x - series_x.mean()) / series_x.std()
                y = (series_y - series_y.mean()) / series_y.std()

                # Calcular correlação cruzada para lags de -max_lag até +max_lag
                lags = np.arange(-max_lag, max_lag + 1)
                ccf_values = [x.corr(y.shift(lag)) for lag in lags]

                lags = np.arange(-max_lag, max_lag + 1)
                ccf_values = [x.corr(y.shift(lag)) for lag in lags]

                # Interpretação automática
                max_corr_idx = np.nanargmax(np.abs(ccf_values))
                best_lag = lags[max_corr_idx]
                best_corr = ccf_values[max_corr_idx]

                interpretation = (
                    f"🔎 **Highest correlation at lag {best_lag}:** {best_corr:.2f}.<br>"
                    f"{'🡺 ' + var1 + ' may lead ' + var2 if best_lag > 0 else '🡸 ' + var2 + ' may lead ' + var1 if best_lag < 0 else '⏸️ No temporal lead-lag detected. Theres is no evidence that one variable anticipates the other or the other following the other one in time.'}"
                )

                # Criar gráfico em Plotly
                fig = go.Figure()
                fig.add_trace(go.Bar(x=lags, y=ccf_values, marker_color='seagreen'))
                fig.update_layout(
                    title=f'Cross-Correlation between {var1} and {var2}',
                    xaxis_title='Lag',
                    yaxis_title='Correlation',
                    template='plotly_white'
                )

                st.plotly_chart(fig, use_container_width=True)
                st.markdown(interpretation, unsafe_allow_html=True)
        else:
            st.info("Select two different variables to compute cross-correlation.")


    with st.expander("📊 Economic variables vs Defaults analysis over time", expanded=False):

        #st.title("Economic variables vs Defaults analysis over time")
        st.markdown(
            "<h2 style='color: #179297; text-align: center;'>Economic variables vs Defaults analysis over time</h2>",
            unsafe_allow_html=True
        )

        df_plot_def = df_total.merge(def_group, on='Date', how='inner')

        # Excluir 'Date' da seleção
        variablesx = [col for col in df_plot_def.columns if col != 'Date']
        selected_varsx = st.multiselect("Select the variables for the plot:", variablesx, default=['EXPOSIÇÃO NPL', 'EXPOSIÇÃO BONS', 'Gross domestic product at market prices'])

        # Botão para normalizar
        normalizex = st.checkbox("Min-Max Normalization", key="minmax_1")

        # Filtrar e normalizar se necessário
        if selected_vars:
            df_plotx = df_plot_def[['Date'] + selected_varsx].copy()

            if normalizex:
                scaler = MinMaxScaler()
                df_plotx[selected_varsx] = scaler.fit_transform(df_plotx[selected_varsx])

            # Plot com Plotly
            df_meltedx = df_plotx.melt(id_vars='Date', value_vars=selected_varsx,
                                    var_name='Variable', value_name='Value')

            figx = px.line(df_meltedx, x='Date', y='Value', color='Variable',
                        title="Selected variables over time")

            st.plotly_chart(figx, use_container_width=True, key='final_plot')
        else:
            st.info("Select at one variable for the plot.")
    #########################################################################

    
