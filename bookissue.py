from Getconn import getconn

class BookIssue:
    def __init__(self):
        self.mydb=getconn()
        self.cur=self.mydb.cursor()

    def issue(self):
        try:
            self.b_id=int(input("enter the book id:"))
            self.b_name=input("enter the Book name to be issued:")
            self.p_id=int(input("enter the person id"))
            self.qtyissue=int(input("enter the quantity of book issue"))
            a="insert into issue values({},'{}',{},{})".format(self.b_id,self.b_name,self.p_id,self.qtyissue)
            self.cur.execute(a)
            if self.cur.rowcount>0:
                self.mydb.commit()
                print("row inserted")
            else:
                self.mydb.rollback()
                print('no records')
        except Exception as err:
            print(err)
            print("Error while inserting the records")

            
    def display(self):
        self.cur.execute("select * from issue")
        ret=self.cur.fetchall()
        for i in ret:
            print(i)
            
    def search(self):
        eid=input("enter person id:")
        A="select * from issue where p_id={}".format(eid)
        self.cur.execute(A)
        B=self.cur.fetchall()
        print(B)


    def delete(self):
        bid=int(input("enter the user id:"))
        self.cur.execute("delete from issue where p_id={}".format(bid))
        if self.cur.rowcount>0:
            self.mydb.commit()
            print("successfully deleted the rows")
        else:
            self.mydb.rollback()
            print("no records deleted")
                         

    def returnbook(self):
        b_id=int(input("enter book id:"))
        p_id=int(input("enter person id:"))
        qty=int(input("enter the quantity of book:"))
        rec=(b_id,p_id,qty)
        self.cur.execute("select * from issue")
        r=self.cur.fetchall()
        for i in r:
            if i[0]==rec[0] and i[2]==rec[1]:
               a="update issue set qtyissue={} where b_id={} and p_id={}".format(i[3]-qty,i[0],i[2])#book quantity automatically minus from issue book while you returning the book
               self.cur.execute(a)
               if self.cur.rowcount >0:

                  self.mydb.commit()
                  print("Records updated successfully..")
               else:
                  self.mydb.rollback()
                  print("No records updated")
        

    def issuebook(self):
        b_id=int(input("enter book id:"))
        p_id=int(input("enter person id:"))
        qty=int(input("enter the quantity of book:"))
        rec=(b_id,p_id,qty)
        self.cur.execute("select * from issue")
        r=self.cur.fetchall()
        for i in r:
            if i[0]==rec[0] and i[2]==rec[1]:
               a="update issue set qtyissue={} where b_id={} and p_id={}".format(i[3]+qty,i[0],i[2])#book quantity automatically plus from issue book while you issuing the book
               self.cur.execute(a)
               if self.cur.rowcount >0:

                  self.mydb.commit()
                  print("Records updated successfully..")
               else:
                  self.mydb.rollback()
                  print("No records updated")
        
            

    def updatebook(self):#update the Books from libaray after updating the book issue list
        def updateissue(self):
            b_id=int(input('enter the book id:'))
            qty=int(input("enter the quantity of book:"))
            rec=(b_id,qty)
            self.cur.execute("select * from Books")
            r=self.cur.fetchall()
            for i in r:
                if i[0]==rec[0]:
                    a1="update Books set quantity={} where bks_id={}".format(i[3]-qty,i[0])
                    self.cur.execute(a1)
                    if self.cur.rowcount >0:
                       self.mydb.commit()
                       print("Records updated successfully..")
                    else:
                       self.mydb.rollback()
                       print("No records updated")
            

        def updatereturn(self):
            b_id=int(input('enter the book id:'))
            qty=int(input("enter the quantity of book:"))
            rec=(b_id,qty)
            self.cur.execute("select * from Books")
            r=self.cur.fetchall()
            for i in r:
                if i[0]==rec[0]:
                    a1="update Books set quantity={} where bks_id={}".format(i[3]+qty,i[0])
                    self.cur.execute(a1)
                    if self.cur.rowcount >0:
                       self.mydb.commit()
                       print("Records updated successfully..")
                    else:
                       self.mydb.rollback()
                       print("No records updated")
            

        while True:
             print('*'*50)
             print("1.update book while issue book\n2.update book while return book")
             choice=input("enter your choice:")
             if choice=='1':
                 updateissue(self)
             elif choice=='2':
                 updatereturn(self)
             else:
                 print("invalid choice")
                 
             ch=input('do you wish to continue')
             if ch=='y':
                 continue
             else:
                 print("go to main menu")
                 break
             

























                
































        
        
























                    
