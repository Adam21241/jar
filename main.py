from functions import add_jar, read_id
from functions import read_balance
from functions import read_currency
from functions import read_amount
from jar import Jar


if __name__ == "__main__":

    Jar.initialize_db()
    x = 0

    while x != "-1":
        print("\nType 0 to create new jar")
        print("Type 1 to check balance and currency of given jar")
        print("Type 2 to change currency in given jar")
        print("Type 3 to transfer money")
        print("Type -1 to terminate")

        x = input()

        if x == "0":
            id = read_id()
            if not id:
                continue
            balance = read_balance()
            currency = read_currency()

            if not add_jar(id, balance, currency, to_db=True):
                continue

        if x == "1":
            id = read_id()
            if not id:
                continue

            if not add_jar(id):
                continue

            print(f"\nBalance for jar {id} = {Jar.jars[id].balance}")
            print(f"Currency for jar {id} = {Jar.jars[id].currency}")

        if x == "2":
            id = read_id()
            if not id:
                continue

            if not add_jar(id):
                continue

            currency = read_currency(return_default=False)
            if not currency:
                continue

            Jar.jars[id].set_currency(currency)

        if x == "3":
            sender_id = read_id(kind="sender")
            if not sender_id:
                continue
            if not add_jar(sender_id):
                continue

            receiver_id = read_id(kind="receiver")
            if not receiver_id:
                continue
            if not add_jar(receiver_id):
                continue

            amount = read_amount()
            if not amount:
                continue

            Jar.jars[sender_id].transfer(
                Jar.jars[receiver_id],
                amount
            )

        if x == "-1":
            Jar.close_connection()
            print("\nThank you for using program. Bye!")
            break


# TODO
# simple unit tests
# prepare checks, especially flake
