q1=input("capital of india? ")
q2=int(input("number of vowels? "))
q3=int(input("how many states are present in INDIA? "))
q4=input("which is the national bird of india? ")
q5=int(input("number of consonants? "))
s=0
if q1.lower()=="delhi":
    s=s+1
   # print("correct! ")
if q2==5:
    s=s+1    
    #print("correct! ")
if q3==28:
    s=s+1    
#    print("correct! ")
if q4.lower()=="peacock":
    s=s+1    
  #  print("correct! ")   
if q5==21:
    s=s+1    
  #  print("correct! ")
print("your score",s)
if s==5:
    print("excellent",s)
elif s<3:
    print("poor",s) 
elif s>3 and s<5:
    print("good",s)    
    