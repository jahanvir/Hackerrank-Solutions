def gridChallenge(grid):
    # Write your code here
    temp=[]
    for g in grid:
        temp.append(sorted(g))
    row=len(grid)
    col=len(grid[0])
    for i in range(col):
        for j in range(row-1):
            if temp[j][i]>temp[j+1][i]:
                return "NO"
    return "YES"