n = int(input('Enter the no of fibonacci terms you want: '))

def fibonacci(n):
    a = 0
    b = 1
    print(a)

    for i in range(n-1):
        a = a+b
        b = a-b
        if a % 2 == 0 :
            print(a)
fibonacci(n)

#a;;amf;m;
