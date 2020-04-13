a=[78,45,37,78,45,67,64,78,78]
item=int(input("enter the searching element"))
i=0
while(i<len(a)):
    if item==a[i]:
        print(f"{a[i]} is present in {i+1} position")
    i+=1