import re
test=range(1,13000000)
f=open('ids','r')
data=f.readlines()
lst=[]
for line in data:
	try:
		line = re.sub(',|\n|id|"','',line)
		if len(line) > 1:
			lst.append(int(line))
 		else:
			print line	
	except:
		print "F"

g=open('get_ids','w')
x=set(test)-set(lst)
for  line in list(x):
	g.write(str(line))
	g.write('\n')
	print line
g.close()

	

