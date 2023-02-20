name = input("Please enter your name: ")
print("name: " + name)

age = input("Please enter your age: ")
print("age: " + age)

# group members, the next task is "do something with this input." Create a pull request with code that will do something

if int(age) < 16:
    print("Sorry you are to young to drive, " + name)
else:
    print("Enjoy your drive, " + name)