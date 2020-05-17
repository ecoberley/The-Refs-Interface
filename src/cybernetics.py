import xlrd
from src.cybernetic import *

filename = "search_lists.xlsx"
cybernetics_spreadsheet = xlrd.open_workbook(filename).sheet_by_index(1)

cybernetics = []
for i in range(1, cybernetics_spreadsheet.nrows):
    temp_cybernetic = Cybernetic(cybernetics_spreadsheet.row_values(i))
    cybernetics.append(temp_cybernetic)
print("Imported cybernetics_list...")


def search_cybernetics(args):
    results = cybernetic_desc_format(0)
    query = args[1].lower()
    for idx in range(0, len(cybernetics)):
        if cybernetics[idx].to_string().lower().__contains__(query):
            if idx != len(cybernetics) - 1:
                results += cybernetics[idx].to_string() + "\n"
            else:
                results += cybernetics[idx].to_string()
    if results == cybernetic_desc_format(0):
        return "No results found"
    else:
        return results


def cybernetic_desc_format(args):
    return "[Name • Surgery Type • Cost • Humanity Loss •  Availability • Description]\n"
