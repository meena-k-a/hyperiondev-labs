import math
#This program creates two calculators (investment calculator and homeloan repayment calculator) for a finance company 
print("\nchoose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment\t-\t to calculate the amount of interest you'll earn on your investment")
print("bond\t\t-\t to calculate the amount you'll have to pay on a home loan\n")

choice=input("\tEnter your Choice Investment/Bond\t")

# INVESTMENT finance calculation
if choice.lower()=="investment":
    p=float(input("\tHow much money you want to deposit?\t"))
    r=float(input("\tEnter the interest rate\t"))
    t=int(input("\tHow many years you plan on investing(number of years)?\t"))
    interest=input("\tWhich interest you want simple/compound?\t")
    if interest.upper()=="SIMPLE":
        a=p*(1+(r/100)*t) 
        print(f"\t Total amount once the interest rate {r} apllied on your deposit {p} for {t} years is {a}")
    elif interest.upper()=="COMPOUND":
        a=p*(1+(r/100))**t  
        print(f"\t Total amount once the interest rate {r} apllied on your deposit {p} for {t} years is {a}")
    else:
        print("\tYou have entered wrong interest type") 
    
# BOND finance calculation
elif choice.lower()=="bond":
    p=float(input("\tWhat is the present value of the house?\t"))
    r=float(input("\twhat is the annual interest rate\t"))
    i=(r/100)/12
    n=int(input("\tNumber of the months you plan to repay the bond\t"))

    x=(i*p)/(1-(1+i)**(-n))
    print(f"\t The amount you have to be repaid on a home loan each month is {x}.")
    
else:
    print("you entered wrong choice.")
