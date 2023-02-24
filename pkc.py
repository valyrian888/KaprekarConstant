def ask():
        global x
        x = int(input("Enter: "))

def pkc(x):
    global d
    a=x//1000
    b=(x//100) - (10*a)
    c= (x//10)-(100*a)-(10*b)
    d=(x%10)

    l = [a,b,c,d]
        #l= ascend /// l1= desc
    l.sort(reverse = True)
    #print(l)
    l2=l[::-1]
    #print(l2)
    #t1=max and t2=min
    t1=l[0]*1000  +l[1]*100+ l[2]*10+ l[3]
    t2=l2[0]*1000  +l2[1]*100+ l2[2]*10+ l2[3]
    d=t1-t2   #difference
    print(x,'=>',t1,'-',t2,'=',d)


ask()
while (x !=6174 ):
        pkc(x)
        x=d



        
