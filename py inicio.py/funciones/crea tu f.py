def hey (name):    #f personalizada con o sin argumento 
    print(3432, name)
    print('baby')

hey("james") #llama tu f, y coloca el nombre--(variable  o dato que se reenplace en el esapacio)-- al que quieres reenplace

#--f ---2----------(+)(-)(*)(/)...
def calculator(number):
    print(number+222)
# option 1------------   

# x=int(input())
# calculator(x)
# print(x)

#option 2---------------
print(calculator(int(input())))

#--f--3---

def bmi(weight, height):
    idex=(weight) / (height*weight)
    print(idex)

print(bmi((int(input(  ))), ((int(input(  ))))))

#valor predetermined del argumento ---si no le da un  argumnento pondra el predeterminado
def greet(name="--invitado--" ):
    print("venvenido--->", name)

print(greet()) #sin valor