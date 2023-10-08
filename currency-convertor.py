from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from forex_python.converter import CurrencyRates
from decimal import Decimal

loginForm = Tk()
loginForm.title('Currency Converter')
loginForm.geometry('500x160')
right = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
down = int(loginForm.winfo_screenheight() / 2 - 200 / 2)
loginForm.geometry('+{}+{}'.format(right, down))
loginForm.resizable(0, 0)
loginForm.iconbitmap('images/login.ico')

c = CurrencyRates()

supported_currencies = c.get_rates('USD')  # You can use any base currency

currency_codes = list(supported_currencies.keys())

# Function
def resetForm():
    txtamount.set("")

def loginFunctionSqlServer():
    amount_str = txtamount.get()
    amount = Decimal(amount_str)
    from_currency = firstcombo.get()
    to_currency = secondcombo.get()

    result = c.convert(from_currency, to_currency, amount)

    msg.showinfo(':)', result)

lblamount = Label(loginForm, text='Amount:')
lblamount.grid(row=0, column=0, padx=10, pady=10)

txtamount = StringVar()
entamount = Entry(loginForm, width=20, textvariable=txtamount)
entamount.grid(row=0, column=1, padx=10, pady=10)

lblFrom = Label(loginForm, text='From:')
lblFrom.grid(row=1, column=0, padx=10, pady=10)

firstcombo = ttk.Combobox(loginForm, values=currency_codes)
firstcombo.grid(row=1, column=1, padx=10, pady=10)

lblTo = Label(loginForm, text='To:')
lblTo.grid(row=1, column=2, padx=10, pady=10)

secondcombo = ttk.Combobox(loginForm, values=currency_codes)
secondcombo.grid(row=1, column=3, padx=10, pady=10)

btnlogin = ttk.Button(loginForm, text='Convert', width=10, command=loginFunctionSqlServer)
btnlogin.grid(row=2, column=1, padx=10, pady=10, sticky=E)

loginForm.mainloop()


