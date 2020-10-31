import xlrd
loc = ("island_info.xlsx")
wb = xlrd.open_workbook(loc)



#Description Array -------------------------------------------------------------------------
#Open description Worksheet
#Initialise an array of 10X10
#Fill the array using the Excel sheet

description_sheet = wb.sheet_by_index(0)
description_init_array = [["" for i in range(10)] for j in range(10)]

for x in range(4):
    for y in range(4):
        description_init_array[x][y] = description_sheet.cell_value(x,y)


