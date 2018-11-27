def get_summ(one, two, delimiter='&'):
    return str(one).upper() + str(delimiter).upper() + str(two).upper()

res = get_summ('Anton', 'Bondarev', '-')
print(res)