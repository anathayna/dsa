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

# in multiple arguments, map() returns a list of tuples containing the corresponding items from all iterables
cubes = list(map(lambda x: x**3, items)) # map(funcao, sequencia) applies to every member of iterable and returns the result
print(cubes)
print((lambda x: x**2)(5)) # inline function
print((lambda x, y: x*y)(3, 4))

number_list = range(-10, 10)
less_than_five = list(filter(lambda x: x < 5, number_list)) # takes a function returning True or False and applies it to a sequence
print(less_than_five) # returning a list of only those members of the sequence for which the function returned True

x = [2, 3, 4, 5, 6]
y = []

for v in x:
    if v % 2:
        y += [v*5]

print(y)

y = list(map(lambda v: v*5, filter(lambda u: u % 2, x))) # using lambda and map you can have two for loops in one line
print(y)

def double_numbers(num):
    return num * 2

nums = [1, 2, 3, 4, 5]
result = map(double_numbers, nums)
result_list = list(result)
print(result_list)

result = map(lambda x: x*2, nums)
result_list = list(result)
print(result_list)

print("\n")