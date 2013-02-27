__author__ = 'garyg'

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print 'List D =>',D
print 'food   =>', D['food']
print 'qty    =>', D['quantity']
print 'Increase qty by 1...'
D['quantity'] += 1
print D

print '='*40
print 'Create keys by assigment'
D={}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
