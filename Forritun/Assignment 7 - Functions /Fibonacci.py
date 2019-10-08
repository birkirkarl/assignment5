def fibo(x):
    array=[1,1]
    if x!=1:
        for i in range(2,x):
            tala=(array[i-2])+(array[i-1])
            array.append(tala)
        for n in range(0, len(array)):
            print(array[n], end=' ')
    else:
        print(x)

n = int(input("Input the length of Fibonacci sequence (n>=1): "))

fibo(n)