n=4

for i in range(1,n*2,1):
    for j in range(1,n*2,1):
        if (i==n):
            line = " * "
            print(line,end="")
        elif (i<n):
            if (j>=n):
                for k in range(n,j+1,1):
                    line = " * "
                    print(line,end="")
            else:
                line = "   "
                print(line,end="")
        else:
            if (j<n):
                for k in range(1,j+1,1):
                    line = " * "
                    print(line,end="")