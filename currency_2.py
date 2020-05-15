from forex_python.converter import CurrencyRates
import json
import sys

the_rates= CurrencyRates(force_decimal=True)
ask_1 = input("Which currency will you like to exchange?(ex. USD) :")

ask_2= input("With what currency will you like to exchange it?(ex. JPY) :")
ask_3  = int(input("What will be the amount to exchange? :"))


def convert_my_currency(convert_m,currency,amount):

    convert_m = ask_1
    currency= ask_2
    amount  = ask_3
    
    print(the_rates.convert(convert_m.upper(),currency.upper(),amount))
   
    question= input("Will you like to exchange another currency?(Y/N) :")


    while question == "Y" or question == "y": 
        convert_m  = input("Which currency will you like to exchange?(ex. USD) :")
        currency = input("With what currency will you like to exchange it?(ex. JPY) :")
        amount = int(input("What will be the amount to exchange? :"))
         
        
        print(the_rates.convert(convert_m.upper(),currency.upper(),amount))

        question= input("Will you like to exchange another currency?(Y/N) :")
        

    
    else:
        sys.exit()


convert_my_currency(ask_1,ask_2,ask_3)


#rates = {}

#rates['Currencies'] = []

#rates['currencies'].append({
#    'Currency':ask_1,
#    'Convert to': ask_2,
#    'Amount Exchanged': ask_3}) 

#with open("data.json","w") as currency_file :
#    json.dump(rates,currency_file)
