# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
dict_ = {}

for _ in range(n):
    key_value = input()
    key_value = key_value.split(' ')
    dict_[key_value[0]] = key_value[1]

while True:
    try:
        name = input()
        if name in dict_:
            print('{0}={1}'.format(name, dict_.get(name)))
        else:
            print('Not found')
    except EOFError:
        break
