def leiaDinheiro(msg):
    while True:
        print(f'{msg}', end='')
        val = input()

        if not float(val):
            print(f'\033[0;91m [ERRO] Digite um valor monetário!\033[m')
            ok = False
        else:
            money = float(val)
            ok = True
            return money
        if ok:
            break