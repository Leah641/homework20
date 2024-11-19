# homework20

# start with 1
n=1
SUM=0

# the formula:
f = 1

while f > 0.0000000000001 :
    f = 1/n ** 2
    n += 1
    SUM += f

print("SUM =",SUM)
