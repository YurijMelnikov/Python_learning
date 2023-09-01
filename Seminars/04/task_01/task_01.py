"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""


text = "a a a b c a a d c d d"
text = text.split()
print(text)

for i in range (len(text)):
    counter = 1
    for j in range (i+1, len(text)):
        if text[i] ==  text[j]:
            text[j] = text[i]+"_"+str(counter)
            counter+=1
print(text)
        
