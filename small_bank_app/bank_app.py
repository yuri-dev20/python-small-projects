import csv
from datetime import datetime
import pandas as pd


class Bank:
    ACCOUNTS = "accounts.csv"
    ACCOUNTS_COLUMNS = ["name", "sex", "id", "age", "balance"]

    @classmethod
    def initiate_bank(cls):
        try:
            pd.read_csv(cls.ACCOUNTS)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["name", "sex", "id", "age", "balance"])
            df.to_csv(cls.ACCOUNTS, index=False)

    @classmethod
    def register_account(cls, name, sex, id, age, balance=None):
        with open(cls.ACCOUNTS, mode="a", newline="") as file:
            new_account = {
                "name": name,
                "sex": sex,
                "id": id,
                "age": age,
                "balance": balance
            }

            csv_writer = csv.DictWriter(
                file,
                fieldnames=cls.ACCOUNTS_COLUMNS)

            csv_writer.writerow(new_account)

    @classmethod
    def verify_id(cls, id):
        user_data = pd.read_csv(cls.ACCOUNTS)

        valid_id = user_data[user_data["id"] == id]
        if valid_id.empty:
            return False
        else:
            return True

    @classmethod
    def remove_account(cls, id):
        user_data = pd.read_csv(cls.ACCOUNTS)

        user_data.drop(user_data[user_data["id"] ==
                       id].index, axis=0, inplace=True)

        user_data.to_csv(cls.ACCOUNTS, index=False)
        print(user_data)

    @classmethod
    def show_account_info(cls, id):
        user_data = pd.read_csv(cls.ACCOUNTS)

        user = user_data[user_data["id"] == id]
        print(user)

    @classmethod
    def show_accounts(cls):
        user_data = pd.read_csv(cls.ACCOUNTS)
        print(user_data)

    @classmethod
    def deposit(cls, id, amount):
        print()

        user_data = pd.read_csv(cls.ACCOUNTS)
        user_data.loc[user_data["id"] == id, "balance"] += amount
        user_data.to_csv(cls.ACCOUNTS, index=False)

    @classmethod
    def extract(cls, id, amount):
        print()

        user_data = pd.read_csv(cls.ACCOUNTS)
        user_data.loc[user_data["id"] == id, "balance"] -= amount
        user_data.to_csv(cls.ACCOUNTS, index=False)

    @classmethod
    def edit_my_account(cls, id, name, sex, age):
        print()

        user_data = pd.read_csv(cls.ACCOUNTS)
        if not name == "" and not name == 0:
            user_data.loc[user_data["id"] == id, "name"] = name
        if not sex == "" and not sex.isdigit():
            user_data.loc[user_data["id"] == id, "sex"] = sex
        if not age == "" and age.isdigit():
            user_data.loc[user_data["id"] == id, "age"] = age

        user_data.to_csv(cls.ACCOUNTS, index=False)
        cls.show_accounts()
