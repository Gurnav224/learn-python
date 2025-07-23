

items =   ["apple", "banana", "mango", "orange", "banana"]

unqiue_item = set()


for item in items:
    if item in unqiue_item:
        print("dulicate item", item)
        break
    else:
        unqiue_item.add(item)


print(unqiue_item)