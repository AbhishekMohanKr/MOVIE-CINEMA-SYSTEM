
import mysql.connector as sql
conn=sql.connect(host = 'localhost',user='root',passwd='manager',database='soft')
c1=conn.cursor()
if conn.is_connected():
    print ("Enter your choice as 1,2,3&4")
    print ("$$$$$$$$$$$$ PALLAVAN THEATRE BOOKING (AC & NON AC) $$$$$$$$$$$$$$")
    print ("SIGN UP")
    print ("LOG IN")
    print ("PALLAVAN THEATRE")
    con = input ("do you want to continue or not :")
    ch=int(input("Enter your choice :"))
else:
    print("Database is not connected")

if ch==1:
    v_mname = input("Enter the movie name :")
    v_phno = input("Enter phone number :")
    v_tic = input("Enter total tickets :" )
    v_sex = input ("Enter your sex :" )
    v_fname = input ("Enter your first name :")
    v_lname = input ("Enter your last name :")
    v_passwd = input ("Enter your passwd :")
    v_userID = input ("Enter your userID :")
    v_snacks = input ("Order your snacks :")
    v_ins="insert into theatre values( '{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(v_mname,v_phno,v_tic,v_sex,v_fname,v_lname,v_passwd,v_userID,v_snacks)
    c1.execute(v_ins)
    conn.commit()
    print (" ticket booked congrats")
    print ("Thank you for visiting pallavan theatre")
    print ("ratings")
    ch=int(input("Enter your choice :"))

if ch ==2:
    print ("##############WELCOME TO THE BOX OFFICE (AC)##################")
    c = input ("Enter your movie name :")
    a = input ("Enter your name :")
    d = input ("Enter total tickets :")
    b = input ("Enter your ph_no :")
    pswd= input("Enter the password :")
    sks = input(" Order your snacks :")
    print ("*********************TICKET BOOKED***********************")
    ch=int(input("Enter your choice :"))

if ch ==3:
    print ("************welcome to 1st class ticket booking **************")
    c = input ("Enter your movie name :")
    a = input ("Enter your name :")
    d = input ("Enter total tickets :")
    b = input ("Enter your ph_no :")
    pswd= input("Enter the password :")
    sks = input(" Order your snacks :")
    print ("**TICKET BOOKED**")
    ch=int(input("Enter your choice :"))

if ch == 4:
    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!WELCOME TO 2nd CLASS TICKET BOOKING !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    a = input ("Enter your name :")
    b = input ("Enter your movie name :")
    c = input ("Enter your ph_no :")
    d = input ("Enter total tickets :")
    pswd= input("Enter the password :")
    sks = input(" Order your snacks :")
    print ("///////////////ENJOY THE MOVIE AND HAVE FUN/////////////////")
