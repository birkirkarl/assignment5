integer=int(input('Write an integer:'))
quotient=0
remainder =0
milli=integer



while integer > 0:
    quotient=int(integer/2)
    if integer%2 != 0:
        remainder= (round(integer-int(quotient)*2, 0))
    print(integer,'divided by 2 gives the quotient',int(quotient),' and remainder',remainder,'.')
    integer=quotient

    
