import re
import psycopg2
import json
from tqdm import tqdm
f=open('/media/usb/HN/HN_Stories_3')
data=f.read()
test=re.findall('{.*?}',data,re.DOTALL)[600000:]
length=len(test)
gen = (y for y in test[-1:0:-1])
test=[]
print len(test)
def connection():
	con = psycopg2.connect("dbname='myproject' user='myproject' host='localhost' password='myproject'")
	return con
con=connection()
 
def stories(data):
		cur=con.cursor()
	        #print str(t['type'])	

		if 'story' in str(t['type']):
			#print 555555555555
	    		#t['text']=re.sub('"','""',t['text'])
	    		#t['text']=re.sub("'","",t['text'])
			#t['text']=t['text'].encode('utf-8')
		        #t['text']=t['text'].replace("\\",'')
			#print t['text']
			#print t.keys()
			#if 'parent' not in t.keys():
	    		#	t['parent']=0
	    		if 'descendants' in t.keys():
	    			values=(t['id'],str(t['by']),t['descendants'],t['score'],t['time'],str(t['title']),str(t['type']),str(t['url']))
	   	        else:
							
	    			values=(t['id'],str(t['by']),0,t['score'],t['time'],str(t['title']),str(t['type']),str(t['url']))
	    		
	    		cur.execute("""insert into HN_Stories values {}""".format(values))
		        con.commit()			
	    		cur.close()
		cur.close()


def comments(data):
		
		cur=con.cursor()
	
		if 'text' in t.keys():
	    		t['text']=re.sub('"','""',t['text'])
	    		t['text']=re.sub("'","",t['text'])
			t['text']=t['text'].encode('utf-8')
		        t['text']=t['text'].replace("\\",'')
			#print t['text']
			#print t.keys()
			if 'parent' not in t.keys():
	    			t['parent']=0
	    		if 'kids' in t.keys():
	    			values=(t['id'],str(t['kids']).replace('[','{').replace(']','}'),t['parent'],t['text'],t['time'],str(t['type']),str(t['by']))
	   	        else:
				values=(t['id'],'{}',t['parent'],t['text'],t['time'],str(t['type']),str(t['by']))
		
	    		
	    		cur.execute("""insert into HN_Comments values {}""".format(values))
		        con.commit()			
	    		cur.close()
		cur.close()
for ix in tqdm(xrange(1,length)):
		try:
			
			t=json.loads(gen.next())
			try:	
		        	stories(t)
				comments(t)
			  	
			except:
				#print "failed"
				con.close()
				con=connection()
		except:
	 		pass
		if ix % 1000 == 0 :
			print ix
			print t
cur = con.cursor()
con.commit()
#resp=cur.execute(""" select count(*) from HN_Comments""")
#print resp
con.close()
