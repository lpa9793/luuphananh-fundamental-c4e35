new_string="ThiS is String with Upper and lower case Letters"
words={}
s=new_string.lower()
for i in s:
    words[i]=words.get(i,0)+1
items=list(words.items())
items.sort()
del items[0]
for i,j in items:
    print(i,j)