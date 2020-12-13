def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith7 = multiplier_of(7)
multiplywith10 = multiplier_of(10)
print(multiplywith7(7))
print(multiplywith10(15))