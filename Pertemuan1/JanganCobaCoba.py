def main():
    data = input()[1:-1].split(",")
    if data != ['']:
        data = [int(angka) for angka in data]
    data2 = int(input())
    try:
        return data.index(data2)
    except ValueError:
        return '"Tidak ditemukan"'

print(main())