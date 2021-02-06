class store:
    @staticmethod
    def getproduct():
        product = ['Shampoo', 'Chocolate', 'Books', 'Dal', 'Tooth paste']
        for a in range(len(product)):
            print(product[a])
            a = a + 1

    @staticmethod
    def buyproduct():
        product = ['shampoo', 'chocolate', 'books', 'dal', 'tooth paste']
        n = input('Enter the name of the product you want to buy:- ')
        if n in product:
            print('Thanks for buying this product!!')
            product.remove(n)
            return True
        elif n not in product:
            print(f'{n} is not avalable please check later.')
            return False

    @staticmethod
    def getprice():
        name = input('Enter the product of which you want to know the price:- ')
        if name=='shampo':
            print(f'The price of Shampo is {300}RS')
        elif name=='chocolate':
            print(f'The price of Chocolate is {40}RS')
        elif name=='books':
            print(f'The price of Book is {600}RS')
        elif name=='dal':
            print(f'The price of Dal is {200}RS')
        elif name=='tooth paste':
            print(f'The price of Tooth paste is {300}RS')
        else:
            print('This product is not in stock.')

try:
    if __name__ == "__main__":
        while True:
            welcome = '''*****WELCOME TO THE SAIYAM's STORE*****
            choose what do you want to do:- 
            1.List all products
            2.Buy a product
            3.Read the price of products
            4.Exit store
            '''
            print(welcome)
            a = int(input('Enter your choice here:- '))
            if a==1:
                store.getproduct()
            elif a==2:
                store.buyproduct()
            elif a==3:
                store.getprice()
            elif a==4:
                exit()
            else:
                print('Please enter a valid number.')

except Exception as e:
    print('Please enter a valid number.')    
