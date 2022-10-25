# exercise_1(считает сумму цифр в файле)
count = 0
file_ = open('test.txt', 'r')
content_file = file_.readline()
for i in content_file:
    if i.isdigit():
        count += int(i)
print(count)


# exercise_2
file_ = open('test.txt', 'r')
content_file = file_.read()
list_dig = []
list_word = []
for i in content_file.split():
    if i.isdigit():
        list_dig.append(int(i))
    else:
        list_word.append(i)
list_dig.sort()
list_word.sort()
list_dig.extend(list_word)
print(list_dig)


# exercise_3
file_ = open('test.txt', 'w')
string_ = input('Введите строку: ')
while string_ != '':
    file_.write(string_ + '\n')
    string_ = input('Введите строку: ')
file_.close()

# exercise_4
file_ = open('test.txt', 'r')
list_ = file_.read().split('\n')
count = 0
for i in list_:
    count += 1
    print(f"В {count} строке {len(i)} символов")

# homework
list_ = [5, 6, 'sun', 'raise', 11]
file_ = open('test.txt', 'w')
list_dig = []
list_str = []
for i in list_:
    if i == str(i):
        list_str.append(i)
        list_str.sort(key=len)
    else:
        list_dig.append(i)
list_str.extend(sorted(list_dig))
print(list_str)

