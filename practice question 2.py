import math
H = int(input("Enter an integer representing initial height, H: "))
V = int(input("Enter an integer representing initial velocity, V: "))
Vn = int(input("Enter an integer representing final velocity, Vn: "))

def rebound_height(H, V, Vn):
    result = pow(V / Vn, 2)
    return H * result

Hn = rebound_height(H, V, Vn)
print(round(Hn))


