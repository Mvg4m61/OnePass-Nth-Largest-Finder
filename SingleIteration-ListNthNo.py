def largen():
    
    l1 = []
    l2 = []
    for i in range(8):
        num = int(input("\nEnter: "))
        l1.append(num)
    l = l1
    l.sort()
    print(l,"\n")
    n = int(input("\nEnter n: "))
    
    if n>8:
        print("\nSorry, n cannot be greater than 8! Try again.\n")
        largen()
    k = n-1
    g = 0
    for i in range(n):
        l2.append(g)
    j = 0
    for e in l1: #Single iteration
        while e<l2[j]:
            j=j+1
        else:
            for i in range(k-1,j-1,-1):
                l2[i+1]=l2[i]
                
            l2[j]=e
            j = 0
                
    print("\nNth largest number through single iteration: ",l2[k])
largen()