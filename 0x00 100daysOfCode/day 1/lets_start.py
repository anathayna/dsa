# a simple output
print("hello, world! hello, 🐍!\n") # time complexity: O(1)



print("### variables ###")

number = 3
print(number)

string = "hello"
print(string+"\n")



print("### conditions ###")

a = 3
b = 9

if b % a == 0 :
    print("b is divisible by a\n")
elif b + 1 == 10 :
    print("increment in b produces 10\n")
else:
    print("you're in else statement\n")



print("### functions ###")

def check_divisibility(a, b):
    if a % b == 0 :
        print("a is divisible by b")
    else:
        print("a is not divisible by b")

check_divisibility(4, 2)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print("\n")

fib(100)



print("### strings ###")

a = 'this is a string'
print(a)
b = "this is a string"
print(b)
c = '''this is a string\n'''
print(c)

c = '''strings are immutable'''



print("### list ###") # data structures aka arrays

nums = [] # sequenced data types

nums.append(21)
nums.append(42.5)
nums.append("string")

print(nums)
print("\n")