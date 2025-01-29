l=  'sabic'

x=[l,"sarto", 23423, 2.222]

# n elementos ---f--- lent()---for a sequence no only in the list

print(len(l)) 
print(len(x))

#new element in the  end of list......only in the list ---f---.append()

x .append(2222)
print(x[4])

#new element in a position specific

x .insert(2, "massif")
print(x[2])

print(x)

#elimina a element in the list 

x.pop(2)
print(x)