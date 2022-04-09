# Amar Nagim
# Je kunt herhaald getallen raden
# het spel stopt na 20 te raden getallen of als je aangeeft (eerder) te willen stoppen. Elke te raden getal heet een ronde. Het spel heeft dus maximaal 20 ronden.
# Het programma neemt een random geheim te raden getal in gedachten tussen de 1 en de 1000
# Je mag 10 keer raden. Is het dan nog niet geraden, dan stopt die ronde.
# Voor elk geraden getal wordt de score opgehoogd met 1. Je kunt dus maximaal 20 punten scoren.
# Na elke gok geeft het programma antwoord:
# geraden, of hoger of lager
# Als het (absolute) verschil tussen het getal dat jij gokt en het geheime te raden getal kleiner is dan 50 dan meldt het programma in de terminal: 'Je bent warm’
# Als het (absolute) verschil tussen het getal dat jij gokt en het geheime te raden getal kleiner is dan 20 dan meldt het programma in de terminal: 'Je bent heel warm’
# Na elke ronde meldt het programma de score tot dan toe in de terminal
# Na elke ronde vraagt het programma: ‘Nog een getal raden?’ tenzij er al 20 ronden zijn geweest.
# Aan het einde meldt het programma de eindscore.
# Tip: begin met het automatiseren van alleen de ronde


import time
import random
import sys
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
from tracemalloc import start



window = Tk()
window.geometry("450x300")
window.title('raadeens')


initialFrame = Frame(window)
initialFrame.pack(pady=25)

centerFrameTitle = Frame(window)
centerFrameTitle.pack()

def generateRandomNumber():
  number = random.randint(1, 1000)
  return number

tryAmount = 1
roundAmount = 0
score = 0

def startGame():
  global roundAmount
  destroyAll()
  number = generateRandomNumber()
  centerFrameTitle = Frame(window)
  centerFrameTitle.pack()
  header = Label(centerFrameTitle, text="Random number has been generated", font=("Arial", 18, font.BOLD)).pack(pady=10)

  roundLabelFrame = Frame(window)
  roundLabelFrame.pack()

  roundLabel = Label(roundLabelFrame, text=f'round {roundAmount}/20')
  roundLabel.pack()
  
  centerFrame = Frame(window)
  centerFrame.pack(pady=37)

  statusMessage = Label(centerFrame, text="", fg='red')
  statusMessage.pack(pady=2)
  userInput = ttk.Entry(centerFrame, font=("Arial", 15))
  userInput.pack()
  

  def checkUserInputFunction(number):
    global score
    global tryAmount
    global roundAmount

    print(f'{number} random number')

    if tryAmount != 10:
      userInputValue = int(userInput.get())
      difference = userInputValue - number
      print(f'{number} difference')
      print(f'{userInputValue} userinput')
      if userInputValue == number:
        roundAmount+=1
        score+=1
        statusMessage.config(fg='green')
        statusMessage['text'] = f'You guessed the right number! {tryAmount}/10'
        roundLabel['text'] = f'round {roundAmount}/20'
        infoMessage = messagebox.showinfo(None, f'You guessed the right number! {tryAmount}/10, press okay to continue. Current score: {score}')
        tryAmount=0
        def regenerateNumberFunction():
          statusMessage.config(fg='black')
          statusMessage['text'] = f'Random number has been generated.. '
        statusMessage.after(2000, lambda: regenerateNumberFunction())
        window.after(2500, startGame)


      elif difference <= 20 and difference >= 1 or difference <= -1 and difference >= -20:
        if userInputValue < number: 
          print('Tip: higher')
          statusMessage.config(fg='red')
          statusMessage['text'] = f'You are very warm.. Tip: higher. {tryAmount}/10'  
        elif userInputValue > number:
          print('Tip: lower')  
          statusMessage.config(fg='red')
          statusMessage['text'] = f'You are very warm.. Tip: lower. Try {tryAmount}/10'  
      elif difference <= 50 and difference >= 1 or difference <= -1 and difference >= -50:
        if userInputValue < number: 
          print('Tip: higher')
          statusMessage.config(fg='red')
          statusMessage['text'] = f'You are warm.. Tip: higher. {tryAmount}/10'  
        elif userInputValue > number:
          print('Tip: lower')  
          statusMessage.config(fg='red')
          statusMessage['text'] = f'You are warm.. Tip: lower. Try {tryAmount}/10'  
      elif userInputValue > number:
          statusMessage.config(fg='black')
          statusMessage['text'] = f'Tip: lower {tryAmount}/10'  
      elif userInputValue < number:
          statusMessage.config(fg='black')
          statusMessage['text'] = f'Tip: higher {tryAmount}/10'  
      tryAmount+=1

    else:
      generateRandomNumber()
      statusMessage.config(fg='red')
      ifClose = messagebox.showwarning(None, f'You have exceeded your tries. You had {tryAmount}. Score: {score}')
      if ifClose:
        window.destroy()
      roundAmount+=1
      roundLabel['text'] = f'round {roundAmount}/20'

  entryDescription = Label(centerFrame, text='enter your guess', font=("Arial", 10, font.ITALIC)).pack()
  checkInputButton = Button(centerFrame, text="check number", command=lambda: checkUserInputFunction(number)).pack(side=LEFT, pady=30)
  stopButton = Button(centerFrame, text="stop", command=lambda: window.destroy()).pack(side=LEFT, pady=30)


header = Label(centerFrameTitle, text="Guess the number game", font=("Arial", 20, font.BOLD)).pack(pady=10)

centerFrame = Frame(window)
centerFrame.pack()

explanation = Label(centerFrame, text="""A number between 1 and 1000 will be randomly generated. 
Guess it within 10 tries. There are 20 rounds, you can stop whenever 
you want and retrieve your points.""").pack(pady=15)

startButton = Button(centerFrame, text="start game", command=startGame).pack(pady=10)

def destroyAll():
  for child in window.winfo_children():
    child.destroy()

  
window.mainloop()




