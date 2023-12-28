# collections


def greet():
    def decorator():
        print('welcome')
        hello()
        print('thank you')

        return decorator

def hello():
    print('hello world')

nums = [2,4,3,5,6,8]

it=iter(nums)
"""this is only for practice"""
for i in nums:
    print(i)

def fun(n):
    a=n
    if(a%2==0):
        print("even")
    else:
        print("odd")
    

              