# Libraries for the model
from doctest import master
from click import command
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import warnings


# Libraries for tkinter
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import sqlite3
import sys
import random
from PIL import Image, ImageTk
from turtle import color
from PIL import Image,ImageTk
from pyparsing import replaceWith
from regex import F
from time import strftime

from fullInterfaceDatabase import DbConnection

# from test import showWindow

# from model_interface.test import test

# Loading the model
model = load_model(r"C:\Users\SHADY SUPERSUSER\Desktop\jupyter_models\TubNorPneoCo.model")


# Code to test an image
def test(filename):
    # Loading an image to test the model
    img = image.load_img(filename, target_size=(224, 224))

    x = image.img_to_array(img)

    x = np.expand_dims(x, axis=0)

    img_data = preprocess_input(x)

    classes = model.predict(img_data)

    # Classes
    result0 = classes[0][0]
    result1 = classes[0][1]
    result2 = classes[0][2]
    result3 = classes[0][3]
    result4 = classes[0][4]

    if result0 > result1 and result0 > result2 and result0 > result3 and result0 > result4:
        # messagebox.showinfo("++Result",f"Person is affected by covid with pneumonia - {round(result0 * 100, 2)}% sure")
        return f"Covid with pneumonia - {round(result0 * 100, 2)}% sure"
    if result1 > result0 and result1 > result2 and result1 > result3 and result1 > result4:
        # messagebox.showinfo("++Result",f"Person is affected by covid19 - {round(result1 * 100, 2)}% sure")
        return f"Covid19 - {round(result1 * 100, 2)}% sure"
    if result2 > result0 and result2 > result1 and result2 > result3 and result2 > result4:
        # messagebox.showinfo("++Result",f"Person is affected by Pneumonia - {round(result2 * 100, 2)}% sure")
        return f"Pneumonia - {round(result2 * 100, 2)}% sure"
    if result3 > result0 and result3 > result1 and result3 > result2 and result3 > result4:
        # messagebox.showinfo("++Result",f"Person is normal - {round(result3 * 100, 2)}% sure")
        return f"Normal - {round(result3 * 100, 2)}% sure"
    if result4 > result0 and result4 > result1 and result4 > result2 and result4 > result3:
        # messagebox.showinfo("++Result",f"Person is affected by Tuberculosis - {round(result4 * 100, 2)}% sure")
        return f"Tuberculosis - {round(result4 * 100, 2)}% sure"


