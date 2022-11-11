import tkinter as tk
from tkinter import ttk
from tkinter import *

# intializing the screen
screen = tk.Tk()
screen.title("TABS")

# configuring size of the screen
screen.geometry('500x400')

#Create Tab Control
GUI = ttk.Notebook(screen)

#Tab1
TAB1 = ttk.Frame(GUI)
GUI.add(TAB1, text='Tab 1')

#Tab2
TAB2 = ttk.Frame(GUI)
GUI.add(TAB2, text='Tab 2')
GUI.pack(expand=1, fill="both")

#Tab3
TAB3 = ttk.Frame(GUI)
GUI.add(TAB3, text='Tab 3')

def Calculate_Liquidity_Ratios():
	global asset, liabilities, inventory, cash

	asset = int(asset.get())
	liabilities = int(liabilities.get())
	inventory = int(inventory.get())
	cash = int(cash.get())

	Current_Ratio = asset/liabilities
	Quick_Ratio = (asset-inventory)/liabilities
	Cash_Ratio = cash/liabilities

	label = Label(TAB1, text=" ")
	label.pack(anchor="w")

	Current_Ratio_Label = Label(TAB1, text= "Current Ratio = "+ str(Current_Ratio))
	Quick_Ratio_Label = Label(TAB1, text="Quick Ratio = " + str(Quick_Ratio))
	Cash_Ratio_Label = Label(TAB1, text="Cash Ratio = " + str(Cash_Ratio))
	Current_Ratio_Label.pack(anchor="w")
	Quick_Ratio_Label.pack(anchor="w")
	Cash_Ratio_Label.pack(anchor="w")

def Calculate_Profitability_Ratios():
	global revenue, income, COG

	revenue = int(revenue.get())
	income = int(income.get())
	COG = int(COG.get())

	Gross_Margin =(revenue-COG)/revenue
	Operating_Margin = income/revenue
	Net_Profit_Margin = (income/revenue)*100

	label = Label(TAB1, text=" ")
	label.pack(anchor="w")

	Gross_Margin_Label = Label(TAB1, text="Gross_Margin = " + str(Gross_Margin))
	Opeerating_Margin_Label = Label(TAB1, text="Operating_Margin = " + str(Operating_Margin))
	Net_profit_Label = Label(TAB1, text="Net_Profit_Margin = " + str(Net_Profit_Margin))
	Gross_Margin_Label.pack(anchor="w")
	Opeerating_Margin_Label.pack(anchor="w")
	Net_profit_Label.pack(anchor="w")

def Calculate_Leverage_Ratios():
	global equity, liability, dept

	equity = int(equity.get())
	liability = int(liability.get())
	dept = int(dept.get())

	Debt_to_Equity_Ratio = liability/equity
	Debt_to_Capital_Ratio = dept/(dept+equity)

	label = Label(TAB1, text=" ")
	label.pack(anchor="w")

	Debt_to_Equity_Label = Label(TAB1, text="Debt to Equity Ratio = " + str(Debt_to_Equity_Ratio))
	Debt_to_Capital_Label = Label(TAB1, text="Debt to Capital Ratio = " + str(Debt_to_Capital_Ratio))

	Debt_to_Equity_Label.pack(anchor="w")
	Debt_to_Capital_Label.pack(anchor="w")

def Calculate_Operating_Ratios():
	global income2, equity2, assets2

	income2 = int(income2.get())
	equity2 = int(equity2.get())
	assets2 = int(assets2.get())

	Return_on_Equity_Ratio = (income2/equity2)*100
	Return_on_Assets_Ratio = income2/assets2

	label = Label(TAB1, text=" ")
	label.pack(anchor="w")

	Return_on_Equity_Label = Label(TAB1, text="Return on Equity Ratio = " + str(Return_on_Equity_Ratio))
	Return_on_Assets_Label = Label(TAB1, text="Return on Assets Ratio = " + str(Return_on_Assets_Ratio))

	Return_on_Equity_Label.pack(anchor="w")
	Return_on_Assets_Label.pack(anchor="w")

