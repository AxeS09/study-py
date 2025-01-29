er ={
    "barn":"siu",
    "car":"pe",
    "simon": 55
}

s=er.get("car")
print(s)

ola=er.items()
print(ola)

o=er.values()
p=er.keys()

print(o,p)


er.update({"simon":5,"wasp":2})
print(er)


er.pop("car")
print(er)


print("car" in er)