func = lambda Lstar,Lsun, dau: ((Lstar / Lsun)**1/2) * dau

def main():
    Lstar = float(input('Введите болометрический показатель(светимость) звезды, для того, чтобы узнать средний радиус обитаемой зоны вокруг звезды: '))
    Lsun = 3.86 * 10 ** 33
    dau = 149597870700
    d = func(Lstar,Lsun, dau)

    print('Седний радиус обитаемой зоны вокруг звезды:', d)
    
if __name__ == "__main__":
    main()    
