def card_verification(card_number):
    double = True
    index = -2
    sum = 0
    for number in range(len(card_number)-1):
        if double:
            if int(card_number[index])*2 > 9:
                sum += int(card_number[index])*2-9
            else:
                sum += int(card_number[index])*2
            double = False
        else:
            sum += int(card_number[index])
            double = True
        index -= 1
    return 'Card is VALID!' if (sum + int(card_number[-1])) % 10 == 0 else 'Card NOT valid!'


print(card_verification(input('Enter card number to be verified (no spaces): ')))
