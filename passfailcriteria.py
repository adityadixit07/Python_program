sub1=int(input("enter first sub marks:\n"))
sub2=int(input("enter second sub marks:\n"))
sub3=int(input("enter third sub marks:\n"))
if(sub1<33 or sub2<33 or sub3<33):
 print("you are fail")
elif((sub1+sub2+sub3)/3<40):
    print("you are fail due to%age criteria")
else:
    print("passed the exams")
    