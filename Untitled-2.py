# Program 6: Count vowels in a string
s = input().lower()
v = "aeiou"
c = 0
for ch in s:
    if ch in v:
        c += 1
print(c)
