"""
сколько раз встречается конкретная цифра в этом списке?
sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
ответ будет 11 раз
для цифры 5 в поиске
sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
"""

sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53: 125} ]
sp = str (sp)
print (sp)
counter = 0
for five in sp:
    if five == '5':
        counter+=1
print (counter)