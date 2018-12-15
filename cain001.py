
arr=[1,2,3]
a=[]
l=len(arr)
for out1 in range(l):
    for out2 in range(out1+1,l):
        #print([arr[out1],arr[out2]])
        a.append([arr[out1],arr[out2]])

print(a)
