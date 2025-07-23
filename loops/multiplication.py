

table = 2
upto = 10


for i in range(1, upto + 1):
    if i == 5:
        continue
    else:
        print(f"{table} * {i} = {table * i}")