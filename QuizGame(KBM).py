from tkinter import * #this will download all the class and methods from tkinter
from tkinter.ttk import Progressbar
from pygame import mixer 
import pyttsx3

engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

mixer.init()

mixer.music.load('kbc.mp3')#for the entry music
mixer.music.play(-1) #-1 will keep music on loop

def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()


    b=event.widget
    value=b['text']

    for i in range(15):
        if value==correct_answers[i]: #if condtn true complete code executed
            if value==correct_answers[14]:
                def close():
                
                    root2.destroy()
                    root.destroy()

                def playagain():
                    lifeLine50Button.config(state=NORMAL,image=image50)
                    audiencePoleButton.config(state=NORMAL,image=audiencePole)
                    phoneLifelineButton.config(state=NORMAL,image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0,END)
                    questionArea.insert(END,questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])

                    amountLabel.config(image=amountimage)
            
                mixer.music.stop() #entry music will stop 
                mixer.music.load('kbcwon.mp3') #will play the won music
                mixer.music.play()
                root2=Toplevel()
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('Sorry !! You won 0 pounds')
                imgLabel=Label(root2,image=centerImage,bd=0)
                imgLabel.pack(pady=30)

                winLabel=Label(root2,text='You WON',font=('arial',40,'bold'),bg='black',fg='white')
                winLabel.pack()

                playagainButton=Button(root2,text='Play Again',font=('arial',20,'bold'),bg='black',fg='white',bd=0,cursor='hand2',command=playagain)
                playagainButton.pack()

                closeButton=Button(root2,text='Close',font=('arial',15,'bold'),bg='black',fg='white',activebackground='lightblue',cursor='hand2',command=close)
                closeButton.pack()

                happyimage=PhotoImage(file='happy.png')
                sadLabel=Label(root2,image=happyimage,bg='black')
                sadLabel.place(x=30,y=280)

                sadLabel1=Label(root2,image=happyimage,bg='black')
                sadLabel1.place(x=400,y=280)


                root2.mainloop()
                break



            questionArea.delete(1.0,END)#firstly delete the old que
            questionArea.insert(END,questions[i+1])#inserts the new question

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountImages[i])
        
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                lifeLine50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audiencePole)
                phoneLifelineButton.config(state=NORMAL,image=phoneImage)
                
                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountLabel.config(image=amountimage)
            

            root1=Toplevel()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('Sorry !! You won 0 pounds')
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loseLabel=Label(root1,text='You lose',font=('arial',40,'bold'),bg='black',fg='white')
            loseLabel.pack()

            tryagainButton=Button(root1,text='Try Again',font=('arial',20,'bold'),bg='black',fg='white',bd=0,cursor='hand2',command=tryagain)
            tryagainButton.pack()

            closeButton=Button(root1,text='Close',font=('arial',15,'bold'),bg='black',fg='white',activebackground='lightblue',cursor='hand2',command=close)
            closeButton.pack()

            sadimage=PhotoImage(file='sad.png')
            sadLabel=Label(root1,image=sadimage,bg='black')
            sadLabel.place(x=30,y=280)

            sadLabel1=Label(root1,image=sadimage,bg='black')
            sadLabel1.place(x=400,y=280)


            root1.mainloop()
            break


def lifeline50():
    lifeLine50Button.config(image=image50X,state=DISABLED)
    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton2.config(text='')
        optionButton4.config(text='')


    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='') 

    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='') 

    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='') 

    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='') 

    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')

def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX,state=DISABLED)
    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620,y=190)
    progressbarC.place(x=660,y=190)
    progressbarD.place(x=700,y=190)

    progressbarLabelA.place(x=580,y=320)
    progressbarLabelB.place(x=620,y=320)
    progressbarLabelC.place(x=660,y=320)
    progressbarLabelD.place(x=700,y=320)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=20)

    if questionArea.get(1.0,'end-1c')==questions[2]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=20)

    if questionArea.get(1.0,'end-1c')==questions[3]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=10)

    if questionArea.get(1.0,'end-1c')==questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=60)
        progressbarD.config(value=10)

    if questionArea.get(1.0,'end-1c')==questions[5]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=40)

    if questionArea.get(1.0,'end-1c')==questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=40)

    if questionArea.get(1.0,'end-1c')==questions[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=10)

    if questionArea.get(1.0,'end-1c')==questions[8]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=70)

    if questionArea.get(1.0,'end-1c')==questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=70)
        progressbarC.config(value=90)
        progressbarD.config(value=10)

    if questionArea.get(1.0,'end-1c')==questions[10]:
        progressbarA.config(value=87)
        progressbarB.config(value=11)
        progressbarC.config(value=65)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=92)
        progressbarD.config(value=90)
    
    if questionArea.get(1.0,'end-1c')==questions[12]:
        progressbarA.config(value=10)
        progressbarB.config(value=40)
        progressbarC.config(value=50)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[14]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=40)


def phoneLifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70,y=260)
    phoneLifelineButton.config(image=phoneImageX,state=DISABLED)

