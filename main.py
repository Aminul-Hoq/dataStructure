import os
import xlsxwriter

path = "E:/Python/cy/cy"
workbook = xlsxwriter.Workbook("./test1.xlsx")
worksheet = workbook.add_worksheet()


def readFileList():
    row = 1
    title = ["Ocean Name", "Number", "year:month:date:hour", "data type", "", "latitude", "longitude", "wind speed"]
    worksheet.write_row(0, 0, title)
    dir_list = os.listdir(path)
    for x in dir_list:
        if x.endswith(".txt"):
            with open(path+"/"+x, "r") as filestream:
                data = []
                for line in filestream:
                    currentline = line.split(",")
                    currentline[-1] = currentline[-1].strip()
                    data.append(currentline)
                print(data)
                worksheet.write_row(row, 0, data[0])
                row += 1

    workbook.close()


if __name__ == '__main__':
    readFileList()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
