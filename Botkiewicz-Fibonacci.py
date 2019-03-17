fib = ['1','1','0']
while(int(fib[2]) < 1000):
    fib[2] = int(fib[0]) + int(fib[1])
    print (fib[0], ' + ', fib[1], '= ', fib[2])
    fib[0]=fib[1]
    fib[1]=fib[2]






