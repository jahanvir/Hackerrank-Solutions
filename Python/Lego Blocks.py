def legoBlocks(n, m):
    # Write your code here
    mod=10**9+7
    r=[0]*(m+1)
    a=[0]*(m+1)
    
    a[0]=1
    for j in range(m+1):
        a[j] += a[j-1] if j-1>=0 else 0
        a[j] += a[j-2] if j-2>=0 else 0
        a[j] += a[j-3] if j-3>=0 else 0
        a[j] += a[j-4] if j-4>=0 else 0
        
    #print(datetime.datetime.now())    
    for j in range(1, m+1):
        a[j] = a[j] % mod
        a[j] = a[j] ** n
        a[j] = a[j] % mod
    #print(datetime.datetime.now())
    
    r[1] = 1
    for j in range(2, m+1):
        r[j] = a[j]
        for k in range(1, j):
            r[j] -= r[k]*a[j-k]
        r[j] = r[j] % mod
    #print(datetime.datetime.now())
    return r[m]%mod
