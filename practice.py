# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 1000:
    print(a)
    a, b = b, a+b


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name = letters[0] + letters[13] + letters[19] + letters[7] + letters[14] + letters[13] + letters[-2]
print(name)

x = int(input("Please enter an integer: "))
# input requires user input seems like stating the variable required
#outside the brackets, in this case int for integer.
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# Measure some strings:
words = ['cat', 'window', 'defenestrate', 'Wowowowowowowow']
for w in words:
    print(w, len(w))