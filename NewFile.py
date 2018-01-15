import pandas,os
from pandas import ExcelWriter
import xlsxwriter


ExlOperation=pandas.read_excel('C:/Users/rahul.mishra/Desktop/clearcare_new/Excel_Input.xlsx')

import geopy

from geopy.geocoders import Nominatim

nom=Nominatim()

ExlOperation["Address"]=ExlOperation["location"].apply(nom.geocode)

ExlOperation["latitude"]=ExlOperation["Address"].apply(lambda x : x .latitude if x !=None else None)

ExlOperation["longitude"]=ExlOperation["Address"].apply(lambda x : x .longitude if x !=None else None)

ExlOut=ExlOperation.to_dict()

workbook = xlsxwriter.Workbook('data1.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for key,value in ExlOut.items():
    row += 1
    worksheet.write(row, col, key)
    for item in ExlOut[key]:
        worksheet.write(row, col + 1, item)
        row += 1

workbook.close()



