import pymysql;


def manual_result():	
	seatno=input("Enter the Seat Number ")
	seatno.upper();
	branch=input("Enter branch and class: eg BECSE ")
	branch.upper();
	# branch+=".txt"

	your_result = result(branch,seatno)
	print("your_result is :",your_result)


def result(branch,seatno):
	your_result=""
	branch+=".txt"
	with open(branch,"rt") as P:
		data=P.read()
	L=data.split(' ')
	# print(L)
	j1=0;j2=0;j3=0;
	cgpa=[]
	for i in range(len(L)):
		if(L[i]=='(CGPA)' or L[i] == 'CGPA'):
			j1=i
			cgpa.append(j1)
		# if(L[i]=='NEW'):
		#   j2=i
		 # if(L[i]=='NIL'):
		 #  j3=i;
	L1=[];L2=[];L3=[];

	# CGPA REGULAR
	for i in range(1,len(cgpa)):
		while(cgpa[i-1]<cgpa[i]):
			L1.append(L[cgpa[i-1]])
			cgpa[i-1]=cgpa[i-1]+1;
	# print(L1)
	# print("")
	# CGPA BACKLOG
	while(cgpa[1]<len(L)):
		L2.append(L[cgpa[1]])
		cgpa[1]=cgpa[1]+1;
	# print(L2)

	# while(j2<j3):
	#   L3.append(L[j2])
	#   j2=j2+1

	#searching in CGPA REGULAR

	j1=0;j2=0;j3=0;j4=0;j5=0;
	for i in range(len(L1)):
		if(L1[i]=="CLEARED" and L1[i-1]!="NOT"):
			j1=i;
		if(L1[i]=="NOT" and L1[i+1]=="CLEARED"):
			j2=i;
		if(L1[i]=="HELD"):
			j3=i;
		if(L1[i]=="WPC"):
			j4=i
		if(L1[i]=="DETAINED"):
			j5=i

	nestedList=[]

	R1=[];R2=[];R3=[];R4=[];R5=[];
	while(j1<j2):
		R1.append(L1[j1])
		j1=j1+1

	nestedList.append(R1)   

	while(j2<j3):
		R2.append(L1[j2])
		j2=j2+1
	nestedList.append(R2)
	while(j3<j4):
		R3.append(L1[j3])
		j3=j3+1
	nestedList.append(R3)
	while(j4<j5):
		R4.append(L1[j4])
		j4=j4+1
	nestedList.append(R4)
	while(j5<len(L1)):
		R5.append(L1[j5])
		j5=j5+1
	nestedList.append(R5)
	# print(R5)
	listname=-1;
	for list1 in range(len(nestedList)):
		for i in nestedList[list1]:
			s=i.split('\n\n')
			for j in s:
				if(j==seatno):
					listname=list1;
	if(listname==-1):
		pass
		# print("NOT IN REGULAR,SEARCHING IN ANOTHER ");
	elif(listname==0):
		your_result = "CLEARED"
		# print('CLEARED')
	elif(listname==1):
		your_result = "NOT CLEARED"
		# print('NOT CLEARED')
	elif(listname==2):
		your_result = "HELD"
		# print('HELD')
	elif(listname==3):
		your_result ="WPC"
		# print('WPC')
	elif(listname==4):
		your_result="DETAINED"
		# print('DETAINED')

	#searching in  CGPA BACKLOG
	k1=0;k2=0;k3=0;k4=0;k5=0;k6=0;k7=0;k8=0;k9=0;k0=0;P9=[];P0=[];
	for i in range(len(L2)):
		if(L2[i]=="DECLEARED" and L2[i+1]=="PASS"):
			k1=i;
			# '''print(L2[k1])
			# print("")'''
		if(L2[i]=="KEEP" and L2[i+1]=="TERM"):
			k2=i;
			# '''print(L2[k2])
			# print("")'''
		if(L2[i]=="F-ATKT"):
			k3=i;
			# '''print(L2[k3])
			# print("")'''
		if(L2[i]=="ABSENT"):
			k4=i
			# '''print(L2[k4])
			# print("")'''
		if(L2[i]=="FAIL"):
			k5=i;
		if(L2[i]=="RESERVED" and L2[i+1]!="FOR"):
			k6=i
			# '''print(L2[k6])
			# print("")'''
		if(L2[i]=="OFFICE" and L2[i+1]=="VERIFICATION"):
			k7=i
			# '''print(L2[k7])
			# print("")'''
		if(L2[i]=="ELIGIBILITY" and L2[i+1]=="CERTIFICATE"):
			k8=i
			# '''print(L2[k8])
			# print("")'''
		if(L2[i]=="WPC"):
			k9=i
			# '''print(L2[k9])
			# print("")'''
		if(L2[i]=="DETAINED"):
			k0=i;
	# print(k0)
			# '''print(L2[k0])
			# print("")'''

	P1=[];P2=[];P3=[];P4=[];P5=[];P6=[];P7=[];P8=[];
	nestedList2=[]
	while(k1<k2):
		P1.append(L2[k1])
		k1=k1+1
	# print(P1)
	# print("")
	nestedList2.append(P1)
	while(k2<k3):
		P2.append(L2[k2])
		k2=k2+1
	# '''print(P2)
	# print("")'''
	nestedList2.append(P2)
	while(k3<k4):
		P3.append(L2[k3])
		k3=k3+1
	# '''print(P3)
	# print("")'''
	nestedList2.append(P3)
	while(k4<k5):
		P4.append(L2[k4])
		k4=k4+1
	# '''print(P4)
	# print("")'''
	nestedList2.append(P4)
	while(k5<k6):
		P5.append(L2[k5])
		k5=k5+1
	# '''print(P5)
	# print("")'''
	nestedList2.append(P5)
	while(k6<k7):
		P6.append(L2[k6])
		k6=k6+1
	# '''print(P6)
	# print("")'''
	nestedList2.append(P6)
	while(k7<k8):
		P7.append(L2[k7])
		k7=k7+1
	# '''print(P7)
	# print("")'''
	nestedList2.append(P7)
	while(k8<k9):
		P8.append(L2[k8])
		k8=k8+1
	# '''print(P8)
	# print("")'''
	nestedList2.append(P8)
	while(k9<k0):
		P9.append(L2[k9])
		k9=k9+1
	# '''print(P9)
	# print("")'''
	nestedList2.append(P9)
	while(k0<len(L2)):
		P0.append(L2[k0])
		k0=k0+1
	# print(P0)
	# print("")
	nestedList2.append(P0)

	listname1=-1
	for list1 in range(len(nestedList2)):
		for i in nestedList2[list1]:
			s=i.split('\n\n')
			for j in s:
				if(j==seatno):
					listname1=list1;

	if(listname1==0):
		your_result ="PASS" 
		# print("PASS")
	elif(listname1==1):
		your_result = "ATKT" 
		# print("ATKT")
	elif(listname1==2):
		your_result = "F-ATKT" 
		# print("F-ATKT")
	elif(listname1==3):
		your_result = "ABSENT" 
		# print("ABSENT")
	elif(listname1==4):
		your_result = "FAIL" 
		# print("FAIL")
	elif(listname1==5):
		your_result = "RHR" 
		# print("RHR")
	elif(listname1==6):
		your_result = "OV"      
		# print("OV")
	elif(listname1==7):
		your_result = "EC"      
		# print("EC")
	elif(listname1==8):
		your_result = "WPC"         
		# print("WPC")
	elif(listname1==9):
		your_result = "DETAINED"        
		# print("DETAINED")
	return your_result

