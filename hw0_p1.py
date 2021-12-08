input_poly = input("Input the polynominals: ")
print("Output Result: ",end="")
poly_List=input_poly.split("(")
#利用(去split整個多項式相乘的自串
del poly_List[0]
for i in range(len(poly_List)):
	poly_List[i]=poly_List[i][:-1]
	nominus_list=poly_List[i].split("-")
	poly_List[i]="+-1*".join(nominus_list)
	poly_List[i]=poly_List[i].split("+")
#先把負號處理成+-*
#在透過+去split掉 這樣就可以把每個多項式中的每一項分開
def produce(poly_List,number):
	eventual={}
	#eventual 是一個裝有係數跟X Y Z的dictionary
	for i in range(len(poly_List[0])):
		for j in range(len(poly_List[1])):
			co=1
			div_mul1=poly_List[0][i].split("*")
			div_mul2=poly_List[1][j].split("*")
			#取出要相乘的兩項數分別的係數
			if len(div_mul1)>1 and len(div_mul2)>1:
				co=int(div_mul1[0])*int(div_mul2[0])
				del div_mul1[0]
				del div_mul2[0]
			#兩項數分別的係數相乘會等於兩項數相乘之後的係數
			elif len(div_mul1)>1:
				co=int(div_mul1[0])
				del div_mul1[0]
			#若有一項的係數是1 那相乘的項的係數會等於另一個項的係數
			elif len(div_mul2)>1 :
				co=int(div_mul2[0])
				del div_mul2[0]
			div_var1=[]
			div_var2=[]
			k=0
			while k<len(div_mul1[0]):
				if k <len(div_mul1[0])-2 and div_mul1[0][k+1] == "^":
					div_var1.append(div_mul1[0][k:k+3])
					k=k+3
				else:
					div_var1.append(div_mul1[0][k])
					k=k+1
			l=0
			while l<len(div_mul2[0]):
				if l <len(div_mul2[0])-2 and div_mul2[0][l+1] == "^":
					div_var2.append(div_mul2[0][l:l+3])
					l=l+3
				else:
					div_var2.append(div_mul2[0][l])
					l=l+1
			#這部分是處理未知數的次方 假設有偵測到^ 那要把"X^k"(k為整數)
			#裝入div_var1 div_var2裡面 如果只是單純的一次方(也就是沒有^)
			#也一樣要裝進上面那兩個list裡面
			dic1 = {}
			for index in range(len(div_var1)):
				if (div_var1[index][0] not in dic1):
					if len(div_var1[index])==1:
						dic1[div_var1[index][0]]=1
					else :
						dic1[div_var1[index][0]]=int(div_var1[index][2])
				else :
					num=dic1[div_var1[index][0]]
					if len(div_var1[index])==1:
						dic1[div_var1[index][0]]=num+1
					else :
						dic1[div_var1[index][0]]=num+int(div_var1[index][2])
			for index in range(len(div_var2)):
				if (div_var2[index][0] not in dic1):
					if len(div_var2[index])==1:
						dic1[div_var2[index][0]]=1
					else :
						dic1[div_var2[index][0]]=int(div_var2[index][2])
				else :
					num=dic1[div_var2[index][0]]
					if len(div_var2[index])==1:
						dic1[div_var2[index][0]]=num+1
					else :
						dic1[div_var2[index][0]]=num+int(div_var2[index][2])
			#dic1是一個 未知數為key 次方為value的dictionary 
			#把剛剛的div_var1 跟div_var2 的東西放進去
			dic2={}
			for key in sorted(dic1.keys()):
				dic2[key]=dic1[key]
			#dic2就是把key去sort 例如說讓X在Y前面
			str1=""
			for key,value in dic2.items():
				if value==1:
					str1=str1+key
				else:
					str1=str1+key+"^"+str(value)
			if str1 not in eventual:
				eventual[str1]=co
			else :
				num2=eventual[str1]
				eventual[str1]=num2+co
			#把相乘之後的結果放到eventual裡面 key一樣裝有未知數 value就是相乘之後的
			#係數 並要處理假設都有同樣未知數 係數要相加
	final_str=""
	count=0
	for key,value in eventual.items():
		if value==1:
			if count==0:
				final_str+=key
			else :
				final_str+="+"+key
		elif value==-1:
			final_str+="-"+key
		elif value >1:
			if count==0:
				final_str+=str(value)+"*"+key
			else :
				final_str+="+"+str(value)+"*"+key
		else :
			final_str+=str(value)+"*"+key
		count+=1
	#final_str就是兩個多項式相乘最終的結果
	#並要處理係數是1的情況不能把1print出來
	if number==2:	
		return final_str	
	elif number >2:
		poly_List=poly_List[2:]
		nominus_list=final_str.split("-")
		temp="+-1*".join(nominus_list)
		temp=temp.split("+")
		poly_List.insert(0,temp)
		return produce(poly_List,number-1)
	#如果是三個以上的多項式相乘的話就要用recursive的方法
print(produce(poly_List,len(poly_List)))
#print出結果
