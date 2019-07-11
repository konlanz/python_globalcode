def get_name():
    name = input("whats your name ? ")
    print(name)
    return name
    



def get_age():
    age = int(input("what's your age "))
    print(age)
    return(age)


def calculate(sadd, x, z):
    add = x + z
    print(add)
    return add


get_age()
get_name()
calculate("hello", 40,60)