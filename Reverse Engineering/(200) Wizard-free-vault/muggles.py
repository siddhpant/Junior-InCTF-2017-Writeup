import hashlib 
import struct
import re as sbc
obj_1=hashlib.md5()
abc=12132
str1=''
str2=''
xorer=[117, 5, 36, 94, 6, 23, 113, 44, 71, 105, 6, 125, 1, 6, 90, 31, 54, 57, 117,
        118, 2, 123, 61, 112, 1, 74, 106, 98, 69, 2, 12, 93]

print "\t-------- MAGIC RESISTANT -----------  "
print "[*] This is to prevent leaking top level secrets to the Wizarding world"
inp1=raw_input("LEVEL 1: \n Enter the password:").strip('\n')
obj_1.update(inp1)
if cmp("8a0e2e33fc0ef5f4d1b9243139a2aa4f",str(obj_1.hexdigest())) == 0:
    print "Well.. I still think that you are a squib"
    inp2=map(int,raw_input("LEVEL 2: \n Enter the Muggle numbers:").strip().split(' '))
    list1=[]
    for i in range(len(inp1)):
        list1.append(chr(ord(inp1[i])^inp2[i]))
    fin="".join(list1)
    for i in inp2:
        str1+=chr(i)
    obj_1.update(str1)
    if cmp(fin,"=:P3_7R")==0:
        print "I am starting to feel that you are a Muggle after all"
        inp3=raw_input("\tLEVEL 3: \n\t Final Check :: Two step verification \nEnter key 1:").strip('\n')        
        inp4=raw_input("Enter key 2:").strip('\n')
        if sbc.match("^[\w\d_-]*$",inp3):
            if len(inp3) is 16 and len(inp4) is 4:
                obj_1.update(inp3)
                mod_inp3=int(sbc.sub(r'\D', "", inp3).strip())
                if inp3[5] == inp4[1]:
                    if len(sbc.findall(inp4,inp3)) == 3:
                        obj_1.update(inp4)
                        if inp3[9]=='7':
                            r=[]
                            for i in range(4):
                                r.append((ord(inp1[i])^int(inp2[i])))
                            tot=0
                            for i in range(4):
                                str2+=chr((r[i]-60)%30+80)
                                tot=tot+r[i]
                            if cmp(str2,inp4)==0:
                                tot=tot*11
                                if tot == mod_inp3 and inp4[3] == inp3[13]:
                                    md5_final=obj_1.hexdigest()
                                    flag=''
                                    for ii in range(32):
                                        flag+=str(chr(ord(md5_final[ii])^xorer[ii]))
                                    print "-------So you are not a wizard after all------"
                                    print "inctf{"+flag+"}"
                                    exit() 
            else:
                print "Don't get too smart, Wizard!!"
print "---------------------------------------------------------------------------------------------"
print "Thou art of Magic blood \nLeave this place Good Sir"
