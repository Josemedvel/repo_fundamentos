import sys

if len(sys.argv) < 3:
    sys.exit()

num_tablas = int(sys.argv[1])
limite_sup = int(sys.argv[2])

for i in range(1, num_tablas + 1):
    with open(f"tabla_{i}.txt", "a") as file:
        for j in range(1, limite_sup + 1):
            file.write(f"{i} x {j} = {i * j}\n")