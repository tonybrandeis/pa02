CS103a PA02 Finance Tracker
===
This program simulates a finance tracker with a suite of tests.

- ```transcations.py``` store financial transactions with the
  fields ```'item #','amount','category','date','description'```
  . It also implements functions to add, delete and summarize transactions.
- ```tracker.py```  contains the user interface code, which calls to the Transaction class to add transactions, find
  transactions, delete transactions, summarize transactions, etc.
- ```test_transaction.py``` contains the pytest to test methods in ```transcations.py```.

### pylint script

```angular2html
$ pylint transactions.py
************* Module transactions
transactions.py:69:0: C0301: Line too long (111/100) (line-too-long)
transactions.py:103:0: C0301: Line too long (106/100) (line-too-long)
transactions.py:115:0: C0301: Line too long (105/100) (line-too-long)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:42:0: C0115: Missing class docstring (missing-class-docstring)
transactions.py:54:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:79:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:88:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:100:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:112:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:124:4: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 7.87/10

$ pylint test_transactions.py
************* Module test_transactions
test_transactions.py:17:13: W0621: Redefining name 'dbfile' from outer scope (line 11) (redefined-outer-name)
test_transactions.py:19:4: C0103: Variable name "db" doesn't conform to snake_case naming style (invalid-name)
test_transactions.py:24:13: W0621: Redefining name 'empty_db' from outer scope (line 17) (redefined-outer-name)
test_transactions.py:54:11: W0621: Redefining name 'small_db' from outer scope (line 24) (redefined-outer-name)
test_transactions.py:61:8: C0103: Variable name "s" doesn't conform to snake_case naming style (invalid-name)
test_transactions.py:81:4: C0103: Variable name "a" doesn't conform to snake_case naming style (invalid-name)
test_transactions.py:92:13: W0621: Redefining name 'med_db' from outer scope (line 54) (redefined-outer-name)
test_transactions.py:101:4: W0612: Unused variable 'rowid' (unused-variable)
test_transactions.py:107:16: W0621: Redefining name 'med_db' from outer scope (line 54) (redefined-outer-name)
test_transactions.py:130:27: W0621: Redefining name 'med_db' from outer scope (line 54) (redefined-outer-name)
test_transactions.py:139:28: W0621: Redefining name 'med_db' from outer scope (line 54) (redefined-outer-name)
test_transactions.py:147:27: W0621: Redefining name 'med_db' from outer scope (line 54) (redefined-outer-name)
test_transactions.py:155:26: W0621: Redefining name 'med_db' from outer scope (line 54) (redefined-outer-name)
test_transactions.py:7:0: C0411: standard import "import random" should be placed before "import pytest" (wrong-import-order)

-----------------------------------
Your code has been rated at 8.08/10

$ pylint tracker.py
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:120:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:153:0: C0301: Line too long (117/100) (line-too-long)
tracker.py:43:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:62:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:99:24: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:114:9: R1714: Consider merging these comparisons with "in" to "choice in ('11', 'h', 'help')" (consider-using-in)
tracker.py:61:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:61:0: R0912: Too many branches (14/12) (too-many-branches)
tracker.py:61:0: R0915: Too many statements (51/50) (too-many-statements)
tracker.py:125:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:138:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:139:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:142:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:143:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:151:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:152:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:158:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:159:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:168:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:169:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:175:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:176:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:36:0: W0611: Unused import sys (unused-import)
tracker.py:36:0: C0411: standard import "import sys" should be placed before "from transactions import Transaction" (wrong-import-order)

-----------------------------------
Your code has been rated at 7.01/10
```

### pytest script

```angular2html
$ python tracker.py

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

> 2
category name: food
category description: dine or grocery
> 2
category name: fun
category description: recreational activities
> 5
transaction name: A
transaction amount: 54
category name: food
date (yyyy-mm-dd): 20220315
transaction description: dine
> 5
transaction name: B
transaction amount: 72
category name: fun
date (yyyy-mm-dd): 20210214
transaction description: race car
> 5
transaction name: C
transaction amount: 108
category name: food
date (yyyy-mm-dd): 20220117
transaction description: grocery
> 1
id  name            description
---------------------------------------------
1   food            dine or grocery
2   fun             recreational activities
> 4
id  item #          amount     category        date            description
--------------------------------------------------------------------------------
1   A               54         food            20220315        dine
2   B               72         fun             20210214        race car
3   C               108        food            20220117        grocery
> 7
Date            total_amount
------------------------------
20210214        72
20220117        108
20220315        54
> 8
Month           total_amount
------------------------------
None            234
> 9
Year            total_amount
------------------------------
None            234
> 10
Category        total_amount
------------------------------
food            162
fun             72
> 0
bye
```





