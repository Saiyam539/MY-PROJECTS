num1 = int(input('Enter the first number:- '))
num2 = int(input('Enter the second number:- '))

if num2>num1:
    min = num1
else:
    min = num2

for i in range(1, min+1):
    if num1%i==0 and num2%i==0:
        HCF = i

print(f'The HCF of {num1} and {num2} is {HCF}')