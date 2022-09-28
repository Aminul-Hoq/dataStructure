month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
year = 1945
title = "bio"

for x in range(77):
    for m in month:
        print(title + m + str(year + x) + ".txt")
