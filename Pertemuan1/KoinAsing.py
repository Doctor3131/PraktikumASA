def main():
    data = input()
    for koin in set(data):
        if data.count(koin) == 1:
            return data.index(koin) + 1
    return "Tidak ditemukan"

main()