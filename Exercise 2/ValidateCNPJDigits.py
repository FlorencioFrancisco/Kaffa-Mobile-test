from itertools import cycle

def ValidateCNPJDigits (cnpj):
    cnpj_numbers = [number for number in cnpj]# transform string into int array
    if (len(cnpj) == 18):# if cnpj has special characters remove then
        cnpj_numbers.pop(15)
        cnpj_numbers.pop(10)
        cnpj_numbers.pop(6)
        cnpj_numbers.pop(2)
    cnpj_numbers = list(map(int,cnpj_numbers))
    verification_digit_1 = ValidationDigit(cnpj_numbers[:12])# first verification digit
    if (verification_digit_1 == cnpj_numbers[12]):
        verification_digit_2 = ValidationDigit(cnpj_numbers[:13])# second verification digit
        if (verification_digit_2 == cnpj_numbers[13]):
            return True
    return False
    
def ValidationDigit(cnpj_numbers):
    cnpj_inverted = [cnpj_numbers[i] for i in range(len(cnpj_numbers)-1,-1,-1)]# invert the digits in the array
    cycle_numbers = cycle(list(range(2,10)))# crate a infite array of number from 2 to 9
    vefification_digit = 0
    for number, cycle_number in zip(cnpj_inverted, cycle_numbers):# multiply inverted array with cycle array and sum the results
        vefification_digit += number * cycle_number
    vefification_digit = vefification_digit % 11# use modulus of 11
    vefification_digit = 11 - vefification_digit# subtract 11 the result
    if (vefification_digit > 9):# get the last digit
        vefification_digit = 0
    return vefification_digit


cnpj = input('Type the CNPJ: ')
if (ValidateCNPJDigits(cnpj)):
    print('That is a valid CNPJ')
else:
    print('That is an invalid CNPJ number')

