#20401172025 | Taneesha Mehta | BTech CSEAI3

#E-BOOKSHELF MANAGMENT (PWP PROJECT)

#based on python-mysql connectivity



#ORIGINAL DATA BASE IN MYSQL:

#Creating database:
def createDB():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234')
    cur = con.cursor()
    cur.execute('create database if not exists library')
    con.commit()
    cur.close()
    con.close()

#Creating the table:
def createTB():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    cur.execute('create table if not exists books(id int primary key, book varchar(50), author varchar(50), status text, rating int)')
    con.commit()
    cur.close()
    con.close()



#Functions available for user:
    
#1. insert function:
def insert():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',password='1234',database='library')
    cur=con.cursor()
    ID=int(input('enter id'))
    book=input('enter book')
    auth=input('enter author')
    stat=input('read/reading/wanttoread?')
    rate=""
    if stat=='read':
        rate=int(input('enter rating out of 10'))
        cur.execute("insert into books(id,book,author,status,rating)values({},'{}','{}','{}',{})".format(ID,book,auth,stat,rate))
    else:
        cur.execute("insert into books(id,book,author,status,rating)values({},'{}','{}','{}',NULL)".format(ID,book,auth,stat))
    con.commit()
    print('record inserted successfully')

#2. modifying the status of the book function:
def modify():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',password='1234',database='library')
    cur=con.cursor()
    book=input('enter book name')
    stat=input('read/reading/wanttoread?')
    rate=""
    if stat=='read':
        rate=int(input('enter rating out of 10'))
        cur.execute('update books set rating={} where book="{}"'.format(rate,book))
    cur.execute('update books set status="{}" where book="{}"'.format(stat,book))
    con.commit()
    print('record updated successfully')

#3. search book by id function:
def search():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',password='1234',database='library')
    cur=con.cursor()
    ID=int(input('enter book id'))
    cur.execute('select * from books where id={}'.format(ID))
    for i in cur.fetchall():
        print(i)
        break

#4. display entire bookshelf function:
def display():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',password='1234',database='library')
    cur=con.cursor()
    cur.execute('select * from books')
    for i in cur.fetchall():
        print(i)

#5. display books starting with given letter function:
def display_byfirstletter():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    letter = input('enter the starting letter of the book: ')
    cur.execute('select * from books where book like "{}%"'.format(letter))
    data = cur.fetchall()
    if data:
        for i in data:
            print(i)
    else:
        print("No books found starting with letter", letter)

#6. display by author function:
def display_byauth():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',password='1234',database='library')
    cur=con.cursor()
    auth=input('enter author')
    cur.execute('select * from books where author="{}"'.format(auth))
    for i in cur.fetchall():
        print(i)

#7. display by status function:
def display_status():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',password='1234',database='library')
    cur=con.cursor()
    stat=input('enter status read/reading/wanttoread?')
    cur.execute('select * from books where status="{}"'.format(stat))
    for i in cur.fetchall():
        print(i)

#8. display by rating>5 function:
def display_rating():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    cur.execute('select * from books where rating>5')
    for i in cur.fetchall():
        print(i)

#9. sort books by highest ratings function:
def sort_byrating():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    cur.execute("select * from books order by rating desc")
    for i in cur.fetchall():
        print(i)

#10. show average rating function:
def average_rating():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    cur.execute("select avg(rating) from books where rating is not null")
    avg = cur.fetchone()[0]
    print("Average rating:", avg)

#11. update rating function:
def update_rating():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    book = input("Enter book name: ")
    new_rate = int(input("Enter new rating: "))
    cur.execute("update books set rating={} where book='{}'".format(new_rate, book))
    con.commit()
    print("Rating updated")

#12. random book suggestion function:
def random_book():
    import mysql.connector as mc
    import random
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    cur.execute("select * from books")
    rows = cur.fetchall()
    if rows:
        print("Today's book suggestion:")
        print(random.choice(rows))


#13. delete function:
def delete():
    import mysql.connector as mc
    con = mc.connect(host='localhost', user='root', password='1234', database='library')
    cur = con.cursor()
    ID = int(input('id of book you want to delete'))
    cur.execute('delete from books where id={}'.format(ID))
    con.commit()
    print('record deleted successfully')




#User interface:
    
#main menu:
def menu():
    print('Hello user!\nWelcome to your E-bookshelf:')
    
    while True:
        print('Type\n1 for inserting record')
        print('2 for modifying record')
        print('3 for searching book')
        print('4 for displaying all books in shelf')
        print('5 for displaying books starting with a particular letter')
        print('6 for displaying books by particular author')
        print('7 for displaying books by status')
        print('8 for displaying books with rating above 5')
        print('9 for sorting books by highest ratings.')
        print('10 for displaying the average rating.')
        print('11 for updating a rating of a book.')
        print('12 for getting a random book suggestion')
        print('13 for deleting a record')
        print('14 for EXIT')
        
        n = int(input('Enter choice: '))
        if n == 1:
            insert()
            print('Thankyou for visiting') 
        elif n == 2:
            modify()
            print('Thankyou for visiting') 
        elif n == 3:
            search()
            print('Thankyou for visiting') 
        elif n == 4:
            display()
            print('Thankyou for visiting') 
        elif n == 5:
            display_byfirstletter()
            print('Thankyou for visiting') 
        elif n == 6:
            display_byauth()
            print('Thankyou for visiting') 
        elif n == 7:
            display_status()
            print('Thankyou for visiting') 
        elif n == 8:
            display_rating()
            print('Thankyou for visiting') 
        elif n == 9:
            sort_byrating()
            print('Thankyou for visiting') 
        elif n == 10:
            average_rating()
            print('Thankyou for visiting') 
        elif n == 11:
            update_rating()
            print('Thankyou for visiting') 
        elif n == 12:
            random_book()
            print('Thankyou for visiting') 
        elif n == 13:
            delete()
            print('Thankyou for visiting') 
        elif n == 14:
            print('Sad to see you go')
            break


#Calling the program:
menu()
