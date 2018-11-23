#1 - 12вар. Напишите программу, которая считывает из файла строку, соответствующую тексту,
#сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
#Запишите полученный текст в файл.

#Sample Input:
#a3b4c2e10b1

#Sample Output:
#aaabbbbcceeeeeeeeeeb


import re
with open('3.txt','r+') as f:
    a = re.split(r"(\d+)",f.readline())[:-1]
    result = ''.join([y * int(x) for x,y in zip(a[1::2], a[::2])])        
    f.seek(0)
    f.write(result)
