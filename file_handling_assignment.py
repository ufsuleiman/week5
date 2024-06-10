file = open('my_file.txt', 'w')
file.write('i am coding\n')
file.write('do you code?\n')
file.write('let\'s code together')
file.close()


with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)


with open('my_file.txt', 'a') as file:
    file.write('\nI code everyday')


with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)

 
