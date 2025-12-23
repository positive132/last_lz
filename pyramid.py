import math 
func = lambda s1, s2, h : 1/3 * h * (s1 + s2 + (s1 * s2) ** 1/2)
def main():
    s1 = float(input('Введите площадь нижнего основания в м^3: '))
    s2 = float(input('Введите площадь верхнего основания в м^3: '))
    h = float(input('Введите высоту усечённой пирамиды в м: '))
    V = func(s1, s2, h)
    print('ОбЪём усечённой пирамиды составляет:',V)
if __name__ == "__main__":
    main()    
