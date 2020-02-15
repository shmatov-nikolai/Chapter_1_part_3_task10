'''
10. Напишите программу на Python для построения следующего шаблона, используя вложенный
цикл for.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

vershina = int(input("Введите высоту шаблона: "))

def build_template(num):
    center = (num+1)//2
    for i in range(1, center):
        print ("* " * i, sep = '\n')
    for i in reversed(range(1, center-1)):
        print ("* " * i, sep = '\n')
    


build_template(vershina)