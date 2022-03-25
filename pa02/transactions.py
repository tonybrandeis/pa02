import sqlite3
#
# here are some helper function to change the query result of database
#

# trans is a transaction tuple (rowid, name, amount, category, date, description)
# Author: Tony Qiu
def to_trans_dict(trans_tuple):
    trans = {'rowid': trans_tuple[0],
             'name': trans_tuple[1],
             'amount': trans_tuple[2],
             'category': trans_tuple[3],
             'date': trans_tuple[4],
             'description': trans_tuple[5]}
    return trans

# convert a list of category tuples into a list of dictionaries
# Author: Tony Qiu
def to_trans_dict_list(trans_tuple):
    return [to_trans_dict(trans) for trans in trans_tuple]


# trans is a transaction tuple (sum_by(date/month/year/cat), total_amount)
# Author: Tony Qiu
def to_sum_trans_dict(trans_tuple):
    trans = {'sum_by': trans_tuple[0],
             'sum': trans_tuple[1]}
    return trans

# convert a list of category tuples into a list of dictionaries
# Author: Tony Qiu
def to_sum_trans_dict_list(trans_tuple):
    return [to_sum_trans_dict(trans) for trans in trans_tuple]


# Transaction Class is DAO for transactions table in sqlite database
# Author: Tony Qiu
class Transaction():
    def __init__(self,dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                       (name text, amount INTEGER, category text, date text, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    # return all of the transactions as a list of dicts.
    # Author: Tony Qiu
    def select_all(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* FROM transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    # add an transactions record into database.
    # Author: Tony Qiu
    def add(self, trans):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)"
                    , (trans['name'], trans['amount'], trans['category'], trans['date'], trans['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    # delete an transactions record by rowid.
    # Author: Tony Qiu
    def delete(self, rowid):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("DELETE FROM transactions WHERE rowid=(?)", (rowid,))
        con.commit()
        con.close()

    # summarize the total amount of transactions by date
    # Author: Tony Qiu
    def summarize_by_date(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date, SUM(amount) AS total_amount FROM transactions
                       GROUP BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_sum_trans_dict_list(tuples)

    # summarize the total amount of transactions by month
    # Author: Tony Qiu
    def summarize_by_month(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT strftime('%m', date) as month, SUM(amount) AS total_amount FROM transactions
                       GROUP BY month''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_sum_trans_dict_list(tuples)

    # summarize the total amount of transactions by year\
    # Author: Tony Qiu
    def summarize_by_year(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT strftime('%Y', date) as year, SUM(amount) AS total_amount FROM transactions
                       GROUP BY year''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_sum_trans_dict_list(tuples)

    # summarize the total amount of transactions by category
    # Author: Tony Qiu
    def summarize_by_cat(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT category, SUM(amount) AS total_amount FROM transactions
                       GROUP BY category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_sum_trans_dict_list(tuples)