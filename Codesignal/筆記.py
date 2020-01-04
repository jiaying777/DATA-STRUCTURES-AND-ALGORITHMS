#0924

a = 6
b = -4
a / b 
# = -1.5
a // b #地板除法 （向下取整數值）
# = -2

#十進制轉二進制
def convertToBinary(n):
	if n>1:
		convertToBinary(n//2)
	print(n%2 , end = '')

#數值的二進制長度
def countbits(n):
	return n.bit_length()




#0925


#list交換位子
a = [4,2,9,5]
a[0],a[1]=a[1],a[0]
#第一個值[0]與第二個[1]交換

#重新排序
sorted(a) #>>>[2,4,5,9]
sorted(ａ, reverse=False)  #reverse = True 降序(大到小) ， reverse = False 升序（默認）

#list重新排序
a.sort()  

#進制轉換
int('n',x) #將數值n 從x進制轉換成十進制
hex(n) #十進制轉十六進制

def baseConversion(n, x):
    return hex(int(n,x))[2:]
#[2:]擷取第三個以後  ex:0x4 -> x代表(16進制) -> 代表轉換成十六進制時 數值為4




#0926

list = [4, 3, 1, 2, 3, 4, 1, 7, 8]
a,b,c,d,e,f,g,h,i = list
#a=4 , b=3 , c=1.........

a,b,*list,c = list
#a=4 , b=3 , c=8
#list = [1, 2, 3, 4, 1, 7]

a=[]
*a,b = list
#a = [4, 3, 1, 2, 3, 4, 1, 7]
#b = 8


#1004

str.upper()        # 把所有字符中的小寫字母轉換成大寫字母
str.lower()          # 把所有字符中的大寫字母轉换成小寫字母
str.capitalize()     # 把第一個字母轉化为大寫字母，其餘小寫
str.title()          # 把每個單詞的第一个字母轉化大寫，其餘小寫 

s.isupper() #判斷字串大寫
s.islower() #判斷字串小寫
s.isdigit() #判斷是否為數值
s.isspace() #判斷空格，包含換行




#dict
#按照key值排序
def sortedDictValues1(adict): 
	items = adict.items() 
	items.sort() 
	return [value for key, value in items] 

def sortedDictValues2(adict): 
	keys = adict.keys() 
	keys.sort() 
	return [dict[key] for key in keys]

def sortedDictValues3(adict): 
	keys = adict.keys() 
	keys.sort() 
	return map(adict.get, keys)

#用lambda表答来排序
sorted(d.items(), lambda x, y: cmp(x[1], y[1]))
print sorted(dict1.items(), key=lambda d: d[0])
#d為任一字串皆可，[0]代表按照第0位排序--->Key

sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)#反序 
print sorted(dict1.items(), key=lambda d: d[1])
#[1]代表按照第1位排序--->Value


# 字串格式化
i='Hello'
j=123
print('%s'%i) #s字串
print('%d'%j) # %d-->int %f-->浮點數
#https://openhome.cc/Gossip/Python/StringFormat.html
