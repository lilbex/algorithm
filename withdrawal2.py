def withdraw_money():
    denoms = (100, 50, 20, 10, 5, 2, 1)
    while True:
        try:
            withdraw = int(raw_input('amount of money: '))
            break
        except Exception as e:
            print('Incorrect input: %s' % e)


    # If we get here we know the user entered a valid value,
    # so we can output their results!
    print("Here is the bill breakdown for the amount input")
    for d in denoms:
        count = withdraw // d
        print('%i x $%i' % (count, d))
        withdraw -= count * d

withdraw_money()