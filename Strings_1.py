# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    n_donuts = "Number of donuts: "
    if count >= 10:
        return n_donuts + "Many"
    else:
        return n_donuts + str(count)

#print(donuts(10))

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        first = s[2:-2]
        return first

#print(both_ends("az"))


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
  front  = s[0]
  back = s[1:]
  fixed = back.replace(front, "*") 
  return front + fixed

#print(fix_start("otorrinolaringologo"))
#yes, I cheated xD

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.

def mixup(a, b):
    a_replaced = a.replace(a[:2], b[:2]) 
    b_replaced = b.replace(b[:2], a[:2])
    x = a_replaced + " " + b_replaced
    return x
#print(mixup("sopa", "camarones"))