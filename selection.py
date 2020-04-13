a=[7,9,5,3,1,2,6,7]

for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
        if a[min]>a[j]:
            min=j
    a[i],a[min]=a[min],a[i]

print(a)