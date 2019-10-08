s = str(input('Enter a sentence: '))
upper=0
lower=0
digits=0
bil=0
for i in range(0, len(s)):
    if s[i].isdigit():
        digits=digits+1
    if s[i].isupper():
        upper=upper+1
    elif s[i].islower():
        lower=lower+1
    elif s[i].isspace():
        bil=bil+1

punctuation=len(s)-upper-lower-digits-bil
print('{:>15}'.format('Upper case')+'{:>6}'.format(upper))
print('{:>15}'.format('Lower case')+'{:>6}'.format(lower))
print('{:>15}'.format('Digits')+'{:>6}'.format(digits))
print('{:>15}'.format('Punctuation')+'{:>6}'.format(punctuation))
