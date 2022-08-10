EV="EV"
EBITDA="EBITDA"
amortization="Amortization"
monthlyAmortization ="MonthlyAmortization"
EV_EBITDA= "EV/EBITDA"

formula=str(input('What formula do you want?'))

def EnterpriseValue():
    MarketCap=int(input('MarketCap:'))
    CashDebt=int(input('CashDebt:'))
    Cash=int(input('Cash:'))
    global EV_val
    EV_val= MarketCap + CashDebt + Cash
    print(MarketCap + CashDebt + Cash)

def EBITDAf():
   Netincome=int(input('Net income:'))
   taxes=int(input('Taxes:'))
   interestexpenses=int(input('Interest expense:'))
   depreciationValue=int(input('Depreciation val:'))
   amortizationVal=int(input('Amortization(lowering the value of a loan,focuses on spreading loan payments out overtime):'))
   global EBITDA_val
   EBITDA_val=Netincome + taxes +interestexpenses + depreciationValue + amortizationVal
   print(Netincome +taxes + interestexpenses+ depreciationValue +amortizationVal)

def Amortization():
    totalMonthlyPayment= int(input('Monthly Payment:'))
    outstandingLoanBalance = int(input('Loan Balance:'))
    interest = int(input('Interest:'))
    global Amortization_val
    Amortization_val = totalMonthlyPayment -(outstandingLoanBalance *(interest))
    print(totalMonthlyPayment - (outstandingLoanBalance *(interest/12)))
def monthlyAMORT():
    loanAmount=int(input('Loan total:'))
    monthlyInterest=int(input('Monthly Interest:'))
    numberOfPayments=int(input('How many years is the loan:'))
    newInterest= monthlyInterest/12
    newPayments= numberOfPayments *12
    global monthlyAMORTVAL
    monthlyAMORTVAL = loanAmount*(newInterest*(1.000375+newInterest))**newPayments/(((1.00375+newInterest)**newPayments)-1)
    print(loanAmount*(newInterest*((1.000375+newInterest))**newPayments/((1.00375+newInterest)**newPayments)-1))
#https://www.investopedia.com/terms/a/amortization.asp where the formula was gotten

def EV_EBITDAform():
    EnterpriseEV = int(input('EV:'))
    EBITDA = int(input('EBITDA:'))
    print(EnterpriseEV/EBITDA)


if formula == EV:
    EnterpriseValue()
if formula == EBITDA:
    EBITDAf()
if formula == amortization:
    Amortization()
if formula == monthlyAmortization:
    monthlyAMORT()
if formula == EV_EBITDA:
    EV_EBITDAform()

