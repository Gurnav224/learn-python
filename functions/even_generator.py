



def event_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
                
                
                
for num in event_generator(10):
    print(num)