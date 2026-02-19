a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

print("Before swapping:")
print("a =", a, "b =", b, "c =", c)

# Swap values (example: a→b, b→c, c→a)
a, b, c = b, c, a

print("After swapping:")
print("a =", a, "b =", b, "c =", c)