from tkinter import *
from subprocess import call
import tkinter.messagebox
import speech_recognition as sr
import threading
import queue
import time
import os
import sys
import datetime

class GUI:
    class tkinter:
        global fg_color
        fg_color='#254f62'
        global bg_color
        bg_color='#c6d9ec'
        global back_image
        global icon_image
        global prec_image
        global help_image
        
        class Main:
            
            def main():
                root0=Tk()
                root0.withdraw()
                x=root=Toplevel()
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                #print(screen_width)
                #print(screen_height)
                root.geometry('1366x768')
                root.minsize(800,700)
                global back_image
                back_image=PhotoImage(file='C:\\Users\\RAHUL\\Documents\\pexels-photo-248152_1_.gif')
                global icon_image
                icon_image=PhotoImage(file='C:\\Users\\RAHUL\\Pictures\\Sound_image.gif')
                label1=Label(root,image=back_image).pack(side='top',fill='both')
                label2=Label(root,text='Extra Element Analysis',font='impact 34',fg=fg_color,bg=bg_color).place(x=400,y=15)
                sulphur_button=Button(root,text='Sulphur ',font='impact 30',fg=fg_color,bg=bg_color,padx=10,pady=5,command=GUI.tkinter.Sulphur.sulphur).place(x=500,y=300)
                nitro_button=Button(root,text='Nitrogen',font='impact 30',fg=fg_color,bg=bg_color,padx=10,pady=5,command=GUI.tkinter.Nitro.nitro).place(x=500,y=420)
                halogen_button=Button(root,text='Halogen ',font='impact 30',fg=fg_color,bg=bg_color,padx=10,pady=5,command=GUI.tkinter.Halogen.halogen).place(x=500,y=540)
                #button bindings for toolbar animation
                def enter(event):#first button event
                    sound_button.config(height='70',width='70')
                def enter2(event):#second event
                    help_file_button.config(height='70',width='70')
                def enter3(event):#third event
                    prec_button.config(height='70',width='70')
                def leave(event):#fourth event
                    sound_button.config(height='60',width='60')
                def leave2(event):#fifth event
                    help_file_button.config(height='60',width='60')
                def leave3(event):#sixth event
                    prec_button.config(height='60',width='60')

                def sound():
                    os.system("""echo "Extra Element, Analysis. Sulphur. Nitrogen. Halogen. Help File. Precautions. Speech Synthesis. Exit." | spd-say -e -r -50""")
                def helpfile():
                    filename='/home/hp/Documents/extraelements.pdf'
                    call(['xdg-open',filename])
                    
                global sound_image
                sound_image=PhotoImage(file='C://Users//RAHUL//Downloads//Sound (1).gif')
                sound_button=Button(root,image=sound_image,bg=bg_color,fg=fg_color,height='60',width='60',text='Sound', command=sound)
                sound_button.bind('<Enter>',enter)
                sound_button.bind('<Leave>',leave)
                sound_button.place(x=15,y=300)
                
                global help_image
                help_image=PhotoImage(file='C://Users//RAHUL//Downloads//Help.gif')
                help_file_button=Button(root,text='help file',image=help_image,bg=bg_color,height='60',width='60', command=helpfile)
                help_file_button.bind('<Enter>',enter2)
                help_file_button.bind('<Leave>',leave2)
                help_file_button.place(x=15,y=400)
                
                global prec_image
                prec_image=PhotoImage(file='C://Users//RAHUL//Downloads//prec.gif')
                def prec():
                    #root.withdraw()
                    root1=Toplevel()
                    global back_image
                    bg_image=Label(root1,image=back_image).pack(side='top',fill='both')
                    label1=Label(root1,text='PRECAUTIONS',font='impact 36',fg='red',bg=bg_color).place(x=450,y=20)
                    label2=Label(root1,text="1) Don't Touch the sodium metal with your fingers,Use forceps only",font='impact 20',fg='red',bg=bg_color).place(x=20,y=120)
                    label3=Label(root1,text='2) Never through the sodium metal into the sink',font='impact 20',fg='red',bg=bg_color).place(x=20,y=220)
                    label4=Label(root1,text='3) Always use freshly prepared ferrous sulphate & sodium nitroprussie solution',font='impact 20',fg='red',bg=bg_color).place(x=20,y=320)
                    label5=Label(root1,text='4) In layer test, Shake the test tube by putting thumb on the mouth of test tube',font='impact 20',fg='red',bg=bg_color).place(x=20,y=420)
                    label6=Label(root1,text='5) Remove Sodium cyanide & Sodium sulphide before performing test for Halogens',font='impact 20',fg='red',bg=bg_color).place(x=20,y=520)
                    def home():
                        root1.withdraw()
                        GUI.tkinter.Main.main()
                    home_button=Button(root1,text='Home',fg=fg_color,bg=bg_color,font='impact 20',command=home,padx=3,pady=3).place(x=10,y=650)
                prec_button=Button(root,image=prec_image,bg=bg_color,height='60',width='60',command=prec)
                prec_button.bind('<Enter>',enter3)
                prec_button.bind('<Leave>',leave3)
                prec_button.place(x=15,y=500)
                def exit():
                    message=tkinter.messagebox.askquestion('quit','Do you really want to quit?')
                    if message=='yes':
                        root.withdraw()
                #prec_text=Label(root,text='Precautions',font='impact 28',fg=fg_color,bg=bg_color).place(x=550,y=220)
                exit_button=Button(root,text='Exit',font='impact 20',fg=fg_color,bg=bg_color,command=exit,padx=3,pady=3).place(x=20,y=700)
                speech_button=Button(root,text='Speech Synthesis',font='impact 20',fg=fg_color,bg=bg_color,command=Thread,padx=3,pady=3).place(x=488,y=700)
                #sound_button=Button(root,text='Sound',font='impact 20',fg=fg_color,bg=bg_color,command=sound,padx=3,pady=3).place(x=20,y=650)
                clock = Label(root, font='impact 20', fg=fg_color,bg=bg_color)
                clock.place(x=1090, y=710) 

                def tick():
                    date = str(datetime.date.today())
                    time_string = time.strftime('%H:%M:%S')
                    clock.config(text=date+"  "+time_string)
                    clock.after(200, tick)

                tick()
                root.mainloop()
                root0.mianlopp()

            # sulphur analysis
        class Sulphur:        
            
            def sulphur():
                root.withdraw()
                root2=Toplevel()#2nd window
                #root.minsize(800,700)
                global back_image
                back_image=PhotoImage(file='C:\\Users\\RAHUL\\Documents\\pexels-photo-248152_1_.gif')
                bg=Label(root2,image=back_image).pack(side='top',fill='both')
                label1=Label(root2,text='Test for Sulphur',font='impact 35',fg=fg_color,bg=bg_color).place(x=480,y=5)
                label2=Label(root2,text='Sodium Nitroprusside Test',font='impact 20',fg=fg_color,bg=bg_color).place(x=300,y=150)
                label3=Label(root2,text='>Take 1-2ml of the sodium extract in the test tube.',font='impact 20',fg=fg_color,bg=bg_color).place(x=300,y=200)
                label4=Label(root2,text='>add 1ml of freshly prepared sodium nitroprusside solution into it',font='impact 20',fg=fg_color,bg=bg_color).place(x=300,y=250)
                #labell5=Label(root2,text='>A violet color precipitate indicates the presence of sulphur?',font='impact 20',fg=fg_color,bg=bg_color).place(x=25,y=350)
                label6=Label(root2,text='Do you see a Violet Colour precipitate?',font='impact 23',fg=fg_color,bg=bg_color).place(x=400,y=450)
                class reac:
                    def react():
                        tkinter.messagebox.showinfo('','Sulphur is present')
                        answer=tkinter.messagebox.askquestion('','Do you want to see the reaction?')
                        if answer=='yes':
                            label2=Label(root2,text='Na\u2082S + Na\u2082[Fe(CN)\u2085NO]--->Na\u2084[Fe(CN)\u2085NOS]',fg=fg_color,font='impact 25',bg=bg_color).place(x=350,y=630)
                class no_reac:
                    def noreact():
                        tkinter.messagebox.showinfo('','Sulphur is not present')
                class home1:
                    def home():
                        root2.withdraw()
                        GUI.tkinter.Main.main()
                class back1:
                    def back():
                        root2.withdraw()
                        GUI.tkinter.Main.main()
                def sound():
                    os.system("""echo "Test for Sulphur. Sodium Nitroprusside Test. Take 1 to 2 mililitres of the sodium extract in the test tube, and add 1 mililitre of freshly prepared sodium nitroprusside solution into it. What do you see? Do you see a Violet Colour precipitate?" | spd-say -e -r -50 -t female3""")
                home_button=Button(root2,text='Home',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3,command=home1.home).place(x=10,y=680)
                back_button=Button(root2,text='Back',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3,command=back1.back).place(x=1200,y=680)
                sound_button=Button(root2,text='Sound',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3,command=sound).place(x=600,y=680)
                opt_button1=Button(root2,text='Yes',fg=fg_color,bg=bg_color,font='impact 22',padx=3,pady=4,command=reac.react).place(x=400,y=525)
                opt_button2=Button(root2,text=' No ',fg=fg_color,bg=bg_color,font='impact 22',padx=3,pady=4,command=no_reac.noreact).place(x=840,y=525)


                
            
            #nitrogen analysis
        class Nitro:
                def nitro():
                    root.withdraw()
                    root1=Toplevel()
                    #root.minsize(800,700)
                    global back_image
                    bg=Label(root1,image=back_image).pack(side='top',fill='both')
                    label1=Label(root1,text='Test for Nitrogen',font='impact 35',fg=fg_color,bg=bg_color).place(x=480,y=5)
                    label2=Label(root1,text=">Take 1-2 ml of the Lassainge's Extract in a test tube, and add ferrous sulphate solution to it",font='impact 20',fg=fg_color,bg=bg_color).place(x=150,y=200)
                    label3=Label(root1,text=">A dirty green precipitate of ferrous oxide may be obtained.",font='impact 20',fg=fg_color,bg=bg_color).place(x=150,y=240)
                    label4=Label(root1,text=">If no precpitate is formed or seen",font='impact 20',fg=fg_color,bg=bg_color).place(x=150,y=280)
                    label5=Label(root1,text=">Add a few drops of dilute sodium hydroxide solution to obtain it.",font='impact 20',fg=fg_color,bg=bg_color).place(x=150,y=320)
                    label6=Label(root1,text=">Now heat this mixture gently with shaking for 1 minute and add dilute sulphuric acid into it.",font='impact 20',fg=fg_color,bg=bg_color).place(x=150,y=360)
                    
                    def nitro_reac():
                        tkinter.messagebox.showinfo('','Nitrogen is Present')
                        msg=tkinter.messagebox.askquestion('','Do you want to see reaction?')
                        if msg=='yes':
                            label8=Label(root1,text='FeSO\u2084 + 2NaOH--->Fe(OH)\u2082 + Na\u2082SO\u2084',font='ariel 18',fg=fg_color,bg=bg_color).place(x=405,y=630)
                    def nitro_reac1():
                        tkinter.messagebox.showinfo('','Nitrogen is Absent')
                    label7=Label(root1,text='Do you see a Prussian Blue color precipitate?',font='impact 20',fg=fg_color,bg=bg_color).place(x=390,y=530)
                    yes_button=Button(root1,text='YES',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3,command=nitro_reac).place(x=390,y=570)
                    no_button=Button(root1,text=' NO ',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3, command=nitro_reac1).place(x=840,y=570)
                    def home():
                        root1.withdraw()
                        GUI.main()
                    def back():
                        root1.withdraw()
                        GUI.main()
                    def sound():
                        os.system("""echo "Test for Nitrogen. Take 1 to 2 mililitres of Lassainge's Extract in a test tube, and add ferrous sulphate solution to it. A dirty green precipitate of ferrous oxide may be obtained. If no precipitate is formed or seen, add a few drops of dilute sodium hydroxide solution to obtain the it. Now heat this mixture gently with a little shaking for 1 minute and finally add dilute sulphuric acid into it." | spd-say -e -r -70 -t female3""")
                    home_button=Button(root1,text='Home',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3,command=home).place(x=10,y=680)
                    back_button=Button(root1,text='Back',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3,command=back).place(x=1220,y=680)
                    sound_button=Button(root1,text='Sound',font='impact 20',fg=fg_color,bg=bg_color,padx=3,pady=3,command=sound).place(x=600,y=680)


                
            
            #halogen analysis
                    
        class Halogen:
                def halogen():
                    root.withdraw()
                    root3=Toplevel()
                    global back_image
                    bg_image=Label(root3,image=back_image).pack(side='top',fill='both')                                            
                    label1=Label(root3,text='Silver Nitrate Test',font='impact 35',fg=fg_color,bg=bg_color).place(x=440,y=5)
                    def present():
                        root3.withdraw()
                        root4=Toplevel()
                        global back_image
                        bg_image=Label(root4,image=back_image).pack(side='top',fill='both')
                        label6=Label(root4,text='STEPS TO PROCEED',font='impact 28',fg=fg_color,bg=bg_color).place(x=510,y=40)
                        label=Label(root4,text='-> Take 1-2ml of sodium extract in test tube & acidify it with dilute nitric acid',font='impact 18',fg=fg_color,bg=bg_color).place(x=120,y=100)
                        label2=Label(root4,text='-> Add silver nitrate solution(0.5 ml).',font='impact 18',fg=fg_color,bg=bg_color).place(x=120,y=140)
                        label3=Label(root4,text='-> A white precipiate soluble in ammonium hydroxide indicates the presence of CHLORINE',font='impact 18',fg=fg_color,bg=bg_color).place(x=120,y=180)
                        label4=Label(root4,text='-> A pale yellow precipitate soluble in acess ammonium hydroxide solution indicates the presence of BROMINE',font='impact 18',fg=fg_color,bg=bg_color).place(x=120,y=220)
                        label5=Label(root4,text='-> And a yellow precipitate insoluble in ammonium hydroxide indicates the presence of IODINE',font='impact 18',fg=fg_color,bg=bg_color).place(x=120,y=260)
                        def react2():
                            label=Label(root4,text='Nax + AgNO\u2083--->AgX + NaNO\u2083',font='impact 16',fg=fg_color,bg=bg_color).place(x=120,y=400)
                            label1=Label(root4,text='If X=Cl then AgCl will be formed which is white color precipitate',font='impact 16',fg=fg_color,bg=bg_color).place(x=120,y=430)
                            label2=Label(root4,text='If X=Br then AgBr will be formed which is pale yellow color precipitate',font='impact 16',fg=fg_color,bg=bg_color).place(x=120,y=460)
                            label3=Label(root4,text='If X=I then AgI will be formed which is yellow color precipitate',font='impact 16',fg=fg_color,bg=bg_color).place(x=120,y=490)
                        button=Button(root4,text='Reactions of involved in above tests',font='impact 15',fg=fg_color,bg=bg_color,command=react2).place(x=480,y=300)
                        def home():
                            root4.withdraw()
                            GUI.tkinter.Main.main()
                        def back():
                            root4.withdraw()
                            halogen()
                        def sound():
                            os.system("""echo "STEPS TO PROCEED. Take 1 to 2 mililitres of sodium extract in test tube and acidify it with dilute nitric acid. Add to it 0.5 mililitres silver nitrate solution. A white precipiate soluble in ammonium hydroxide indicates the presence of CHLORINE. A pale yellow precipitate soluble in acess ammonium hydroxide solution indicates the presence of BROMINE. And a yellow precipitate insoluble in ammonium hydroxide indicates the presence of IODINE'" | spd-say -e -r -50""")
                        home_button=Button(root4,text='Home',font='impact 22',fg=fg_color,bg=bg_color,command=home,padx=3,pady=3).place(x=10,y=650)
                        back_button=Button(root4,text='Back',font='impact 22',fg=fg_color,bg=bg_color,command=back,padx=3,pady=3).place(x=1200,y=650)
                        sound_button=Button(root4,text='Sound',font='impact 22',fg=fg_color,bg=bg_color,padx=3,pady=3,command=sound).place(x=600,y=650)
                    pre_button=Button(root3,text='Nitrogen/Sulphur is present',fg=fg_color,bg=bg_color,font='impact 26',command=present).place(x=400,y=150)
                    def home():
                        root3.withdraw()
                        GUI.tkinter.Main.main()
                    def back():
                        root3.withdraw()
                        GUI.tkinter.Main.main()
                    def sound():
                        os.system("""echo "Sliver Nitrate Test. Option 1. Nitrogen or Sulphur is present. Option 2. Nitrogen or Sulphur is absent" | spd-say -e -r -60""")
                    home_button=Button(root3,text='Home',font='impact 22',fg=fg_color,bg=bg_color,command=home).place(x=10,y=650)
                    back_button=Button(root3,text='Back',font='impact 22',fg=fg_color,bg=bg_color,command=back).place(x=1220,y=650)
                    sound_button=Button(root3,text='Sound',font='impact 22',fg=fg_color,bg=bg_color,padx=3,pady=3,command=sound).place(x=600,y=650)
                    def absent():
                        root3.withdraw()
                        root5=Toplevel()
                        global back_image
                        bg_image=Label(root5,image=back_image).pack(side='top',fill='both')
                        label4=Label(root5,text='STEPS TO PROCEED',font='impact 28',fg=fg_color,bg=bg_color).place(x=510,y=100)
                        label1=Label(root5,text='-> Take 1ml of sodium extract in test tube & acidify it with conc. nitric acid(2-3ml)',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=200)
                        label2=Label(root5,text='-> Boil the mixture to reduce the original volume to half to get rid of HCN/H2S & perform silver nitrate test',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=240)
                        labell3=Label(root5,text='-> When the silver nitrate test is positive then go to Layer Test',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=280)
                        def layer():
                            root5.withdraw()
                            root6=Toplevel()
                            global back_image
                            bg_image=Label(root6,image=back_image).pack(side='top',fill='both')
                            label1=Label(root6,text='LAYER TEST',font='impact 30',fg=fg_color,bg=bg_color).place(x=510,y=20)
                            label2=Label(root6,text='Take 1-2ml of sodium extract in a test tube & add 1ml of carbon tetrachloride/chloroform to it.',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=120)
                            label2=Label(root6,text='Add 1ml of chlorine water & shake the test tube well',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=160)
                            label3=Label(root6,text='If the organic layer turns orange then it indicates bromine',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=200)
                            label4=Label(root6,text='If the organic layer turns violet then it indicates iodine',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=240)
                            label5=Label(root6,text='If no color change then chlorine is present',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=280)
                            def test():
                                label1=Label(root6,text='2NaBr + Cl\u2082---> 2NaCl + Br\u2082 \t(Br\u2082 gives orange color to organic layer)',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=500)
                                label2=Label(root6,text='2NaI + Cl\u2082---> 2NaCl + I\u2082 \t(I\u2082 gives violet color to organic layer)',font='impact 20',fg=fg_color,bg=bg_color).place(x=120,y=540)
                            button1=Button(root6,text='Reactions of Layer Test',font='impact 24',fg=fg_color,command=test,bg=bg_color).place(x=450,y=400)
                            def home():
                                root6.withdraw()
                                GUI.tkinter.Main.main()
                            def back():
                                root6.withdraw()
                                absent()
                            def sound():
                                os.system("""echo "LAYER TEST. Take 1 to 2 mililitres of sodium extract in a test tube and add 1 mililitres of carbon tetrachloride or chloroform to it. Add 1 mililitres of chlorine water and shake the test tube well. If the organic layer turns orange then it indicates bromine. If the organic layer turns violet then it indicates iodine. If no color change then chlorine is present" | spd-say -e -r -60""")
                            exit_button=Button(root6,text='Home',fg=fg_color,bg=bg_color,font='impact 22',command=home).place(x=10,y=650)
                            back_button=Button(root6,text='Back',fg=fg_color,bg=bg_color,font='impact 22',command=back).place(x=1200,y=650)
                            sound_button=Button(root6,text='Sound',font='impact 22',fg=fg_color,bg=bg_color,padx=3,pady=3,command=sound).place(x=600,y=650)
                        layer_button=Button(root5,text="Go to Layer's Test",fg=fg_color,bg=bg_color,font='impact 20',command=layer).place(x=530,y=350)
                        def back():
                            root5.withdraw()
                            halogen()
                        def home():
                            root5.withdraw()
                            GUI.tkinter.Main.main()
                        def sound():
                                os.system("""echo "STEPS TO PROCEED. Take 1 mililitre of sodium extract in test tube and acidify it with 2 to 3 mililitres concentrated nitric acid. Boil the mixture to reduce the original volume to half to get rid of Hydrogen Cyanide or Hidrogen disulphide and perform silver nitrate test. If the silver nitrate test is positive then proceed to Layer Test." | spd-say -e -r -60""")
                        home_button=Button(root5,text='Home',font='impact 22',fg=fg_color,bg=bg_color,command=home).place(x=10,y=650)
                        back_button=Button(root5,text='Back',font='impact 22',fg=fg_color,bg=bg_color,command=back).place(x=1200,y=650)
                        sound_button=Button(root5,text='Sound',font='impact 22',fg=fg_color,bg=bg_color,padx=3,pady=3,command=sound).place(x=600,y=650)
                    ab_button=Button(root3,text=' Nitrogen/sulphur is absent ',fg=fg_color,bg=bg_color,font='impact 26',command=absent).place(x=400,y=300)

                
                
            
