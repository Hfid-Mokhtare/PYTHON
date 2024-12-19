# how to make a global variable

global_variable = 10

def my_function():
    global global_variable
    global_variable += 5
    print(global_variable)

my_function()  # Output: 15
print(global_variable)  # Output: 15
