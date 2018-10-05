#Robert F. Granzow 06-23-2017


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import datetime

from datetime import date



#update_cell(row, col, value)
Today=str(date.today())
Mood=4
Users=12
new_value=[Today,Mood,Users]

print(Today)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('powerful-genre-218209-aec5a70ae8c1.json', scope)
gc = gspread.authorize(credentials)

wks = gc.open("Test1").sheet1


col=[]
col_index=[]
row=[]
row_index=[]

#Récupérer les emplacements des dimensions
#column=glist[0]
column=wks.col_values(1,'FORMATTED_VALUE')
j=0
for i in column:
    if len(column)>0 and i!='None':
        #print(i)
        row.append(i)
        j=j+1
        row_index.append(j)

rows=wks.row_values(1,'FORMATTED_VALUE')
j=0
for i in rows:
    if len(rows)>0 and i!='None':
        #print(i)
        col.append(i)
        j=j+1
        col_index.append(j)

print(row_index)
print(col_index)
        
        
        

#Calcule le nombre de colonnes qui ont été populées
x=len(col)

y=len(row)




for i in row_index:
    wks.update_cell(i,len(col)+1,new_value[i-1])
    #print(i)
    #print(len(col)+1)
    #print(new_value[i-1])
    
    #wks.update_cell(i,