class sButtons:


    def __init__(self,master):
        
        self.TITLE = "Input X-ray or CT-scan Image"
        self.text = ""
        self.index = 0
        self.diseaseName=""


        full_canv.update_idletasks()
        bottom_canv = Canvas(full_canv, bg='#bd781d', highlightthickness=0)
        bottom_canv.place(y=30, relx=0, relwidth=1,
                          relheight=((full_canv.winfo_reqheight() - 30) / full_canv.winfo_reqheight()))

        self.signFrm=Frame(bottom_canv,highlightthickness=0,bg='orange')
        # self.signFrm.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)

        self.cover_canv = Canvas(bottom_canv, bg="lavender", highlightthickness=0)
        self.cover_canv.place(rely=0.05, relx=0.1, relheight=0.9, relwidth=0.8)

        self.coverTopCan=Canvas(self.cover_canv,bg='white',highlightthickness=0)
        self.coverTopCan.place(rely=0,relx=0,relheight=0.3,relwidth=1)

        #Addin background logo label
        logoImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Pictures\images (2).jpg")
        logoImage=logoImage.resize((220,150),Image.ANTIALIAS)
        logoImage=ImageTk.PhotoImage(logoImage,master=root)
        self.logoLbl=Label(self.coverTopCan,image=logoImage,text='',bd=0,bg='lavender')
        self.logoLbl.place(relx=0.4,rely=0.27)
        self.logoLbl.image=logoImage

        #Middle Content Canvas
        self.coverContCan=Canvas(self.cover_canv,bg='white',highlightthickness=0)
        self.coverContCan.place(rely=0.3,relx=0,relheight=0.4,relwidth=1)

        self.coverContLbl=Label(self.coverContCan,bg='white',fg='black', font=("Georgia", 20),text='Life Care lung Disease Detection Model\n Register now to check your lung status')
        self.coverContLbl.place(relx=0.3,rely=0.3)

        
        self.coverbuttCan=Canvas(self.cover_canv,bg='white',highlightthickness=0)
        self.coverbuttCan.place(rely=0.7,relx=0,relheight=0.3,relwidth=1)
        

        #Addin background to button
        signupImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Desktop\pythonProjects\FaceRecognitionMUTattendance\assets\Blue-Button-PNG.png")
        signupImage=signupImage.resize((150,90),Image.ANTIALIAS)
        signupImage=ImageTk.PhotoImage(signupImage,master=root)
        self.signBTN = Button(self.coverbuttCan, text="",image=signupImage,bd=0,relief=FLAT,compound=CENTER, bg="white", fg="orange", font=("Georgia", 20),command=self.signup) #signup
        self.signBTN.place(rely=0, relx=0.43) # , relwidth=1
        self.signBTN.image=signupImage



    def signup(self): 
        # Registration top label
        self.TITLE = "Enter you details to Signup"
        self.text = ""
        self.index = 0

        full_canv.update_idletasks()
        bottom_canv = Canvas(full_canv, bg='#bd781d', highlightthickness=0)
        bottom_canv.place(y=30, relx=0, relwidth=1,
                          relheight=((full_canv.winfo_reqheight() - 30) / full_canv.winfo_reqheight()))

        self.signFrm=Frame(bottom_canv,highlightthickness=0,bg='orange')
        # self.signFrm.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)

        self.login_canv = Canvas(bottom_canv, bg="lavender", highlightthickness=0)
        self.login_canv.place(rely=0.05, relx=0.2, relheight=0.9, relwidth=0.6)

        # Top animated label
        self.sign_title_lbl = Label(self.login_canv, text="", bg="lavender", fg="orange", font=("Georgia", 20))
        self.sign_title_lbl.place(y=45, x=0, relwidth=1)

        # Content canvas for the content
        self.contCan=Canvas(self.login_canv,bg='lavender',highlightthickness=0)
        self.contCan.place(relx=0,rely=0.19,relheight=0.52,relwidth=1)

        # Labels
        self.first_lbl = Label(self.contCan, text="First Name", bg="lavender", fg="#111111", font=("Georgia", 14))
        self.first_lbl.grid(row=0,column=0,sticky='w',padx=(150,10))#,pady=(10,0)
        self.last_lbl = Label(self.contCan, text="Last Name", bg="lavender", fg="#111111", font=("Georgia", 14))
        self.last_lbl.grid(row=2,column=0,sticky='w',padx=(150,10))
        self.phone_lbl = Label(self.contCan, text="Phone Number", bg="lavender", fg="#111111", font=("Georgia", 14))
        self.phone_lbl.grid(row=4,column=0,sticky='w',padx=(150,10))
        self.email_lbl = Label(self.contCan, text="Email", bg="lavender", fg="#111111", font=("Georgia", 14))
        self.email_lbl.grid(row=6,column=0,sticky='w',padx=(150,10))
        self.gender_lbl = Label(self.contCan, text="gender", bg="lavender", fg="#111111", font=("Georgia", 14))
        self.gender_lbl.grid(row=8,column=0,sticky='w',padx=(150,10))
        self.pass_lbl = Label(self.contCan, text="Password", bg="lavender", fg="#111111", font=("Georgia", 14))
        self.pass_lbl.grid(row=10,column=0,sticky='w',padx=(150,10))

        # Login Entries
        self.first_ent = Entry(self.contCan, bg="lavender", font=("Raleway", 13), fg="#2B2B2B", bd=0,width=33)
        self.first_ent.grid(row=0,column=1,sticky='w')
        self.last_ent = Entry(self.contCan, bg="lavender", font=("Raleway", 13), fg="#2B2B2B", bd=0,width=33)
        self.last_ent.grid(row=2,column=1,sticky='w')
        self.phone_ent = Entry(self.contCan, bg="lavender", font=("Raleway", 13), fg="#2B2B2B", bd=0,width=33)
        self.phone_ent.grid(row=4,column=1,sticky='w')
        self.email_ent = Entry(self.contCan, bg="lavender", font=("Raleway", 13), fg="#2B2B2B", bd=0,width=33)
        self.email_ent.grid(row=6,column=1,sticky='w')
        self.gender_ent = Entry(self.contCan, bg="lavender", font=("Raleway", 13), fg="#2B2B2B", bd=0,width=33)
        self.gender_ent.grid(row=8,column=1,sticky='w')
        self.pass_ent = Entry(self.contCan, bg="lavender", show="*", font=("Raleway", 13), fg="#2B2B2B", bd=0,width=33)
        self.pass_ent.grid(row=10,column=1,sticky='w')

        # lbl_result=Label(middle_canv,bg="lavender",font=("Raleway",15,"bold"),fg="#2B2B2B",bd=0)
        # lbl_result.place(y=390,x=35,height=25,width=335)

        # Canvases
        self.first_canv = Canvas(self.contCan, bg="grey", highlightthickness=0,width=300,height=1)
        self.first_canv.grid(row=1,column=1,sticky='w',pady=(0,20))

        self.last_canv = Canvas(self.contCan, bg="grey", highlightthickness=0,width=300,height=1)
        self.last_canv.grid(row=3,column=1,sticky='w',pady=(0,20))

        self.phone_canv = Canvas(self.contCan, bg="grey", highlightthickness=0,width=300,height=1)
        self.phone_canv.grid(row=5,column=1,sticky='w',pady=(0,20))

        self.email_canv = Canvas(self.contCan, bg="grey", highlightthickness=0,width=300,height=1)
        self.email_canv.grid(row=7,column=1,sticky='w',pady=(0,20))

        self.gender_canv = Canvas(self.contCan, bg="grey", highlightthickness=0,width=300,height=1)
        self.gender_canv.grid(row=9,column=1,sticky='w',pady=(0,20))

        self.pass_canv = Canvas(self.contCan, bg="grey", highlightthickness=0,width=300,height=1)
        self.pass_canv.grid(row=11,column=1,sticky='w',pady=(0,20))

        # Canvas for buttons
        self.butCan=Canvas(self.login_canv,bg='lavender',highlightthickness=0)
        self.butCan.place(rely=0.71,relx=0,relheight=0.29,relwidth=1)

        self.logLbl=Label(self.butCan,text='Already signed up?',bg='lavender',fg="black", font=("Raleway", 15))
        self.logLbl.grid(row=0,column=0,padx=(290,0),pady=(20,0))

        self.logLbl=Label(self.butCan,text='login',bg='lavender',fg="orange", font=("Raleway", 15))
        self.logLbl.grid(row=0,column=1,padx=(5,0),pady=(20,0))
        self.logLbl.bind("<ButtonPress>",self.login)

        
        
        #Addin background to button
        signImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Desktop\pythonProjects\FaceRecognitionMUTattendance\assets\Blue-Button-PNG-Picture.png")
        signImage=signImage.resize((100,50),Image.ANTIALIAS)
        signImage=ImageTk.PhotoImage(signImage,master=root)
        self.signBtn=Button(self.butCan,text='Sign Up',bd=0,image=signImage,bg='lavender',fg="black", font=("Raleway", 15),command=self.submitDetails)
        self.signBtn.grid(row=1,columnspan=2,pady=(10,0),padx=(270,0))
        self.signBTN.image=signImage

        self.slideTitleSign()

    def submitDetails(self):
        if len(self.first_ent.get())==0 or len(self.last_ent.get())==0 or len(self.phone_ent.get())==0 or len(self.email_ent.get())==0 or len(self.gender_ent.get())==0 or len(self.pass_ent.get())==0:
            messagebox.showerror("Error","Please complete all required fields!")
        else:
            DbConn=DbConnection()
            if DbConn.userExists(username=self.first_ent.get()):
                    messagebox.showerror("Unsuccesful", "Course name already exist!")
            else:
                DbConn.addUser(fname=self.first_ent.get(),lname=self.last_ent.get(),pno=self.phone_ent.get(),email=self.email_ent.get(),gender=self.gender_ent.get(),password=self.pass_ent.get())
                messagebox.showinfo("Success","User added succefully")
                self.first_ent.delete("0",END)
                self.last_ent.delete("0",END)
                self.phone_ent.delete("0",END)
                self.email_ent.delete("0",END)
                self.gender_ent.delete("0",END)
                self.pass_ent.delete("0",END)
                
                self.login(None)



    def slideTitleSign(self):

        COLORS = ['red', 'maroon', 'navyblue', 'brown', 'orange']
        self.text += self.TITLE[self.index]
        root.update_idletasks()
        self.index += 1
        self.sign_title_lbl.config(text=self.text, fg=COLORS[random.randint(0, len(COLORS) - 1)])
        if len(self.text) == len(self.TITLE):
            self.text = ""
            self.index = 0
        root.after(200, self.slideTitleSign)

    def login(self,event):

        # Registration top label
        self.TITLE = "Enter you details to Login"
        self.text = ""
        self.index = 0

        full_canv.update_idletasks()
        bottom_canv = Canvas(full_canv, bg='#bd781d', highlightthickness=0)
        bottom_canv.place(y=30, relx=0, relwidth=1,
                          relheight=((full_canv.winfo_reqheight() - 30) / full_canv.winfo_reqheight()))

        self.signFrm=Frame(bottom_canv,highlightthickness=0,bg='orange')
        # self.signFrm.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)

        self.login_canv = Canvas(bottom_canv, bg="lavender", highlightthickness=0)
        self.login_canv.place(rely=0.05, relx=0.2, relheight=0.9, relwidth=0.6)

        # Top animated label
        self.login_title_lbl = Label(self.login_canv, text="", bg="lavender", fg="orange", font=("Georgia", 20))
        self.login_title_lbl.place(y=45, x=0, relwidth=1)

        # Content canvas for the content
        self.logContCan=Canvas(self.login_canv,bg='lavender',highlightthickness=0)
        self.logContCan.place(relx=0,rely=0.15,relheight=0.7,relwidth=1)

        # Label widgets
        self.log_user_lbl = Label(self.logContCan, text="Username", bg="lavender", font=("Georgia", 15))
        self.log_user_lbl.place(y=80, x=100)
        self.log_pass_lbl = Label(self.logContCan, text="Password", bg="lavender", font=("Georgia", 15))
        self.log_pass_lbl.place(y=180, x=100)

        # Entry widgets
        self.log_user_ent = Entry(self.logContCan, bg="lavender", font=("Georgia", 13), bd=0, fg="grey")
        self.log_user_ent.place(y=130, x=100, relwidth=0.8)
        self.log_pass_ent = Entry(self.logContCan, bg="lavender", font=("Georgia", 13), bd=0, fg="grey")
        self.log_pass_ent.place(y=230, x=100, relwidth=0.8)

        # Canvases
        self.log_user_canv = Canvas(self.logContCan,  bg="grey", highlightthickness=0)
        self.log_user_canv.place(y=160, x=100, relwidth=0.80, relheight=0.01)
        self.log_pass_canv = Canvas(self.logContCan, bg="grey",highlightthickness=0)
        self.log_pass_canv.place(y=260, x=100, relwidth=0.80, relheight=0.01)

        self.fog_lbl = Label(self.logContCan, text="Forget ", bg="lavender", font=("Georgia", 13, "underline"))
        self.fog_lbl.place(y=350, relx=0.73)
        self.pass_lbl = Label(self.logContCan, text="Password ? ", bg="lavender", fg="red", font=("Georgia", 13, "underline"))
        self.pass_lbl.place(y=350, relx=0.808)
        self.pass_lbl.bind('<Button-1>', ) #pass_update_page

        # def showWindow2():
        #     minimizeWindow(None)
        #     obj=showWindow()
            



        self.log_btn = Button(self.logContCan, text="Login", bg="green", font=("Georgia", 13), bd=0, command=self.test)  #showWindow2
        self.log_btn.place(y=290, relx=0.22, relheight=0.07, relwidth=0.2)
        self.cancel_btn = Button(self.logContCan, text="Cancel", bg="red", font=("Georgia", 13), bd=0, command=self.cancel_T)  #showWindow2
        self.cancel_btn.place(y=290, relx=0.55, relheight=0.07, relwidth=0.2)

        self.host_lbl = Label(self.logContCan, text="*You can also change host here: ", bd=0, bg="lavender",
                         font=("Georgia", 13, "underline"))
        self.host_lbl.place(rely=0.96, relx=0.4)
        self.host_btn = Button(self.logContCan, text="Change host", bg="orange", font=("Georgia", 9), bd=0) #, command=Login_fine
        self.host_btn.place(rely=0.96, relx=0.7)

        self.slideTitle_login()

    def slideTitle_login(self):

        COLORS = ['red', 'maroon', 'navyblue', 'brown', 'orange']
        self.text += self.TITLE[self.index]
        root.update_idletasks()
        self.index += 1
        self.login_title_lbl.config(text=self.text, fg=COLORS[random.randint(0, len(COLORS) - 1)])
        if len(self.text) == len(self.TITLE):
            self.text = ""
            self.index = 0
        root.after(200, self.slideTitle_login)

    def cancel_T(self):
        self.log_user_ent.delete("0",END)
        self.log_pass_ent.delete("0",END)
        self.signup()
        


    def test(self):
        # Registration top label
        self.TITLE = "Input X-ray or CT-scan Image"
        self.text = ""
        self.index = 0

        self.filename = ""

        full_canv.update_idletasks()
        testbottom_canv = Canvas(full_canv, bg='#bd781d', highlightthickness=0)
        testbottom_canv.place(y=30, relx=0, relwidth=1,
                          relheight=((full_canv.winfo_reqheight() - 30) / full_canv.winfo_reqheight()))

        # master.update_idletasks()
        # bottom_canv = Canvas(master=master, bg='#bd781d', highlightthickness=0)
        # bottom_canv.place(y=30, relx=0, relwidth=1,
        #                   relheight=((master.winfo_reqheight() - 30) / master.winfo_reqheight()))


        self.login_canv = Canvas(testbottom_canv, bg="lime", highlightthickness=0)
        self.login_canv.place(rely=0.05, relx=0.05, relheight=0.9, relwidth=0.9)

        # Top animated label
        self.login_title_lbl = Label(self.login_canv, text="", bg="lavender", fg="orange", font=("Georgia", 20))
        self.login_title_lbl.place(y=45, x=0, relwidth=1)

        # Button to submit selected image
        self.homBut = Button(self.login_canv, text='Home', bg='red', fg='white', font=("Raleway", 15, "bold"),
                             command=lambda: test(self.filename))
        # self.homBut.place(y=45, x=0, relwidth=1)


        # left canvas for the content
        self.testleftContCan = Canvas(self.login_canv, bg='#EDEDED', highlightthickness=0)
        self.testleftContCan.place(relx=0, rely=0, relheight=1, relwidth=0.6)

       

        #Content for left Canvas

        # Canvas for image to test
        self.picCan = Canvas(self.testleftContCan, bg='white', highlightthickness=0)
        self.picCan.place(relx=0.03, rely=0.03, relheight=0.78, relwidth=0.94)

        # Adding background to picCan
        root.update()
        width = self.picCan.winfo_width()
        height = self.picCan.winfo_height()
        image_back = Image.open(r"C:\projos\datasets\lung diseases\train\covid_with_PNEUMONIA\cwp(42).jpeg")
        image_back = image_back.resize((width, height), Image.ANTIALIAS)
        image_back = ImageTk.PhotoImage(image_back,master=master)# master=master
        self.picCan.create_image(0, 0, anchor="nw", image=image_back)
        self.picCan.image = image_back

        # Card for output
        # self.cardCan = Canvas(self.testContCan, bg='red', highlightthickness=0)
        # self.cardCan.place(relx=0.51, rely=0.03, relheight=0.94, relwidth=0.45)

        
        # fullCan=Canvas(root,bg='lavender',highlightthickness=0)
        # fullCan.place(relx=0,rely=0,relheight=1,relwidth=1)
        # fullCan.create_image(0,0,anchor="nw",image=bgImage)

        

        

        # # Button to show canvas
        # btnImage=Image.open("./dots.png")
        # btnImage=btnImage.resize((43,43),Image.ANTIALIAS)
        # btnImage=ImageTk.PhotoImage(btnImage,master=root)

        # self.showCanBtn=Button(self.cardCanTitle,text="",font=("Millet",30,"bold"),border=0,bg="silver",fg="orange",image=btnImage,compound=CENTER,command=self.showCanv)
        # self.showCanBtn.place(relx=0.9, rely=0)
        # self.showCanBtn.image=btnImage

        # self.showCanBtn = Button(self.cardCanTitle, text='',image=btnImage, bg='green', fg='white', font=("Raleway", 15, "bold"),
        #                      command=lambda: showResults())
        # self.showCanBtn.place(relx=0.8, rely=0)

        # self.cardTopLbl=Label(self.cardCanTitle,text='Patients Information',bg='silver',fg='#777', font=("Raleway", 22, "bold"))
        # self.cardTopLbl.place(relx=0.2,rely=0.2)

        # self.cardCancont=Canvas(self.cardCan, bg='beige', highlightthickness=0)
        # # self.cardCancont.place(relx=0.05, rely=0.3, relheight=0.63, relwidth=0.9)

        # self.cardNameLbl=Label(self.cardCancont,text='Name',bg='beige',fg='grey', font=("Raleway", 15))
        # self.cardNameLbl.grid(row=0,column=0,sticky='w',padx=1,pady=20)
        # self.cardDisLbl=Label(self.cardCancont,text='Disease',bg='beige',fg='grey', font=("Raleway", 15))
        # self.cardDisLbl.grid(row=1,column=0,sticky='w',padx=1,pady=20)
        # self.cardPrescLbl=Label(self.cardCancont,bg='beige',fg='grey',text='Prescription', font=("Raleway", 15))
        # self.cardPrescLbl.grid(row=2,column=0,sticky='w',padx=1,pady=20)

        # #Input labels
        # self.cardNameLblCont=Label(self.cardCancont,text='Admin',bg='beige',fg='grey', font=("Raleway", 15, "bold"))
        # self.cardNameLblCont.grid(row=0,column=1,sticky='w',pady=10)
        # self.cardDisLblCont=Label(self.cardCancont,text='',bg='beige',fg='grey', font=("Raleway", 15, "bold"))
        # self.cardDisLblCont.grid(row=1,column=1,sticky='w',pady=10)
        # self.cardPrescLblCont=Label(self.cardCancont,text='Chemotherapy',bg='beige',fg='grey', font=("Raleway", 15, "bold"))
        # # self.cardPrescLblCont.grid(row=2,column=1,sticky='w',pady=10)
        
        # Canvas for button in left Canvas
        self.testbutCan=Canvas(self.testleftContCan,bg='#EDEDED',highlightthickness=0)
        self.testbutCan.place(relx=0, rely=0.85, relheight=0.15, relwidth=1)

        #Image label
        self.imgLbl=Label(self.testbutCan,text='',bg='lavender',fg='#777', font=("Raleway", 16))
        self.imgLbl.place(relx=0.22,rely=0.36)

        # Button to select image
        self.selectbBut = Button(self.testbutCan, text='Select image', bg='green', fg='white', font=("Raleway", 15, "bold"),
                             command=self.open)
        self.selectbBut.grid(row=0, column=1, padx=(5, 0), pady=(30, 0))#

        def showResults():
            result=test(self.filename)
            self.diseaseName=result
            self.cardNameLblCont.place(relx=0.43,rely=0.116,relwidth=0.51)
            self.cardDisLblCont.place(relx=0.43,rely=0.151,relwidth=0.51)
            self.cardPrescMsgCont.place(relx=0.09,rely=0.34,relwidth=0.4)
            self.cardDisLblCont.configure(text=self.diseaseName)

        # Button to submit selected image
        self.subBut = Button(self.testbutCan, text='Submit', bg='green', fg='white', font=("Raleway", 15, "bold"),
                             command=lambda: showResults())
        self.subBut.grid(row=0, column=2, padx=(320, 0), pady=(30, 0))#

        # Button to submit selected image
        self.logoutBut = Button(self.testbutCan, text='Logout', bg='red', fg='white', font=("Raleway", 15, "bold"),
                             command=self.signup) #command=lambda: test(self.filename),
        self.logoutBut.grid(row=0, column=3, padx=(90, 0),pady=(30, 0))

        # Right Canvas
        self.testRightContCan = Canvas(self.login_canv, bg='#EDEDED', highlightthickness=0)
        self.testRightContCan.place(relx=0.6, rely=0, relheight=1, relwidth=0.4)
        self.testRightContCan.update()
        bgImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Pictures\realistic-blank (2).jpg")
        bgImage=bgImage.resize((self.testRightContCan.winfo_width(),self.testRightContCan.winfo_height()),Image.ANTIALIAS)
        bgImage=ImageTk.PhotoImage(bgImage,master=root)
        self.testRightContCan.create_image(0,0,anchor="nw",image=bgImage)
        self.testRightContCan.image = bgImage

        #logo for receipt
        #Addin background logo label
        logoImage1=Image.open(r"C:\Users\SHADY SUPERSUSER\Pictures\images (2).jpg")
        logoImage1=logoImage1.resize((100,100),Image.ANTIALIAS)
        logoImage1=ImageTk.PhotoImage(logoImage1,master=root)
        self.preslogoLbl=Label(self.testRightContCan,image=logoImage1,text='',bd=0,bg='#EDEDED')
        self.preslogoLbl.place(relx=0.09,rely=0.067)
        self.preslogoLbl.image=logoImage1

        #Print Prescription
        #Addin background print label
        printImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Pictures\4020167.png")
        printImage=printImage.resize((30,30),Image.ANTIALIAS)
        printImage=ImageTk.PhotoImage(printImage,master=root)
        self.presPrintBtn=Button(self.testRightContCan,image=printImage,text='',bd=0,bg='#EDEDED',command=self.printing)
        self.presPrintBtn.place(relx=0.79,rely=0.05)
        self.presPrintBtn.image=printImage

        #Open Receipt
        #Addin background print label
        toReceiptImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Pictures\dots.png")
        toReceiptImage=toReceiptImage.resize((30,30),Image.ANTIALIAS)
        toReceiptImage=ImageTk.PhotoImage(toReceiptImage,master=root)
        self.toReceiptBtn=Button(self.testRightContCan,image=toReceiptImage,text='',bd=0,bg='#EDEDED',command=self.showCanv)
        self.toReceiptBtn.place(relx=0.89,rely=0.05)
        self.toReceiptBtn.image=toReceiptImage




        #Input labels
        self.cardNameLblCont=Label(self.testRightContCan,text='Admin',anchor='w',bg='#EDEDED',fg='black', font=("Georgia", 7))
        # self.cardNameLblCont.place(relx=0.43,rely=0.116,relwidth=0.51)
        self.diagnosisLbl=Label(self.testRightContCan,text='Diagnosis',anchor='w',bg='#EDEDED',fg='black', font=("Georgia", 7))
        self.diagnosisLbl.place(relx=0.33,rely=0.156)
        self.cardDisLblCont=Label(self.testRightContCan,text='',anchor='w',bg='#EDEDED',fg='black', font=("Georgia", 7))
        # self.cardDisLblCont.place(relx=0.43,rely=0.151,relwidth=0.51)
        self.cardAdressCont=Label(self.testRightContCan,text='78, Muranga',anchor='w',bg="#EDEDED",fg='black', font=("Georgia", 7))
        self.cardAdressCont.place(relx=0.43,rely=0.191,relwidth=0.51)
        self.cardPrescMsgCont=Message(self.testRightContCan,text='2 antibiotics(isoniazid and rifampicin) for 6 months. 2 additional antibiotics (Pyrazinamide and ethambutol) for the first 2 months of the 6-month treatmrnt period',anchor='w',bg='#EDEDED',fg='black', font=("Raleway", 15))
        # self.cardPrescLblCont.place(relx=0.09,rely=0.34)

    def showCanv(self):
        # Card for output
        # self.prescCan = Canvas(self.testRightContCan, bg='lime', highlightthickness=0)
        # self.prescCan.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Receipt Canvas
        self.receiptCan = Canvas(self.testRightContCan, bg='#EDEDED', highlightthickness=0)
        self.receiptCan.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.receiptCan.update()
        receiptBgImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Pictures\receipt.png")
        receiptBgImage=receiptBgImage.resize((self.receiptCan.winfo_width(),self.receiptCan.winfo_height()),Image.ANTIALIAS)
        receiptBgImage=ImageTk.PhotoImage(receiptBgImage,master=root)
        self.receiptCan.create_image(0,0,anchor="nw",image=receiptBgImage)
        self.receiptCan.image = receiptBgImage

        #Print Receipt
        #Adding background print label
        printRecImage=Image.open(r"C:\Users\SHADY SUPERSUSER\Pictures\4020167.png")
        printRecImage=printRecImage.resize((25,25),Image.ANTIALIAS)
        printRecImage=ImageTk.PhotoImage(printRecImage,master=root)
        self.receiptPrintBtn=Button(self.receiptCan,image=printRecImage,text='',bd=0,bg='#FFFFFF',command=self.printing)
        self.receiptPrintBtn.place(relx=0.85,rely=0.032)
        self.receiptPrintBtn.image=printRecImage

        # Button to close canvas
        self.prescCloseBtn = Button(self.receiptCan, text='x',bd=0, bg='#FFFFFF', fg='black', font=("Raleway", 25, "bold"),
                             command=lambda:self.receiptCan.place_forget()) #command=lambda: test(self.filename),
        self.prescCloseBtn.place(relx=0.91, rely=0)

        # Content of canvas
        self.receiptNameLbl=Label(self.receiptCan,text='Admin',anchor='w',bg='#FFFFFF',fg='black', font=("Georgia", 7))
        self.receiptNameLbl.place(relx=0.092,rely=0.15,relwidth=0.3)

        # Datetime
        def my_time():
            time_string = strftime('%x')  # time format
            timeLbl.config(text=time_string)
            timeLbl.after(1000, my_time)  # time delay of 1000 miliseconds


        my_font = ('times', 15, 'bold')  # display size and style
        timeLbl = Label(self.receiptCan, font=my_font,fg='black', bg='#FFFFFF')
        timeLbl.place(rely=0.35, relx=0.28)# , relheight=0.35, , relwidth=0.09
        my_time()

        self.receiptActionLbl=Label(self.receiptCan,text='X-ray Screening',anchor='w',bg='#FFFFFF',fg='black', font=("Georgia", 7))
        self.receiptActionLbl.place(relx=0.09,rely=0.55,relwidth=0.3)

        self.receiptDescLbl=Label(self.receiptCan,text='X-ray images',anchor='w',bg='#FFFFFF',fg='black', font=("Georgia", 7))
        self.receiptDescLbl.place(relx=0.39,rely=0.55,relwidth=0.3)

        self.receiptAction2Lbl=Label(self.receiptCan,text='Disease Detection',anchor='w',bg='#FFFFFF',fg='black', font=("Georgia", 7))
        self.receiptAction2Lbl.place(relx=0.09,rely=0.60,relwidth=0.3)

        self.receiptAction2Lbl=Label(self.receiptCan,text='Lung Disease Detection model',anchor='w',bg='#FFFFFF',fg='black', font=("Georgia", 7))
        self.receiptAction2Lbl.place(relx=0.39,rely=0.6,relwidth=0.33)

        self.receiptprescrLbl=Label(self.receiptCan,text='',anchor='w',bg='#FFFFFF',fg='black', font=("Georgia", 7))
        self.receiptprescrLbl.place(relx=0.16,rely=0.87)
        self.receiptprescrLbl.config(text=self.diseaseName)


        # self.prescNameLbl=Label(self.prescContCan,text='Name',bg='beige',fg='grey', font=("Raleway", 15))
        # self.prescNameLbl.grid(row=0,column=0,sticky='w',padx=1,pady=20)
        # self.prescDisLbl=Label(self.prescContCan,text='Disease',bg='beige',fg='grey', font=("Raleway", 15))
        # self.prescDisLbl.grid(row=1,column=0,sticky='w',padx=1,pady=20)
        # self.PrescLbl=Label(self.prescContCan,bg='beige',fg='grey',text='Prescription', font=("Raleway", 15))
        # self.PrescLbl.grid(row=2,column=0,sticky='w',padx=1,pady=20)

        # #Input labels
        # self.cardNameLblCont=Label(self.prescContCan,text='Admin',bg='beige',fg='grey', font=("Raleway", 15, "bold"))
        # self.cardNameLblCont.grid(row=0,column=1,sticky='w',pady=10)
        # self.cardDisLblCont=Label(self.prescContCan,text='',bg='beige',fg='grey', font=("Raleway", 15, "bold"))
        # self.cardDisLblCont.grid(row=1,column=1,sticky='w',pady=10)
        # self.cardPrescLblCont=Label(self.prescContCan,text='Chemotherapy',bg='beige',fg='grey', font=("Raleway", 15, "bold"))
        # # self.cardPrescLblCont.grid(row=2,column=1,sticky='w',pady=10)


    def slideTitle_test(self):
        COLORS = ['red', 'maroon', 'navyblue', 'brown', 'orange']
        self.text += self.TITLE[self.index]
        self.index += 1
        self.login_title_lbl.config(text=self.text, fg=COLORS[random.randint(0, len(COLORS) - 1)])
        if len(self.text) == len(self.TITLE):
            self.text = ""
            self.index = 0
        self.contCan.after(150, self.slideTitle_test)
    

    def open(self):
        self.filename = filedialog.askopenfilename(initialdir=r"D:\lung diseases\train",
                                                   title="Select a file", filetypes=(
                ("All files", "*.*"), ("png files", "*.png"), ("jpg files", "*.jpg")))
        self.imgLbl.config(text=self.filename.split("/")[-1])

    def printing(self):
        messagebox.showerror('Error',"Please connect to a printer to print")











    def printMessage(self):
        print('Wow! This actually worked')