# mydb = pymysql.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#  database="student"
# )
# cur = mydb.cursor()
# if(mydb):
# 	print("CONNECTED TO DATABASE")
# else:
# 	print("FAILED TO CONNECT TO DATABASE")

# count_query = 'select count(*) from data'
# cur.execute(count_query);
# count = cur.fetchall()
# countt = [j for i in count for j in i]
# print("total result = ",countt[0]); #efficient
# select_query = 'select seat_no,branch,class from data'
# total_rows = cur.execute(select_query)
# data = cur.fetchall()
# i=0
# for row in data:
# 	print(i)
# 	resultt = list(row)
# 	# print(list(row))
# 	seatno=resultt[0]
# 	branch = resultt[1] #CSE or EC/ECT...
# 	clss = str.join("",resultt[-1].split(".")); #S.E.-->SE
# 	if(branch == 'INFORMATION' and clss=="SE"):
# 		# ourresult = result(clss + 'INFORMATION',resultt[0])	
# 		ourresult = result(clss + 'CSE',resultt[0])
# 		query = 'update data set Result=%s where seat_no=%s'
# 		value = (ourresult,seatno)
# 		resp = cur.execute(query,value)
# 		mydb.commit()
# 	elif('/' in branch):
# 		clss1 = branch.split('/')
# 		clss2=clss1[0]
# 		ourresult = result(clss+clss2,seatno)
# 		query = 'update data set Result=%s where seat_no=%s'
# 		value = (ourresult,seatno)
# 		resp = cur.execute(query,value)
# 		mydb.commit()
# 	else:
# 		ourresult = result(clss+branch,seatno)
# 		query = 'update data set Result=%s where seat_no=%s'
# 		value = (ourresult,seatno)
# 		resp = cur.execute(query,value)
# 		mydb.commit()
# 	i+=1
manual_result()
print('operation Success')	









