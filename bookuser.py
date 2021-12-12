from Getconn import getconn


class BookUser:
    def __init__(self):
        self.mydb=getconn()
        self.cur=self.mydb.cursor()

    def adduser(self):
        try:
            self.uid=int(input('enter the user id')) 
            self.name=input("enter the user's name:")
            self.pno=input("Enter the phone no.:")
            self.city=input("enter the city:")
            self.date=input('enter the date of birth:')

            self.cur.execute("Insert into user values({},'{}','{}','{}','{}')".format(self.uid,self.name,self.pno,self.city,self.date))                    
        
            if self.cur.rowcount>0:
                  self.mydb.commit()
                  print("rows inserted")

            else:
                self.mydb.rollback()
                print("NO record added")
                
        except Exception as err:
            print(err)
            print("Error while inserting the records")

    def display(self):
        print("display Books")
        self.cur.execute("select * from user")
        ret =self.cur.fetchall()
        for r in ret:
          print(r)

    def search(self):
        u_id=input('enter the user id')
        self.cur.execute("select * from user where user_id={}".format(u_id))
        a=self.cur.fetchall()
        print(a)

    def update(self):
        while True:
            print('*'*50)
            print('user details')
            print('1.name\n2.phone\n3.city\n4.Date of Birth')
            x=int(input("Enter the choice to be modified:"))
            print('NOTE-The updation will be done on the basis of user id')
            if x==1:
                p=int(input("enter the user id:"))
                name=input("enter the new name:")
                q="update user set name='{}' where user_id={}".format(name,p)
                
            elif x==2:
                p=int(input("enter the user id:"))
                pno=input("enter the new phone number of user:")
                q="update user set phone_no='{}' where user_id={}".format(pno,p)    
        
            elif x==3:
                p=int(input("enter the user id:"))
                city1=input("enter the new city of user:")
                q="update user set city='{}' where user_id={}".format(city1,p)

            elif x==4:
                p=int(input("enter the user id:"))
                bd=input("enter the new Birth date of user:")
                q="update user set birth_date='{}' where user_id={}".format(bd,p)

            else:
                print('invalid choice')


            self.cur.execute(q)
            if self.cur.rowcount >0:

               self.mydb.commit()
               print("Records updated successfully..")
            else:
               self.mydb.rollback()
               print("No records updated")
               
            choice=input('do you wish to continue?:')
            if choice=='y':
                continue
            else:
                print("Go to main menu")
                break

    def delete(self):
         p=int(input("enter the user id whose detailed has to be deleted:"))
         sql="delete from user where user_id={}".format(p)
         self.cur.execute(sql)
         if self.cur.rowcount >0:
            self.mydb.commit()
            print("Successfully deleted the rows...")
         else:
            self.mydb.rollback()
            print("No records deleted")


























         
                
























                         
