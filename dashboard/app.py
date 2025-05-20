import os
import numpy as np
import pandas as pd
import streamlit as st
from config import *
from get_data import *

from tabs.tab0_general_overview import *
from tabs.tab4_pca import * 
from tabs.tab1_macroeconomic_analysis import * 
from tabs.tab2_bpstat_analysis import * 
from tabs.tab3_concatdata_analysis import *

# Set page configuration
st.set_page_config(layout="wide", page_title="LDPs calibration dashboard")

start_date = '2006-01-01'

# Define function to load data
@st.cache_data
def load_data(ttl=3600*24):
    "Not needed right now because we are using the data from the repo"
    try:
        # macroeconomic data
        macro_ecb_data = process_ecb_indicators(MAP_CATEGORIES_ECB_INDICADORS_URLS, start_date=start_date) # annual data (number)
        
        df_unemployment = extract_data_from_ecb( # monthly data (start of period)
            MAP_OTHER_ECB_INDICATORS["Unemployment rate"]['url'].split("datasets/")[1].split('/')[1] ,
              start_date).rename(columns={''
              'TIME_PERIOD': 'Date',
              'OBS_VALUE': 'Unemployment rate'}) 

        df_labour_prod = extract_data_from_ecb( # quarterly data (start of period)
            MAP_OTHER_ECB_INDICATORS["Labour Productivity (per persons)"]['url'].split("datasets/")[1].split('/')[1],
              start_date).rename(
                columns={'TIME_PERIOD': 'Date',
                         'OBS_VALUE': 'Labour Productivity (per persons)'})  

        df_inflation = extract_data_from_bank_pt( # monthly data (end of period)
            MAP_OTHER_BPSTAT_INDICATORS["CPI (Consumer Price Index) MA12"]['url'], None) 
         
        df_euribors = extract_euribors(start_date) # monthly data (start of period)

        # LDPs data (Small companies)  
        df_small_ldp = get_ldp_data(SMALL_ENTREPRISE_MAP_INDICATORS_KEYS)
        
        # LDPs data (Medium companies)
        df_medium_ldp = get_ldp_data(MEDIUM_ENTREPRISE_MAP_INDICATORS_KEYS)
        # LDPs data (Large companies)
        df_large_ldp = get_ldp_data(LARGE_ENTREPRISE_MAP_INDICATORS_KEYS)
        # LDPs data (All companies)
        df_all_ldp= get_ldp_data(ALL_ENTREPRISE_MAP_INDICATORS_KEYS)

        return macro_ecb_data, df_unemployment, df_labour_prod, df_inflation, df_euribors, df_medium_ldp, df_large_ldp, df_small_ldp, df_all_ldp
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return empty dataframe if loading fails


# Load the data from the web
macro_ecb_data = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/macro_ecb_data.csv')
df_unemployment = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/unemployment_rate.csv')
df_unemployment['Date'] = pd.to_datetime(df_unemployment['Date'], errors='coerce')
df_labour_prod = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/labour_productivity.csv')
df_labour_prod['Date'] = pd.to_datetime(df_labour_prod['Date'], errors='coerce')
df_inflation = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/inflation_cpi_ma12.csv')
df_euribors = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/euribors.csv')
df_medium_ldp = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/medium_ldp.csv')
df_large_ldp = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/large_ldp.csv')
df_small_ldp = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/small_ldp.csv')
df_all_ldp = pd.read_csv('https://raw.githubusercontent.com/TRAVEL-GVM/Data/main/Data/LDP/all_ldp.csv')


