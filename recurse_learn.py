
def fib(num):
    if num == 0 or num == 1:
        return 1
    return fib(num-2) + fib(num-1)

if __name__ == '__main__':
    print(fib(4))