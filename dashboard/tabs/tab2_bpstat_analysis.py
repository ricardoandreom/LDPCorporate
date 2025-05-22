import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def show_bpstat_tab(df, cols_sector):
    """

    """

    ########################################################################################
    st.header("Risk drivers")

    with st.expander("📊 Analysis Overview", expanded=True):
    
        # Start with a compelling problem statement
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #179297; margin-bottom: 20px;">
        <h4 style="color: #179297; margin-top: 0;">Analysis Overview</h4>
        <p>This section provides an in-depth analysis of key risk drivers across various business sectors. Use the tools below to explore trends, correlations, and normalized data for better insights:</p>
        <ul>
        <li><strong>Sector Selection:</strong> Choose a specific business sector or analyze all sectors combined.</li>
        <li><strong>Data Visualization:</strong> Generate line plots for single or multiple variables to observe trends over time.</li>
        <li><strong>Normalization:</strong> Optionally normalize variables to compare data on a standardized scale.</li>
        <li><strong>Correlation Matrix:</strong> Identify relationships between selected variables using a triangular correlation heatmap.</li>
        </ul>
        <p>These tools are designed to help you uncover patterns and dependencies that drive business risks, enabling more informed decision-making.</p>
        </div>
        """, unsafe_allow_html=True)

    ############################################################################################

    # Add a selectbox for sector selection
    sector = st.selectbox(
        "Select the business sector to analyze:",
        ldp_sectors, index=0)
    
    if sector == 'All':
        df_filtered = df[cols_sector]
    else:
        df_filtered = df.filter(like=sector)
        if 'Date' not in df_filtered.columns:
            df_filtered['Date'] = df['Date']
            df_filtered = df_filtered[['Date'] + [col for col in df_filtered.columns if col != 'Date']]

    # Seção de visualização de dados
    with st.expander("🔍 Data preview", expanded=False):
        st.dataframe(df_filtered, use_container_width=True, hide_index=True)
    
    ##########################################################################################################


    st.markdown(
        "<p style='font-size: 16px;'>Select the variables you want to include in the plot and correlation matrix:</p>",
        unsafe_allow_html=True
    )

    selected_columns_monoplot = st.multiselect(
        "Select the columns to make a one variable line plot:",
        options=df_filtered.columns[1:],
        default=df_filtered.columns[4])
    
    selected_columns_mutliplot = st.multiselect(
        "Select the columns to plot in the multivariable line plot:",
        options=df_filtered.columns[1:],
        default=df_filtered.columns[4:7])
    
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.line(
            df_filtered,
            x="Date", 
            y=selected_columns_monoplot, 
            title=f"{selected_columns_monoplot[0]} over time",
            color_discrete_sequence=['#179297'],
            markers=True
        )
        fig1.update_layout(
            legend=dict(
                orientation="h",          # horizontal
                yanchor="top",
                y=-0.2,                   # distância abaixo do gráfico (ajusta conforme necessário)
                xanchor="center",
                x=0.5
            )
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        normalize = st.checkbox("Normalize variables", value=False)

        if normalize:
            df_normalized = df_filtered.copy()
            columns_to_normalize = [col for col in df_filtered.columns if col != "Date"]
            df_normalized[columns_to_normalize] = (df_filtered[columns_to_normalize] - df_filtered[columns_to_normalize].mean()) / df_filtered[columns_to_normalize].std()
        else:
            df_normalized = df_filtered

        multiplot = pd.melt(
            df_normalized,
            id_vars=["Date"], 
            value_vars=selected_columns_mutliplot,  
            var_name="Variable",  
            value_name="Value"  
        )

        fig2 = px.line(
            multiplot,
            x="Date",
            y="Value",
            markers=True,
            color="Variable",
            title="Selected Variables Over Time",
            labels={"Value": "Value", "Date": "Time", "Variable": "Variable"},
            color_discrete_sequence=['#179297', '#FF5733', '#33FF57', '#3357FF']  
        )

        fig2.update_layout(
            height=400,  
            margin=dict(l=20, r=20, t=40, b=20) 
        )

        fig2.update_layout(
            legend=dict(
                orientation="h",          # horizontal
                yanchor="top",
                y=-0.2,                   # distância abaixo do gráfico (ajusta conforme necessário)
                xanchor="center",
                x=0.5
            )
        )

        st.plotly_chart(fig2, use_container_width=True)

    #######################################################################################

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        "<h2 style='color: #179297; text-align: center;'>Correlation Matrix</h2>",
        unsafe_allow_html=True
    )

    selected_columns_corr = st.multiselect(
        "Select the columns to the correlation matrix:",
        options=df_filtered.columns[1:],
        default=df_filtered.columns[4:12])

    # Garantir formato datetime e remover hora
    df_filtered["Date"] = pd.to_datetime(df_filtered["Date"])

    min_date = df_filtered["Date"].min().date()
    max_date = df_filtered["Date"].max().date()

    selected_date_range = st.slider(
        "Select the date range:",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
        step=pd.Timedelta(days=1),
        key="date_slider"
    )

    import datetime

    # Converter selected_date_range para datetime.datetime antes da comparação
    start_date = datetime.datetime.combine(selected_date_range[0], datetime.datetime.min.time())
    end_date = datetime.datetime.combine(selected_date_range[1], datetime.datetime.min.time())

    # Aplicar filtro
    df_filtered = df_filtered[
        (df_filtered["Date"] >= start_date) & 
        (df_filtered["Date"] <= end_date)
    ]


    if len(selected_columns_corr) > 1:
        if selected_columns_corr:
            filtered_corr_df = df_filtered[selected_columns_corr]

            corr_matrix = filtered_corr_df.corr()

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

            fig6.update_traces(textfont_size=20)
            fig6.update_layout(
                    xaxis=dict(tickfont=dict(size=14)),
                    yaxis=dict(tickfont=dict(size=14))
            )

            st.plotly_chart(fig6, use_container_width=True)
        else:
            st.warning("Please select at least one variable to calculate the correlation matrix.")
