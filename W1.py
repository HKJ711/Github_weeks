#字典的增删改查
my_dict = {"hao":99,"kang":88,"jie":77}
my_dict["wang"] = 66
print(my_dict)
my_dict.pop("hao")
print(my_dict)
my_dict["kang"] = 55
print(my_dict)
print(my_dict["jie"])

#字典的遍历
for k in my_dict:#结果只有key
    print(k)
for k in my_dict.keys():#结果也只有key
    print(k)
for v in my_dict.values():#结果只有value
    print(v)
for k,v in my_dict.items():
    print(k)
    print(v)
    print(k,v)

#字典嵌套美观写法
another_dict = {
    "hao":{
        "语文":99,
        "数学":98,
        "英语":97},
    "kang":{
        "语文":88,
        "数学":87,
        "英语":86},
    "jie":{
        "语文":77,
        "数学":76,
        "英语":75}
}
print(another_dict)

#字典get返回值
my_dict = {"hao":99,"kang":88,"jie":77}
#print(my_dict["wang"])#这样查会崩
print(my_dict.get("wang",0))

#列表推导式
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1,-2]
result = [x*2 for x in nums if x >0]
print(result)

#统计一句话中的词频
sentence = "there is a book on a table"
s = sentence.split()
new_dict = {}
print(s)
for x in s:
    new_dict[x] = new_dict.get(x,0)+1
print(new_dict)