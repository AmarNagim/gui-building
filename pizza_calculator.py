# F1.2.03.O2 - Pizzacalculator
# Amar Nagim
# opdracht: Pizza Calculator

from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time
import tkinter.messagebox as messagebox
import time
import sys

window = Tk()
window.geometry("450x300")
window.title('Pizza Calculator')

totalOrder = 0
orderedPizzaList = []

def main():

    def forgetWidgets():
        destroyWidgets()
        main()
    pizzaSizeVar = StringVar()
    pizzaSizeVar.set("False")

    centerFrameTitle = Frame(window)
    centerFrameTitle.pack()

    centerFrame = Frame(window)
    centerFrame.pack()

    def orderPage():
        titleLabel = Label(centerFrameTitle, text="Pizza Order Pagina", font=("Arial", 13, font.BOLD), fg="black").pack(pady=10)

        pizzaSizeLabel = Label(centerFrame, text="Welk formaat pizza wilt u?", font=("Arial", 13), fg="black").pack(pady=70, side=LEFT)
        pizzaLarge = Radiobutton(centerFrame, text="large", variable=pizzaSizeVar, value='large').pack(side=LEFT)
        pizzaMedium = Radiobutton(centerFrame, text="medium", variable=pizzaSizeVar, value='medium').pack(side=LEFT)
        pizzaSmall = Radiobutton(centerFrame, text="small", variable=pizzaSizeVar, value='small').pack(side=LEFT)

    orderPage()        
    
    def destroyWindow():
        window.destroy()

    def secondPageButtons():
        retryButtonFrame = Frame(window)
        retryButtonFrame.pack()
        retryButton = Button(retryButtonFrame, text="Nog een pizza bestellen", command=forgetWidgets).pack(pady=25, padx=5, side=LEFT)
        ExitButton = Button(retryButtonFrame, text="Website sluiten", command=destroyWindow).pack(padx=5, side=LEFT)

    def buttonFunction(): 
        global totalOrder
        global orderedPizzaList
        seperator = ''
        print(pizzaSizeVar.get())
        if pizzaSizeVar.get() != "False": 
            destroyWidgets()
            centerFrameSecondTitle = Frame(window)
            centerFrameSecondTitle.pack()
            SecondtitleLabel = Label(centerFrameSecondTitle, text="Order Bevestigen Pagina", font=("Arial", 13, font.BOLD), fg="black").pack(pady=10)   
            centerFramePriceLabel = Frame(window)
            centerFramePriceLabel.pack()
        if pizzaSizeVar.get() == 'small':
            totalOrder+=8
            orderedPizzaList.append('Pizza small €8,-')
        elif pizzaSizeVar.get() == 'medium':
            totalOrder+=10
            orderedPizzaList.append('Pizza medium €10,-')
        elif pizzaSizeVar.get() == 'large':
            totalOrder+=12
            orderedPizzaList.append('Pizza large €12,-')
        for a in range(len(orderedPizzaList)):
            currentPizza = Label(centerFramePriceLabel, text=orderedPizzaList[a], font=("Arial", 15), fg="black").pack()
        if pizzaSizeVar.get() != "False": 
            secondPageButtons()
            totalPriceLabel = Label(centerFramePriceLabel, text=f"Totaalprijs is €{totalOrder},-", font=("Arial", 15), fg="black").pack(pady=0)
            print(totalOrder)            
    button = Button(window, text="doorgaan naar betalen", command=buttonFunction)
    button.pack()

    def destroyWidgets():
        for child in window.winfo_children():
            child.destroy()
main()
window.mainloop()

# small = '€8,-'                                                             # variables
# medium = '€10,-'
# large = '€12,-'

# small_digit = 8
# medium_digit = 10
# large_digit = 12

# total_order = []
# seperator = """ 
#                       """
# total_price = []                   

# print('Welkom bij Dominos!')
# print('')

# def order():                                                              # function of the script

#    global total_order                                                     # bringing the global variables into the function
#    global seperator
#    global total_price
#    global small
#    global medium
#    global large
#    global small_digit
#    global medium_digit 
#    global large_digit
   
   
#    print('Kies hieronder de opties van uw pizza:')
#    time.sleep(1)

#    size = input('Small, medium of large: ').lower()
#    print('')
#                                                                         # choice of pizza sizes and lists
#    if size == 'small':  
#     print(f'U heeft pizza small gekozen. Dit kost {small}')
#     total_order.append(f'Pizza small {small}')
#     total_price.append(small_digit)
#    elif size == 'medium':
#     print(f'U heeft pizza medium gekozen. Dit kost {medium}')
#     total_order.append(f'Pizza medium {medium}') 
#     total_price.append(medium_digit)
#    elif size == 'large':
#     print(f'U heeft pizza large gekozen. Dit kost {large}')
#     total_order.append(f'Pizza large {large}')
#     total_price.append(large_digit)
#    else:
#        order()
#        print('We hebben u niet begrepen. Probeer het opnieuw.')
   
#    order_again = {'j':True,'n':False}.get(input('Wilt u nog een pizza bestellen? J/N: ').lower())  # order again option 
   
#    if order_again == True:
#        print('')
#        print('U word over enkele ogenblikken doorgestuurd naar ons pizza keuzemenu.')
#        time.sleep(1)
#        order()
#    else:
#        print('')
#        print('')
#        print(f"Uw totale bestelling: {(seperator.join(total_order))} ")                            # order overview
#        total_price_sum = sum(total_price)
#        print (f'                      De totaalprijs is: €{total_price_sum},-')
#        time.sleep(10)
#        sys.exit



# order()


