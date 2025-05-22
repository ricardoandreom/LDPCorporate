import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def show_macrodata_tab(macro_ecb_df, unemployment_df, labour_prod_df, inflation_df, euribors_df):
    """

    """
    st.header("Macroeconomic data")

    ######################################################################################
    with st.expander("📊 Macroeconomic data", expanded=True):
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #179297; margin-bottom: 20px;">
        <h4 style="color: #179297; margin-top: 0;">Macroeconomics Overview</h4>
        <p>This section provides tools to analyze macroeconomic data and identify key trends and relationships. Use the following features to explore the data:</p>
        <ul>
        <li><strong>Data Preview:</strong> View the first few rows of the dataset for a quick overview.</li>
        <li><strong>Time Series Plots:</strong> Generate line plots for selected variables to observe trends over time.</li>
        <li><strong>Sector Analysis:</strong> Select specific sectors or variables to focus your analysis.</li>
        <li><strong>Correlation Matrix:</strong> Visualize relationships between variables using a triangular correlation heatmap.</li>
        </ul>
        <p>These tools are designed to help you uncover patterns and dependencies in the data, enabling better decision-making and insights into macroeconomic trends.</p>
        </div>
        """, unsafe_allow_html=True)


    # Seção de visualização de dados
    with st.expander("🔍 Data preview (first 3 rows)", expanded=False):
        st.dataframe(macro_ecb_df.head(3), use_container_width=True, hide_index=True)


    ################################################################

    with st.expander("📈 Time series plots", expanded=True):

        col1, col2 = st.columns(2)

        with col1:
            fig1 = px.line(
                unemployment_df,
                x="Date", 
                y="Unemployment rate", 
                title="Unemployment Rate over time",
                color_discrete_sequence=['#179297'],
                markers=True
            )
            fig1.update_traces(marker=dict(size=3))
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            euribors_melted = euribors_df.melt(
                id_vars=["Date"],
                value_vars=["Euribor 1M", "Euribor 3M", "Euribor 6M", "Euribor 1Y"], 
                var_name="Euribor Type",
                value_name="Rate" 
            )

            fig2 = px.line(
                euribors_melted,
                x="Date",
                y="Rate",
                color="Euribor Type", 
                markers=True,
                title="Euribor Rates over time",
                labels={"Rate": "Rate (%)", "Euribor Type": "Type"},
                color_discrete_sequence=[PRIMARY_COLORS[0], PRIMARY_COLORS[1], PRIMARY_COLORS[2], PRIMARY_COLORS[3]]  # Custom colors for the lines
            )

            fig2.update_layout(
                height=400,  
                margin=dict(l=20, r=20, t=40, b=20),
            )
            fig2.update_traces(marker=dict(size=3))

            st.plotly_chart(fig2, use_container_width=True)

        #######################################################################################
        
        col3, col4 = st.columns(2)

        with col3:
            fig3 = px.line(
                labour_prod_df,
                x="Date",
                y="Labour Productivity (per persons)", 
                title="Labour productivity over time",
                color_discrete_sequence=['#179297'],
                markers=True,
                labels={"Labour Productivity (per persons)": "Labour productivity"}
            )
            st.plotly_chart(fig3, use_container_width=True)

        ########################################################################################
        with col4:
            fig4 = px.line(
                inflation_df,
                x="Date",
                y=inflation_df.columns[1], 
                title="CPI over time",
                markers=True,
                color_discrete_sequence=['#179297'],
                labels={"CPI all-items (annual inflation rate)-12 month moving average": "Annual inflation rate-12M moving average"}
            )
            fig4.update_traces(marker=dict(size=3))
            st.plotly_chart(fig4, use_container_width=True)

        st.markdown("<hr>", unsafe_allow_html=True)

    ########################################################################################

    with st.expander("📊 Multiple time series plot", expanded=True):

        st.markdown(
        "<h2 style='color: #179297; text-align: center;'>Multiple time series plot</h2>",
        unsafe_allow_html=True
    )

        st.markdown(
            "<p style='font-size: 16px;'>Select the variables you want to include in the plot and correlation matrix:</p>",
            unsafe_allow_html=True
        )

        col10, col11, col12, col13 = st.columns(4)

        with col10:
            st.markdown("<h5 style='color: black;'>GDP and expenditure components</h5>", unsafe_allow_html=True)
            selected_gdp = st.multiselect(
                "Select the columns to plot:",
                options=MAP_CATEGORIES_ECB_INDICADORS["GDP and expenditure components"],
                default=MAP_CATEGORIES_ECB_INDICADORS["GDP and expenditure components"][:1]
            )

        with col11:
            st.markdown("<h5 style='color: black;'>Corporations</h5>", unsafe_allow_html=True)
            selected_corporations = st.multiselect(
                "Select the columns to plot:",
                options=MAP_CATEGORIES_ECB_INDICADORS["Corporations"],
                default=MAP_CATEGORIES_ECB_INDICADORS["Corporations"][:1]
            )

        with col12:
            st.markdown("<h5 style='color: black;'>Households</h5>", unsafe_allow_html=True)
            selected_households = st.multiselect(
                "Select the columns to plot:",
                options=MAP_CATEGORIES_ECB_INDICADORS["Households"],
                default=MAP_CATEGORIES_ECB_INDICADORS["Households"][:1]
            )

        with col13:
            st.markdown("<h5 style='color: black;'>Government finance statistics</h5>", unsafe_allow_html=True)
            selected_government = st.multiselect(
                "Select the columns to plot:",
                options=MAP_CATEGORIES_ECB_INDICADORS["Government finance statistics"],
                default=MAP_CATEGORIES_ECB_INDICADORS["Government finance statistics"][:1]
            )

        # Combine all selected columns
        all_selected_columns = selected_gdp + selected_corporations + selected_households + selected_government

        min_date, max_date = macro_ecb_df["Date"].min(), macro_ecb_df["Date"].max()
        selected_date_range = st.slider(
            "Select the date range:",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date), 
            step=1 
        )

        filtered_df = macro_ecb_df[
            (macro_ecb_df["Date"] >= selected_date_range[0]) &
            (macro_ecb_df["Date"] <= selected_date_range[1])
        ]
        minmax_normalize = st.checkbox("Apply Min-Max normalization")

        if all_selected_columns:
            df_to_plot = filtered_df.copy()

            # Aplicar normalização Min-Max se checkbox estiver marcado
            if minmax_normalize:
                df_to_plot[all_selected_columns] = (
                    df_to_plot[all_selected_columns] - df_to_plot[all_selected_columns].min()
                ) / (df_to_plot[all_selected_columns].max() - df_to_plot[all_selected_columns].min())

            # Transformar para formato longo
            filtered_df_melted = df_to_plot.melt(
                id_vars=["Date"], 
                value_vars=all_selected_columns, 
                var_name="Variable", 
                value_name="Value"
            )

            # Criar o gráfico
            fig5 = px.line(
                filtered_df_melted,
                x="Date",
                y="Value",
                color="Variable", 
                title="Selected Variables Over Time" + (" (Normalized)" if minmax_normalize else ""),
                markers=True,
                color_discrete_sequence=['#179297', EXTENDED_COLORS[1], EXTENDED_COLORS[2], EXTENDED_COLORS[3],
                                        EXTENDED_COLORS[4], EXTENDED_COLORS[5], EXTENDED_COLORS[6]],
                labels={"Value": "Normalized values" if minmax_normalize else "Value", "Date": "Date", "Variable": "Variable"}
            )

            fig5.update_layout(
                legend=dict(
                    orientation="h",          # horizontal
                    yanchor="top",
                    y=-0.2,                   # distância abaixo do gráfico (ajusta conforme necessário)
                    xanchor="center",
                    x=0.5
                )
            )


            st.plotly_chart(fig5, use_container_width=True)
        else:
            st.warning("Please select at least one variable to display.")

        st.markdown("<hr>", unsafe_allow_html=True)

        ##########################################################################################

        st.markdown(
            "<h2 style='color: #179297; text-align: center;'>Correlation Matrix</h2>",
            unsafe_allow_html=True
        )

        if len(all_selected_columns) > 1:
            if all_selected_columns:
                filtered_corr_df = macro_ecb_df[
                        (macro_ecb_df["Date"] >= selected_date_range[0]) &
                        (macro_ecb_df["Date"] <= selected_date_range[1])
                ][all_selected_columns]

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
                fig6.update_traces(textfont_size=24)

                fig6.update_layout(
                    xaxis=dict(tickfont=dict(size=14)),
                    yaxis=dict(tickfont=dict(size=14))
                )

                st.plotly_chart(fig6, use_container_width=True)
            else:
                st.warning("Please select at least one variable to calculate the correlation matrix.")