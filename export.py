#!/usr/bin/python3

import json

import pandas as pd

'''=====----- Variables -----===== '''
INPUT_EXCEL_FILE = 'data/db_parking.xlsx'
OUTPUT_XML_FILE = 'data/output_xml_file.xml'

addr_df = pd.read_excel(INPUT_EXCEL_FILE)
addr_df.rename(columns={'Название': 'address'}, inplace=True)
addr_df.to_xml(OUTPUT_XML_FILE, encoding='utf-8')

#####=====----- THE END -----=====#########################################