#searching in NEW


# w1=0;w2=0;w3=0;w4=0;w5=0;w6=0;w7=0;w8=0;w9=0;w0=0;
# for i in range(len(L3)):
#   if(L3[i]=="DECLEARED" and L3[i+1]=="PASS"):
#       w1=i;
#   if(L3[i]=="KEEP" and L3[i+1]=="TERM"):
#       w2=i;
#   if(L3[i]=="F-ATKT"):
#       w3=i;
#   if(L3[i]=="ABSENT"):
#       w4=i
#   if(L3[i]=="FAIL"):
#       w5=i
#   if(L3[i]=="RESERVED" and L3[i+1]!="FOR"):
#       w6=i
#   if(L3[i]=="OFFICE" and L3[i+1]=="VERIFICATION"):
#       w7=i
#   if(L3[i]=="ELIGIBILITY" and L3[i+1]=="CERTIFICATE"):
#       w8=i
#   if(L3[i]=="WPC"):
#       w9=i
#   if(L3[i]=="DETAINED"):
#       w0=i
# M1=[];M2=[];M3=[];M4=[];M5=[];M6=[];M7=[];M8=[];M9=[];M0=[];
# nestedList3=[]
# while(w1<w2):
#   M1.append(L3[w1])
#   w1=w1+1
# nestedList3.append(M1)
# while(w2<w3):
#   M2.append(L3[w2])
#   w2=w2+1
# nestedList3.append(M2)
# while(w3<w4):
#   M3.append(L3[w3])
#   w3=w3+1
# nestedList3.append(M3)
# while(w4<w5):
#   M4.append(L3[w4])
#   w4=w4+1
# nestedList3.append(M4)
# while(w5<w6):
#   M5.append(L3[w5])
#   w5=w5+1
# nestedList3.append(M5)
# while(w6<w7):
#   M6.append(L3[w6])
#   w6=w6+1
# nestedList3.append(M6)
# while(w7<w8):
#   M7.append(L3[w7])
#   w7=w7+1
# nestedList3.append(M7)
# while(w8<w9):
#   M8.append(L3[w8])
#   w8=w8+1
# nestedList3.append(M8)
# while(w9<w0):
#   M9.append(L3[w9])
#   w9=w9+1
# nestedList3.append(M9)
# while(w0<len(L3)):
#   M0.append(L3[w0])
#   w0=w0+1
# nestedList3.append(M0)

# listname3=-1;
# for list2 in range(len(nestedList3)):
#   for i in nestedList3[list2]:
#       s=i.split('\n\n')
#       for j in s:
#           if(j==seatno):
#               listname3=list2;
# if(listname3==0):
	# print("PASS")
# elif(listname3==1):
	# print("ATKT")
# elif(listname3==2):
#   # print("F-ATKT")
# # elif(listname3==3):
#   print("ABSENT")
# # elif(listname3==4):
#   print("FAIL")
# # elif(listname3==5):
#   print("RHR")
# # elif(listname3==6):
#   print("OV")
# # elif(listname3==7):
#   print("EC")
# # elif(listname3==8):
#   print("WPC")
# # elif(listname3==9):
#   print("DETAINED")

