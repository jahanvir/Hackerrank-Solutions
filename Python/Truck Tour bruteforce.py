def truckTour(petrolpumps):
    # Write your code here
    
    n=len(petrolpumps)
    index=0
    petrol=0
    for i in range(n):
        index=i
        petrol=0
        for j in range(n):
            pos=(index+j)%n
            petrol+=petrolpumps[pos][0]-petrolpumps[pos][1]
            if petrol<0:
                break
            if j==n-1:
                return index