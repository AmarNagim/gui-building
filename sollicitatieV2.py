# sollicitatie Cirscusdirecteur voor Circus HotelDeBotel
# criteria: 
# Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek
# In bezit van een Diploma MBO-4 ondernemen
# In bezit van een geldig Vrachtwagen rijbewijs
# In bezit van een hoge hoed
# Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm
# Is langer dan 150 cm
# Is zwaarder dan 90 kg
# Heeft Certificaat “Overleven met gevaarlijk personeel”


import random
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import time
import sys

window = Tk()

window.geometry('500x475')

titleFrame = Frame(window)
titleFrame.pack(pady=10)

title = Label(titleFrame, text="Vacature Ruimte Vuilsnisman", font=("Arial", 20, font.BOLD)).pack()
class code():
  def main():
    question1Frame = Frame(window)
    question1Frame.pack()
    experienceNumberList = list(range(71))
    question1 = Label(question1Frame, text="Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?").pack(side=LEFT)
    question1Answers = ttk.Combobox(question1Frame, state='readonly', value=experienceNumberList, width=3)
    question1Answers.pack(side=LEFT, padx=10)

    question2StringVar = StringVar()
    question2StringVar.set("None")

    question2Frame = Frame(window)
    question2Frame.pack()
    question2 = Label(question2Frame, text="Bent u in bezit van een diploma MBO-4 ondernemen?").pack(side=LEFT)
    question2AnswerYes = Radiobutton(question2Frame, text="Ja", variable=question2StringVar, value='Yes').pack(side=LEFT)
    question2AnswerNo = Radiobutton(question2Frame, text="Nee", variable=question2StringVar, value='No').pack(side=LEFT)

    question3StringVar = StringVar()
    question3StringVar.set("None")

    question3Frame = Frame(window)
    question3Frame.pack()
    question3 = Label(question3Frame, text="Bent u in bezit van een geldig vrachtwagen rijbewijs?").pack(side=LEFT)
    question2AnswerYes = Radiobutton(question3Frame, text="Ja", variable=question3StringVar, value='Yes').pack(side=LEFT)
    question2AnswerNo = Radiobutton(question3Frame, text="Nee", variable=question3StringVar, value='No').pack(side=LEFT)

    question4StringVar = StringVar()
    question4StringVar.set("None")

    question4Frame = Frame(window)
    question4Frame.pack()
    question4 = Label(question4Frame, text="Bent u in bezit van een hoge hoge hoed?").pack(side=LEFT)
    question4AnswerYes = Radiobutton(question4Frame, text="Ja", variable=question4StringVar, value='Yes').pack(side=LEFT)
    question4AnswerNo = Radiobutton(question4Frame, text="Nee", variable=question4StringVar, value='No').pack(side=LEFT)

    question5Frame = Frame(window)
    question5Frame.pack()
    lengthList = list(range(140, 221))
    question5 = Label(question5Frame, text="Wat is uw lengthe? (cm)").pack(side=LEFT)
    question5Answers = ttk.Combobox(question5Frame, value=lengthList, width=4)
    question5Answers.pack(side=LEFT, padx=10)

    question6Frame = Frame(window)
    question6Frame.pack()
    lengthList = list(range(30, 251))
    question6 = Label(question6Frame, text="Wat is uw lichaamsgewicht? (kg)").pack(side=LEFT)
    question6Answers = ttk.Combobox(question6Frame, value=lengthList, width=4)
    question6Answers.pack(side=LEFT, padx=10)

    question7StringVar = StringVar()
    question7StringVar.set("None")

    question7Frame = Frame(window)
    question7Frame.pack()
    question7 = Label(question7Frame, text="Bezit u een \"Overleven met gevaarlijk personeel certificaat\"?").pack(side=LEFT)
    question7AnswerYes = Radiobutton(question7Frame, text="Ja", variable=question7StringVar, value='Yes').pack(side=LEFT)
    question7AnswerNo = Radiobutton(question7Frame, text="Nee", variable=question7StringVar, value='No').pack(side=LEFT)

    # question that don't matter
    question9StringVar = StringVar()
    question9StringVar.set("None")

    question9Frame = Frame(window)
    question9Frame.pack()
    question9 = Label(question9Frame, text="Bent u van maandag tot vrijdag beschikbaar?").pack(side=LEFT)
    question9AnswerYes = Radiobutton(question9Frame, text="Ja", variable=question9StringVar, value='Yes').pack(side=LEFT)
    question9AnswerNo = Radiobutton(question9Frame, text="Nee", variable=question9StringVar, value='No').pack(side=LEFT)

    question10StringVar = StringVar()
    question10StringVar.set("None")

    question10Frame = Frame(window)
    question10Frame.pack()
    question10 = Label(question10Frame, text="Kan je goed met collega\'s samenwerken?").pack(side=LEFT)
    question10AnswerYes = Radiobutton(question10Frame, text="Ja", variable=question10StringVar, value='Yes').pack(side=LEFT)
    question10AnswerNo = Radiobutton(question10Frame, text="Nee", variable=question10StringVar, value='No').pack(side=LEFT)

    question11StringVar = StringVar()
    question11StringVar.set("None")

    question11Frame = Frame(window)
    question11Frame.pack()
    question11 = Label(question11Frame, text="Werk je liever zelfstandig?").pack(side=LEFT)
    question11AnswerYes = Radiobutton(question11Frame, text="Ja", variable=question11StringVar, value='Yes').pack(side=LEFT)
    question11AnswerNo = Radiobutton(question11Frame, text="Nee", variable=question11StringVar, value='No').pack(side=LEFT)

    question12StringVar = StringVar()
    question12StringVar.set("None")

    question12Frame = Frame(window)
    question12Frame.pack()
    question12 = Label(question12Frame, text="Heb je een blauwe spijkerbroek?").pack(side=LEFT)
    question12AnswerYes = Radiobutton(question12Frame, text="Ja", variable=question12StringVar, value='Yes').pack(side=LEFT)
    question12AnswerNo = Radiobutton(question12Frame, text="Nee", variable=question12StringVar, value='No').pack(side=LEFT)

    def checkAnswers():
      question1UserInput = question1Answers.get()
      question2UserInput = question2StringVar.get()
      question3UserInput = question3StringVar.get()
      question4UserInput = question4StringVar.get()
      question5UserInput = question5Answers.get()
      question6UserInput = question6Answers.get()
      question7UserInput = question7StringVar.get()
      question8UserInput = question8StringVar.get()
      question9UserInput = question9StringVar.get()
      question10UserInput = question10StringVar.get()
      question11UserInput = question11StringVar.get()
      question12UserInput = question12StringVar.get()
      return question1UserInput, question2UserInput, question3UserInput, question4UserInput, question5UserInput, question6UserInput, question7UserInput, question8UserInput, question9UserInput, question10UserInput, question11UserInput, question12UserInput
      
    def lastPage():
      window.geometry('500x220')

      titleFrame = Frame(window)
      titleFrame.pack(pady=10)
      title = Label(titleFrame, text="Vacature Toelatings Resultaat", font=("Arial", 20, font.BOLD)).pack() 

      resultFrame = Frame(window)
      resultFrame.pack()
    
      if resultVar == 'failed':
        result = Label(resultFrame, text='Helaas mag u niet solliciteren.\n U voledoet niet aan onze eisen.', fg='red').pack(pady=25)
      elif resultVar == 'passed':
        result = Label(resultFrame, text='U mag solliciteren!\n U voldoet aan onze eisen. \n Wij nemen binnenkort contact met u op.', fg='green').pack(pady=25)
        

    def requirements():
      global resultVar
      resultVar = 'failed'
      question1UserInput, question2UserInput, question3UserInput, question4UserInput, question5UserInput, question6UserInput, question7UserInput, question8UserInput, question9UserInput, question10UserInput, question11UserInput, question12UserInput = checkAnswers()
      if int(question1UserInput) >= 4 and question2UserInput == 'Yes' and question3UserInput == 'Yes' and question4UserInput== 'Yes' and int(question5UserInput) >= 150 and int(question6UserInput) >= 90 and question7UserInput == 'Yes':
        if question8UserInput == 'Female' and redHairStringVar.get() == 'Yes' and int(lengthHairCombobox.get()) >= 20 or question8UserInput == 'Male' and int(questionMaleSelectedQuestion.get()) >= 10:
          resultVar = 'passed' 

      for widgets in window.winfo_children():
        widgets.destroy() 
      lastPage()    



    question8StringVar = StringVar()
    question8StringVar.set("None")

    question8Frame = Frame(window)
    question8Frame.pack()
    question8 = Label(question8Frame, text="Wat is uw geslacht?").pack(side=LEFT)
    question8AnswerMale = Radiobutton(question8Frame, text="Man", variable=question8StringVar, value='Male').pack(side=LEFT)
    question8AnswerFemale = Radiobutton(question8Frame, text="Vrouw", variable=question8StringVar, value='Female').pack(side=LEFT)
    question8AnswerOther = Radiobutton(question8Frame, text="Anders", variable=question8StringVar, value='Other').pack(side=LEFT)



    redHairStringVar = StringVar()
    redHairStringVar.set("None")

    mustacheStringVar = StringVar()
    mustacheStringVar.set("None")

    def displaySelected(*args):
      print('function called')
      question1UserInput, question2UserInput, question3UserInput, question4UserInput, question5UserInput, question6UserInput, question7UserInput, question8UserInput, question9UserInput, question10UserInput, question11UserInput, question12UserInput = checkAnswers()

      if question8UserInput == 'Male':
        for widgets in genderSelectedFrame.winfo_children():
            widgets.destroy()

        for widgets in lengthHairFrame.winfo_children():
            widgets.destroy()
            
        mustacheLabel = Label(genderSelectedFrame, text="Heeft u een snor").pack(side=LEFT)
        mustacheAnswerYes = Radiobutton(genderSelectedFrame, text="Ja", variable=mustacheStringVar, value='Yes').pack(side=LEFT)
        mustacheAnswerNo = Radiobutton(genderSelectedFrame, text="Nee", variable=mustacheStringVar, value='No').pack(side=LEFT)


        def mustacheLengthFunction(*args):
          global questionMaleSelectedQuestion
          redHairStringVar.set('None')
          if mustacheStringVar.get() == 'Yes':
            mustacheStringVar.set('Yes')
            maleSelectedQuestion = Label(mustacheFrame, text="Hoe breed is uw snor? (cm)")
            maleSelectedQuestion.pack(side=LEFT)
            mustacheLength = list(range(1,20))
            questionMaleSelectedQuestion = ttk.Combobox(mustacheFrame, value=mustacheLength, width=4)
            questionMaleSelectedQuestion.pack(side=LEFT)
            print('pass male')
          if mustacheStringVar.get() == 'No':
            for widgets in mustacheFrame.winfo_children():
              widgets.destroy()
            mustacheStringVar.set('None')  
        traceCommandMustache = mustacheStringVar.trace
        traceCommandMustache('w', mustacheLengthFunction) 

      elif question8UserInput == 'Female':
        # if genderSelectedFrame.winfo_exists() == 1:
        for widgets in genderSelectedFrame.winfo_children():
            widgets.destroy()
        for widgets in lengthHairFrame.winfo_children():
            widgets.destroy()
        for widgets in mustacheFrame.winfo_children():
            widgets.destroy()    

        redHairLabel = Label(genderSelectedFrame, text="Heeft u rood krulhaar?").pack(side=LEFT)
        redHairAnswerYes = Radiobutton(genderSelectedFrame, text="Ja", variable=redHairStringVar, value='Yes').pack(side=LEFT)
        redHairAnswerNo = Radiobutton(genderSelectedFrame, text="Nee", variable=redHairStringVar, value='No').pack(side=LEFT)

        def redCurlyHair(*args):
          global lengthHairCombobox
          mustacheStringVar.set('None')
          if redHairStringVar.get() == 'Yes':
            redHairStringVar.set('Yes')
            lengthHairList = list(range(5, 100))
            lengthHairLabel = Label(lengthHairFrame, text='Hoelang is uw haar? (cm)').pack(side=LEFT)
            lengthHairCombobox = ttk.Combobox(lengthHairFrame, value=lengthHairList, width=4)
            lengthHairCombobox.pack(side=LEFT)
          if redHairStringVar.get() == 'No':
            for widgets in lengthHairFrame.winfo_children():
              widgets.destroy()         
            redHairStringVar.set('None')
        traceCommandRedHair = redHairStringVar.trace
        traceCommandRedHair('w', redCurlyHair)    
      elif question8UserInput == 'Other':
        for widgets in genderSelectedFrame.winfo_children():
            widgets.destroy()
        for widgets in lengthHairFrame.winfo_children():
            widgets.destroy()
        for widgets in mustacheFrame.winfo_children():
            widgets.destroy()    

      if question1UserInput != 'None' and question2UserInput != 'None' and question3UserInput != 'None' and question4UserInput != 'None' and question5UserInput != 'None' and question6UserInput != 'None' and question7UserInput != 'None' and question8UserInput != 'None' and question9UserInput != 'None' and question10UserInput != 'None' and question11UserInput != 'None' and question12UserInput != "None":
        # print('pass')
        confirmationButton.pack(pady=25)

      
        

    genderSelectedFrame = Frame(window)
    genderSelectedFrame.pack()
    lengthHairFrame = Frame(window)
    lengthHairFrame.pack()
    mustacheFrame = Frame(window)
    mustacheFrame.pack()
    traceCommand = question8StringVar.trace
    traceCommand('w', displaySelected)

    buttonFrame = Frame(window)
    buttonFrame.pack()  

    confirmationButton = Button(buttonFrame, text="controleer sollicitatie", command= requirements)
    confirmationButton.pack(pady=25)
    confirmationButton.pack_forget()

  main()
  window.mainloop()
