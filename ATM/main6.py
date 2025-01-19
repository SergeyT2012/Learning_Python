import requests
from bs4 import BeautifulSoup as Bs
url = "https://minfin.com.ua/ua/currency/"
import requests
from bs4 import BeautifulSoup as Bs

class Bank:
    def __init__(self, pin, balance, bank_balance, usd, eur, pln):
        self.usd = usd
        self.eur = eur
        self.pln = pln
        self.pin = pin
        self.balance = balance
        self.bank_balance = bank_balance
        self.write_bank_balance()
        self.check_pin()

    def check_pin(self):
        for i in range(3):
            user_pin = int(input("Enter pin: "))
            if user_pin == self.pin:
                self.main_menu()
                break
            else:
                print("Incorrect PIN!")

    def main_menu(self):
        user_menu = int(input("1) check balance \n2) withdraw money \n3) put money\n4) rates \n5) exit\n"))
        if user_menu == 1:
            self.check_balance()
        elif user_menu == 2:
            self.get_money()
        elif user_menu == 3:
            self.put_money()
        elif user_menu == 4:
            self.rates()
        elif user_menu == 5:
            exit()

    def write_bank_balance(self):
        with open('bank_balance.txt','w') as bank_file:
            bank_file.write(f"Balance: {self.balance}")

    def read_bank_balance(self):
        with open('bank_balance.txt', 'r') as bank_file:
            return bank_file.read()

    def check_balance(self):
        print(f"Balance: {self.balance} \nUSD: {self.usd}\nEUR: {self.eur}\nPLN: {self.pln}")
        self.return_to_main_menu()

    def get_money(self):
        get_money_amount = int(input("How much money do you want to withdraw? "))
        if get_money_amount <= self.balance and get_money_amount < self.bank_balance:
            self.bank_balance = self.bank_balance - get_money_amount
            self.balance = self.balance - get_money_amount
            print(f"Successfully withdrawn!\nUser Money Amount: {self.balance}")
            with open('bank_balance.txt', 'w') as bank_file:
                bank_file.write(f"User Money Amount: {self.balance}")
        elif get_money_amount > self.bank_balance:
            print(f"Not enough money in the bank!")
        elif get_money_amount > self.balance:
            print(f"Not enough money in your bank account! Current balance: {self.balance}")
        self.return_to_main_menu()

    def put_money(self):
        put_money_amount = int(input("How much money do you want to put into your account? "))
        self.bank_balance = self.bank_balance + put_money_amount
        self.balance = self.balance + put_money_amount
        print(f"User Money Amount: {self.balance}")
        with open('bank_balance.txt', 'w') as bank_file:
            bank_file.write(f"User Money Amount: {self.balance}")
        self.return_to_main_menu()


    def rates(self):
        text = Bs(requests.get("https://minfin.com.ua/ua/currency/").content, "html.parser")
        lst_rates = [i.text for i in text.select(".sc-1x32wa2-9.bKmKjX")]
        value_usd = round(float(lst_rates[2].replace(".", "").replace(",", ".")), 2)
        value_eur = round(float(lst_rates[5].replace(".", "").replace(",", ".")), 2)
        value_pln = round(float(lst_rates[8].replace(".", "").replace(",", ".")), 2)
        with open('bank_balance.txt', 'a') as bank_file:
            bank_file.write(f"\nUSD to UAH: {value_usd}\nEUR to UAH: {value_eur}\nPLN to UAH: {value_pln}")
        rates_confirmation = int(input("1) Check rates;\n2) Convert UAH into ___;\n"))
        if rates_confirmation == 1:
            print(f"USD to UAH: {value_usd}\nEUR to UAH: {value_eur}\nPLN to UAH: {value_pln}")
            self.return_to_main_menu()
        elif rates_confirmation == 2:
            convert_confirmation = int(input("What do you want to convert into? \n1)USD\n2)EUR\n3)PLN\n"))
            if convert_confirmation == 1:
                convertion_value = int(input("How much money do you want to convert? "))
                if convertion_value > self.balance:
                    print("Not enough money on account!")
                    self.rates()
                else:
                    self.usd = round(convertion_value / value_usd, 2)
                    self.balance = self.balance - convertion_value
                    self.write_bank_balance()
                    with open('bank_balance.txt', 'a') as bank_file:
                        bank_file.write(f"\nConverted value(USD){self.usd}")
                    print(f"USD: {self.usd}")
                    self.return_to_main_menu()
            elif convert_confirmation == 2:
                convertion_value = int(input("How much money do you want to convert? "))
                if convertion_value > self.balance:
                    print("Not enough money on account!")
                    self.rates()
                else:
                    self.eur = round(convertion_value / value_eur, 2)
                    self.balance = self.balance - convertion_value
                    self.write_bank_balance()
                    with open('bank_balance.txt', 'a') as bank_file:
                        bank_file.write(f"\nConverted value(EUR){self.eur}")
                    print(f"EUR: {self.eur}")
                    self.return_to_main_menu()
            elif convert_confirmation == 3:
                convertion_value = int(input("How much money do you want to convert? "))
                if convertion_value > self.balance:
                    print("Not enough money on account!")
                    self.rates()
                else:
                    self.pln = round(convertion_value / value_pln, 2)
                    with open('bank_balance.txt', 'a') as bank_file:
                        bank_file.write(f"\nConverted value(PLN){self.pln}")
                        self.write_bank_balance()
                    print(f"PLN: {self.pln}")
                    self.return_to_main_menu()
            else:
                print("Invalid input!")
                self.rates()

    def return_to_main_menu(self):
        return_to_main_menu = input("Do you want to return to the main menu? (Y/N)\n")
        if return_to_main_menu == "Y" or return_to_main_menu == "y":
            self.main_menu()
        else:
            exit()

user = Bank(1111, 5000, 100000, 0, 0, 0)