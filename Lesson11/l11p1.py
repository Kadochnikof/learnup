data = open('log.txt', 'a')
row = str()
while row != "off":
    row = input("Введите фразу для добавления в файл:")
    if row != "off":
        data.write(str(row) + "\n")
    
data.close()