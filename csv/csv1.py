for line in open("sample.csv"):
    title, year, director = line.split(",")
    print year