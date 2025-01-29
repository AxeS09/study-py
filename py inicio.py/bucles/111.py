#uso de operaciones comparacion y operaciones logicas-------con condicionales de seleccion 
age=int(input())
if age  < 18: print("discount")  #primera condicion 
elif age >= 75:   #comprovar otra condicion
    print("senior discount")
else:   #sisque no se cumplen 
    print("regular price")