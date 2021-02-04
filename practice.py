# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 1000:
    print(a)
    a, b = b, a+b


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name = letters[0] + letters[13] + letters[19] + letters[7] + letters[14] + letters[13] + letters[-2]
print(name)