def phoneclick():
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f'The answer is {correct_answers[i]}')
            engine.runAndWait()


correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "11:23PM", "CSK", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]




questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which Language?",
             "Finish the sequence: 9, 18, 27, „?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "who founded microsoft"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "RCB",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter","6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]


root=Tk() #this will help to create gui window

root.geometry('1270x652+0+0') #1270x652 for the width nd height and +0+0 for x and y dist
root.title('Kaun Banega Millionaire created by Shrawani Autkar')#this will give us the title

root.config(bg='black')

leftframe=Frame(root,bg='black',padx=90)
leftframe.grid(row=0,column=0)

topFrame=Frame(leftframe,bg='black',pady=15)
topFrame.grid()

centerFrame=Frame(leftframe,bg='black',pady=15)
centerFrame.grid(row=1,column=0)

bottomFrame=Frame(leftframe)
bottomFrame.grid(row=2,column=0)

rightframe=Frame(root,pady=25,padx=50,bg='black')
rightframe.grid(row=0,column=1)

image50=PhotoImage(file='50-50.png')
image50X=PhotoImage(file='50-50-X.png') #image50 is a object variable name

lifeLine50Button=Button(topFrame,image=image50,bg='black',border=0,activebackground='black',width=180,height=80,command=lifeline50) #created button for the above image
lifeLine50Button.grid(row=0,column=0)

audiencePole=PhotoImage(file='audiencePole.png')
audiencePoleX=PhotoImage(file='audiencePoleX.png')


audiencePoleButton=Button(topFrame,image=audiencePole,bg='black',border=0,activebackground='black',width=180,height=80,command=audiencePoleLifeline) #created button for the above image
audiencePoleButton.grid(row=0,column=1)

phoneImage=PhotoImage(file='phoneAFriend.png')
phoneImageX=PhotoImage(file='phoneAFriendX.png')

phoneLifelineButton=Button(topFrame,image=phoneImage,bg='black',border=0,activebackground='black',width=180,height=80,command=phoneLifeline) #created button for the above image
phoneLifelineButton.grid(row=0,column=2)
callimage=PhotoImage(file='phone.png')

callButton=Button(root,image=callimage,bd=0,bg='black',activebackground='black',cursor='hand2',command=phoneclick)

centerImage=PhotoImage(file='center.png')

logoLabel=Label(centerFrame,image=centerImage,bg='black',width=300,height=200)
logoLabel.grid(row=0,column=0)

amountimage=PhotoImage(file='Picture0.png')
amountimage1=PhotoImage(file='Picture1.png')
amountimage2=PhotoImage(file='Picture2.png')
amountimage3=PhotoImage(file='Picture3.png')
amountimage4=PhotoImage(file='Picture4.png')
amountimage5=PhotoImage(file='Picture5.png')
amountimage6=PhotoImage(file='Picture6.png')
amountimage7=PhotoImage(file='Picture7.png')
amountimage8=PhotoImage(file='Picture8.png')
amountimage9=PhotoImage(file='Picture9.png')
amountimage10=PhotoImage(file='Picture10.png')
amountimage11=PhotoImage(file='Picture11.png')
amountimage12=PhotoImage(file='Picture12.png')
amountimage13=PhotoImage(file='Picture13.png')
amountimage14=PhotoImage(file='Picture14.png')
amountimage15=PhotoImage(file='Picture15.png')

amountImages= [amountimage1,amountimage2,amountimage3,amountimage4,amountimage5,amountimage6,
               amountimage7,amountimage8,amountimage9,amountimage10,amountimage11,amountimage12,
               amountimage13,amountimage14,amountimage15]



amountLabel=Label(rightframe,image=amountimage,bg='black')
amountLabel.grid(row=0,column=0) 

layoutImage=PhotoImage(file='lay.png')

layoutLabel=Label(bottomFrame,image=layoutImage,bg='black')
layoutLabel.grid(row=0,column=0)

questionArea=Text(bottomFrame,font=('arial',18,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)#due to wrap pura word niche jyega agr half hai toh
questionArea.place(x=70,y=10)

questionArea.insert(END,questions[0])

labelA=Label(bottomFrame,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=60,y=110)

optionButton1=Button(bottomFrame,text=first_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=100)

labelB=Label(bottomFrame,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=330,y=110)

optionButton2=Button(bottomFrame,text=second_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton2.place(x=370,y=100)

labelC=Label(bottomFrame,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=60,y=190)

optionButton3=Button(bottomFrame,text=third_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=180)

labelD=Label(bottomFrame,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=330,y=190)

optionButton4=Button(bottomFrame,text=fourth_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

progressbarA=Progressbar(root,orient=VERTICAL,length=120)
progressbarB=Progressbar(root,orient=VERTICAL,length=120)
progressbarC=Progressbar(root,orient=VERTICAL,length=120)
progressbarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarLabelA=Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelB=Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelC=Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelD=Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='white')



optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)



root.mainloop() #this mainloop method will keep the window on hold and we can see the window
