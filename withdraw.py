"""
withdraw_money()
a.  prompt user for a money amount in US Dollars (no cents, i.e. no
    fractional part allowed)
b.  print a preamble which says that user will see the breakdown of the
    money in banknotes
c.  print maximum number of $100 bills that can be given for the amount
    given by user
d.  print maximum number of $50 bills that can be given for the amount left
    over from previous step
e.  print maximum number of $20 bills that can be given for the amount left
    over from previous step
f.  print maximum number of $10 bills that can be given for the amount left
    over from previous step
g.  print maximum number of $5 bills that can be given for the amount left
    over from previous step
h.  print maximum number of $2 bills that can be given for the amount
    left over from previous step
i.  print maximum number of $1 bills that can be given for the amount left
    over from previous step
"""

def withdraw_money(withdraw):
    cash =  withdraw
    if withdraw < 10 and withdraw > 1000:
        return False

    hundreds = 0
    fifty = 0
    twenty = 0

    while withdraw >= 100:
        hundreds += 1
        withdraw -= 100

    while withdraw >= 50:
        fifty += 1
        withdraw -= 50

    while withdraw >= 20:
        twenty += 1
        withdraw -= 20
    
    currency_combination = ([hundreds, fifty, twenty])
    total_amount = ([hundreds*100, fifty*50, twenty*20])
    sums = sum(total_amount)
    if sums != cash:
        print('Sorry, we don\'t have you currency combination')
    else:
        return currency_combination
print(withdraw_money(665))




