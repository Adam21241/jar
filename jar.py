import sqlite3
from datetime import datetime
import logging

from consts import to_usd_converter
from consts import jars_creation_query
from consts import transactions_creation_query


logging.basicConfig(level=logging.INFO)


class Jar:

    con = sqlite3.connect('jar.db')
    cur = con.cursor()
    jars = {}

    def initialize_db() -> None:
        """
        Creates empty tables (jars, transactions) if they do not exist.
        """

        Jar.cur.execute(jars_creation_query)
        Jar.cur.execute(transactions_creation_query)
        Jar.con.commit()

    def check_existence_in_db(id) -> bool:
        """
        Checks if jar with given id exists in db.
        """

        if Jar.cur.execute(
            "select id from jars where id = ?",
            (id, )
        ).fetchall():
            return True

        else:
            return False

    def __init__(
        self, id, balance=None, currency=None, is_in_db=False
    ) -> None:

        if is_in_db:
            logging.info(
                f"Jar {id} already exists in db!"
            )

            jar = Jar.cur.execute(
                "select * from jars where id = ?",
                (id, )
            ).fetchall()[0]

            self.id = jar[0]
            self.balance = jar[1]
            self.currency = jar[2]

            logging.info(f"Jar {id} added into dict!")

        else:
            self.id = id
            self.balance = balance
            self.currency = currency

            Jar.cur.execute(
                (
                    'insert into jars (id, balance, currency) '
                    'values (?, ?, ?)'
                ),
                (self.id, self.balance, self.currency)
            )
            Jar.con.commit()

            logging.info(f"Jar {id} added into dict and saved into db!")

    def set_currency(self, currency: str) -> None:
        self.balance = \
            self.balance * to_usd_converter[self.currency] / \
            to_usd_converter[currency]
        self.currency = currency

        Jar.cur.execute(
            'update jars set currency = ? where id = ?',
            (currency, self.id)
        )
        Jar.cur.execute(
            'update jars set balance = ? where id = ?',
            (self.balance, self.id)
        )
        Jar.con.commit()

        logging.info((
            "Successfully changed currency in jar "
            f"{self.id} into {self.currency}"
        ))

    def transfer(self, Jar, amount: float) -> None:
        """
        Send money into other jar.
        """

        if self.currency != Jar.currency:
            logging.error((
                f"Transaction failed because the {self.currency} "
                f"currency is not set in jar {Jar.id}!"
            ))

        else:
            if self.balance - amount < 0:
                logging.error((
                    f"Not enough balance in jar {self.id} "
                    "to perform this operation!"
                ))
            else:
                self.balance -= amount
                Jar.balance += amount

                Jar.cur.execute(
                    'update jars set balance = ? where id = ?',
                    (self.balance, self.id)
                )
                Jar.cur.execute(
                    'update jars set balance = ? where id = ?',
                    (Jar.balance, Jar.id)
                )
                Jar.cur.execute(
                    (
                        'insert into transactions '
                        '(sender, receiver, amount, currency, date) '
                        'values (?, ?, ?, ?, ?)'
                    ),
                    (
                        self.id,
                        Jar.id,
                        amount,
                        self.currency,
                        datetime.now()
                    )
                )
                Jar.con.commit()

                logging.info((
                    f"Successfully transferred {amount} {self.currency} "
                    f"from jar {self.id} into jar {Jar.id}!"
                ))
                logging.info((
                    f"Balance after transaction in jar {self.id} "
                    f"(sender): {self.balance} {self.currency}"
                ))
                logging.info((
                    f"Balance after transaction in jar {Jar.id} "
                    f"(receiver): {Jar.balance} {Jar.currency}"
                ))

    def close_connection() -> None:
        Jar.con.close()
        logging.info("Successfully closed connection with db!")
