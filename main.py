str1=input("Введите первую строку: ")
print("Ваша 1-я строка: ", str1)
str2=input("Введите вторую строку: ")
print("Ваша 2-я строка: ", str2)
letters=[]
result="Ваши строки являются анаграммами"
for i in str1:
    if i not in letters:
        letters.append(i)
for j in str2:
    if j not in letters:
        result="Ваши строки не являются анаграммами"
        break
print(result)