# create anual data
def create_total_data(ldp):

    ldp_data = ldp.copy()
    ldp_data['Date'] = pd.to_datetime(ldp_data['Date']).dt.year

    df_unemployment_dec = df_unemployment[df_unemployment['Date'].dt.month == 12]
    df_unemployment_dec['Date'] = df_unemployment_dec['Date'].dt.year

    df_labour_prod_dec = df_labour_prod[df_labour_prod['Date'].dt.month == 1]
    df_labour_prod_dec['Date'] = df_labour_prod_dec['Date'].dt.year - 1

    df_inflation_dec = df_inflation.copy()
    df_inflation_dec['Date'] = pd.to_datetime(df_inflation_dec['Date'])
    df_inflation_dec = df_inflation_dec[df_inflation_dec['Date'].dt.month == 12]
    df_inflation_dec['Date'] = df_inflation_dec['Date'].dt.year

    df_euribors_dec = df_euribors.copy()
    df_euribors_dec['Date'] = pd.to_datetime(df_euribors_dec['Date'])
    df_euribors_dec = df_euribors_dec[df_euribors_dec['Date'].dt.month == 12]
    df_euribors_dec['Date'] = df_euribors_dec['Date'].dt.year

    annual_data = macro_ecb_data.merge(ldp_data, on='Date', how='left')
    annual_data = annual_data.merge(df_unemployment_dec, on='Date', how='left')
    annual_data = annual_data.merge(df_labour_prod_dec, on='Date', how='left')
    annual_data = annual_data.merge(df_inflation_dec, on='Date', how='left')
    annual_data = annual_data.merge(df_euribors_dec, on='Date', how='left')

    ### only macrodata total
    total_macrodata = macro_ecb_data.merge(df_unemployment_dec, on='Date', how='left')
    total_macrodata = total_macrodata.merge(df_labour_prod_dec, on='Date', how='left')
    total_macrodata = total_macrodata.merge(df_inflation_dec, on='Date', how='left')
    total_macrodata = total_macrodata.merge(df_euribors_dec, on='Date', how='left')

    return annual_data, total_macrodata

# Create dashboard title and introduction
st.image("design docs/travel.webp",width=250)

st.markdown(
    """
    <h3 style='color: #179297;'>Company type selection</h3>
    """,
    unsafe_allow_html=True
)

# Add a selectbox for company type selection
company_type = st.selectbox(
    "Select the type of companies to analyze:",
    ["Small", "Medium", "Large", "All"]
)

# Set file path based on company type
if company_type == "All":
    df_ldp = df_all_ldp.copy()
    total_data = create_total_data(df_ldp)[0]
    macrodata_total = create_total_data(df_ldp)[1]
    cols_sector = all_companies_all_columns

elif company_type == "Small":
    df_ldp = df_small_ldp.copy()
    total_data = create_total_data(df_ldp)[0]
    macrodata_total = create_total_data(df_ldp)[1]
    cols_sector = small_all_columns

elif company_type == "Medium":
    df_ldp = df_medium_ldp.copy()
    total_data = create_total_data(df_ldp)[0]
    macrodata_total = create_total_data(df_ldp)[1]
    cols_sector = medium_all_columns

elif company_type == "Large":
    # fazer update para large
    df_ldp = df_large_ldp.copy()
    total_data = create_total_data(df_ldp)[0]
    macrodata_total = create_total_data(df_ldp)[1]
    cols_sector = large_all_columns


# Create tabs
tab0, tab1, tab2, tab3, tab4 = st.tabs([
    "General overview", 
    "Macroeconomic data analysis", 
    "BPSTAT data analysis", 
    "Macroeconomic data vs Risk drivers",
    "Principal Components Analysis"
])

with tab0:
    show_visao_geral_tab(df_unemployment, df_euribors, macro_ecb_data, df_labour_prod, df_inflation, df_ldp, company_type)

with tab1:
    show_macrodata_tab(
        macro_ecb_data, df_unemployment, df_labour_prod, df_inflation, df_euribors
    )

with tab2:
    show_bpstat_tab(df_ldp, cols_sector)

with tab3:
    show_macro_vs_riskdrivers_tab(total_data, macrodata_total, cols_sector)

with tab4:
    plot_pca_results_tab(df_ldp, macrodata_total, cols_sector)