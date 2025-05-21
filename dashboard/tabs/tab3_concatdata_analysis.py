import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def show_macro_vs_riskdrivers_tab(df_total, df_macro, cols_sector):
    """

    """

    with st.expander("📊 Analysis Overview", expanded=True):
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #179297; margin-bottom: 20px;">
        <h4 style="color: #179297; margin-top: 0;">Macroeconomic data vs Risk drivers</h4>
        <p>This section provides tools to analyze macroeconomic data vs BPSTAT data and identify key trends and relationships. Use the following features to explore the data:</p>
        <ul>
        <li><strong>Data Preview:</strong> View the first few rows of the dataset for a quick overview.</li>
        <li><strong>Time Series Plots:</strong> Generate line plots for selected variables to observe trends over time.</li>
        <li><strong>Sector Analysis:</strong> Select specific sectors or variables to focus your analysis.</li>
        <li><strong>Correlation Matrix:</strong> Visualize relationships between variables using a triangular correlation heatmap.</li>
        </ul>
        <p>These tools are designed to help you uncover patterns and dependencies in the data, enabling better decision-making and insights into macroeconomic trends.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔍 Data Preview (first 3 rows)", expanded=False):
        st.write("Preview of the dataset:")
        st.dataframe(df_total)

    with st.expander("📈 Time Series Plots", expanded=True):
        st.write("Select variables to plot:")

        col1, col2 = st.columns(2)
        with col1:
            selected_macro = st.multiselect(
            "Select which macroeconomics you want for the PCA analysis?",
            options=df_macro.columns[1:], default=df_macro.columns[1:5], key="selected_macrodata"
            )
        with col2:
            # Add a selectbox for sector selection
            sectorx = st.selectbox(
                "Select the business sector to analyze:",
                ldp_sectors, index=0, key="sectorx")
            
            if sectorx == 'All':
                selected_bpstat = cols_sector
                df_filtered = df_total[selected_bpstat]
            else:
                df_filtered = df_total.filter(like=sectorx)

                if 'Date' not in df_filtered.columns:
                    df_filtered['Date'] = df_total['Date']
                    df_filtered = df_filtered[['Date'] + [col for col in df_filtered.columns if col != 'Date']]

            
            bpstat_sector = st.multiselect(
                "Select the bpstat sectors to analyze:",
                options=df_filtered.columns[1:].tolist(), default=df_filtered.columns[1:5].tolist(), key="bpstat_sector")

            plot_cols = ['Date'] + bpstat_sector + selected_macro 

        min_date, max_date = df_total["Date"].min(), df_total["Date"].max()
        selected_date_range = st.slider(
            "Select the date range:",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date), 
            step=1, key='acb'
        )

        df_total = df_total[
            (df_total["Date"] >= selected_date_range[0]) &
            (df_total["Date"] <= selected_date_range[1])
        ]
        
        # Add a checkbox to normalize the data
        normalize_data = st.checkbox("Normalize variables for the plot", value=False)

        df_plot = df_total[plot_cols]

        if normalize_data:
            # Normalize the data (excluding the 'Date' column)
            df_plot[df_plot.columns[1:]] = (df_plot[df_plot.columns[1:]] - df_plot[df_plot.columns[1:]].min()) / (
                df_plot[df_plot.columns[1:]].max() - df_plot[df_plot.columns[1:]].min()
            )
            st.write("Variables have been normalized using Min-Max scaling.")   

        st.dataframe(df_plot.tail(5), hide_index=True)
        
        # Botão para ativar normalização Min-Max
        normalize = st.checkbox("Apply Min-Max normalization", key='ptk')

        # Copiar o DataFrame original
        df_plot_processed = df_plot.copy()

        # Aplicar Min-Max se checkbox estiver ativado
        if normalize:
            df_plot_processed[plot_cols] = (
                df_plot_processed[plot_cols] - df_plot_processed[plot_cols].min()
            ) / (df_plot_processed[plot_cols].max() - df_plot_processed[plot_cols].min())

        # Criar o gráfico de linha
        fig = px.line(
            df_plot_processed,
            x='Date',
            y=plot_cols,
            title=f"Time series plot for {sectorx} companies and Macroeconomic Variables" + (" (Normalizado)" if normalize else "")
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Valores Normalized" if normalize else "Values",
            legend_title="Variables",
            hovermode="x unified"
        )
        fig.update_traces(mode='lines+markers')

        # Mostrar gráfico
        st.plotly_chart(fig, use_container_width=True)


    with st.expander("📊 Correlation Matrix", expanded=True):

        st.markdown(
            "<h2 style='color: #179297; text-align: center;'>Correlation Matrix</h2>",
            unsafe_allow_html=True
        )
        st.write("Visualize relationships between variables:")

        if len(plot_cols) > 1:
            if plot_cols:
                df_corr = df_total[plot_cols[1:]]

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
                fig6.update_traces(textfont_size=18)


                fig6.update_layout(
                    xaxis=dict(tickfont=dict(size=14)),
                    yaxis=dict(tickfont=dict(size=14))
                )

                st.plotly_chart(fig6, use_container_width=True)
            else:
                st.warning("Please select at least one variable to calculate the correlation matrix.")

