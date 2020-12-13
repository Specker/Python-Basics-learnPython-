# Try to fix the code to print out the correct information by changing the string.

quote = "He who looks into the abyss realizes that there is nothing looking back at him. The only thing he sees is his own character, Ricky, do you understand? Bud? The abyss? The shit abyss?"  

print("Length of s = %d" % len(quote))

print("The first occurrence of the letter a = %d" % quote.index("a"))

print("a occurs %d times" % quote.count("a"))

print("The first five characters are '%s'" % quote[:5])
print("The next five characters are '%s'" % quote[5:10])
print("The thirteenth character is '%s'" % quote[12])
print("The characters with odd index are '%s'" % quote[1::2])
print("The last five characters are '%s'" % quote[-5:])

print("String in uppercase: %s" % quote.upper())