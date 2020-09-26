
def ValidateCNPJ (cnpj):
    if ((len(cnpj) == 14) & (cnpj.isnumeric() )):# look for 14 numbers
        return True
    elif (len(cnpj) == 18):# look for 18 characters
        special_characters = cnpj[2] + cnpj[6] + cnpj[10] + cnpj[15] # isolate the special characters
        cnpj_numbers = [char for char in cnpj] # isolate numbers
        cnpj_numbers.pop(15)
        cnpj_numbers.pop(10)
        cnpj_numbers.pop(6)
        cnpj_numbers.pop(2)
        # check if the special characters are in the correct order and if the rest of the string is numeric
        if ((special_characters == '../-') & (''.join(cnpj_numbers).isnumeric())): 
            return True
    else:
        return False

cnpj = input('Type the CNPJ: ')
if (ValidateCNPJ(cnpj)):
    print('That is a valid CNPJ')
else:
    print('That is an invalid CNPJ number')