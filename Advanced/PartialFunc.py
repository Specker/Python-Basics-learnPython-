
# Edit the function provided by calling partial() and replacing the first three variables in func(). 
# Then print with the new partial function using only one input variable so that the output equals 60.

from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

function = partial(func,6, 6, 5 )

if function(8) == 60:
    print('"Thank you come again" - Apu')
else:
    print('Thank you try again')
