from Getconn import getconn

class BookDetail:
    def __init__(self):
        self.mydb=getconn()
        self.cur=self.mydb.cursor()

    def add_book(self):
        try:
            self.i_d=int(input("Enter the book ID:"))
            self.name=input("Enter the book Name:")
            self.author=input("Enter the author's name:")
            self.quantity=int(input("Enter the quantity of book:"))
            rec=(self.i_d,self.author,self.quantity)
            self.cur.execute("select * from Books")
            r=self.cur.fetchall()
            
            
            self.cur.execute("Insert into Books values({},'{}','{}',{})".format(self.i_d,self.name,self.author,self.quantity))
                                                                                        
            if self.cur.rowcount>0:
                self.mydb.commit()
                print("rows inserted")

            else:
                self.mydb.rollback()
                print("NO record added")
                    
        except Exception as err:
            print(err)
            print("Error while inserting the records")

    def display_book(self):
        print("display Books")
        self.cur.execute("select * from Books")
        ret =self.cur.fetchall()
        for r in ret:
          print(r)

    def delete_book(self):
        while True:
            print("1.Book ID\n2.Book NAME")
            print('*'*50)
            cho=int(input("enter your choice:"))
            if cho==1:
                eid=int(input("Enter the Boojs ID you wish to remove:"))
                sql="delete from Books where bks_id={}".format(eid)
                self.cur.execute(sql)
                if self.cur.rowcount >0:
                    self.mydb.commit()
                    print("Successfully deleted the rows...")
                else:
                    self.mydb.rollback()
                    print("No records deleted")
            elif cho==2:
                name=input("enter the book name:")
                sql="delete from Books where name='{}'".format(name)
                self.cur.execute(sql)
                if self.cur.rowcount >0:
                    self.mydb.commit()
                    print("Successfully deleted the rows...")
                else:
                    self.mydb.rollback()
                    print("No records deleted")     
            else:
                print("invalid choice")
            choi=input("Do you wish to continue?")
            if choi=='y':
                continue
            else:
                print("go to main menu")
                break
            
    def update_book(self):
        while True:
            print('1.book id\n2.book name\n3.author name\n4.book quantity')
            ch1=input('enter your choice from the menu which want to modify:')
            ch2=input('enter option to be changed on basis of:')
            if ch1=='1':
                if ch2=='1':
                    a=int(input("enter the book id:"))
                    b=int(input("enter the new book id:"))

                    c="Update Books set bks_id={} where bks_id={}".format(b,a)

                elif ch2=='2':
                    a=input("enter the book name :")
                    b=int(input("enter the new book id:"))

                    c="Update Books set bks_id={} where name='{}'".format(b,a)

                elif ch2=='3':
                    a=input("enter the book Author name :")
                    b=int(input("enter the new book id:"))

                    c="Update Books set bks_id={} where author='{}'".format(b,a)


                elif ch2=='4':
                    a=int(input("enter the book quantity :"))
                    b=int(input("enter the new book id:"))

                    c="Update Books set bks_id={} where quantity={}".format(b,a)
                self.cur.execute(c)
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
                    print("go to main menu")
                    break
          
                
            elif ch1=='2':
                if ch2=='1':
                    a=int(input("enter the book id:"))
                    b=input("enter the new book name:")

                    c="Update Books set name='{}' where bks_id={}".format(b,a)

                elif ch2=='2':
                    a=input("enter the book name :")
                    b=input("enter the new book name:")

                    c="Update Books set name='{}' where name='{}'".format(b,a) 

                elif ch2=='3':
                    a=input("enter the book Author name :")
                    b=input("enter the new book name:")

                    c="Update Books set name='{}' where author='{}'".format(b,a)


                elif ch2=='4':
                    a=int(input("enter the book quantity :"))
                    b=input("enter the new book name:")

                    c="Update Books set name='{}' where quantity={}".format(b,a)
                self.cur.execute(c)
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
                    print("go to main menu")
                    break     

            elif ch1=='3':
                if ch2=='1':
                    a=int(input("enter the book id:"))
                    b=input("enter the new book author name:")

                    c="Update Books set author='{}' where bks_id={}".format(b,a)

                elif ch2=='2':
                    a=input("enter the book name :")
                    b=input("enter the new book author name:")

                    c="Update Books set author='{}' where name='{}'".format(b,a) 

                elif ch2=='3':
                    a=input("enter the book Author name :")
                    b=input("enter the new book author name:")

                    c="Update Books set author='{}' where author='{}'".format(b,a)


                elif ch2=='4':
                    a=int(input("enter the book quantity :"))
                    b=input("enter the new book author name:")

                    c="Update Books set author='{}' where quantity={}".format(b,a)
                self.cur.execute(c)
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
                    print("go to main menu")
                    break    

            elif ch1=='4':
                if ch2=='1':
                    a=int(input("enter the book id:"))
                    b=input("enter the new book quantity:")

                    c="Update Books set quantity={} where bks_id={}".format(b,a)

                elif ch2=='2':
                    a=input("enter the book name :")
                    b=input("enter the new book quantity:")

                    c="Update Books set quantity={} where name='{}'".format(b,a) 

                elif ch2=='3':
                    a=input("enter the book Author name :")
                    b=input("enter the new book quantity:")

                    c="Update Books set quantity={} where author='{}'".format(b,a)


                elif ch2=='4':
                    a=int(input("enter the book quantity :"))
                    b=input("enter the new book quantity:")

                    c="Update Books set quantity={} where quantity={}".format(b,a)
                self.cur.execute(c)
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
                    print("go to main menu")
                    break    

            
    def search_book(self):
        

        print("********************************************************************")
        while True: 
            print("*********Menu for searching Details on the basis of choice***********")
            print('1.book id\n2.book name\n3.author name')
            ch=input('enter a choice')
            if ch=='1':
                x=input('Enter the book id to be searched')
                
                y="select * from Books where bks_id={}".format(x)
                self.cur.execute(y)
                r=self.cur.fetchall()
                print(r)
                
            elif ch=='2':
                x=input('Enter the book name to be searched')
                
                y="select * from Books where name='{}'".format(x)
                self.cur.execute(y)
                r=self.cur.fetchall()
                print(r)
            

            elif ch=='3':
                x=input('Enter the book author name to be searched')
                
                y="select * from Books where author='{}'".format(x)
                self.cur.execute(y)
                r=self.cur.fetchall()
                print(r)
               
                    
            choice=input('do you wish to continue?:')
            if choice=='y':
                continue
            else:
                print("go to main menu")
                break
            



















                        
        
            
             
            



                             
