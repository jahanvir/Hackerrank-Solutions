def truckTour(petrolpumps):
    # Write your code here
    
    n=len(petrolpumps)
    index=0
    petrol=0
    for i in range(n):
        petrol+=petrolpumps[i][0]-petrolpumps[i][1]
        if petrol<0:
            index=i+1
            petrol=0
    return index