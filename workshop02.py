print ('''----------------------------------------
---- ทายตัวเลขที่มีค่าอยู่ที่ 1 - 100 กันเถอะ ----
----------------------------------------''')

import random
RN = random.randint( 1 , 100 )
NB = -1

try :
    while (NB != RN):
        NB = int(input("ป้อมตัวเลขที่ต้องการทาย : "))
        if NB == RN:
                print (f"ยินดีด้วยคุณทายถูก")
                print ("----------------------------------------")
        else :
            if NB < RN:
                    print (f"คุณทายผิดตัวเลขที่ป้อนน้อยไป | {RN}  เลขที่ถูกต้อง")
            else :
                    print (f"คุณทายผิดตัวเลขที่ป้อนมากไป | {RN}  เลขที่ถูกต้อง")
            print ("----------------------------------------")
except ValueError :
    print('ใส่ตัวเลขเท่านั้นห้ามใส่ตัวอักษร')
    print ("----------------------------------------")
except Exception :
    print('มีข้อพลาดเกิดขึ้น')
    print ("----------------------------------------")