from env import *
import xlrd
loc = ("island_info.xlsx")
wb = xlrd.open_workbook(loc)


long_desc_sheet = wb.sheet_by_index(0)
short_desc_sheet = wb.sheet_by_index(1)
is_impass_sheet = wb.sheet_by_index(2)
item_sheet = wb.sheet_by_index(3)
environment_sheet = wb.sheet_by_index(4)


item_list = []


def find_location_input(x, y):
    return ("{0}_{1}".format(number_dic[x], number_dic[y]))


def excel_import():
    for x in range(0, 10):
        for y in range(0, 10):
            #print(long_desc_sheet.cell_value(x, y))
            eval(find_location_input(x, y)).add_long_desc(
                long_desc_sheet.cell_value(x, y))

            eval(find_location_input(x, y)).add_short_desc(
                short_desc_sheet.cell_value(x, y))

            eval(find_location_input(x, y)).add_is_impass(
                is_impass_sheet.cell_value(x, y))

            eval(find_location_input(x, y)).add_environment(
                environment_sheet.cell_value(x, y))

            items = (item_sheet.cell_value(x, y)).split(",")
            for item in items:
                eval(find_location_input(x, y)).add_items(item.strip())
