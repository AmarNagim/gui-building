# kaasspel (leerpad-01 werken met condities)
# Tkinter interface

from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time
import tkinter.messagebox as messagebox
window = Tk()
window.geometry("450x300")

def main():
    global question1Var
    global question2Var
    global question3Var
    global question4Var
    global question5Var
    global question6Var
    
    

    question1Var = StringVar(value='False')
    question1Var.set(None)
    question2Var = StringVar(value='False')
    question2Var.set(None)
    question3Var = StringVar(value='False')
    question3Var.set(None)
    question4Var = StringVar(value='False')
    question4Var.set(None)
    question5Var = StringVar(value='False')
    question5Var.set(None)
    question6Var = StringVar(value='False')
    question6Var.set(None)
    
    
    
    
    centerFrameTitle = Frame(window)
    centerFrameTitle.pack()

    titleLabel = Label(centerFrameTitle, text="Ik ga raden wat jouw favoriete kaas is", font=("Arial", 13, font.BOLD), fg="black").pack(pady=10)
    centerFrame = Frame(window)
    centerFrame.pack()
    question1 = Label(centerFrame, text="Is de kaas geel?", font=("Arial", 13), fg="black").pack(pady=10, side=LEFT)
    question1True = Radiobutton(centerFrame, text="True", variable=question1Var, value='True').pack(side=LEFT)
    question1False = Radiobutton(centerFrame, text="False", variable=question1Var, value='False').pack(side=LEFT)
    
    centerFrame2 = Frame(window)
    centerFrame2.pack()
    question2 = Label(centerFrame2, text="Zitten er gaten in?", font=("Arial", 13), fg="black").pack(pady=5, side=LEFT)
    question2True = Radiobutton(centerFrame2, text="True", variable=question2Var, value='True').pack(side=LEFT)
    question2False = Radiobutton(centerFrame2, text="False", variable=question2Var, value='False').pack(side=LEFT)
    
    centerFrame3 = Frame(window)
    centerFrame3.pack()
    question3 = Label(centerFrame3, text="Is de kaas belachelijk duur?", font=("Arial", 13), fg="black").pack(pady=5, side=LEFT)
    question3True = Radiobutton(centerFrame3, text="True", variable=question3Var, value='True').pack(side=LEFT)
    question3False = Radiobutton(centerFrame3, text="False", variable=question3Var, value='False').pack(side=LEFT)
    
    centerFrame4 = Frame(window)
    centerFrame4.pack()
    question4 = Label(centerFrame4, text="Heeft de kaas blauwe schimmels?", font=("Arial", 13), fg="black").pack(pady=5, side=LEFT)
    question4True = Radiobutton(centerFrame4, text="True", variable=question4Var, value='True').pack(side=LEFT)
    question4False = Radiobutton(centerFrame4, text="False", variable=question4Var, value='False').pack(side=LEFT)
    
    centerFrame5 = Frame(window)
    centerFrame5.pack()
    question5 = Label(centerFrame5, text="Is de kaas hard als steen?", font=("Arial", 13), fg="black").pack(pady=5, side=LEFT)
    question5True = Radiobutton(centerFrame5, text="True", variable=question5Var, value='True').pack(side=LEFT)
    question5False = Radiobutton(centerFrame5, text="False", variable=question5Var, value='False').pack(side=LEFT)
    
    centerFrame6 = Frame(window)
    centerFrame6.pack()
    question6 = Label(centerFrame6, text="Heeft de kaas een korst?", font=("Arial", 13), fg="black").pack(pady=5, side=LEFT)
    question6True = Radiobutton(centerFrame6, text="True", variable=question6Var, value='True').pack(side=LEFT)
    question6False = Radiobutton(centerFrame6, text="False", variable=question6Var, value='False').pack(side=LEFT)

    def buttonFunction():
        question1Answer = question1Var.get()
        question2Answer = question2Var.get()
        question3Answer = question3Var.get()
        question4Answer = question4Var.get()
        question5Answer = question5Var.get()
        question6Answer = question6Var.get()
        
        # if question1Answer == 'True' and question2Answer == 'True' and question3Answer == 'True':
        #     print('Emmenthaler')
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Emmenthaler')
        # elif question1Answer == 'True' and question2Answer == 'True' and question3Answer == 'False':
        #     print('Leerdammer')
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Leerdammer')
        # elif question1Answer == 'True' and question2Answer == 'False' and question5Answer == 'True':
        #     print('Pamigiano Reggiano')
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Pamigiano Reggiano')
        # elif question1Answer == 'True' and question2Answer == 'False' and question5Answer == 'False':
        #     print('Goudse kaas')     
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Goudse kaas')
        # elif question1Answer == 'False' and question4Answer == 'True' and question6Answer == 'True':
        #     print('Bleu de Rochbaron') 
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Bleu de Rochbaron')
        # elif question1Answer == 'False' and question4Answer == 'True' and question6Answer == 'False':
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Foume d\'Ambert')
        #     print('Foume d\'Ambert')    
        # elif question1Answer == 'False' and question4Answer == 'False' and question6Answer == 'True':
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Camembert')
        #     print('Camembert')  
        # elif question1Answer == 'False' and question4Answer == 'False' and question6Answer == 'True':
        #     cheeseGuess = messagebox.showinfo(None, f'De kaas die je in gedachten hebt is Mozzarella')
        #     print('Mozzarella')    
        # else:
        #     cheeseGuess = messagebox.showerror('ERROR', f'Helaas wist ik de kaas in gedachten niet te raden :(')
        # if cheeseGuess:
            # window.destroy()
    button = Button(window, text="test", command=buttonFunction)
    button.pack()

main()


print('Ik ga raden wat jouw favoriete kaas is.')
time.sleep(1)
print('')

print("Beantwoord de vragen hieronder")

geel = {'y':True,'n':False}.get(input("Is de kaas geel? Y/N: ").lower())
gaten = {'y':True,'n':False}.get(input("Zitten er gaten in? Y/N: ").lower())
duur = {'y':True,'n':False}.get(input("Is de kaas belachelijk duur? Y/N: ").lower())

blauwe_schimmels = {'y':True,'n':False}.get(input("Heeft de kaas blauwe schimmels? Y/N: ").lower())
hard = {'y':True,'n':False}.get(input("Is de kaas hard als steen? Y/N: ").lower())
korst = {'y':True,'n':False}.get(input("Heeft de kaas een korst? Y/N: ").lower())

# Emmenthaler 
if all((geel, gaten, duur)):
         print('Hmm... Ik denk dat de kaas die je in gedachten hebt Emmenthaler is.')
# Leerdammer         
elif all((geel, gaten,not duur)):
         print('Hmm... Ik denk dat de kaas die je in gedachten hebt Emmenthaler is.')  
# Pamigiano Reggiano                
elif all((geel,not gaten,hard)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Pamigiano Reggiano is.')
# Goudse kaas
elif all((geel,not gaten,not hard)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Goudse kaas is.') 
# Bleu de Rochbaron
elif all((not geel,blauwe_schimmels,korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Bleu de Rochbaron is.')
# Camembert
elif all((not geel,not blauwe_schimmels,korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Camembert is.')
# Mozzerella
elif all((not geel,not blauwe_schimmels,not korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Mozzerella is.')
# Foume d'Ambert
elif all((not geel,blauwe_schimmels,not korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Foume d\'Ambert is.')

time.sleep('True')
print('')

print("Bedankt voor het spelen!")    

window.mainloop()