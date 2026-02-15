Register_number=609
x=int(input("Enter the number of scores to be added to list:"))
scores=[0]*x
low_risk=[];low=0
medium_risk=[]
high_risk=[]
critical_risk=[];critical=0
valid=0;ignored=0
for i in range(x):
    scores[i]=int(input(f"Enter the score {i+1}:"))
print(scores,"\n")
print("Last digit of Registration Number:",Register_number%10,"\n")
for i in scores:
    if i<0:
        print(i,"is Invalid score.")
        ignored=ignored+1
    elif (i>=0) and (i<=30):
        low_risk=low_risk+[i]
        low=low+1
        valid=valid+1
    elif (i>=31) and (i<=60):
        medium_risk=medium_risk+[i]
        valid=valid+1
    elif (i>=61) and (i<=100):
        high_risk=high_risk+[i]
        valid=valid+1
    else:
        critical_risk=critical_risk+[i]
        critical=critical+1
        valid=valid+1
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk,"\n")
if (Register_number%10)%2!=0:
    critical_risk=[]
else:
    low_risk=[]
print("After Personalized Filtering:")
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk,"\n")
print("Total Valid Entries:",valid)
print("Ignored Entries:",ignored)
print("Removed due to Personalization:",critical)
