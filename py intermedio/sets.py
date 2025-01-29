alar={1, "boll", True, 2.33}

alar.add(66) #new element 
alar .remove(True) #removed element

print(alar)

alar.clear()#elimina todos elementos 
print(alar)

#une 2 sets --ignored the duplicate  elements ---f---.union()
si=434
set2={"sii", si, 34, 1, True, 2}

new_set= alar .union(set2)
print(new_set)

#elements that are in the set 1 an not in th set 2 ====f===.difference()

set1={"apple","banana","cherry"}
set3={"banana","orange"}
uni= set1.difference(set3)
print(uni) 