class Speech:
    def speech_recognition():
        while True:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
            try:
                print('say something:')
                speech_str=r.recognize_google(audio)
                print('done')
                if speech_str=='nitrogen':
                    GUI.tkinter.Nitro.nitro()
                elif speech_str=='sulphur':
                    GUI.tkinter.Sulphur.sulphur()
                    if speech_str=='home':
                        GUI.tkinter.Sulphur.home1.home()
                    elif speech_str=='back':
                        GUI.tkinter.Sulphur.back1.back()
                    elif speech_str=='yes':
                        GUI.tkinter.Sulphur.reac.react()
                    elif speech_str=='no':
                        GUI.tkinter.Sulphur.no_reac.noreact()
                elif speech_str=='halogens':
                    GUI.tkinter.Halogen.halogen()
                elif speech_str=='precautions':
                    GUI.tkinter.Main.prec()
            except sr.UnknownValueError:
                print('Try Again')
                #tkinter.messagebox.showinfo('','Try Again')
            except sr.RequestError:
                print('Check your Network')
                #tkinter.messagebox.showinfo('','Check your network connection')
class Thread:
    t1=threading.Thread(target=Speech.speech_recognition,args=(),daemon=True)
    t1.start()
    #print('thread started')


    
if __name__=='__main__':
    GUI.tkinter.Main.main()










    
'''

class Threading:
    global t2
    def speech():
        #t2.start()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Now! Listening")
            audio = r.listen(source)
         
        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("You said: " + r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY"))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        text=r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
        if text=='nitrogen':
            GUI.main.nitro()
    def __init__(self):
        #t1=threading.Thread(target=GUI,args=(),daemon=True)
        global t2
        t2=threading.Thread(target=Threading.speech,args=(),daemon=True)
        q=queue.Queue()
        #q.put(t1)
        q.put(t2)
        time.sleep(10)
        q.get(t2)
def main2():
    GUI.main()
    Threading()
main2()
'''
