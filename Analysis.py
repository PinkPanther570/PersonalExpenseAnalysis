#记录用户输入的数据
everyday_dic={}
while True:
    date=input("请输入花销产生的日期，格式示例：2026.09.17，如已经没有需要记录的花销，请输入N")
    if date == "N":
        break
    info_dic = {}
    while True:
        sort=input("请输入花销的类别")
        money=int(input("请输入该类别花费的金额（元）"))
        info_dic[sort]=money
        check2 = input("当天是否还有其他花销？输入Y/N")
        if check2 == "N":
            everyday_dic[date]=info_dic
            break

#汇总每一天的花销情况
print(f"每天的花销情况统计如下{everyday_dic}。")

#展示各个类别的花销情况
sort_dic= {}
for key in everyday_dic.keys():
    data=everyday_dic[key]
    for x in data.keys():
        if x in sort_dic.keys():
            sort_dic[x]+=int(data[x])
        else:
            sort_dic[x]=int(data[x])
print(f"各个类别的花销情况如下{sort_dic}")

#计算最大类别花销
max_value=max(sort_dic.values())
max_sort= {}
for y in sort_dic.keys():
    if sort_dic[y]==max_value:
        max_sort[y]=max_value
print(f"花销最大的类别如下：{max_sort}")

#计算合计花销
amount=0
for i in sort_dic.keys():
    amount+=sort_dic[i]
print(f"合计花销为{amount}元")

#计算合计花销
count=len(everyday_dic)
print(f"平均每日花销为{amount/count}元")

