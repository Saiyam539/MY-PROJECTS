def FindLastTerm():
    a = int(input('Enter the first number here:- '))
    n = int(input('Enter the number of terms in AP:- '))
    d = int(input('Enter the common difference here:- '))

    print(f'The last term of the AP is {a + (n-1)*d}')

def FindCommonDiffer():
    an = int(input('Enter the last term of AP:- '))
    a = int(input('Enter the first number of AP:- '))
    n = int(input('Enter the number of terms in AP:- '))

    print(f'The comman difference of AP is {(an - a)/(n-1)}')

def FindNumberOfTerm():
    an = int(input('Enter the last term of AP:- '))
    a = int(input('Enter the first number of AP:- '))
    d = int(input('Enter the common difference here:- '))

    print(f'The number of terms in this AP is {((an-a)/d)+1}')

try:
    if __name__ == "__main__":
        welcome = '''*****WELCOME TO THE AP CALCULATOR*****
        1.Find last term
        2.Find common difference
        3.Find number of terms
        4.Exit
        '''
        print(welcome)
        a = int(input('Enter your choice here:- '))

        if a==1:
            FindLastTerm()
        elif a==2:
            FindCommonDiffer()
        elif a==3:
            FindNumberOfTerm()
        elif a==4:
            exit()
        else:
            print('Please enter a valid number.')
except ValueError as e:
    print('Please enter a valid number.')