def Option():
	global count
	if count == 0:
		if clicked.get() == "Profitability Ratios":
			global revenue, income, COG
			L1 = Label(TAB1, text="Current Revenue")
			L1.pack(anchor="w")
			revenue = Entry(TAB1, width=50)
			revenue.pack(anchor="w")

			L2 = Label(TAB1, text="Operating Income")
			L2.pack(anchor="w")
			income = Entry(TAB1, width=50)
			income.pack(anchor="w")

			L3 = Label(TAB1, text="Cost Of Goods")
			L3.pack(anchor="w")
			COG = Entry(TAB1, width=50)
			COG.pack(anchor="w")

			CALCULATE = ttk.Button(TAB1 ,text="Calculate" , command =Calculate_Profitability_Ratios)
			CALCULATE.pack(anchor="w",pady=5)

			count += 1


		elif clicked.get() == "Liquidity Ratios":
			global asset, liabilities, inventory, cash

			L1 = Label(TAB1, text="Total Current Assets")
			L1.pack(anchor="w")
			asset = Entry(TAB1, width=50)
			asset.pack(anchor="w")

			L2 = Label(TAB1, text="Total Current Liabilities")
			L2.pack(anchor="w")
			liabilities = Entry(TAB1, width=50)
			liabilities.pack(anchor="w")

			L3 = Label(TAB1, text="Inventory")
			L3.pack(anchor="w")
			inventory = Entry(TAB1, width=50)
			inventory.pack(anchor="w")

			L4 = Label(TAB1, text="Cash")
			L4.pack(anchor="w")
			cash = ttk.Entry(TAB1, width=50)
			cash.pack(anchor="w")

			CALCULATE = ttk.Button(TAB1 ,text="Calculate" , command =Calculate_Liquidity_Ratios)
			CALCULATE.pack(anchor="w",pady=5)

			count += 1


		elif clicked.get() == "Leverage Ratios":
			global equity, liability, dept

			L1 = Label(TAB1, text="Total Shareholder Equity")
			L1.pack(anchor="w")
			equity = Entry(TAB1, width=50)
			equity.pack(anchor="w")

			L2 = Label(TAB1, text="Total Current Liabilities")
			L2.pack(anchor="w")
			liability = Entry(TAB1, width=50)
			liability.pack(anchor="w")

			L3 = Label(TAB1, text="Total Dept")
			L3.pack(anchor="w")
			dept = Entry(TAB1, width=50)
			dept.pack(anchor="w")

			CALCULATE = ttk.Button(TAB1 ,text="Calculate" , command =Calculate_Leverage_Ratios)
			CALCULATE.pack(anchor="w",pady=5)

			count += 1


		elif clicked.get() == "Operating Ratios":
			global income2, equity2, assets2

			L1 = Label(TAB1, text="Net Income")
			L1.pack(anchor="w")
			income2 = Entry(TAB1, width=50)
			income2.pack(anchor="w")

			L2 = Label(TAB1, text="Shareholder Equity")
			L2.pack(anchor="w")
			equity2 = Entry(TAB1, width=50)
			equity2.pack(anchor="w")

			L3 = Label(TAB1, text="Total Assets")
			L3.pack(anchor="w")
			assets2 = Entry(TAB1, width=50)
			assets2.pack(anchor="w")

			CALCULATE = ttk.Button(TAB1, text="Calculate", command=Calculate_Operating_Ratios)
			CALCULATE.pack(anchor="w",pady=5)

			count += 1
	else:
		return False

count = 0

# Dropdown menu options
options = [
	"Profitability Ratios",
	"Liquidity Ratios",
	"Leverage Ratios",
	"Operating Ratios",
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Pick Ratio Type")

# Create Dropdown menu
DropDownMenu = OptionMenu(TAB1, clicked, *options)
DropDownMenu.pack(anchor="w",pady=5)

# Create button, it will change label text
button = Button(TAB1, text="Click Me", command=Option)
button.pack(anchor="w",)

# Create Label
label = Label(TAB1, text=" ")
label.pack(anchor="w")


#TAB 2
label = Label(TAB2, text="Future Value And Present Value Calculator")
label.config(font=('Helvetica bold', 13))
label.pack()


L1 = Label(TAB2, text="Amount")
L1.pack(anchor="w")
Amount = Entry(TAB2, width=50)
Amount.pack(anchor="w")

L2 = Label(TAB2, text="Annual Interest")
L2.pack(anchor="w")
Interest = Entry(TAB2, width=50)
Interest.pack(anchor="w")

L3 = Label(TAB2, text="Number Of Years")
L3.pack(anchor="w")
NOY = Entry(TAB2, width=50)
NOY.pack(anchor="w")

def Future_Value():
	global  Amount,Interest,NOY


	Amount = int(Amount.get())
	Interest = int(Interest.get())
	NOY = int(NOY.get())

	Interest = Interest/100

	Future_Value = Amount * ((1+Interest)**NOY)
	Present_Value = Future_Value/((1+Interest)**NOY)

	Future_Value_Label = Label(TAB2, text="Future Value = " + str(Future_Value))
	Future_Value_Label.config(font=('Helvetica bold', 20))
	Future_Value_Label.pack(anchor="w")

def Present_Value():
	global  Amount,Interest,NOY

	Amount = int(Amount.get())
	Interest = int(Interest.get())
	NOY = int(NOY.get())

	Interest = Interest/100


	Future_Value = Amount * (1+Interest)**NOY
	Present_Value = Future_Value/((1+Interest)**NOY)
	print(Future_Value)


	Present_Value_Label = Label(TAB2, text="Present Value = " + str(Present_Value))
	Present_Value_Label.pack(anchor="w")


CALCULATE_Future_Value = ttk.Button(TAB2, text="Future Value", command=Future_Value)
CALCULATE_Future_Value.pack(anchor="w",pady=10)

CALCULATE_Present_Value = ttk.Button(TAB2, text="Present Value", command=Present_Value)
CALCULATE_Present_Value.pack(anchor="w",pady=5)




screen.mainloop()