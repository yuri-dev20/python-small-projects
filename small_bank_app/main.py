from bank_app import Bank
import random
from pathlib import Path


def main():
    database_path = Path()

    if not database_path / "accounts.csv" == None:
        Bank.initiate_bank()

        while True:

            print("*" * 80)

            print("Hello and welcome to the Jhon's Bank APP")

            print()

            print("Please enter a following option: ")
            print("Register a account: (1)")
            print("Deposit: (2)")
            print("Extract: (3)")
            print("Edit my account: (4)")
            print("Remove a account: (5)")
            print("Show a account info: (6)")
            print("Show a accounts registered and its infos: (7)")
            print("End operations: (8)")

            print("*" * 80)

            user_choice = int(input("Type in: "))

            while True:
                if not user_choice in range(1, 10):
                    user_choice = int(input("Please enter a valid number: "))
                else:
                    break

            print()

            if user_choice == 1:
                print("Enter new account info: ")
                user_name = input("Name: ")
                user_sex = input("Sex: ")
                user_id = random.randint(10000, 99999)
                user_age = int(input("Age: "))

                user_balance_choice = input(
                    "Don you want to make a initial deposit?: (S/N) ")
                if user_balance_choice.upper() == "S":
                    user_initial_balance = float(
                        input("Initial balance deposit: "))

                    Bank.register_account(
                        user_name, user_sex, user_id, user_age, user_initial_balance)
                else:
                    Bank.register_account(
                        user_name, user_sex, user_id, user_age, 0)

            if user_choice == 2:
                Bank.show_accounts()
                id = int(input("Wich account will deposit: "))
                amount = int(input("Enter a amount to deposit: "))
                Bank.deposit(id, amount)

            if user_choice == 3:
                Bank.show_accounts()
                id = int(input("Wich account will extract: "))
                amount = int(input("Enter a amount to extract: "))
                Bank.extract(id, amount)

            if user_choice == 4:
                print("The following accounts are available - ")
                Bank.show_accounts()

                user_id = int(
                    input("Please inform a id for the account that will be edited: "))

                if Bank.verify_id(user_id) == False:
                    while True:
                        user_id = int(
                            input("Please inform a id for the account that will be edited: "))
                        if Bank.verify_id(user_id) != False:
                            break

                print()
                print("You can edit name, sex and age so please enter in the following")
                new_user_name = input(
                    "New Name (Leave it blank if doesn't want to change): ")
                print(new_user_name)
                new_sex = input(
                    "New Sex (Leave it blank if doesn't want to change): ")
                new_age = input(
                    "New Age (Leave it blank if doesn't want to change) ")
                print(new_age)

                Bank.edit_my_account(user_id, new_user_name, new_sex, new_age)

            if user_choice == 5:
                print()
                Bank.show_accounts()
                user_id = int(input("Please enter a user id for removal: "))

                if not Bank.verify_id(user_id):
                    while True:
                        user_choice = input(
                            "Do you want to cancel the following operation? (Yes/No)")
                        user_id = print(
                            "Please enter a valid user id for removal: ")
                        if not Bank.verify_id(user_id) or user_choice.lower == "yes":
                            break

                Bank.remove_account(user_id)

            if user_choice == 6:
                print()

                user_id = int(input("Please enter a valid id: "))
                consult_result = Bank.verify_id(user_id)

                if consult_result == False:
                    while True:
                        user_id = int(input("Please enter a valid id: "))
                        consult_result = Bank.verify_id(user_id)
                        if consult_result != False:
                            break

                Bank.show_account_info(user_id)

            if user_choice == 7:
                print("The following accounts are registered - ")
                Bank.show_accounts()

            if user_choice == 8:
                print("Thanks and come back!")
                break

            print()


if __name__ == "__main__":
    main()
