try:
    num = int(input("Ingresa un número:\t"))
    i = 0
    while i <= num:
        print(i)
        i = i + 5
except Exception:
    print("Error")