def segitiga(n):
    if n == 0:
        print()
    else:
        segitiga(n-1)
        for i in range(n):
            print('*', end='')
        print()

segitiga(3)