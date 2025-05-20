import json
import sys
from pathlib import Path
from get_data import convert_df_to_excel
import folium
import plotly.express as px
import pandas as pd
import streamlit as st
import xlsxwriter 


# Add the parent directory to system path
sys.path.append(str(Path(__file__).parent.parent))
from config import BACKGROUND_COLORS, TEXT_COLORS


def show_visao_geral_tab(unemployment_df, euribors_df, macro_ecb_df, labour_prod_df, inflation_df, ldp_df, type_company):
    """
    """

    # overview metrics
    desemprego_atual = unemployment_df["Unemployment rate"].iloc[-1]
    desemprego_ano_anterior = unemployment_df["Unemployment rate"].iloc[-13]
    var_desemprego = 100 * (desemprego_atual - desemprego_ano_anterior) / desemprego_ano_anterior

    euribor_atual = euribors_df["Euribor 1Y"].iloc[-1]
    euribor_ano_anterior = euribors_df["Euribor 1Y"].iloc[-13]
    var_euribor = 100 * (euribor_atual - euribor_ano_anterior) / euribor_ano_anterior

    pib_df = macro_ecb_df[['Date', 'Gross domestic product at market prices']]
    pib_atual = pib_df["Gross domestic product at market prices"].iloc[-1]
    pib_ano_anterior = pib_df["Gross domestic product at market prices"].iloc[-2]
    var_pib = 100 * (pib_atual - pib_ano_anterior) / pib_ano_anterior

    labour_atual = labour_prod_df["Labour Productivity (per persons)"].iloc[-1]
    labour_ano_anterior = labour_prod_df["Labour Productivity (per persons)"].iloc[-13]
    var_labour = 100 * (labour_atual - labour_ano_anterior) / labour_ano_anterior

    inflation_atual = inflation_df["CPI all-items (annual inflation rate)-12 month moving average"].iloc[-1]

    # Header and Key Metrics Row with enhanced styling
    st.markdown(
        """
    <style>
    .metric-card {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 15px;
        margin: 5px 0px 5px 0px;
        text-align: center;
        justify-content: center;
        height: 100%;
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #179297;
        margin: 5px 0;
    }
    .metric-label {
        font-size: 16px;
        color: #179297;
        margin-bottom: 10px;
    }
    .metric-icon {
        font-size: 32px;
        color: #179297;
        margin-top: 5px;
    }
    .section-divider {
        height: 2px;
        background: linear-gradient(to right, #e8f5e9, #179297, #e8f5e9);
        margin: 30px 0 20px 0;
        border-radius: 2px;
    }    
    .section-divider-space{
        margin: 30px 0 20px 0;
    }
    .header-title {
        color: #179297;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .header-subtitle {
        color: #179297; 
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .info-card {
        background-color: #f1f8e9;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    .info-card-2 {
        background-color: #f1f8e9; 
        padding: 15px; 
        border-radius: 8px; 
        margin-bottom: 20px; 
        border-left: 4px solid #66bb6a;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.header("General overview - 1Y relative difference")    

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">Unemployment rate 12M relative difference</div>
            <div class="metric-value">
                {var_desemprego:.2f}% {"🠗" if var_desemprego < 0 else "↑"}
            </div>
            <div class="metric-icon">🧑‍💼❌</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">EURIBOR 12M relative difference</div>
            <div class="metric-value">
                {var_euribor:.1f}% {"🠗" if var_euribor < 0 else "↑"}
            </div>
            <div class="metric-icon">💶📉🏠</div>
        </div>
        """,
            unsafe_allow_html=True,
            )

    with col3:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">GDP 12M relative difference</div>
            <div class="metric-value">{var_pib:.2f}% {"🠗" if var_pib < 0 else "↑"}
            </div>
            <div class="metric-icon">🌍📉</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">CPI 12M Moving Average</div>
            <div class="metric-value">{inflation_atual:.1f}%</div>
            <div class="metric-icon">🧺📈</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col5:
        st.markdown(
            f"""
        <div class="metric-card">
            <div class="metric-label">Labour productivity 12M relative difference</div>
            <div class="metric-value">
                {var_labour:.1f}% {"🠗" if var_labour < 0 else "↑"}
            </div>
            <div class="metric-icon">🧑‍🏭📉</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Add a styled divider and enhanced text
    st.markdown(
        """
    <div class="section-divider-space"></div>
    """,
        unsafe_allow_html=True,
    )


    st.markdown("<hr>", unsafe_allow_html=True)

    unemployment_df_ = unemployment_df.copy()
    unemployment_df_['Date'] = pd.to_datetime(unemployment_df_['Date']).dt.date  

    labour_prod_df_ = labour_prod_df.copy()
    labour_prod_df_['Date'] = pd.to_datetime(labour_prod_df_["Date"]).dt.date

    ldp_df_ = ldp_df.copy()
    ldp_df_['Date'] = pd.to_datetime(ldp_df_['Date']).dt.date

    with st.expander("Original Macro economic data — Non annual data - Expand to view and download", expanded=True):

        col20, col21, col22, col23 = st.columns(4)

        with col20:

            st.markdown(
                """
            <div class="header-title">Unemployment rate</div>
            """,
                unsafe_allow_html=True,
            )
            st.dataframe(unemployment_df_, use_container_width=True, hide_index=True)
            st.download_button(label="Download in xlsx format",
                                data=convert_df_to_excel(unemployment_df_),
                                file_name='cpi.xlsx',
                                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        with col21:
            st.markdown(
                """
            <div class="header-title">Inflation rate</div>
            """,
                unsafe_allow_html=True,
            )
            st.dataframe(inflation_df, use_container_width=True, hide_index=True)
            st.download_button(label="Download in xlsx format",
                                data=convert_df_to_excel(inflation_df),
                                file_name='inflation.xlsx',
                                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        
        with col22:
            st.markdown(
                """
            <div class="header-title">Labour productivity</div>
            """,
                unsafe_allow_html=True,
            )
            st.dataframe(labour_prod_df_, use_container_width=True, hide_index=True)
            st.download_button(label="Download in xlsx format",
                                data=convert_df_to_excel(labour_prod_df_),
                                file_name='labour.xlsx',
                                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        with col23:

            st.markdown(
                """
            <div class="header-title">Euribor rates</div>
            """,
                unsafe_allow_html=True,
            )
            st.dataframe(euribors_df, use_container_width=True, hide_index=True)
            st.download_button(label="Download in xlsx format",
                                data=convert_df_to_excel(euribors_df),
                                file_name='euribors.xlsx',
                                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            
    with st.expander("Original Macro economic data — Annual data - Expand to view and download", expanded=True):
        st.markdown(
                """
            <div class="header-title">Annual Macroeconomic data</div>
            """,
                unsafe_allow_html=True,
            )
        
        st.dataframe(macro_ecb_df, use_container_width=True, hide_index=False)

        st.download_button(label="Download in xlsx format",
                                data=convert_df_to_excel(macro_ecb_df),
                                file_name='macroeconomic_ecb.xlsx',
                                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


    with st.expander("Original BPSTAT - Expand to view and download", expanded=True):
        st.markdown(
                f"""
            <div class="header-title">{type_company} BPSTAT data</div>
            """,
                unsafe_allow_html=True,
            )
        #ldp_ = ldp_df.copy()
        #ldp_['Date'] = pd.to_datetime(ldp_['Date']).dt.date
        st.dataframe(ldp_df_, use_container_width=True, hide_index=False)

        st.download_button(label="Download in xlsx format",
                                data=convert_df_to_excel(ldp_df_),
                                file_name='ldp.xlsx',
                                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

