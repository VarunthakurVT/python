# if you are creating the empty set so 
emptyset=set()

# if you are creating set with values do 
s={1,(1.1,),2,3,4,5,6}

print(type(s))
other_set={1,2,3,4,8,9,10}

print(s & other_set) #this is for the interestion 

print(s|other_set) #this is for union 
s_copy=s.copy()
s.pop()
print(s)