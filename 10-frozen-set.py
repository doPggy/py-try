# 不可变集合
## 创建
'''一旦创建，不得修改'''
s = frozenset([1, 2, 3, 'a', 4])
print(s)
## 应用
'''字典的键值'''
flight_distance = {}
flight_distance[frozenset(['fuzhou', 'beijing'])] = 123
flight_distance[frozenset(['fuzhou', 'xiamen'])] = 2
flight_distance[frozenset(['fuzhou', 'guizhou'])] = 3323
print(flight_distance)