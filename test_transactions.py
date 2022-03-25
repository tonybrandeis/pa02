"""
test_transactions runs tests for each method in transactions.py
"""

import pytest
from transactions import Transaction, to_trans_dict
import random


@pytest.fixture
def dbfile(tmpdir):
    """ create a database file in a temporary file system """
    return tmpdir.join('test_transactions.db')


@pytest.fixture
def empty_db(dbfile):
    """ create an empty database """
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    """create a small database, and tear it down later"""
    trans_1 = {'rowid': 1,
               'name': 'A',
               'amount': 54,
               'category': 'food',
               'date': '20220315',
               'description': 'dine'}
    trans_2 = {'rowid': 2,
               'name': 'B',
               'amount': 72,
               'category': 'fun',
               'date': '20220317',
               'description': 'race car'}
    trans_3 = {'rowid': 3,
               'name': 'C',
               'amount': 108,
               'category': 'food',
               'date': '20220318',
               'description': 'grocery'}
    id1 = empty_db.add(trans_1)
    id2 = empty_db.add(trans_2)
    id3 = empty_db.add(trans_3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)


@pytest.fixture
def med_db(small_db):
    """ create a database with 10 more elements than small_db"""
    rowids = []
    categories = ['food', 'fun', 'home', 'car', 'edu']
    # add 10 transcations
    random.seed(42)
    for i in range(10):
        s = str(i)
        trans = {'rowid': 4 + i,
                 'name': 'name' + s,
                 'amount': random.randint(15, 250),
                 'category': categories[random.randint(0, 4)],
                 'date': '202203' + str(random.randint(10, 31)),
                 'description': 'description' + s}
        rowid = small_db.add(trans)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])


@pytest.mark.simple
def test_to_trans_dict():
    ''' teting the to_cat_dict function '''
    a = to_trans_dict((7, 'K', 188, 'food', '20220319', 'kkkk'))
    assert a['rowid'] == 7
    assert a['name'] == 'K'
    assert a['amount'] == 188
    assert a['category'] == 'food'
    assert a['date'] == '20220319'
    assert a['description'] == 'kkkk'
    assert len(a.keys()) == 6


@pytest.mark.add
def test_add(med_db):
    """ add a category to db, the select it, then delete it"""
    trans0 = {'rowid': 7,
              'name': 'K',
              'amount': 188,
              'category': 'food',
              'date': '20220319',
              'description': 'kkkk'}
    trans_0 = med_db.select_all()
    rowid = med_db.add(trans0)
    trans_1 = med_db.select_all()
    assert len(trans_1) == len(trans_0) + 1


@pytest.mark.delete
def test_delete(med_db):
    """ add a category to db, delete it, and see that the size changes"""
    # first we get the initial table
    trans0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    sample = {'rowid': 7,
              'name': 'K',
              'amount': 188,
              'category': 'food',
              'date': '20220319',
              'description': 'kkkk'}
    rowid = med_db.add(sample)
    trans1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    trans2 = med_db.select_all()
    assert len(trans0) == len(trans2)
    assert len(trans2) == len(trans1) - 1


@pytest.mark.date
def test_summarize_by_date(med_db):
    """test summarize_by_date using med_db"""
    test = med_db.summarize_by_date()
    print(test)
    assert test[0]['sum'] == 178  # 'sum_by': '20220310'
    assert test[3]['sum'] == 72  # 'sum_by': '20220313'


@pytest.mark.month
def test_summarize_by_month(med_db):
    """test summarize_by_month using med_db"""
    test = med_db.summarize_by_month()
    print(test)
    assert test[0]['sum'] == 1428


@pytest.mark.year
def test_summarize_by_year(med_db):
    """test summarize_by_year using med_db"""
    test = med_db.summarize_by_year()
    print(test)
    assert test[0]['sum'] == 1428


@pytest.mark.year
def test_summarize_by_cat(med_db):
    """test summarize_by_cat using med_db"""
    test = med_db.summarize_by_cat()
    print(test)
    assert test[0]['sum'] == 237  # 'sum_by': 'car'
    assert test[2]['sum'] == 362  # 'sum_by': 'food'
