import math

macarons = ["a", "a", "b"]
different = []
same = []

for var in macarons:
    if var not in different:
        different.append(var)
    else:
        same.append(var)
price = 0
if (len(different) <= 5):
    price = price + len(different) * unit_price * (1 - (len(different) - 1) / 10)
if (len(same) <= 5):
    price = price + len(different) * unit_price * (1 - (len(different) - 1) / 10)

w = len(different) % 5
x = math.floor(len(different)/5)
if len(different) > 5:
    for j in range(0,x):
        price = price + 5*unit_price*(1-0.4)
    price = price + w*unit_price*(1 - (w-1)/10)

k = len(same) % 5
y = math.floor(len(same)/5)

if len(same) > 5:
    for j in range(0, y):
        price = price + 5 * unit_price * (1 - 0.4)
    price = price + k * unit_price * (1 - (k - 1) / 10)
return math.floor(price)