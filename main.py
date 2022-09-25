import os
import xlsxwriter

path = "E://Python//cy//cy"
workbook = xlsxwriter.Workbook(path +"/test.xlsx")
worksheet = workbook.add_worksheet()


def readFileList():
    row = 0
    col = 0
    dir_list = os.listdir(path)
    for x in dir_list:
        if x.endswith(".txt"):
            with open(path+"/"+x, "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    currentline[-1] = currentline[-1].strip()
                    print("row : " + str(row))
                    print("column : " + str(col))
                    print("data : " + str(currentline))
                    worksheet.write_column(row, col, currentline)
                    col += 1
                row += 1
            row = 0
    workbook.close()


if __name__ == '__main__':
    readFileList()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
