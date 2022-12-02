proposal = input("Введите предложение: ").lower()
lis = proposal.split( )
temp = []
for i in lis:
    if i not in temp:
        temp.append(i)
        a = lis.count(i)
        print(i, a)
    