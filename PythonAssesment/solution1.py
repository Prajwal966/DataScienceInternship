num = input('Enter the length of the list: ')
number_list = []
name_list = []
for i in range(int(num)):
    number = input()
    number_list.append(number)
for i in range(int(num)):
    name = input()
    name_list.append(name)

res = {}
for key in number_list:
    for value in name_list:
        res[key] = value
        name_list.remove(value)
        break
print(res)