import re
import pymysql

a=re.compile("\n[A-Z0-9/\s.()]+\n");

with open("NameList.txt") as f:
	total=f.read()
	x=re.findall(a,total)[0:];
	#print(x)

 
l1=[]
for i in x:
	y=i.split(' ')
	y=[j for j in y if j!='']
	if(len(y)>1):
		l1.append(y)
		#print(y)
#print(l1)
'''for i in l1:
	print(i[0][1:],i[-2],i[-3],i[-4],i[-5],' '.join(i[1:-5]))'''

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
 database="student"
)
c=0;
mycursor=mydb.cursor()
for i in l1:
	if '/' in i[-5]:
		sql="insert into data(seat_no,course,branch,class,PRN,Name) values(%s,%s,%s,%s,%s,%s)"
		value=(i[0][1:],i[-2],i[-3],i[-4],i[-5],' '.join(i[1:-5]))
		#print(sql)
		mycursor.execute(sql,value);
		c=c+1;
mydb.commit();
print("NO of rows inserted= ",c)