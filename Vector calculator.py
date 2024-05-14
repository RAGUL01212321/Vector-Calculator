import time
import sys
import math 
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='goodday10rs',database='vector_calculator')
cursor=con.cursor()
print('''************** Welcome to Vector operator **************''')
time.sleep(1)
def magnitude(a,b,c):
    fa=a**2
    fb=b**2
    fc=c**2
    mag=math.sqrt(fa+fb+fc)
    return mag
def choice():
    choice=input('Do you want to continue(y/n):')
    if choice=='y' or choice=='Y':
        print('******************************************************')
        vector()
    else:
        sys.exit('Thankyou')
def note(d):  # "d" will be the magnitude 
    c=input('Do you want to leave a note(Y/N): ')
    if c=='y' or c=='Y':
        l=input('Type your note:')
        sql = "INSERT INTO vec(magnitude,note,calc_on,calc_time) VALUES ('{}','{}',curdate(),curtime())".format(d,l)
        cursor.execute(sql)
        con.commit()
    else:
        l='-'
        sql = "INSERT INTO vec(magnitude,note,calc_on,calc_time) VALUES ('{}','{}',curdate(),curtime())".format(d,l)
        cursor.execute(sql)
        con.commit()
def vector():
    print('''What operation would like to perform :
    1. Addition of vector
    2. Subtraction of vector
    3. Dot product
    4. Cross product of 2 vectors
    5. Box product
    6. Cross product of 4 vectors 
    7. Dot product of 4 vectors
    8. angle between two vectors 
    9. view the magnitude of previous vector with time and date
        ''')
    i=int(input('enter your choice :'))
    if i in [1,2,3,4,8]:
        print('Enter the details of VECTOR 1')
        v1x=int(input('Enter the (i) component of vector-1:'))
        v1y=int(input('Enter the (j) component of vector-1:'))
        v1z=int(input('Enter the (k) component of vector-1:'))
        print('Enter the details of VECTOR 2')
        v2x=int(input('Enter the (i) component of vector-2:'))
        v2y=int(input('Enter the (j) component of vector-2:'))
        v2z=int(input('Enter the (k) component of vector-2:'))
        print('******************************************************')
        print('vector 1 = <',v1x,v1y,v1z,'>')
        print('vector 2 = <',v2x,v2y,v2z,'>')
        print('******************************************************')         
    if i==1:
        fvx=v1x+v2x
        fvy=v1y+v2y
        fvz=v1z+v2z
        print('calculating...')
        time.sleep(2)
        print('Result = <',fvx,fvy,fvz,'>')
        magnitude(fvx,fvy,fvz)
        note(magnitude(fvx,fvy,fvz))
        sql = "INSERT INTO vector_calc(magnitude) VALUES ('{}')".format(magnitude(fvx,fvy,fvz))
        cursor.execute(sql)
        con.commit()
        time.sleep(1)  
        choice()            
    if i==2:
        print('''please select from the below 
        1. (vector 1) - (vector 2)
        2. (vector 2) - (vector 1) ''')
        j=int(input('Enter the number : '))
        if j==1:
            fvx=v1x-v2x
            fvy=v1y-v2y
            fvz=v1z-v2z
            print('Calculating...')
            time.sleep(2)
            print('Result = <',fvx,fvy,fvz,'>')
            magnitude(fvx,fvy,fvz)
            note()
            choice()

        if j==2:
            fvx=v2x-v1x
            fvy=v2y-v1y
            fvz=v2z-v1z
            print('Calculating...')
            time.sleep(2)
            print('Result = <',fvx,fvy,fvz,'>')
            magnitude(fvx,fvy,fvz)
            note(magnitude(fvx,fvy,fvz))
            choice()
    if i==3:
        fvx=v1x*v2x
        fvy=v1y*v2y
        fvz=v1z*v2z
        dot_product=fvx+fvy+fvz
        for o in range(3):
            time.sleep(1)
            if o!=1:    
                print('.')
            if o==1:
                print('Calculating...')
        print('Dot product of the vectors is :',dot_product)
        choice()
    if i==4:
        vxc=(v1y*v2z)-(v1z*v2y)
        vyc=(v1x*v2z)-(v1z*v2x)
        vzc=(v1x*v2y)-(v1y*v2x)
        for k in range(3):
            time.sleep(1)
            if k!=1:    
                print('.')
            if k==1:
                print('Calculating...')
        print('Cross product =<',vxc,vyc,vzc,'>')
        magnitude(vxc,vyc,vzc)
        note(magnitude(fvx,fvy,fvz))
        choice()
    if i==5:
        print('Enter the details of VECTOR 1')
        v1x=int(input('Enter the (i) component of vector-1:'))
        v1y=int(input('Enter the (j) component of vector-1:'))
        v1z=int(input('Enter the (k) component of vector-1:'))
        print('Enter the details of VECTOR 2')
        v2x=int(input('Enter the (i) component of vector-2:'))
        v2y=int(input('Enter the (j) component of vector-2:'))
        v2z=int(input('Enter the (k) component of vector-2:'))
        print('Enter the details of VECTOR 3')
        v3x=int(input('Enter the (i) component of vector-3:'))
        v3y=int(input('Enter the (j) component of vector-3:'))
        v3z=int(input('Enter the (k) component of vector-3:'))
        print('******************************************************')
        print('vector 1 = <',v1x,v1y,v1z,'>')
        print('vector 2 = <',v2x,v2y,v2z,'>')
        print('vector 3 = <',v3x,v3y,v3z,'>')
        print('******************************************************')
        vxb=v1x*((v2y*v3z)-(v2z*v3y))
        vyb=v1y*((v2x*v3z)-(v2z*v3x))
        vzb=v1z*((v2x*v3y)-(v2y*v3x))
        b=vxb+vyb+vzb
        for k in range(3):
            time.sleep(1)
            if k!=1:
                print('.')
            if k==1:
                print('Calculating...')
        print('Box product = ',b)
        choice()
    if i in [6,7]:
        print('Enter the details of VECTOR 1')
        v1x=int(input('Enter the (i) component of vector-1:'))
        v1y=int(input('Enter the (j) component of vector-1:'))
        v1z=int(input('Enter the (k) component of vector-1:'))
        print('Enter the details of VECTOR 2')
        v2x=int(input('Enter the (i) component of vector-2:'))
        v2y=int(input('Enter the (j) component of vector-2:'))
        v2z=int(input('Enter the (k) component of vector-2:'))
        print('Enter the details of VECTOR 3')
        v3x=int(input('Enter the (i) component of vector-3:'))
        v3y=int(input('Enter the (j) component of vector-3:'))
        v3z=int(input('Enter the (k) component of vector-3:'))
        print('Enter the details of VECTOR 4')
        v4x=int(input('Enter the (i) component of vector-4:'))
        v4y=int(input('Enter the (j) component of vector-4:'))
        v4z=int(input('Enter the (k) component of vector-4:'))
        print('******************************************************')
        print('vector 1 = <',v1x,v1y,v1z,'>')
        print('vector 2 = <',v2x,v2y,v2z,'>')
        print('vector 3 = <',v3x,v3y,v3z,'>')
        print('vector 4 = <',v4x,v4y,v4z,'>')
        print('******************************************************')
    if i==6:
        v1xb=v1x*((v2y*v4z)-(v2z*v4y))
        v1yb=v1y*((v2x*v4z)-(v2z*v4x))
        v1zb=v1z*((v2x*v4y)-(v2y*v4x))
        b21=v1xb+v1yb+v1zb
        a1=b21*v3x
        a2=b21*v3y
        a3=b21*v3z
        v2xb=v1x*((v2y*v3z)-(v2z*v3y))
        v2yb=v1y*((v2x*v3z)-(v2z*v3x))
        v2zb=v1z*((v2x*v3y)-(v2y*v3x))
        b12=v2xb+v2yb+v2zb
        b1=b12*v4x
        b2=b12*v4y
        b3=b12*v4z
        v0=a1-b1
        v1=a2-b2
        v2=a3-b3
        for k in range(3):
            time.sleep(1)
            if k!=1:    
                print('.')
            if k==1:
                print('Calculating...')
        print('Cross product = <',v0,v1,v2,'>') 
        magnitude(v0,v1,v2)
        note(magnitude(fvx,fvy,fvz))
        choice()
    if i==7:
        vxc1=(v1y*v2z)-(v1z*v2y)
        vyc1=(v1x*v2z)-(v1z*v2x)
        vzc1=(v1x*v2y)-(v1y*v2x)
        vxc2=(v3y*v4z)-(v3z*v4y)
        vyc2=(v3x*v4z)-(v3z*v4x)
        vzc2=(v3x*v4y)-(v3y*v4x)
        dp4=(vxc1*vxc2)+(vyc1*vyc2)+(vzc1*vzc2)
        for k in range(3):
            time.sleep(1)
            if k!=1:   
                print('.')
            if k==1:
                print('Calculating...') 
        print('Dot product =',dp4)
        choice()
    if i==8:
        fvx=v1x*v2x
        fvy=v1y*v2y
        fvz=v1z*v2z
        dot_product=fvx+fvy+fvz
        mag1=math.sqrt((v1x**2)+(v1y**2)+(v1z**2))
        mag2=math.sqrt((v2x**2)+(v2y**2)+(v2z**2))
        cos=dot_product/(mag1*mag2)
        for i in range(3):
            time.sleep(1)
            if i!=1:
                print('.')
            if i==1:
                time.sleep(1)
                print('calculating...')
        print('The angle between the two vectors is : arccos(',cos,')')
        choice()
    if i==9:
            sql = "select* from vec"
            cursor.execute(sql)
            data=cursor.fetchall()
            for row in data:
                print(row)
            con.commit()
vector()
        