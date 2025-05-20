import pandas as pd
import numpy as np
from pyjstat import pyjstat
from ecbdata import ecbdata
import requests
from datetime import datetime
from io import BytesIO
from config import *

def extract_data_from_bank_pt(series_id, variable_name):
    """
    Function to extract data from BPSTAT API.

    Arguments: series_id int
             variable_name str.
             If variable_name is None, variable_name is set to urls label.

    Returns:   pandas dataframe with Date and variable_name columns
    """

    BPSTAT_API_URL = "https://bpstat.bportugal.pt/data/v1"

    url = f"{BPSTAT_API_URL}/series/?lang=EN&series_ids={series_id}"
    series_info = requests.get(url).json()[0]

    print(f"Extracting data from BPSTAT API...{series_id}")

    domain_id = series_info["domain_ids"][0]
    dataset_id = series_info["dataset_id"]

    dataset_url = f"{BPSTAT_API_URL}/domains/{domain_id}/datasets/{dataset_id}/?lang=EN&series_ids={series_id}"
    dataset = pyjstat.Dataset.read(dataset_url)
    df = dataset.write('dataframe')

    df['Date'] = pd.to_datetime(df['Date'])
    if variable_name is None:
        variable_name = series_info['label']

    df = df.rename(columns={'value': variable_name})
    df = df[['Date', variable_name]]
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    return df


def extract_data_from_ecb(key, start_date='2020-01'):
    """
    Function to extract data from ECB.

    Arguments: key str: URL key
               start_date str:  start date

    Returns:   pandas dataframe with TIME_PERIOD and OBS_VALUE columns
    """

    df = ecbdata.get_series(key,
                            start=start_date, detail='dataonly')

    df.TIME_PERIOD = pd.to_datetime(df.TIME_PERIOD)
    df = df[['TIME_PERIOD', 'OBS_VALUE']]

    return df


def extract_euribor_data_from_ecb(tenor, start_date):
    """
    Function to extract Euribor data.
    Extracted from ECB.
    Returns a dataframe with euribor data for a defined tenor from start_date until now.

    Params:
        - tenor (str): '3M' or '6M' or '1M' or '1Y'
        - startdate (str)

    Returns a dataframe with euribor data for the specified tenor from start_date until now.

    Usage example:  extract_euribor_data_from_ecb('1Y', '2020-01-01')
    """

    dict_keys = {
        '3M': 'FM.M.U2.EUR.RT.MM.EURIBOR6MD_.HSTA',
        '6M': 'FM.M.U2.EUR.RT.MM.EURIBOR3MD_.HSTA',
        '1M': 'FM.M.U2.EUR.RT.MM.EURIBOR1MD_.HSTA',
        '1Y': 'FM.M.U2.EUR.RT.MM.EURIBOR1YD_.HSTA'
    }

    df = extract_data_from_ecb(dict_keys[tenor], start_date)
    df.columns = ['Date', 'Euribor ' + tenor]

    return df

def extract_euribors(start_date):
    """
    Function to extract Euribor data for several tenors ('3M','6M','1M','1Y').
    Extracted from ECB.

    Params:
        - start_date (str)

    Returns a dataframe with euribor data for several tenor from start_date until now.

    Usage example:  extract_euribors('2020-01-01')
    """

    dict_keys = {
        '3M': 'FM.M.U2.EUR.RT.MM.EURIBOR6MD_.HSTA',
        '6M': 'FM.M.U2.EUR.RT.MM.EURIBOR3MD_.HSTA',
        '1M': 'FM.M.U2.EUR.RT.MM.EURIBOR1MD_.HSTA',
        '1Y': 'FM.M.U2.EUR.RT.MM.EURIBOR1YD_.HSTA'
    }

    df_aux = extract_data_from_ecb(dict_keys['1M'], start_date)
    df_aux.columns = ['Date', 'Euribor 1M']

    for tenor in ['3M', '6M', '1Y']:
        df_aux1 = extract_data_from_ecb(dict_keys[tenor], start_date)
        df_aux1.columns = ['Date', 'Euribor ' + tenor]

        df_aux = df_aux.merge(df_aux1, on='Date', how='left')
    df_aux['Date'] = pd.to_datetime(df_aux['Date']).dt.date

    return df_aux


def get_ldp_data(dict_indicator_keys):
    """Dados do bpstat sem multiindex"""
    ano_atual = datetime.now().year - 1

    df_final = pd.DataFrame()
    df_final['Date'] = pd.date_range(start='2006-12-31', end=f'{ano_atual}-12-31', freq='A-DEC')

    for setor, series_ids in dict_indicator_keys.items():
        df_setor = pd.DataFrame()
        for series_id in series_ids:
            #print(f"A extrair {setor}: {series_id}")
            df_extracted = extract_data_from_bank_pt(series_id, None)
            df_extracted['Date'] = pd.to_datetime(df_extracted['Date'])

            df_final = df_final.merge(df_extracted, on='Date', how='left')

    #df_final['Date'] =  pd.to_datetime(df_final['Date']).dt.strftime('%Y-%m-%d')
    return df_final



def process_ecb_indicators(indicadores_ecb, start_date="2006-01-01"):
    master_df = pd.DataFrame()
    
    for category, indicators in indicadores_ecb.items():
        print(f"\nProcessando categoria: {category}")
        
        for indicator_name, url in indicators.items():
            print(f"Extraindo: {indicator_name}")
            url = url.split("datasets/")[1].split('/')[1] 
            # Extrai os dados para este indicador
            df = extract_data_from_ecb(url, start_date)
            df['TIME_PERIOD'] = df['TIME_PERIOD'].astype(str).str[-4:].astype(int)
            df.columns = ['Date', indicator_name]
            
            if not df.empty:
                # Renomeia a coluna para o nome do indicador
                df.rename(columns={'value': indicator_name}, inplace=True)
                
                # Combina com o DataFrame mestre
                if master_df.empty:
                    master_df = df
                else:
                    master_df = master_df.merge(df, how='left', on='Date')
            else:
                print(f"⚠️ Falha ao extrair: {indicator_name}")
    
    return master_df.sort_index()


def convert_df_to_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        for idx, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max() + 2, len(col) + 2) # Calcula o tamanho máximo da coluna + padding
            worksheet.set_column(idx, idx, max_len)  # Define a largura de cada coluna

        # Formatar o cabeçalho (linha das colunas)
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'font_color': '#FFFFFF',
            'valign': 'center',
            'align': 'center',
            'fg_color': '#179297',
            'border': 1
        })

        cell_format = workbook.add_format({
            'align': 'center',  # Centraliza horizontalmente
            'valign': 'vcenter',  # Centraliza verticalmente
        })

        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)

        for row_num in range(1, len(df) + 1):
            worksheet.set_row(row_num, None, cell_format)

    output.seek(0)
    return output