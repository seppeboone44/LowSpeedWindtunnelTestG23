filepath = 'raw_testG23-2D.txt'
file = open(filepath, 'r')


pressure_start_column = 8  # Adjust based on column index for P001
pressure_end_column = 121  # Adjust based on column index for P113 (inclusive)
i = 1
alphapressurelist = []
while True:
    content=file.readline()
    if not content:
        break
    columns = content.strip().split()
    pressure_values = columns[pressure_start_column:pressure_end_column + 1]
    alphapressurelist.append(pressure_values)
file.close()

run1 = alphapressurelist[0]
run2 = alphapressurelist[1]
run3 = alphapressurelist[2]
run4 = alphapressurelist[3]
run5 = alphapressurelist[4]
run6 = alphapressurelist[5]
run7 = alphapressurelist[6]
run8 = alphapressurelist[7]
run9 = alphapressurelist[8]
run10 = alphapressurelist[9]
run11 = alphapressurelist[10]
run12 = alphapressurelist[11]
run13 = alphapressurelist[12]
run14 = alphapressurelist[13]
run15 = alphapressurelist[14]
run16 = alphapressurelist[15]
run17 = alphapressurelist[16]
run18 = alphapressurelist[17]
run19 = alphapressurelist[18]
run20 = alphapressurelist[19]
run21 = alphapressurelist[20]
run22 = alphapressurelist[21]
run23 = alphapressurelist[22]
run24 = alphapressurelist[23]
run25 = alphapressurelist[24]
run26 = alphapressurelist[25]
run27 = alphapressurelist[26]
run28 = alphapressurelist[27]
run29 = alphapressurelist[28]
run30 = alphapressurelist[29]
run31 = alphapressurelist[30]
run32 = alphapressurelist[31]
run33 = alphapressurelist[32]
run34 = alphapressurelist[33]
run35 = alphapressurelist[34]
run36 = alphapressurelist[35]
run37 = alphapressurelist[36]
run38 = alphapressurelist[37]
run39 = alphapressurelist[38]
run40 = alphapressurelist[39]
run41 = alphapressurelist[40]
run42 = alphapressurelist[41]
run43 = alphapressurelist[42]
run44 = alphapressurelist[43]

