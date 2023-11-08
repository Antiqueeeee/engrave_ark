from copy import deepcopy
from collections import defaultdict
from tqdm import tqdm


target_engrave = {"怨恨":15,"咒术人偶":15,"强力侧击":15,"肾上腺素":15,"精密短刀":15}
# target_engrave = {"怨恨":15,"咒术人偶":15}
engrave_books = {"强力侧击":12,"肾上腺素":12}
ability_stone = {"怨恨":7,"咒术人偶":7}

for key,value in target_engrave.items():
    target_engrave[key] = target_engrave[key] - engrave_books.get(key,0)
    target_engrave[key] = target_engrave[key] - ability_stone.get(key,0)

# 都有什么刻印
engraves = list(target_engrave.keys())
# 刻印两两搭配能有多少组合
combo_engraves = list()
for i in range(len(engraves)):
    for j in range(i+1,len(engraves)):
        combo_engraves.append([engraves[i],engraves[j]])

# 刻印两两搭配算上数值
# engraves_values = [(2,2),(3,2),(3,3),(3,4),(3,5),(4,3),(5,3)]
engraves_values = [(3,3),(3,5),(4,3),(5,3)]
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
results = list()
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
        results.append(method)
    # print("---"*30)
# print(f"\n有效方案：")
# print(results)