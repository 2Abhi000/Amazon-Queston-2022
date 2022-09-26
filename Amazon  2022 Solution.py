
#Bruteforce Tme Complexity O(n2) Approach 1 if paragraph is given
ar=['Amazon', 'is','the','best','company','to','work','for','.','The','amazon','is','the','beautiful','forest','.']
s=['Amazon','The']
k=[]
c=[]
for i in ar:
    if s[0].lower()==i or s[1].lower()==1 or s[0]==i or s[1]==i:
        k.append((i,ar.index(i)))
        c.append(ar.index(i))
k=list(set(k))
print(k,c)
c.sort()
print(ar[c[0]],ar[c[1]])

 #Bruteforce Approach 2 IfWords and their index is getActiveIndex
ar=[('Amazon',0), ('is',1),('the',2),('best',3),('company',4),('to',5),('work',6),('for',7),('.',14),('The',8),('amazon',9),('is',10),('the',11),('beautiful',12),('forest',13),('.',14)]
s=['Amazon','The']
k=[]
ar.sort()
for i in ar:
    for j in i:
        if s[0].lower()==i or s[1].lower()==1 or s[0]==i or s[1]==i:
            k.append(i[1])
k.sort()
print(k[:2])

#Optimised Time Complexity O(n) Approach 3 Only word and their occurence is given
data=[['Amazon',[11,8,9]],['The',[2,4,10,1,5]]]
l1=data[0][1]
l2=data[1][1]
l=[0]*max(max(l1),max(l2))
symbol1=-1
symbol2=-1
ans=999999999
for i in l1:
    l[i-1]=-1
for i in l2:
    l[i-1]=-2
print(l)
for i in range(len(l)):
    if l[i]==-1:
        symbol1=i
    if l[i]==-2:
        symbol2=i
    if symbol1!=-1 and symbol2!=-1:
        ans=min(ans,abs(symbol2-symbol1))
print(ans)
