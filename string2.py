# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
# +++your code here+++
stringa = 'Bring'
lenend = len(stringa)-3
lastchars = stringa[lenend:]
if len(stringa)>=3 and lastchars == 'ing':
  print(stringa + "ly")
elif len(stringa)>=3 and lastchars != 'ing':
  print(stringa + 'ing')
else:
  print(stringa)
  


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
# +++your code here+++
s = 'This dinner is not super bad!'
findnot = s.find('not')
findbad = s.find('bad')
endbad = findbad + 3
range = endbad - findnot
if findnot == -1 or findbad == -1:
  print(s)
elif findnot<findbad:
  print(s.replace(s[findnot:endbad],'good'))
else:
  print(s)


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
# +++your code here+++
import math
t = "Blue"
u = "Duck"
strlent = len(t)
strlenu = len(u)
strlenthalf = (len(t) * .5)
strlenuhalf = (len(u) * .5)

if (strlent % 2) != 0 or (strlenu % 2) != 0:
  strhalft = int(math.ceil(strlent * .5))
  strhalfu = int(math.ceil(strlenu * .5))
  print(t[0:strhalft]+ u[0:strhalfu] + t[strhalft:] + u[strhalfu:])
else:
  print(t[0:strlenthalf] + u[0:strlenuhalf] + t[strlenthalf:] + u[strlenthalf:])


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
