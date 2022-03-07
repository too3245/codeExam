import sys

input = sys.stdin.readline

text = str(input().strip())

croatia_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = 0

for i in croatia_alpha:
    if i in text:
        word += text.count(i)
        text = text.replace(i," ")

text = text.replace(" ","")
print(len(text)+word)