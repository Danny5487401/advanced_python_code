a = {"danny1": {"company": "China"},
     "danny2": {"company": "China"}
     }

# a.clear()
# print(a)

# fromkeys  可迭代对象变成keys
new_list = ["danny1", "danny2"]
new_dict = dict.fromkeys(new_list, {"company": "daxue"})
# print(new_dict) # {'danny1': {'company': 'daxue'}, 'danny2': {'company': 'daxue'}}
# get默认值，防止keyerror
value1 = new_dict.get("danny3", {})

# setdefault
value2 = new_dict.setdefault("danny3", "name")

# update  两个字典合并
a.update(new_dict)
a.update([("haha", "hehe")])
print(a)
