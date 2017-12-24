# This is a program to run a book shop

# Created for Python 3.6.2

# Imports

# Non user-accessible functions

# User accessible functions

def buy_book():
    transaction = False
    book_number = 1
    running_cost = 0
    while transaction != True:

        completed_purchase = False # So the program loops until the purchase is confirmed
        while completed_purchase != True:
            print('Book number', book_number)
            book_author = input('Author: ')
            book_title = input('Title: ')
            book_price = float(input('Price: £'))

            print('') # Purely for aesthetics for the user

            print('Author: ', book_author)
            print('Title: ', book_title)
            print('Price: £{0:.2f}'.format(book_price))

            detail_confirmation = input('Are these details correct? Y/N: ').upper()

            if detail_confirmation == 'Y':
                completed_purchase = True
                book_number += 1
                running_cost += book_price
                print('Running cost: £{0:.2f}'.format(running_cost))
                while True:
                    completed_transaction = input('Do you want to buy another book? Y/N: ').upper()
                    if completed_transaction == 'Y':
                        transaction = False
                        break
                    elif completed_transaction == 'N':
                        transaction = True
                        print('Total to pay is £{0:.2f}'.format(running_cost))
                        break
                    else:
                        print('Please enter either Y or N')



# Main program

buy_book()
