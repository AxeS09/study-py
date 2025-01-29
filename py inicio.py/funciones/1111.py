def bmi(weight, height):
    idex=(weight) / (height*height)
    return idex
p6=bmi(79, 1.73)
print(p6<18.5)

#retorno varios valores

def rect (leith, width):
    area= leith * width
    perimeter= 2* leith + 2 * width
    return area, perimeter
x, y= rect(45, 80)
print(x,y)