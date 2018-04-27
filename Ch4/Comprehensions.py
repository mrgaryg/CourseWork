__author__ = 'garyg'
from Lists import M

print 'printing coordinates of',M

col2 = [row[1] for row in M]                   # Collect the items in col 2

print 'col2 is =>',col2

print 'M is =>', M

print 'Add 1 to each item in col2', [row[1] + 1 for row in M]

print 'Filter out odd numbers', [row[1] for row in M if row[1] % 2 ==0 ]

diag = [M[i][i] for i in [0,1,2]]
print 'diag is:',diag

doubles = [c*2 for c in 'spam']
print 'double the letters in \'spam\'', doubles

print '-'*30

G =(sum(row) for row in M)               # Create a generator of row sums
print next(G)

print list(map(sum, M))                  # Create a set of rows
print {i : sum(M[i]) for i in range(3)}  # Create key/value table of row sums

# In fact, lists, sets, and dictionaries can all be built with comprehensions in 3.0
print [ord(x) for x in 'spaam'] # List of character ordinals
print {ord(x) for x in 'spaam'} # Sets remove duplicates
print {x: ord(x) for x in 'spaam'} # Dictionary keys are unique
