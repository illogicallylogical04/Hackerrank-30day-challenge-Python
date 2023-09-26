# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for _ in range(n):
    s = input()
    odd = ''
    even = ''
    for i in range(len(s)):
        if i%2==0:
            even += s[i]
        else:
            odd += s[i]
    print(f"{even} {odd}")
