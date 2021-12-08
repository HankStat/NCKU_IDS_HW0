def mySortDict2(data):
	x2y = []
	for k, v in data.items():
		x2y.append([v, k])
	x2y.sort(reverse=True)
	return x2y
#定義一個函數使得dict的key value交換並由大排到小
def printTopK(x2y, k, des):
	print(des)
	for i in range(k):
		print(x2y[i])
	key = x2y[i][0]
	for i in range(k,len(x2y)-1):
		if x2y[i][0] != key:
			break
		print(x2y[i])
	print()
#定義一個函數print出文字敘述(des) 然後根據k(top-k)
#來決定要print幾個
#假設如果有平手的狀況都要印出來 
filename = "IMDB-Movie-Data.csv"
tf = open(filename, "r")
tf.readline()
#把檔案讀進去 並從第二行開始讀
t2r, a2tr, a2r, a2t,  d2a, a2g, agap,all_related= {}, {}, [], {}, {}, {}, {}, {}
for line in tf:
	cols = (line.strip()).split(",")
	title = cols[1]
	genre = cols[2].split("|")
	director = cols[3]
	actors = cols[4].split("|")
	year = int(cols[5])
	rating = float(cols[7])
	totalrevenue = cols[9]
	if totalrevenue=="":
		totalrevenue=0
	if totalrevenue!="":
		totalrevenue=float(totalrevenue)
#利用for迴圈一行一行讀進來 cols就是把換行與空格去掉在split掉的list
#把cols分類 特別注意actors要在用split 然後totalrevenue如果是空格的
#話，就要改成0才能做計算
	for i in range(len(actors)):
		actors[i] = actors[i].strip()
		#把空格去掉
		if actors[i] in a2tr.keys():
			a2tr[actors[i]].append(totalrevenue)
		if actors[i] not in a2tr.keys():
			a2tr[actors[i]] = [totalrevenue]
		#第二題 以(actor, totalreevenue)的形式裝進a2tr裡面
		#假設actor已經在a2tr裡面 那只要累加totalrevenue即可
		if actors[i] == "Emma Watson":
			a2r.append(rating)
		#如果是艾瑪華生的話就把rating加入a2r裡面
		if actors[i] in a2t.keys():
			a2t[actors[i]] +=1
		if actors[i] not in a2t.keys():
			a2t[actors[i]] = 1
		#把(actor, 次數)加入a2t裡面 只要有重複的actor就加1
		for j in range(len(genre)):
			if actors[i] in a2g.keys():
				a2g[actors[i]].append(genre[j])
			if actors[i] not in a2g.keys():
				a2g[actors[i]] = [genre[j]]
		#第五題 以(actor, genre)的形式裝入a2g裡面 如果該名演員在
		#a2g的key時 就append 如果沒有就新增actor這個key
		if actors[i] in agap.keys():
			myyear = agap[actors[i]]
			myyear.extend([year])
			agap[actors[i]] = myyear
		if actors[i] not in agap.keys():
			agap[actors[i]] = [year]
		#第六題 以(actor, year)的形式加入agap裡面 若有重複
		#則把year加入即可
	if year == 2016:
		t2r[title] = rating
	#第一題 假設year=2016 就把title rating裝進t2r裡面
	if director in d2a.keys():
		myactors = d2a[director]
		myactors.extend(actors)
		d2a[director] = myactors
	if director not in d2a.keys():
		d2a[director] = actors
	#第四題 以(director, actorlist)形式加入d2a 
	#若有重複的director 則擴編actorlist即可
	for index in range(len(actors)):
		for index2 in range(len(actors)):
			if index != index2:
				if actors[index] not in all_related.keys():
					all_related[actors[index]]=[actors[index2]]
				else :
					if actors[index2] not in all_related[actors[index]]:
						all_related[actors[index]].append(actors[index2])
	#第七題 先創一個all_related 的dictionary key是每個不同的actor
	#value 是actorlist 代表與key合作的所有演員
	#每一部電影的4個actor兩兩互相都有合作過 因此要用兩層迴圈
	#如果該名演員不在all_related 的key裡面 那就新增那名演員到all_related上面
	#如果該名演員在all_related 的key裡面 那就檢查那名演員的演員合作名單上有沒有出現過
	#沒有的話再新增上去演員合作名單
tf.close()
r2t = mySortDict2(t2r)
printTopK(r2t, 3, "Top-3 movies with the highest ratings in 2016")
#第一題用上面兩個函數就能取前三個

for key ,value in a2tr.items(): 
	a2tr[key]=sum(value)/len(value)
tr2a = mySortDict2(a2tr)
printTopK(tr2a, 2, "The actor generating the highest average revenue")
#第二題 用上面兩個函數即可print出結果

print("The average rating of Emma Watson's movies")
print(sum(a2r)/len(a2r))#平均
print()
#第三題 print平均即可
d2numA = {}
for d, alist in d2a.items():
	d2numA[d] = len(set(alist))
#先刪掉重複的actor 再取長度
na2d = mySortDict2(d2numA)
printTopK(na2d, 3, "top-3 collaboration-actor directors")
#第四題 用上面兩個函數即可print出結果
a2numG = {}
for a, glist in a2g.items():
	a2numG[a] = len(set(glist))
#把(actor, genrelist)形式改成(actor, 不同genre的總數) 透過set的方式
ng2a = mySortDict2(a2numG)
printTopK(ng2a, 2, "top-2 actors playing in the most genres of movies")
#第五題 用上面兩個函數即可print出結果

amaxyear = {}
for a, ylist in agap.items():
	amaxyear[a] = max(ylist)-min(ylist)
#把(actor, yearlist)的形式改成(actor, gapyear)
maxgap2a =  mySortDict2(amaxyear)
printTopK(maxgap2a, 3, "Top-3 actors whose movies lead to the largest maximum gap of years")
#第六題 用上面兩個函數即可print出結果
# print(all_related)
JD_related=all_related["Johnny Depp"]
#JD_related是指跟Johnny Depp 有直接合作關係的演員的list
final=list(JD_related)
#final是指所有有直接跟間接合作關係的演員的list
checklist=list(JD_related)
#checklist是裝有已經搜尋過的演員名單
checklist.append("Johnny Depp")
#因為題目就是問你Johnny Depp 所以checklist要有Johnny Depp
#代表Johnny Depp 已經有搜尋過
while len(JD_related)>0:
	for index in range(len(all_related[JD_related[0]])):
		if all_related[JD_related[0]][index] not in checklist:
			final.append(all_related[JD_related[0]][index])
			if all_related[JD_related[0]][index] in all_related.keys():
				JD_related.append(all_related[JD_related[0]][index])
				checklist.append(all_related[JD_related[0]][index])
	del JD_related[0]
#上面部分
#JD_related的第一個演員的演員合作名單 如果演員合作名單的演員不在checklist
#把該名演員加到最後的final
#如果該名演員不在checklist且該名演員在all_related的key裡面
#代表那名演員有跟其他演員合作 才要把演員加入JD_related 如此一來才能搜尋
#並把該名演員加入checklist 以防重複搜尋同一名演員
print("Find all actors who collaborate with Johnny Depp in direct and indirect ways ")
print(len(final))
# print(final)
#因為名單太多 所以只印出長度