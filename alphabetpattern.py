# A-alphabet pattern
# for i in range(1,7):
#     for j in range(1,9):
#         if (j==5 and i==1)  or (i==2 and (j==4 or j==6)) or (i==3 and (j==3 or j==7)):
#             print(" *",end=" ")
          
#         elif (i==4 and (j==3 or j==4 or j==5 or j==6 or j==7 or j==8)) :
#             print("*",end=" ")  
#         elif (i>=5 and(j==3 or j==8)):
#              print("*",end=" ")    
#         else:
#                   print(" ",end=" ")     
#     print()

# B-alphabet pattern
# for i in range(1,8):
#     for j in range(1,7):
#         if (j==1 or (i==1 and j<5)) or (i==2 and j==6) or (i==3 and j==6) or (i==4 and j<5):
#             print(" *",end=" ")
#         elif (i==5 and j==6) or (i==6 and j==6) or (i==7 and j<5):
#             print(" *",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        

# C-alphabet pattern
# for i in range(1,8):
#     for j in range(1,7):
#         if (i==1 and j>=3 and j<=6) or (i==2 and j==2) or (i>=3 and i<=5 and j==1):
#             print(" *",end=" ")
#         elif(i==6 and j==2) or (i==7 and j>=3 and j<=6):
#             print(" *",end=" ")    
#         else:
#             print(" ",end=" ")
#     print()            

#D-alphabet pattern
# for i in range(1,7):
#     for j in range(1,8):
#         if (j==1 or(i==1 and j<5)) or (i==2 and j==6) or (i==3 and j==7) or (i==4 and j==7):
#             print(" *",end=" ")
#         elif(i==5 and j==6) or  (i==6 and j<5):
#             print(" *",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        


# E-alphabet pattern
# for i in range(1,8):
#     for j in range(1,6):
#         if (i==1 or j==1) or (i==4) or (i==7):
#             print(" *",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        

#F-alphabet pattern
# for i in range(1,8):
#     for j in range(1,6):
#         if (i==1 or j==1) or (i==4):
#             print(" *",end=" ")
#         else:
#             print(" ",end=" ")
#     print()       

#G-alphabet pattern
# for i in range(1,8):
#     for j in range(1,7):
#         if (i==1 and (j>2 and j<7))  or (i==2 and j==2) or ((i>=3 and i<=5) and j==1) or (i==6 and j==2):
#             print("*",end=" ")
#         elif(i==7 and (j>2 and j<7)) or (i>=4 and j==6) or (i==4 and (j>=4 and j<=6)):
#             print("*",end=" ")    
#         else:
#             print(" ",end=" ")
#     print()        

#H-alphabet pattern
# for i in range(1,8):
#     for j in range(1,6):
#         if(j==1 or j==5 or(i==4)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    

#I-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==1 or i==7 or j==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()     


#J-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==1 or (j==4 and i<=6)) or (j==3 and i==7) or (j==2 and i==7) or (j==1 and i==6):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()            

#K-alphabet pattern
# for i in range(1,8):
#     for j in range(1,6):
#         if(j==1)or(i==4 and j==2) or ((i==3 or i==5) and j==3) or ((i==2 or i==6) and (j==4)) or ((i==1 or i==7)) and (j==5) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 


#L-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if (i==7 or j==1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#M-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(j==1 or j==7) or ((j==2 or j==6) and i==2) or ((j==3 or j==5) and i==3) or (j==4 and i==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        


#N-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(j==1 or j==7) or (j==i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        

#O-alphabet pattern
# for i in range(1,7):
#     for j in range(1,8):
#         if  (i==6 and (j>=3 and j<=5)) or (i==1 and (j>=3 and j<=5)) or ((j==2  or j==6 )and (i==2 or i==5)) or ((j==1 or j==7) and (i==3 or i==4)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#P-alphabet pattern
# for i in range(1,8):
#     for j in range(1,7):
#         if (j==1 or (i==1 and j<5)) or (i==2 and j==6) or (i==3 and j==6) or (i==4 and j<5):
#              print(" *",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        
             
#Q-alphabet pattern
# for i in range(1,9):
#     for j in range(1,8):
#         if  (i==6 and (j>=3 and j<=5)) or (i==1 and (j>=3 and j<=5)) or ((j==2  or j==6 )and (i==2 or i==5)) or ((j==1 or j==7) and (i==3 or i==4)):
#             print("*",end=" ")
#         elif (j==5 and i==7) or (j==6 and i==8):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#R-alphabet pattern
for i in range(1, 7):
    for j in range(1, 7):
        if  (j == 1) or ((i == 1 or i == 4) and j <= 5) or (j == 6 and (i == 2 or i == 3)) or (i == 5 and j == 4) or (i == 6 and j == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#S-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==1 and j>=2) or(i==2 and j==1)or (i==3 and j==1)or (i==4 and j>=2 and j<=6)or(i==7 and j<=6):
#             print("*",end=" ")
#         elif(i==5 and j==7)or(i==6 and j==7):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#T-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==1)or(j==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        

#U-alphabet pattern
# for i in range(1,8):
#     for j in range(1,7):
#         if(j==1 and i<=6)or(j==6 and i<=6)or(i==7 and j==5)or(i==7 and j==4)or(i==7 and j==3)or(i==7 and j==2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#V-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==1 and (j==1 or j==7)) or (i==2 and (j==2 or j==6))or (i==3 and (j==3 or j==5)) or (i==4 and (j==4)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#W-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(j==1 or j==7):
#             print("*",end=" ")
#         elif(i==6 and(j==2 or j==6)) or (i==5 and(j==3 or j==5)) or(i==4 and j==4):
#             print("*",end=" ")    
#         else:
#             print(" ",end=" ")
#     print()        


#X-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==j)or(j==8-i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()   


#Y-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==1 and (j==1 or j==7)) or (i==2 and (j==2 or j==6))or (i==3 and (j==3 or j==5)) or (i>=4 and (j==4)) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        


#Z-alphabet pattern
# for i in range(1,8):
#     for j in range(1,8):
#         if(i==1 or i==7) or(i==8-j):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        