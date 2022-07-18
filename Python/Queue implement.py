t=input()
arr=[]
for i in range(int(t)):
    temp=input()
    q=temp.split(" ")
    if q[0]=='1':
        arr.append(q[1])
    if q[0]=='2':
        arr.pop(0)
    if q[0]=='3':
        print(arr[0])