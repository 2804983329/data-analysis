s= '''
#粘贴浏览器上面复制下来的Request Headers
'''
s= s.strip().split('\n')
s= {x.split(':')[0] : x.split(':')[1] for x in s}
print(s)