def xor(x):
    key=10
    n=""
    for i in x:
        n+=chr(ord(i)^key)
    return n

def shift(x):
    m=list(x)
    n=[]
    for i in m:
        if(ord(i)>=65 and ord(i)<=90):
            if ord(i)==88:
                n.append('A')
            elif ord(i)==89:
                n.append('B')
            elif ord(i)==90:
                n.append('C')
            else:
                n.append(chr((ord(i)+3)))

        elif(ord(i)>=97 and ord(i)<=122):
            if ord(i)==120:
                n.append('a')
            elif ord(i)==121:
                n.append('b')
            elif ord(i)==122:
                n.append('c')
            else:
                n.append(chr((ord(i)+3)))
        elif(ord(i)>=48 and ord(i)<=57):
            n.append(str((int(i)+3)%10))
    return n

def encode(x):
    return x.encode("hex")    

if __name__=="__main__":
    print "Decode the following string to find the flag:"
    print "667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268"
    print "Enter what you got after decoding:"
    arr=raw_input()
    a=shift(arr)
    b=xor(a)
    c=encode(b)
    if c=="667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268":
        print "Yeah!....You are a Genious"
        cnt=0
        flag=""
        for i in list(arr):
            cnt+=1
            if cnt==7:
                flag+="{"
            elif cnt==14 or cnt==25 or cnt==27 or cnt==29:
                flag+="_"
            flag+=i
        flag+="}"
        print "The flag is:"
        print flag

    else:
        print "Oops....Try again"
        print "Looking at the source code might help"
