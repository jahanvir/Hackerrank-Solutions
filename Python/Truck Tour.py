def truckTour(petrolpumps):
    # Write your code here
    total=0
    difference=[]
    for p in petrolpumps:
        difference.append(p[0]-p[1])
        
    i=0
    pos=0
    while i<len(difference):
        total+=difference[i]
        if total<0:
            for _ in range(i+1):
                difference.append(difference.pop(0))
            total=0
            pos+=i+1
            i=0
        else:
            i+=1            
        
    return pos