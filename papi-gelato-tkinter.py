from inspect import trace
from tabnanny import check
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time
import tkinter.messagebox as messagebox
import time
import sys

window = Tk()

def main():
    window.geometry('500x200')
    window.title('Papi Gelato')
    for widgets in window.winfo_children():
        widgets.destroy()
    def destroyPage():
        for widgets in window.winfo_children():
            widgets.destroy()
        particulierChoice()


    titleFrame = Frame(window)
    titleFrame.pack()

    title = Label(titleFrame, text="Welkom bij Papi Gelato", font=("Arial", 20, font.BOLD)).pack(pady=10)

    particulierZakelijkFrame = Frame(window)
    particulierZakelijkFrame.pack()

    particulierZakelijkStringVar = StringVar()
    particulierZakelijkStringVar.set('None')

    particulierZakelijkLabel = Label(particulierZakelijkFrame, text="Bent u een zakelijke of een particuliere klant?").pack(side=LEFT)
    particulierZakelijkRadiobuttonParticulier = Radiobutton(particulierZakelijkFrame, text="particulier", variable=particulierZakelijkStringVar, value='particulier').pack(side=LEFT)
    particulierZakelijkRadiobuttonZakelijk = Radiobutton(particulierZakelijkFrame, text="zakelijk", variable=particulierZakelijkStringVar, value='zakelijk').pack(side=LEFT)

    amountIcecreamFrame = Frame(window)
    amountIcecreamFrame.pack()

    amountIcecreamLabel = Label(amountIcecreamFrame, text="Hoeveel bolletjes wilt u?")
    amountIcecreamEntry = Entry(amountIcecreamFrame, width=5)

    amountIcecreamLiterLabel = Label(amountIcecreamFrame, text="Hoeveel liter ijs wilt u?")
    amountIcecreamLiterEntry = Entry(amountIcecreamFrame, width=5)

    availabilityLabelFrame = Frame(window)
    availabilityLabelFrame.pack()

    availableLabel = Label(availabilityLabelFrame)

    icecreamAvailabilityButtonFrame = Frame(window)
    icecreamAvailabilityButtonFrame.pack()


    def checkAvailabilityFunction():
        global particulierZakelijkUserInput
        global amountIcecreamEntryUserInput
        global amountLiterIceacreamUserInput

        particulierZakelijkUserInput = particulierZakelijkStringVar.get()
        amountIcecreamEntryUserInput = amountIcecreamEntry.get()
        amountLiterIceacreamUserInput = amountIcecreamLiterEntry.get()
        
        if particulierZakelijkUserInput == 'particulier':
            if int(amountIcecreamEntryUserInput) < 8:
                availableLabel.config(text=f'We hebben {amountIcecreamEntryUserInput} bolletjes op voorraad', fg='green')
                availableLabel.pack()
                nextPageButton.pack()    

            else:
                availableLabel.config(text=f'Helaas hebben we geen {amountIcecreamEntryUserInput} bolletjes op voorraad', fg='red')
                availableLabel.pack()
                
        else:
            availableLabel.config(text=f'We hebben {amountLiterIceacreamUserInput} liter ijs op voorraad', fg='green')
            availableLabel.pack()  
            nextPageButton.pack()    
    
    icecreamAvailabilityButton = Button(icecreamAvailabilityButtonFrame, command=checkAvailabilityFunction ,text="Bekijk beschikbaarheid")

    nextPageButtonFrame = Frame(window)
    nextPageButtonFrame.pack()
    nextPageButton = Button(nextPageButtonFrame, text='Verder', command=destroyPage)


    def particulierZakelijkFunction(*args):
        icecreamAvailabilityButton.pack()
        particulierZakelijkUserInput = particulierZakelijkStringVar.get()
        if particulierZakelijkUserInput == 'particulier':
            amountIcecreamLiterLabel.forget()
            amountIcecreamLiterEntry.forget()
            amountIcecreamLabel.pack(side=LEFT)
            amountIcecreamEntry.pack(side=LEFT)
        if particulierZakelijkUserInput == 'zakelijk':
            amountIcecreamLabel.forget()
            amountIcecreamEntry.forget()
            amountIcecreamLiterLabel.pack(side=LEFT)
            amountIcecreamLiterEntry.pack(side=LEFT)

    traceCommandParZak = particulierZakelijkStringVar.trace
    traceCommandParZak('w', particulierZakelijkFunction)
    

    def amountOptionMenuFun():
        global flavourStringVar
        global toppingStringVar
        global toppingOptionmenuList
        global flavourOptionmenuList
        particulierZakelijkUserInput
        amountIcecreamEntryUserInput
        amountLiterIceacreamUserInput
        amountOptionMenu = amountIcecreamEntryUserInput + amountLiterIceacreamUserInput
        toppingList = ['geen', 'slagroom', 'sprinkels', 'caramel saus']
        flavourList = ['aardbei', 'chocolade', 'munt', 'vanille']
        toppingOptionmenuList = []
        flavourOptionmenuList = []
        for amount in range(1,int(amountOptionMenu)+1):
            flavourStringVar = StringVar()
            flavourStringVar.set('smaak')
            toppingStringVar = StringVar()
            toppingStringVar.set('topping')
            listAmountFrame = Frame(window)
            listAmountFrame.pack()
            if particulierZakelijkUserInput == 'particulier':
                listAmountLabel = Label(listAmountFrame, text=f'Kies de topping en smaak voor bolletje {amount}').pack(side=LEFT)
                optionMenuToppings = OptionMenu(listAmountFrame, toppingStringVar, *toppingList)
                optionMenuToppings.pack(side=LEFT)
                optionMenuToppings.config(width=7)
                toppingOptionmenuList.append(optionMenuToppings)
            else:
                listAmountLabel = Label(listAmountFrame, text=f'Kies de smaak voor liter {amount}').pack(side=LEFT)
            optionMenuFlavours = OptionMenu(listAmountFrame, flavourStringVar, *flavourList)
            optionMenuFlavours.pack(side=LEFT)
            flavourOptionmenuList.append(optionMenuFlavours)

        orderAgainFrame = Frame(window)
        orderAgainFrame.pack()
        orderAgainButton = Button(orderAgainFrame, text="opnieuw bestellen", command=main).pack() 

        finishOrderFrame = Frame(window)
        finishOrderFrame.pack()
        finishOrderButton = Button(finishOrderFrame, text="afrekenen", command=endPage).pack()
    
    def endPage():
        for widgets in window.winfo_children():
            widgets.destroy()
        window.geometry('800x60')    
        endTitleFrame = Frame(window)
        endTitleFrame.pack()

        endTitleLabel = Label(endTitleFrame, text="Bedankt voor je aankoop. Deze word binnen korte tijd bij je geleverd!", font=('Arial', 20, font.BOLD)).pack(pady=12)
        

    def particulierChoice():
        window.geometry('500x350')
        hoorntjeOrBakjeStringVar = StringVar()
        hoorntjeOrBakjeStringVar.set('None')

        hoorntjeOrBakjeFrame = Frame(window)
        hoorntjeOrBakjeFrame.pack()
        if particulierZakelijkUserInput == 'particulier':
            bolletjeOrHoorntjeLabel = Label(hoorntjeOrBakjeFrame, text="Wilt u het ijs in een hoorntje of bakje?").pack(side=LEFT)
            hoorntjeRadiobutton = Radiobutton(hoorntjeOrBakjeFrame, text="hoorntje", variable=hoorntjeOrBakjeStringVar, value='hoorntje').pack(side=LEFT)
            bakjeRadiobutton = Radiobutton(hoorntjeOrBakjeFrame, text="bakje", variable=hoorntjeOrBakjeStringVar, value='bakje').pack(side=LEFT)
        amountOptionMenuFun()
main()
window.mainloop()