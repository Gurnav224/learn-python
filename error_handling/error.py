file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()
    
    

with open('hello.py','w')  as file:
    file.write("print('hello python')")