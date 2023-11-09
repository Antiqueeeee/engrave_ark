from copy import deepcopy
from collections import defaultdict
from tqdm import tqdm
import json

target_engrave = {"盛放":15,"身披重甲":15,"妙手回春":15,"觉醒":15,"混元":3,"先发制人":3}
# target_engrave = {"怨恨":15,"咒术人偶":15}
engrave_books = {"盛放":9,"身披重甲":9}
ability_stone = {"妙手回春":6,"觉醒":6}

# engraves_values = [(2,2),(3,2),(3,3),(3,4),(3,5),(4,3),(5,3)]
engraves_values = [(3,3),(3,5),(5,3)]


# 先检查点数够不够，点数不够中止，点数够继续运行
max_point = max([sum(i) for i in engraves_values]) * 5 + sum([v for k,v in engrave_books.items()]) + sum([v for k,v in ability_stone.items()])
target_value = sum([v for k,v in target_engrave.items()])
print(f"期望刻印共需要点数:{target_value}点，书石首饰能提供{max_point}点",end="")
if target_value > max_point:
    print(f"还差{abs(target_value - max_point)}点，请调整方案")
    raise
else:
    print("可以尝试。")

for key,value in target_engrave.items():
    target_engrave[key] = target_engrave[key] - engrave_books.get(key,0)
    target_engrave[key] = target_engrave[key] - ability_stone.get(key,0)

# 都有什么刻印
engraves = list(target_engrave.keys())
# 刻印两两搭配能有多少组合
#！！！！！！
#两个职业刻印不能在一起喔
#！！！！
combo_engraves = list()
for i in range(len(engraves)):
    for j in range(i+1,len(engraves)):
        combo_engraves.append([engraves[i],engraves[j]])



# 刻印两两搭配算上数值
combo_engrave_values = list()
for item in combo_engraves:
    for values in engraves_values:
        _item = deepcopy(item)
        _item.append(values)
        combo_engrave_values.append(_item)

# 各个位置的首饰跟刻印数值组合
parts = ["项链","耳环1","戒指1","耳环2","戒指2"]
combo_jewelry = list()
for part in parts:
    for values in combo_engrave_values:
        combo_jewelry.append([part] + values)

# 按part制作字典，用于穷举所有方案
mapping_jewelry = {part:[] for part in parts}
for item in combo_jewelry:
    mapping_jewelry[item[0]].append(item)
for k,v in mapping_jewelry.items():
    print(k,len(v))
with open("temp/mapping_jewelry.json","w",encoding="utf-8") as f:
    json.dump(mapping_jewelry,f,ensure_ascii=False,indent=1)

# 从项链开始一层一层向下穷举
# 如果当前组合的点数足够target_engrave，那么就存到备选方案里面
methods = list()
for necklace in tqdm(mapping_jewelry["项链"]):
    for earring1 in mapping_jewelry["耳环1"]:
        for earring2 in mapping_jewelry["耳环2"]:
            for ring1 in mapping_jewelry["戒指1"]:
                for ring2 in mapping_jewelry["戒指2"]:
                    _sum = 0
                    for j in [necklace,earring1,earring2,ring1,ring2]:
                        _part,_engrave1,_engrave2,(_value1,_value2) = j
                        _sum += sum([_value1,_value2])
                    if _sum >= sum(target_engrave.values()):
                        methods.append([necklace,earring1,earring2,ring1,ring2])
        #                 print(f"当前necklace为：{necklace}")
        #                 print(f"当前earring1为：{earring1}")
        #                 print(f"当前earring2为：{earring2}")
        #                 print(f"当前ring1为：{ring1}")
        #                 print(f"当前ring2为：{ring2}")
                    
        #             break
        #         break
        #     break
        # break


print(f"穷举所有可能，找到符合target_engrave的方案")
_results = list()
for method in tqdm(methods) :
    res = defaultdict(int)
    flag = True
    for item in method:
        _,engrave1,engrave2,(value1,value2) = item
        res[engrave1] += value1
        res[engrave2] += value2
    if len(res) < len(target_engrave):
        continue
    for k,v in target_engrave.items():
        if res.get(k,0) < v:
            flag = False
            break
    if flag:
        _results.append(method)

# 调整数据结构，保存所有方案
results = list()
for res in _results:
    _method = list()
    for med in res:
        item = dict()
        _part,_engrave1,_engrave2,(_value1,_value2) = med
        item[_part] = (_engrave1,_engrave2,_value1,_value2)
        _method.append(item)
    results.append(_method)

with open(f"temp/results.json","w",encoding="utf-8") as f:
    json.dump(results,f,ensure_ascii=False,indent=1)
print(f"已经找到符合标准的方案{len(results)}套。")


# 方案数量虽然比较多，但是需要检索的首饰肯定有重叠，而且应该是大部分都是重叠
#！！！！
#  戒指耳环不应该分1，2喔
#！！！
jewelry_tobe_search = defaultdict(list)
for res in _results:
    for med in res:
        _part,_engrave1,_engrave2,(_value1,_value2) = med
        _values = (_engrave1,_engrave2,_value1,_value2)
        if _values not in jewelry_tobe_search[_part]:
            jewelry_tobe_search[_part].append(_values)
_sum = 0
for k,v in jewelry_tobe_search.items():
    _sum += len(v)
print(f"所有方案中，共需要检索首饰{_sum}件")

# 需要检索的就是最开始组合出来的首饰数量，
# 所以还是要从最开始搭配出来的首饰那里开始筛选

