a=[8,9,12,9,3,3,1,2]

for i in range(1,len(a)):
    temp=a[i]
    j=i-1
    while j>=0 and temp<a[j]:
        a[j],a[j+1]=a[j+1],a[j]
        j-=1
    a[j+1]=temp

print(a)