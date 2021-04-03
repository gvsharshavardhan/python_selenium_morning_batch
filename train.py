s=int(input("enter seat number : "))
r = s % 8 
if s>0 and s<73: 
        if r == 1 or r == 4: 
             print("is lower berth",s)
        elif r == 2 or r == 5: 
             print ( "is middle berth",s)
        elif r == 3 or r == 6: 
             print ("is upper berth",s)
        elif r == 7: 
             print ("is side upper berth",s)
        else:  
             print (" {} : is side lower berth".format(s))
else: 
        print ("invalid seat number",s)
  
 