from numpy import random as random

# data list
a = [random.randint(2),random.randint(2),random.randint(2),random.randint(2),random.randint(2),random.randint(2),random.randint(2),random.randint(2),random.randint(2),random.randint(2)]
print(a)
for i in a:
    b = random.randint(2);
    if b == 0:
        a[i] = 0

    if b == 1:
        b1 = random.randint(2)

        if b1 == 0:
            a[i] = 0

        if b1 == 1:
            a[i] = 1

print(a)