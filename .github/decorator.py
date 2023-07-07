def greet(fn):
    def decorator():
        print('welcome')
        fn()
        print('thank you')

    return decorator
@greet
def hello():
    print('hello world')


hello()