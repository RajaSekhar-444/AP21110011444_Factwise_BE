def get_max_value(l,k):
    n=len(l)
    sum=0
    i=0
    j=n-1
    while(k>0):
        if(l[i]>l[j]):
            sum+=l[i]
            i+=1
        elif(l[j]>l[i]):
            sum+=l[j]
            j-=1
        else:
            if(l[i+1]>l[j-1]):
                sum+=l[i]
                i+=1
            else:
                sum+=l[j]
                j-=1
        k-=1
    return sum
n=int(input())
l=list(map(int,input().split()))
k=int(input())
print(get_max_value(l,k))