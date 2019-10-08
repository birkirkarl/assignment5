num = int(input('Enter an integer: '))
if num > 0:
    cumtotal = 0
    even = 0
    odd = 0
    largest = 0
    while num > 0:
        cumtotal = cumtotal + num
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        if num > largest:
            largest = num
        print('Cumulative total:', cumtotal)
        num = int(input('Enter an integer: '))
    print('Largest number:', largest)
    print('Count of even numbers:', even)
    print('Count of odd numbers:', odd)