from area_figures import Circle, Triangle

# Вычисление площади фигуры без знания типа фигуры в compile-time
lst = (Circle(10), Triangle(8, 15, 17))
for figure in lst:
    print(figure.area)