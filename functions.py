from consts import to_usd_converter
import logging

from jar import Jar


def check_positiveness(input, type: str) -> bool:
    """
    Check if input is convertible
    into positive number or not
    """
    try:
        if type == "int":
            if int(input) >= 0:
                return True
        elif type == "float":
            if float(input) >= 0:
                return True
    except ValueError:
        return False
    return False


def validate(value, kind) -> bool:
    """
    Check if id / balance / amount / currency
    is given in proper format
    """
    if kind == "id":
        if check_positiveness(value, "int"):
            return True

    elif (kind == "balance") or (kind == "amount"):
        if check_positiveness(value, "float"):
            return True

    elif kind == "currency":
        if value in to_usd_converter.keys():
            return True

    return False


def read_id(kind=None):
    print("")
    if kind:
        print(f"[{kind.upper()}] ", end="")

    print("Type jar id:")
    id = input()
    if validate(id, "id"):
        return int(id)
    else:
        logging.warning("Id must be positive integer!")
        return None


def read_balance():
    print("\nType initial jar balance:")
    balance = input()
    if validate(balance, "balance"):
        return float(balance)
    else:
        logging.warning((
            "Balance must be positive float! "
            "Set balance to 0 (default value)"
        ))
        return 0


def read_amount():
    print("\nType amount to transfer:")
    amount = input()
    if validate(amount, "amount"):
        return float(amount)
    else:
        logging.warning((
            "Amount must be positive float! "
        ))
        return None


def read_currency(return_default=True):
    print("\nType jar currency:")
    currency = input()
    if validate(currency, "currency"):
        return currency
    else:
        logging.warning(
            "Currency does not exist or is not supported!"
        )
        if return_default:
            logging.info("Set currency to USD (default value)")
            return "USD"
        else:
            return None


def add_jar(id, balance=None, currency=None, to_db=False) -> bool:
    if not Jar.jars.get(id):
        if not Jar.check_existence_in_db(id):
            if to_db:
                Jar.jars[id] = Jar(
                    id=id,
                    balance=balance,
                    currency=currency,
                    is_in_db=False
                )
            else:
                logging.info("Jar does not exist in db!")
                return False
        else:
            Jar.jars[id] = Jar(
                id=id,
                is_in_db=True
            )
    else:
        logging.info("Jar already exists in dict!")
    return True
