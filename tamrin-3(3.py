entry = input() 
import re 
a = re.sub(" +"," ",entry) 
b = re.sub("^ ","",a) 
c= re.sub(" $","",b) 
listt = re.split("@",c) 
for i in range(1,len(listt)): 
    g = re.search("#", listt[i]) 
    if g==None: 
        j=0 
        while True: 
            if (i+j+1)>len(listt): 
                break 
            d = re.search("#", listt[i + j]) 
            if d!=None: 
                listt[i + j] = re.sub("#", "", listt[i + j], 1) 
                break 
            j+=1 
    listt[i] = re.sub("#","",listt[i],1) 
e = "@".join(listt) 
f = re.sub(" +"," ",e) 
list2 = re.split(r"\\n",f) 
list2[0] = "Formatted Text: "+list2[0] 
for i in list2: 
    print(i)