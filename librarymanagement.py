from bookdetail import BookDetail
from bookmainmenu import main_library
class login(BookDetail):
    def __init__(self):
        BookDetail.__init__(self)

    def sigin(self):
        try:
            while True:
                print("Login Details")
                user = input("Enter the User name :")
                passwd= input("Enter the password:")
                self.cur.execute("select * from login where username ='{}' and password = '{}'".format(user,passwd))
                
                records = self.cur.fetchone()

                if records:
                    main_library()
                else:
                    print("Invalid password")


        except Exception as err:
             print(err)



if __name__== '__main__':
    l=login()
    
    l.sigin()
