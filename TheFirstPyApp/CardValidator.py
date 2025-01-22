sum_odd_digits = 0
sum_even_digits = 0
total = 0
card_number = input('Enter your card number: ')
card_number = card_number.replace('-', '')
card_number = card_number.replace(' ', '')
card_number = card_number[::-1]
if card_number.isdigit():
    for num in card_number[::2]:
        sum_odd_digits += int(num)

    for num in card_number[1::2]:
        num = int(num) * 2
        if num > 9:
            sum_even_digits += (1 + (num % 10))
        else:
            sum_even_digits += num

    total = sum_odd_digits + sum_even_digits

    if total % 10 == 0:
        print('Card is valid')
    else:
        print('Card is invalid')
else:
    print('Invalid card number')