root = Tk()
root.geometry("1000x650")
root.attributes("-fullscreen", 1)


full_canv = Canvas(root, bg='#bd781d', highlightthickness=0)
full_canv.place(rely=0, relx=0, relwidth=1, relheight=1)

# Background color
# j=0
# r=0
# for i in range(100):
#     c=str(777777+r)
#     Frame(full_canv,bg='#'+c).place(x=j, y=0,relwidth=1,relheight=1)
#     j=j+10
#     r=r+1


def minimizeWindow(event):
    root.overrideredirect(0)
    root.iconify()


def restoreWindow(event):
    if root.attributes('-fullscreen'):

        root.overrideredirect(1)
        root.attributes("-fullscreen", 0)
    else:
        print("Hello")
        root.overrideredirect(0)
        root.attributes("-fullscreen", 1)


clos_canv = Canvas(full_canv, bg="#1f1f3a", highlightthickness=0)
clos_canv.place(rely=0, relx=0, relwidth=1, height=30)

dest_label = Label(clos_canv, bg='#1f1f3a', fg="#ffffff", text="X", font=("Arial", 15))
dest_label.pack(side=RIGHT, padx=10)
dest_label.bind("<ButtonPress>", lambda event: sys.exit())

rest_label = Label(clos_canv, bg='#1f1f3a', fg="#ffffff", text="2", font=("Marlett", 12))
rest_label.pack(side=RIGHT, padx=7)
rest_label.bind("<ButtonPress>", restoreWindow)

minimize_label = Label(clos_canv, bg='#1f1f3a', fg="#ffffff", text="-", font=("Arial", 30))
minimize_label.pack(side=RIGHT, padx=7)
minimize_label.bind("<ButtonPress>", minimizeWindow)


b = sButtons(root)

root.mainloop()
