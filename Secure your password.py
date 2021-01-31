# To secure the password 

Secure = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))

def securepassword(password):
    for a,b in Secure:
        password = password.replace(a,b)
    return password
if __name__ == "__main__":
    password = input('Enter your password here:- ')
    password = securepassword(password)
    print(f'Your secured password is {password}')
