num = 2**15
res = 0
nums = list(str(num))
for i in nums:
    i = int(i)
    res += i

print(res)

note = open("note.txt", "r+", encoding="utf-8")
lst = note.read()
lst = lst.split('\n')
lst = [i.split(',') for i in lst]

for i, j in lst:
    print(i, j)