import requests


class CurrencyExchange:
    def __init__(self):
        self.api_key = open(r"C:\Users\DELL\Desktop\API_access_key.txt","r").readline() # Add ur Api key into text file and define the path according to it.
        self.base_currency = "INR"

    def do_request(self,url):
        try:
            res = requests.get(url,headers={"apikey": self.api_key})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None

    def show_base_currency(self):
        return f"Base Currency: {self.base_currency}"

    def set_base_currency(self,base_currency):
        self.base_currency = base_currency
        return f"Base currency set to {self.base_currency}"

    def show_symbols(self):
        response = self.do_request("https://api.apilayer.com/fixer/symbols")
        output = []
        for key,value in response["symbols"].items():
            output.append(f"{key} = {value}")
        return output

    def latest_rates(self):
        base = input("Enter the three-letter currency code of your preferred base currency.(example:eur) : ")
        symbols = input("Enter a list of comma-separated currency codes "
                        "to limit output currencies.(example:gbp,jpy,eur): ")
        response = self.do_request(f"https://api.apilayer.com/fixer/latest?symbols={symbols}&base={base}")
        return f"Date:{response['date']} \nBase Currency : {response['base']} \nRates:{response['rates']}"

    def convert(self):
        convert_from = input("Enter the three-letter currency code of the currency you would like to convert "
                             "from.(example:eur) :")
        convert_to = input("Enter the three-letter currency code of the currency you would like to convert to.("
                           "example:gbp,jpy,eur):")
        amount = int(input("Enter the amount to be converted."))
        response = self.do_request(
            f"https://api.apilayer.com/fixer/convert?to={convert_to}&from={convert_from}&amount={amount}")
        return f"From: {response['query']['from']}\nTo: {response['query']['to']}\nAmount: {response['query']['amount']}\nResult:{response['result']}"

    def rates_on_date(self):
        date = input("Enter the date of your preferred timeframe in format (yyyy-mm-dd): ")
        base = input("Enter the three-letter currency code of your preferred base currency.(example:eur) : ")

        symbols = input("Enter a list of comma-separated currency codes "
                        "to limit output currencies.(example:gbp,jpy,eur): ")
        response = self.do_request(f"https://api.apilayer.com/fixer/{date}?symbols={symbols}&base={base}")
        return f"Base Currency: {response['base']}\nDate: {response['date']}\nResult: {response['rates']}"


    def timeseries(self):
        start_date = input("Enter the start date of your preferred timeframe in format (yyyy-mm-dd): ")
        end_date = input("Enter the end date of your preferred timeframe in format (yyyy-mm-dd): ")
        response = self.do_request(
            f"https://api.apilayer.com/fixer/timeseries?start_date={start_date}&end_date={end_date}&base={self.base_currency}")
        return f"Start Date = {response['start_date']}\nEnd date= {response['end_date']}\nBase Currency= {response['base']}\nResult= {response['rates']}"

    def fluctuation(self):
        start_date = input("Enter the start date of your preferred timeframe in format (yyyy-mm-dd): ")
        end_date = input("Enter the end date of your preferred timeframe in format (yyyy-mm-dd): ")
        response = self.do_request(
            f"https://api.apilayer.com/fixer/fluctuation?start_date={start_date}&end_date={end_date}&base={self.base_currency}")
        return f"Start Date= {response['start_date']}\nEnd Date= {response['end_date']}\nBase Currency= {response['base']}\nResult= {response['rates']}"


c = CurrencyExchange()
while True:
    print("""Choose one of the below options:
                1.Set Base currency. Default base currency is INR.
                2.Show Base Currency.
                3."/symbols" Returns all available currencies.
                4."/latest" Returns real-time exchange rate data for all available or a specific set of currencies.
                5."/convert" Allows for conversion of any amount from one currency to another.
                6."/{date}" Returns historical exchange rate data for all available or a specific set of currencies.
                7."/timeseries" Returns daily historical exchange rate data between two specified dates for all available or a specific set of currencies.
                8."/fluctuation" Returns fluctuation data between two specified dates for all available or a specific set of currencies.
                9. Exit.
    """)
    option = int(input("Enter a number: "))
    if option == 1:
        currency = input("Enter the base currency: ")
        c.set_base_currency(currency)
    elif option == 2:
        print(c.show_base_currency())
    elif option == 3:
        print(c.show_symbols())
    elif option == 4:
        print(c.latest_rates())
    elif option == 5:
        print(c.convert())
    elif option == 6:
        print(c.rates_on_date())
    elif option == 7:
        print(c.timeseries())
    elif option == 8:
        print(c.fluctuation())
    elif option == 9:
        break