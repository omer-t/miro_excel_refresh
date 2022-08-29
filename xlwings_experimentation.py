import xlwings as xw
import urllib
import pandas as pd

# URL do arquivo
url = 'http://www.anp.gov.br/images/DADOS_ESTATISTICOS/Vendas_de_Combustiveis/Vendas_de_Combustiveis_m3.xls'
file_name, headers = urllib.request.urlretrieve(url)

# Workbook
wb = xw.Book(file_name)

# PivotTable name
tabela_interesse = 'Tabela dinâmica3'

# Data
pivot_cache = wb.api.ActiveSheet.PivotTables(tabela_interesse).PivotCache()