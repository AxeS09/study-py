greet= lambda name:'welcome,'+ name
print(greet('boob'))


x=lambda price,count: price*count/price
print(x(20,4))

def mult(n):
    return (lambda a: a*n)(3)

dubber = mult(2)
triple =  mult(3)

print(dubber)

