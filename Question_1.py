def get_string(n):
    p=['zero','one','two','three','four','five','six','seven','eight','nine']
    t=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
    l=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']
    m=['hundred','thousand']
    lent=len(str(n))
    if(lent==1):
        return p[n%10]
    elif(lent==2):
        if(n//10==1):
            if(n%10==0):
                return l[0]
            return t[(n%10)-1]
        else:
            if(n%10==0):
                return l[(n//10)-1]
            else:
                return l[(n//10)-1]+p[n%10]
    elif(lent==3):
        s=p[n//100]+m[0]
        if(n%100==0):
            return s
        else:
            n=n%100
            if(n//10==0):
                return s+'and'+p[n%10]
            elif(n//10==1):
                if(n%10==0):
                    return s+'and'+l[0]
                return s+'and'+t[(n%10)-1]
            else:
                if(n%10==0):
                    return s+'and'+l[(n//10)-1]
                else:
                    return s+'and'+l[(n//10)-1]+p[n%10]
    else:
        return 'one thousand'
            
    
def count_len(p):
    c=0
    for i in p:
        if i!='':
            c+=1
    return c

n=int(input())
total_len=0
for i in range(1,n+1):
    p=get_string(i)
    k=count_len(p)
    total_len+=k
print(total_len)