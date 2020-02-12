import mysql.connector
class Zomato:
    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="hit")
        self.mycursor=self.conn.cursor()
        self.user_menu()

    def user_menu(self):
        user_input=input("""How would you like to proceed?
1.Enter 1 to register
2.Enter 2 to login
3.Anything else to exit
""")
        if user_input=='1':
            self.register()
        elif user_input=='2':
            self.login()
        else:
            print("Bye Buddy!!")


    def register(self):
        name=input("Enter name:")
        email=input("Enter email:")
        password=input("Enter password:")
        self.mycursor.execute("INSERT INTO users(user_id,name,email,password) VALUES(NULL,'{}','{}','{}')".format(name,email,password))
        self.conn.commit()
        print("Registration successful")

    def login(self):
        email=input("Enter email:")
        password=input("Enter password:")

        self.mycursor.execute("SELECT * FROM users WHERE email like '{}' AND password LIKE '{}'".format(email,password))
        if len(self.mycursor.fetchall())==0:
            print("Incorrect credentials")
        else:
            print("Welcome!!")
            
obj=Zomato()

        
