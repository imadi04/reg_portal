import mysql.connector
from tkinter import *
import requests
class Zomato:
    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="hit")
        self.mycursor=self.conn.cursor()
        self.root=Tk()
        self.root.title("Registration Portal")
        self.root.minsize(400,600) #for fixing min height of window
        self.root.maxsize(400,900) #these two lines fix the window size.
        self.root.configure(background="#0089ae")# for changing window background-color.
        self.label1=Label(self.root,text="Registration Portal",bg="#0089ae",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(30,10)) #padding-left(x) and top(y)

        self.label2=Label(self.root,text="""How would you like to proceed?
1.Enter 1 to register
2.Enter 2 to login
3.Anything else to exit
""",bg="#0089ae",fg="#ffffff")
        self.label2.configure(font=("Constantia",12,"bold"))
        self.label2.pack(pady=(30,10)) #padding-left(x) and top(y)

        self.user_input=Entry(self.root) #for creating input field
        self.user_input.pack(ipadx=5,ipady=10) #for changing the size of input/entry box x:width, y:height
        self.click=Button(self.root,text="Enter",width=30,height=2,command=lambda:self.user_menu())
        self.click.pack(pady=(15,15))
        #self.user_menu()
        self.root.mainloop()

    def user_menu(self):
        user_input=self.user_input.get()
        if user_input=='1':
            self.register()
        elif user_input=='2':
            self.login()
        else:
            print("Bye Buddy!!")


    def register(self):
        self.label1=Label(self.root,text="Name:",bg="#0089ae",fg="#ffffff")
        self.label1.configure(font=("Constantia",12,"bold"))
        self.name=Entry(self.root)
        self.name.pack(ipadx=5,ipady=10)
        print(self.name.get())
        self.label2=Label(self.root,text="Email:",bg="#0089ae",fg="#ffffff")
        self.label2.configure(font=("Constantia",12,"bold"))
        self.email=Entry(self.root)
        self.email.pack(ipadx=5,ipady=10)
        self.label3=Label(self.root,text="Password:",bg="#0089ae",fg="#ffffff")
        self.label3.configure(font=("Constantia",12,"bold"))
        self.password=Entry(self.root)
        self.password.pack(ipadx=5,ipady=10)
        self.click=Button(self.root,text="Enter",width=30,height=2,command=lambda:[self.mycursor.execute("INSERT INTO users(user_id,name,email,password) VALUES(NULL,'{}','{}','{}')".format(self.name.get(),self.email.get(),self.password.get())),self.conn.commit()])                                                                                                 
        self.click.pack(pady=(15,15))
        
        print("Registration successful")

    def login(self):
        email=input("Enter email:")
        password=input("Enter password:")

        self.mycursor.execute("SELECT * FROM users WHERE email like '{}' AND password LIKE '{}'".format(email,password))
        if len(self.mycursor.fetchall())==0:
            print("Incorrect credentials")
        else:
            username=email.split('@')
            username=username[0]
            print("Welcome {}!!".format(username))
            
obj=Zomato()

        
