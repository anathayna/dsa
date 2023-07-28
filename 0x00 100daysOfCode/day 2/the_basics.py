print("### break, continue, pass ###")

def break_test(arr):
    for i in arr:
        if i == 5:
            break # takes out of the current loop
        print(i)
    print("")

def continue_test(arr):
    for i in arr:
        if i == 5:
            continue # ends the current iteration in the loop and moves to the next iteration
        print(i)
    print("")

def pass_test(arr):
    pass # does nothing. can be used when a statement is required. syntactically but the program requires no action

arr = [1, 3, 4, 5, 6, 7]
break_test(arr)
continue_test(arr)
pass_test(arr)



print("### map, filter, lambda ###")

items = [1, 2, 3, 4, 5]

cubes = list(map(lambda x: x**3, items))
print(cubes)
print((lambda x: x**2)(5))
print((lambda x, y: x*y)(3, 4))

number_list = range(-10, 10)
less_than_five = list(filter(lambda x: x < 5, number_list))
print(less_than_five)