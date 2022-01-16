# Mehdi Bastani
# https://github.com/mehdibastani

import requests
import xlrd
import xlsxwriter

wb_URL = xlrd.open_workbook("URLs.xlsx")
wb_Pad = xlrd.open_workbook("Pads.xlsx")
sheet_URL = wb_URL.sheet_by_index(0)
sheet_Pad = wb_Pad.sheet_by_index(0)
url_Num_Row = list(range(1, sheet_URL.nrows))
pad_Num_Row = list(range(1, sheet_Pad.nrows))

results = xlsxwriter.Workbook('Results.xlsx')
worksheet = results.add_worksheet()

data_Format1 = results.add_format({'border': True, 'bold': True, 'bg_color': '#ff5e5e'})
data_Format2 = results.add_format({'border': True, 'bg_color': '#d9d9d9'})
data_Format3 = results.add_format({'border': True, 'bg_color': '#ffffff'})

worksheet.write(0, 0, "URLs", data_Format1)
worksheet.write(0, 1, "Status", data_Format1)

sum_rows = 1
for ads in url_Num_Row:
    des_Url = sheet_URL.cell_value(ads, 0)
    for pad in pad_Num_Row:
        temp_Pad = sheet_Pad.cell_value(pad, 0)
        pat = data_Format2 if sum_rows % 2 == 0 else data_Format3

        try:
            request = requests.get(des_Url + temp_Pad)
            worksheet.write(sum_rows, 0, des_Url + temp_Pad, pat)
            worksheet.write(sum_rows, 1, request.status_code, pat)
        except requests.exceptions.ConnectionError:
            request = "Connection refused"
            worksheet.write(sum_rows, 0, des_Url + temp_Pad, pat)
            worksheet.write(sum_rows, 1, request, pat)

        sum_rows = sum_rows + 1

results.close()
