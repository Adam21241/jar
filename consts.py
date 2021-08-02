jars_creation_query = '''
    create table if not exists jars
    (id INTEGER, balance REAL, currency TEXT)
'''

transactions_creation_query = '''
    create table if not exists transactions
    (sender INTEGER, receiver INTEGER, amount REAL, currency TEXT, date TEXT)
'''

to_usd_converter = {
    "USD": 1,
    "GBP": 1.25,
    "EUR": 1.1,
    "PLN": 0.25
}
