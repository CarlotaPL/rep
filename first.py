path = 'C://Users//vdi-student//Desktop//rep//rozliczenie.csv'
mode = 'r'

with open(path, mode) as plik_csv:
    content = plik_csv.readlines()

for i in range(len(content)):
    content[i] = content[i].replace('\n', '')
    content[i] = content[i].split(',')

print(content)

total = 0
for i in range(1,len(content)):
    total +=int(content[i][1])
avg = total/(len(content)-1)
print(round(avg))

#macierzynski
total = 0
for i in range(1,len(content)):
    if content[i][4] == 't' and content[i][3] == 'k':
        total +=1

print(total)