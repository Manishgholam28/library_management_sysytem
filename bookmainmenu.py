from bookdetail import BookDetail
from bookuser import BookUser
from bookissue import BookIssue
def main_library():
    def Book():
        while True:
            print('*'*50)
            print("\t\tBOOK MENU")
            print('*'*50)
            print('1.Adding more books\n2.Removing books\n3.Display books\n4.Search book\n5.Update book')        
            print('*'*50)
            bo=BookDetail()
            choice=int(input("enter your choice:"))
            if choice==1:
                bo.add_book()
            elif choice==2:
                bo.delete_book()
            elif choice==3:
                bo.display_book()
            elif choice==4:
                bo.search_book()    
            elif choice==5:
                bo.update_book()
            else:
                print('invalid choice')
            ch=input('do you wish to continue?:')
            if ch=='y':
                continue
            else:
                print("go to main menu")
                break    
            

    def User():
        while True:
            print('*'*50)
            print("\t\tUSER DETAILS")
            print('*'*50)
            print("1.Add user\n2.Display details\n3.Search\n4.Update\n5.Delete")
            print('*'*50)
            us=BookUser()
            choice=int(input("enter your choice:"))    
            if choice==1:
                us.adduser()
            elif choice==2:
                us.display()
            elif choice==3:
                us.search()
            elif choice==4:
                us.update()
            elif choice==5:
                us.delete()
            else:
                print('invalid choice')
            ch=input('do you wish to continue?:')
            if ch=='y':
                continue
            else:
                print("go to main menu")
                break    
                
    def Issue():
        while True:
            print('*'*50)
            print("\t\tISSUE BOOK")
            print('*'*50)
            print("1.Issue Book\n2.display all issue books\n3.Search person detail\n4.removing the books from book issue list\n5.Return books\n6.Issue Books\n7.Update main library books")
            print('*'*50)
            bi=BookIssue()
            ch=int(input("enter your choice:"))    
            if ch==1:
                bi.issue()
            elif ch==2:
                bi.display()
            elif ch==3:
                bi.search()
            elif ch==4:
                bi.delete()
            elif ch==5:
                bi.returnbook()
            elif ch==6:
                bi.issuebook()
            elif ch==7:
                bi.updatebook()
            else:
                print('invalid choice')
            cho=input('do you wish to continue?:')
            if cho=='y':
                continue
            else:
                print("go to main menu")
                break
                
    while True:
        print('***************--------LIBRARY MANAGEMENT SYSTEM--------********************')
        print('='*50)
        print('1.BOOK DETAILS MENU DRIVE')
        print('2.BOOK USER MENU DRIVE')
        print('3.BOOK ISSUE AND DEPOSITING MENU DRIVE')
        print('4.EXIT')
        CH=int(input("enter your choice:"))
        if CH==1:
            Book()
        elif CH==2:
            User()
        elif CH==3:
            Issue()
        elif CH==4:
            exit()
        else:
            print("invalid choice")
        choi=input('do you wish to continue?:')
        if choi=='y':
            continue
        else:
            print("Thank you")
            break    





























    
