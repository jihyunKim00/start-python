# 함수

def factorial(number):
    count = number -1 
    while count >=2:
        number = number * count 
        count = count -1 
    return(number) 

def say_hello():
    print("안녕!")
    print("Hello!")

say_hello()
say_hello()

print(factorial(21))
print(factorial(13))
print(factorial(8))