code()

# print("""
# ================================
# Sollicitatie "Ruimte Vuilnisman"
# ================================
# """)
# time.sleep(1)
# # questions
# ervaring = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: '))
# diploma = {'ja':True, 'nee':False}.get(input('Bent u in bezit van een diploma MBO-4 ondernemen?: ').lower())
# rijbewijs = {'ja':True, 'nee':False}.get(input('Bent u in bezit van een geldig vrachtwagen rijbewijs?: ').lower())
# hoed = input('Bent u in bezit van een hoge hoge hoed?: ')
# lengte = int(input('Wat is uw lichaamslengte in hele cm?: '))
# gewicht = int(input('Wat is uw lichaamsgewicht in hele kg?: '))
# certificaat = {'ja':True, 'nee':False}.get(input('Bezit u een \"Overleven met gevaarlijk personeel certificaat\"?: ').lower())

# geslacht = input('Bent u een man of vrouw?: ').lower()



# # booleans
# snor = True
# haar = True
# certificaat = True

# if geslacht == 'man':
#   snor = {'ja':True, 'nee':False}.get(input('Heeft u een snor breder dan 10cm?: ').lower())
# elif geslacht == 'vrouw':
#   haar = {'ja':True, 'nee':False}.get(input('Heeft u rood krulhaar langer dan 20 cm?: ').lower())
# else:
#     print('Helaas hebben we u niet begrepen.')
#     sys.exit()

# # questions that don't matter
# input('Bent u van maandag tot vrijdag beschikbaar?: ')
# input('Vul hier 5 slechte en 5 goede punten over jezelf in: ')
# input('Kan je goed met collega\'s samenwerken?: ')
# input('Werk je liever zelfstandig?: ')



# if not all ((snor, haar, certificaat, haar, rijbewijs, diploma, gewicht >= 90, lengte >= 150, ervaring >= 4)):
#     print('Helaas voldoet u niet aan de criteria. Het spijt ons!')
#     time.sleep(5)
#     sys.exit()
# else:
#   print('U voldoet aan de criteria. Uw sollicitatie is verstuurd.')  
