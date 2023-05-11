l = [1,2,3,4,2,5,7]

uniquelist = []
duplicate = []
for i in l:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print(uniquelist)