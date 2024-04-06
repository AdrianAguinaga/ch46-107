# let varname = 1;
# const varname = 1;
variable = ""
varname = 2
varstring = "adrian"
print(varstring + str(varname))
# adrian2
# if(varstring == "adrian")
# {
# }

age = 37
if age < 30:
    print("youre young")
elif age > 30:
    print("no worrys youre still young")
else:
    print("i dont know how you get here")
    
#array
#const colors = ["red", "green", "blue"];
#list
colors = ["red", "green", "blue"]
print(colors)
colors.append("yellow")
print(colors)
colors.remove("red")
print(colors)
print(colors[1])

# for(int i = 0; i <colors.length; i++)
#   let color = colors[i];
#   console.log(color);

for x in colors:
    print(x)

#dictionarys
me = {
    "first_name": "John",
    "last_name":"Doe",
    "age": 21,
}
print(me)
#get a value
print(me["first_name"])
me["age"]=99
me["favorite_color"]="blue"
print(me)

#fuctions
def say_hello():
    print("hello")

def say_goodbye(name, age):
    print("goodbye "+name+ " " + str(age))

#call fuctions
say_hello()
say_goodbye("John Doe",32)

#fuctions
def print_menu():
    print("1)sum")
    print("2)substraction")
    print("3)multiplication")
    print("4)division")
    
#instructions
print_menu()
opt = int(input("Choose an option: "))
num1 = float(input("please provideme the first number:"))
num2 = float(input("please provideme the second number:"))

if opt == 1:
    total = num1 + num2
    print("the sum of those numbers is "+str(total))
elif opt == 2:
    total = num1 - num2
    print("the substractions of those numbers is "+str(total))
elif opt == 3:
    total = num1 * num2
    print("the multiplications of those numbers is "+str(total))
elif opt == 4:
    if num2 == 0:
        print("you cannot divide by zero")
    else:
        total = num1/num2
        print("the division of those numbers is "+str(total))

# create the rest of the logic for the calculator