a = int(input("Введите расстояние (км), которое спортсмен пробежал в первый день: "))
b = int(input("Введите расстояние (км), которое спортсмену необходимо будет пробжать: "))
i =1
while a<b:
    a *= 1.1
    i +=1
print("Для достижения нужного киллометража неободимо пробежать ",i," дней")