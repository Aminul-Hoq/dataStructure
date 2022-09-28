import os
from operator import itemgetter

import xlsxwriter

path = "E:/Python/cy/cy"
workbook = xlsxwriter.Workbook("./test3.xlsx")
workbook1 = xlsxwriter.Workbook("./test4.xlsx")
worksheet = workbook.add_worksheet()
worksheet1 = workbook1.add_worksheet()


def readFileList():
    month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    year = 1945
    filename = "bio"
    row = 1
    row1 = 1
    title = ["Ocean Name", "Number", "year:month:date:hour", "data type", "", "latitude", "longitude", "wind speed"]
    worksheet.write_row(0, 0, title)
    worksheet1.write_row(0,0,title)
    dir_list = os.listdir(path)
    for x in range(77):
        for m in month:
            name = (filename + m + str(year + x) + ".txt")
            if name in dir_list:
                with open(path+"/"+name, "r") as filestream:
                    data = []
                    for line in filestream:
                        currentline = line.split(",")
                        currentline[-1] = currentline[-1].strip()
                        worksheet1.write_row(row1, 0, currentline)
                        data.append(currentline)
                        row1 +=1
                    worksheet.write_row(row, 0, data[0])
                    row += 1
    workbook1.close()
    workbook.close()


if __name__ == '__main__':
    readFileList()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
