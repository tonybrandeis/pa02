#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from transactions import Transaction
from category import Category
import sys

transaction = Transaction('tracker.db')
category = Category('tracker.db')

# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''


def process_choice(choice):
    if choice == '0':
        return
    elif choice == '1':
        cats = category.select_all()
        print_categories(cats)
    elif choice == '2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name': name, 'desc': desc}
        category.add(cat)
    elif choice == '3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name': name, 'desc': desc}
        category.update(rowid, cat)
    elif choice == '4':
        # print("show transactions")
        trans = transaction.select_all()
        print_transcations(trans)
    elif choice == '5':
        name = input("transaction name: ")
        amount = input("transaction amount: ")
        trans_category = input("category name: ")
        date = input("date (yyyy-mm-dd): ")
        desc = input("transaction description: ")
        trans = {'name': name,
                 'amount': amount,
                 'category': trans_category,
                 'date': date,
                 'description': desc}
        transaction.add(trans)
    elif choice == '6':
        print("delete transaction")
        rowid = int(input("rowid: "))
        confirm = input("delete record-%s? (y/n): " % rowid)
        if confirm == 'y':
            transaction.delete(rowid)
    elif choice == '7':
        trans = transaction.summarize_by_date()
        print_sum_transcations('Date', trans)
    elif choice == '8':
        trans = transaction.summarize_by_month()
        print_sum_transcations('Month', trans)
    elif choice == '9':
        trans = transaction.summarize_by_year()
        print_sum_transcations('Year', trans)
    elif choice == '10':
        trans = transaction.summarize_by_cat()
        print_sum_transcations('Category', trans)
    elif choice == '11' or choice=='h' or choice == 'help':
        print(menu)
    else:
        print("choice", choice, "not yet implemented")

    choice = input("> ")
    return (choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice != '0':
        choice = process_choice(choice)
    print('bye')


#
# here are some helper functions of formatted output
#
def print_transactions(items):
    ''' print the transactions '''
    if len(items) == 0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10d %-10s %-10d %-30s" % (
        'item #', 'amount', 'category', 'date', 'description'))
    print('-' * 40)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10d %-10s %-10d %-30s" % values)


def print_category(cat):
    print("%-3d %-15s %-30s" % (cat['rowid'], cat['name'], cat['desc']))


def print_categories(cats):
    print("%-3s %-15s %-30s" % ("id", "name", "description"))
    print('-' * 45)
    for cat in cats:
        print_category(cat)


def print_transcation(trans):
    print("%-3d %-15s %-10s %-15s %-15s %-30s"
          % (trans["rowid"], trans["name"], trans["amount"], trans["category"], trans["date"], trans["description"]))


def print_transcations(trans_ls):
    print("%-3s %-15s %-10s %-15s %-15s %-30s"
          % ("id", "name", "amount", "category", "date", "description"))
    print('-' * 80)
    for trans in trans_ls:
        print_transcation(trans)

def print_sum_transcation(trans):
    print("%-15s %-10s"
          % (trans["sum_by"], trans["sum"]))


# output the summarize result of trascations, `sum_by` is the summarize conditation
def print_sum_transcations(sum_by, trans_ls):
    print("%-15s %-10s"
          % (sum_by, "total_amount"))
    print('-' * 30)
    for trans in trans_ls:
        print_sum_transcation(trans)


# here is the main call!

toplevel()