f = open("text.txt",'r')
c = f.readlines()
newstring = []
for i in c:
    newline = i.strip()
    idx = 0
    while ((idx < (len(i) - 1)) and (i[idx]==' ')):
        idx += 1
    newline ='['+str(idx+12)+'C '+ '[31m' + newline +'\n'
    newstring.append(newline)
c = open("output.ans",'w')
c.writelines(newstring)

