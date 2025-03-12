def gunung(n):
    if n == 0:
        print()
        
    else :
        gunung(n-1)
        for i in range(n):
            print('*', end='')
        gunung(n-1)

gunung(3)