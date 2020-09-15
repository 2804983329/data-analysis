s= '''
'''
s= s.strip().split('\n')
s= {x.split(':')[0] : x.split(':')[1] for x in s}
print(s)