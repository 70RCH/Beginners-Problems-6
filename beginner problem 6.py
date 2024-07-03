#Is it a Triangle?
def triangleTest():
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b > c and a + c > b and b + c > a:
        print ("It is a Triangle")
    else:
        print ("It is not a Triangle")

triangleTest()

#Greetings!
def good_morning(name):
    print(f"Good morning, {name}!")

def good_afternoon(name):
    print(f"Good afternoon, {name}!")

def good_evening(name):
    print(f"Good evening, {name}!")

def greet_user():
    name = input("What’s your name: ")
    time = float(input("What time is it (24 hour format, e.g., 17.59): "))

    hour = int(time)
    
    if 0 <= hour < 13:
        good_morning(name)
    elif 13 <= hour < 18:
        good_afternoon(name)
    elif 18 <= hour < 24:
        good_evening(name)
    else:
        print("Invalid time entered.")

greet_user()

#Even Numbers
def getEven():
    nums = list(map(int, input().split()))
    evens = [num for num in nums if num % 2 == 0]
    return evens

evens = getEven()
print("Even numbers in the list are:", evens)