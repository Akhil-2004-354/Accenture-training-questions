A = []
N = int(input("Enter the length of array: "))
output = []

for i in range(1, N + 1):
    A.append(i)

    if i % 2 == 0:
        output.append("even")
    else:
        output.append("odd")

print(output)



