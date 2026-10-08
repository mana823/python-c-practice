# 练习2.1
from shlex import join


a = 'jfgaoips'
print(a)

# 练习2.2
q = 'fjs'
print(q)
q = 'fjlsa'
print(q)

# 练习2.3
name = 'mana'
message = f'Hi，{name}，good afternoon!'
print(message)

# 练习2.4
name = 'ma na'
name1 = name.title()
print(name1)
name2 = name.upper()
print(name2)
name3 = name.lower()
print(name3)

# 练习2.5 & 练习2.6
名人名字 = '鲁迅'
名人名言 = '横眉冷对千夫指，俯首甘为孺子牛。'
message = f'{名人名字}曾经说过：“{名人名言}”'
print(message)

# 练习2.7
name = ' ma na '
print(name)
name1 = name.lstrip()
print(name1)
name2 = name.rstrip()
print(name2)
name3 = name.strip()
print(name3)
print(f'{name3}\n你好')
print(f'{name3}\n\t你好')   # 哪个符号在前面先运行谁

# 练习2.8
filename = 'python_note.txt'
filename1 = filename.removesuffix('.txt')
print(filename1)

# 练习2.9
print(1+7)
print(2*4)
print(9-1)
print(int(round(16/2, 0)))   # int()变整数  round()保留几位小数
print(16//2)

# 练习2.10
a = 2
message = f'我最喜欢的数字是{a}, 但是你干嘛！'
print(message)

# 练习3.1
names = ['Tom', 'Mana', 'Dream', 'Jerrey']
# 字符拼接用加号，'\n'可以看作字符串
print(names[0] + '\n' + names[1] + '\n' + names[2] + '\n' + names[3])
print(f'{names[0]}\n{names[1]}')   # 花括号可以帮助python区分内容，可以不用'+'拼接

# 练习3.2
print(f'你好，{names[0]}' + '\n' + f'再见，{names[1]}')
print(f'你好，{names[0]}\n再见，{names[1]}')

# 练习3.3
approach = ['骑自行车', '开小车', '坐公交车', '坐地铁', '坐飞机']
print(f'在距离较近的时候，我一般选择{approach[0]}。\n在距离较远的时候，我回去选择{approach[-1]}。')

# 练习3.4
嘉宾 = ['张三', '李四', '王二', '麻子']
print(嘉宾)
print(f'邀请{嘉宾[0]}\t{嘉宾[3]}一起吃饭')

# 练习3.5
print(f'{嘉宾[2]}无法参加！')
del 嘉宾[2]
嘉宾.insert(2, '汤姆')
print(嘉宾)
嘉宾.remove('汤姆')
嘉宾.append('杰瑞')
print(嘉宾)
嘉宾.pop()
print(嘉宾)
嘉宾.pop(0)
print(嘉宾)

# 练习3.6
嘉宾.insert(0, '狗蛋')
嘉宾.insert(1, '富贵')
嘉宾.append('杰克')
print(嘉宾)

# 练习3.7
print('由于餐桌餐具问题，只能邀请两位嘉宾！')
踢 = 嘉宾.pop(2)
print(f'{踢}，我对你十分抱歉')
踢 = 嘉宾.pop(2)
print(f'{踢}，我对你十分抱歉')
踢 = 嘉宾.pop(2)
print(f'{踢}，我对你十分抱歉')
print(f'{嘉宾[0]},{嘉宾[1]}你们仍在赴宴名单内')
del 嘉宾[0:2]         # [0:2] 删掉从索引0到1的数
print(嘉宾)

# 练习3.8
地方 = ['杭州', '哈尔滨', '北京', '上海']
print(地方)
print(sorted(地方))
print(地方)
地方.reverse()
print(地方)
地方.reverse()
print(地方)
地方.sort()
print(地方)
地方.sort()
print(地方)

# 练习3.9
嘉宾 = ['张三', '李四', '王二', '麻子']
print(len(嘉宾))

# 练习3.10
用品= ['phone', 'box', 'pen', 'chair']
print(sorted(用品))
用品.sort()
print(用品)
用品.reverse()
print(用品)
print(len(用品))

# 练习4.1
列表 = ['a', 'b', 'c', 'd']
for i in 列表:
    print(f'I like {i} pizza')
print('I really love pizza!')

# 练习4.2
动物 = ['dog', 'cat', 'horse']
for a in 动物:
    print(f'A {a} would make great pet.')
print('Any of these animals would make a great pet!')

# 练习4.3
for i in range(1,21):
    print(i)

# 练习4.4
numbers = list(range(1,1000001))    # 创建一个一到一百万的列表
for number in numbers:
    # print(number)
    pass   # 响应上面的for in 循环 ,pass直接结束就行了,不然后续无进程响应会报错
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 练习4.5
for b in range(1,21,2):
    print(b)

# 练习4.6
q = list(range(3,31,3))
for s in q:
    print(s)

# 练习4.7
lists = []
for num in range(1,11):
    lists.append(num**2)
print(lists)

# 练习4.8
a = [num**2 for num in range(1,11)]  # 立方推导式外层看情况加括号
print(a)
print(*a)   # *是解包运算符

# 练习4.9
message = 'The first three items in the list are:'
print(message)
print(lists[:3])
message = 'Three items from the middle of the list are:'
print(message)
mid = len(lists)//2
print(lists[mid-1:mid+2])
message = 'The last three items in the list are:'
print(message)
print(lists[-3:])

# 练习4.10
lists = ['a', 'b', 'c', 'd']
friend_pizzas = lists
lists.append('e')
friend_pizzas.append('f')
print('My favorite pizzas are:')
for a in lists:
    print(a)
print("My friends' favorite pizzas are:")
for b in friend_pizzas:
    print(b)

# 练习4.11
foods = ('fish', 'hotdog', 'pizza', 'apple','egg')
for food in foods:
    print(food)
# foods[1] = 'fruit'     修改元组元素会报错
foods = ('banana', 'hotdog', 'meet', 'apple', 'egg')
for food in foods:
    print(food)

# 练习5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car =='audi'? I predict False.")
print(car == 'audi')

# 练习5.2
string1 = 'apple!'
string2 = 'egg?'
if string1 == string2:
    print('True')
else:
    print(False)  # 不打引号也可以，python会自己转换这些关键字并输出
print(string1 == string2)

example1 = 'hi'
example2 = 'Hi'
condition = example1 == example2.lower()
print(condition)

number1 = 10
number2 = 48
if number1 >= 3 and number2 >= 54:
    print(True)
else:
    print(False)    
condition = number1 >= 3 and number2 >= 54    
print(condition)
condition = number1 >= 3 or number2 >= 54
print(condition)
lists = ['a', 'b', 'c', 'd']
if 'g' not in lists:
    print('The data not in the list!')
else:
    print('The data in the list!')
game_active = True
can_edit = False

# 练习5.3
alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points.')
alien_color = 'red'
if alien_color == 'green':
    print('You got 5 points.')  # 没有输出

# 练习5.4
alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points.')
if not alien_color == 'green':
    print('You got 10 points.')

if alien_color == 'green':
    print('You got 5 points.')
else:
    print('You got 10 points.')

# 练习5.5
alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points.')
elif alien_color == 'yellow':
    print('You got 10 points.')
else:    # 与前面条件相反
    print('You get 15 points.')

alien_color = 'yellow'
if alien_color == 'green':
    print('You got 5 points.')
elif alien_color == 'yellow':
    print('You got 10 points.')
else:    # 与前面条件相反
    print('You get 15 points.')

alien_color = 'red'
if alien_color == 'green':
    print('You got 5 points.')
elif alien_color == 'yellow':
    print('You got 10 points.')
else:    # 与前面条件相反
    print('You get 15 points.')

# 练习5.6
age = 7
if age < 2:
    print('Is a baby.')
elif 2 <= age < 4:
    print('Is a young child.')
elif 4 <= age < 13:
    print('Is a child.')
elif 13 <= age < 18:
    print('Is a teenager.')
elif 18 <= age < 65:
    print('Is a young adukt.')
else:
    print('Is a elderly person.')

# 练习5.7
favorite_fruits = ['apple', 'banana', 'watermelon']
if 'apple' in favorite_fruits:
    print('You are really like apple!')   # 运行
if 'hotdog' in favorite_fruits:
    print('You are really like hotdog!')  # 不运行

# 练习5.8 以特殊的方式跟管理员打招呼
user_names = ['admin', '123', '33639', 'abc', '#@']
for user_name in user_names:
    if user_name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello, {user_name}, thank you for logging in again.')

# 练习5.9 处理没有用户的情形
user_names = []
if user_names:   # 判断条件，空列表返回False，下面的命令全部跳过，直接执行同一缩进的else的命令
    for user_name in user_names:
        if user_name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:    
            print('Hello, Jaden, thank you for logging in again.') 
else:            # 执行同一缩进的else的命令
    print('We need to find some users!!')

# 练习5.10 检查用户名
current_users = ['admin', '123', '33639', 'abc', '#@']
new_users = ['ABC', 'admin', '111', '@@']
lower = [user.lower() for user in current_users]  # 把老名单里面的全取出来变成小写做为列表
for new_user in new_users:
    if new_user.lower() in lower:                 # 再把新用户名全部改为小写与变小写的老列表做判断
        print('该用户名已存在！请换一个名称。')
    else:
        print(f"已为您创建用户名'{new_user}'。")
# lower = list(map(str.lower, current_users [:]))  <--也可以这样换一个小写老列表
# 代码解释：
# 1. current_users[:]：创建老列表的副本。
# 2. map(str.lower, ...)：告诉 Python，把 str.lower 这个功能，挨个应用到列表里的每一个元素上。
# 3. list(...)：因为 map 返回的是一个迭代器，我们用 list() 把它重新打包成一个列表。
# 4. 迭代器就像一条一次性的传送带，数据是用一个吐一个。不管是遍历完，还是中途用 break 停掉，会永久流失，在 in 判断时提前找到了，
# 它会消耗掉已经拿出来的数据。所以它不能拿来反复查找和对比，如果想反复使用，必须先用 list() 把它打包成普通的列表。

# 练习5.11 序数
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

# 练习6.1 人
dictionary = {'first_name': 'Li', 'last_name': 'Hua', 'age': '17', 'city': '888'}
print(*dictionary)    # 打印所有键，并用空格隔开
print(*dictionary.values(), sep=',')   # 打印所有值，并用逗号隔开(默认空格)
print(*dictionary.items())   # 打印所有键值对(用圆括号装起来)，并用空格隔开  .items()取出键值对，中文意思是:条目、项目
# 每个键值对一行
for k, v in dictionary.items():
    print(k, v)
# 条件筛选(列表)
lst = [10, 20, 30, 40, 50]
print(*lst[1:4])         # 打印索引 1~3：20 30 40
print(*[x for x in lst if x > 25])  # 条件筛选：30 40 50
# 条件筛选(字典)
d = {"a": 1, "b": 2, "c": 3}

[x for x in d if x != "b"]              # ['a', 'c']  筛的是键
[k for k, v in d.items() if v > 1]      # ['b', 'c']  按值筛
{k: v for k, v in d.items() if v > 1}   # {'b': 2, 'c': 3}   'k: v'意思是组成一个新的字典，k是键，v是值

# 练习6.2 喜欢的数1
dictionary = {'Tom': 3, 'Jerry': 12, 'Jack': 53, 'Bob': 34, 'Mana': 0}
print(f'Tom like {dictionary["Tom"]}')
print(dictionary.values())  
print(dictionary.keys())
# dict_keys(...) 和 dict_values(...) 就是字典的键集合和值集合的视图，能遍历、能转列表，但不是列表本身。

# 练习6.3 词汇表1
词汇表 = {'if': '如果', 'in': '在', 'print': '打印', 'else': '否则', 'remove': '删除'}
print(f'if的含义是{词汇表["if"]}')
for k, v in 词汇表.items():   # 直接拿数据本身，没有符号
    print(f'{k}的含义是{v}')  # if的含义是如果

# 练习6.4 词汇表2
词汇表 = {'if': '如果', 'in': '在', 'print': '打印', 'else': '否则', 'remove': '删除', 'sorted': '排列', 'reverse': '倒序'}
for key, value in 词汇表.items():
    print(f'{key}的含义是{value}')

# 练习6.5 河流
dictionary = {'nile': 'egypt',
              'Yangtze River': 'China',
              'Thames River': 'Englan',
            }
for key, value in dictionary.items():
    if key.lower() == 'nile':
        print(f'The {key.title()} runs through {value.title()}.')
for key in dictionary.keys():    # 也可以不写key()
    print(key)
for value in dictionary.values():
    print(value)

# 练习6.6 调查
favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python', 
        }
names = ['JEN' , 'PHIL', 'TOM' , 'BOB']
for key, value in favorite_languages.items():
    name_lower = [name.lower() for name in names]     # 把名单做为列表小写后对比
    if key.lower() in name_lower:
        print(f'Welcome, {key}!')
    else:
        print(f'Where are you from? {key}!')

# 练习6.7 人们
people = [{
         'first_name': 'Li', 'last_name': 'Hua', 'age': '17', 'city': '888'},         
          {'first_name': 'Ma', 'last_name': 'na', 'age': '18', 'city': '111'},
        ]
for a in people:
    print(f'{a["first_name"].title()} {a["last_name"].title()} age is {a["age"]}, city is {a["city"]}.')

# 练习6.8 宠物
pets = [
        {'宠物': '狗', '主人': '李华'},
        {'宠物': '猫', '主人': '小明'},
        ]
for a in pets:
    print(f'宠物是{a["宠物"]}, 主人是{a["主人"]}')

# 练习6.9 喜欢的地方
favorite_place = {'Li Hua':['游乐园', '鬼屋', '摩天轮'],   # 键值对用逗号隔开
                  'Jerry': ['旋转木马', '海盗船'],
                  'Mana': '无',
                  }
for name, palce in favorite_place.items():
    for a in palce:
        print(f'{name}喜欢去{a}玩。')
for name, palce in favorite_place.items():
    print(f'{name}喜欢去{"、".join(palce)}。')

# 练习6.10 喜欢的数2
dictionary = {'Tom': [3,1], 'Jerry': [12,213,31], 'Jack': 53, 'Bob': 34, 'Mana': 0}
for name, numbers in dictionary.items():
    if isinstance(numbers,list):        # isinstance()函数判断numbers是不是列表类型
        print(f'{name} like {"、".join(map(str,numbers))}')
    else:
        print(f'{name} like {numbers}')
# map(str, numbers) 把列表里的数字全转成字符串，join 再用顿号拼起来。    
for name, numbers in dictionary.items():
    if isinstance(numbers, list):
        print(f"{name} like", *numbers, sep=" ")
    else:
        print(f"{name} like {numbers}")
# 用 * 解包，但去掉外面的括号（利用 print 的 sep）
# 这个方案把 *numbers 放在 print() 的参数里，而不是 f-string 的花括号里，print 会用空格隔开，不会加括号。

# 练习6.11 城市
cities = {'Bei Jing':{'国家': '中国','人口': '较多',},
          'Dong Jing': {'国家': '日本', '人口': '少',},
          'Niu Yue': {'国家': '美国', '人口': 222222}}
for city, message in cities.items():
    print(f'{city}位于{message["国家"]}, 人口是{message["人口"]}')

# 练习6.12 扩展
# 已完成扩展

# 2026.9.28
# 在input()章节，基本都要注释掉，不然影响下面学习的体验，但如果是做笔记，我会再写一个‘#’号
# 练习7.1: 汽车租凭
# car = input("What car do you want? ")
# print(f'Let me see if I can find you a {car}.')
# 练习7.2: 餐馆订位
# people = "How many people will in there?\n"
# people += "We have: "
# massage = input(people)
# massage = int(massage)
# if massage > 8:
#     print('没有空桌。')
# else:
#     print('有空桌。')
# 练习7.3: 10的整数倍
# number = input('判断一个数是不是10的整数倍，请输入一个数: ')
# if int(number) % 10 == 0:
#     print(f'{number}是10的整数倍。')
# else:
#     print(f'{number}不是10的整数倍。')

# 2026.9.28
# 循环章节和input()章节，基本都要注释掉，不然影响下面学习的体验，但如果是做笔记，我会再写一个‘#’号
# 练习7.4: 比萨配料
# 配料 = ""
# 总配料 = []
# massage = '请输入你想要的比萨配料: '
# massage += "(输入'quit'退出程序)\n"
# while 配料 != 'quit':    
#     配料 = input(massage)    
#     总配料.append(配料)    # 只有列表有append()方法，元组没有
#     if 配料 != 'quit':
#         print(f'你想要的配料是{配料}。')
#         print(f'你想要的配料总共有{len(总配料)}种。')
#         print(f'你想要的配料总共有{", ".join(总配料)}。')  # join()方法把列表里的元素用指定的符号拼接起来，返回一个字符串
# # 在python里面，f-string后的变量调用方法时，必须把方法也放进花括号里，否则会报错
# 练习7.5: 电影票
# age = ""    # 先搞一个空的age变量，下面while循环判断条件用，让input()输入的内容赋值给age变量，age变量就有值了
# message = "请输入你的年龄:(输入'quit'退出程序)\n输入:"  # 内容有单引号的时候，外层一定用双引号，反之亦然
# while age != 'quit':
#     age = input(message)   # message是提示信息，input()输入的内容赋值给age变量
#     if age != 'quit':
#         if int(age) < 3:   # int()把字符串变成整数，才能做比较
#             print('免费。')
#         elif 3 <= int(age) < 12:
#             print('10美元。')
#         else:
#             print('15美元。')
# 练习7.6: 三种出路
# 配料 = ""
# 总配料 = []
# massage = '请输入你想要的比萨配料: '
# massage += "(输入'quit'退出程序)\n"
# condition = True     # 设置一个条件变量，初始值为True,方便下面while循环判断条件用
# while condition:    
#     配料 = input(massage)    
#     总配料.append(配料)    # 只有列表有append()方法，元组没有
#     if 配料 != 'quit':           
#         print(f'你想要的配料是{配料}。')
#         print(f'你想要的配料总共有{len(总配料)}种。')
#         print(f'你想要的配料总共有{", ".join(总配料)}。')
#     else:
#         condition = False   # 当输入quit时，条件变量变为False,while循环就会结束
#         print('程序结束。')  # 到判断特定环境，让条件变量变为False,下面while循环判断条件就不成立，循环就会结束

# age = ""    # 先搞一个空的age变量，下面while循环判断条件用，让input()输入的内容赋值给age变量，age变量就有值了
# message = "请输入你的年龄:(输入'quit'退出程序)\n输入:"  # 内容有单引号的时候，外层一定用双引号，反之亦然
# while True:
#     age = input(message)   # message是提示信息，input()输入的内容赋值给age变量,input()放在while循环里面，就可以一直输入
#     if age == 'quit':
#         break
#     if int(age) < 3:   # int()把字符串变成整数，才能做比较
#         print('免费。')
#     elif 3 <= int(age) < 12:
#         print('10美元。')
#     else:
#         print('15美元。')
    
# age = ""    # 先搞一个空的age变量，下面while循环判断条件用，让input()输入的内容赋值给age变量，age变量就有值了
# message = "请输入你的年龄:(输入'quit'退出程序)\n输入:"  # 内容有单引号的时候，外层一定用双引号，反之亦然
# while True:   # 也可以写age != 'quit'，不过while已经把'quit'拦截了，下面的if age == 'quit'就不会执行了，所以while True更好
#     age = input(message)   # message是提示信息，input()输入的内容赋值给age变量
#     if age == 'quit':      # 判断放在input()后面，age变量就有值了，age变量就可以做判断了
#         break       # 为False就结束这一层级包括往后子层级不执行，为True就break，所以不管怎么样，它的子层级的代码都不会执行，直接跳出循环
#     if int(age) < 3:   # int()把字符串变成整数，才能做比较
#         print('免费。')
#     elif 3 <= int(age) < 12:
#         print('10美元。')
#     else:
#         print('15美元。')
# 练习7.7: 无限循环
# while True:
#     print('无限循环\n按Ctrl + C可以强制退出程序')
# 2026.10.3
# 练习7.8: 熟食店
sandwich_orders = ['pastrami', 'beef', 'chicken', 'pastrami', 'pork', 'pastrami']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f'I made your {sandwich} sandwich.')
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()   # pop()方法默认删除列表最后一个元素，并返回这个元素
    finished_sandwiches.append(finished_sandwich)   # append()方法把这个元素添加到另一个列表中
print(f'We have made the following sandwiches: {", ".join(finished_sandwiches)}.')
for sandwich in finished_sandwiches:
    print(f'We have made the following sandwiches: {sandwich}.')
# 练习7.9: 五香烟熏牛肉卖完了
sandwich_orders = ['pastrami', 'beef', 'chicken', 'pastrami', 'pork', 'pastrami']
print('Sorry, we have run out of pastrami.')
while 'pastrami' in sandwich_orders:   # 判断列表中是否有指定元素
    sandwich_orders.remove('pastrami')   # remove()方法删除列表中指定元素
print(sandwich_orders)
# # 练习7.10: 梦想中的度假胜地
# key_values = {}  # 初始化一个空字典，用来存储“名字: 地点”的数据

# while True:  # 【大循环】：负责不断让新朋友输入信息，直到用户选 No 或输入 quit
    
#     # 1. 输入名字
#     names = input('请输入名字:(输入"quit"退出程序)\n输入:')
#     if names == 'quit':
#         break  # 如果输入 quit，直接打破大循环，结束整个程序
        
#     # 2. 输入地点
#     places = input('如果你可以去任何地方度假，你想去哪里？:(输入"quit"退出程序)\n输入:')
#     if places == 'quit':
#         break  # 如果输入 quit，直接打破大循环，结束整个程序
    
#     # 3. 存入字典（关键点！）
#     # 你的直觉非常准：必须在问“是否继续”之前存字典。
#     # 因为如果放在后面，用户选 No 触发了 break，代码就直接跳过这句，数据就丢失了！
#     key_values[names] = places  

#     # 4. 小循环：专门负责“卡住”用户，直到输入合法的 Yes 或 No
#     is_continue = False  # 标记变量：默认不继续（即准备结束程序）
#     while True:  # 【小循环】
#         friends = input("你还有朋友想要参与调查吗？:('Yes'或'No')\n输入:")  
#         # 注：你的注释很棒，只要里面有单引号，外面就必须用双引号，反之亦然
        
#         if friends == 'Yes':
#             is_continue = True  # 用户表示还要继续，把标记设为 True
#             break               # 打破小循环
#         elif friends == 'No':
#             is_continue = False # 用户表示不继续了，标记保持 False
#             break               # 打破小循环
#         else:
#             # 如果输入了其它东西，不 break，不 continue，
#             # 循环会自动回到内层 while True 的开头，重新问这个问题！
#             print('输入错误，请重新输入。')

#     # 5. 小循环结束后，利用刚才的标记，决定大循环的命运
#     if not is_continue:  # 如果 is_continue 是 False（用户选了 No）
#         break  # 打破大循环，整个输入环节结束
    
#     # 如果用户选了 Yes (is_continue 是 True)，
#     # 代码会什么都不做，自然走到大循环末尾，自动回到第一行，开始问下一个人的名字！

# # 6. 打印最终结果
# for name, place in key_values.items():
#     # .title() 会把每个单词的首字母变成大写，比如 "beijing" 变成 "Beijing"
#     print(f'{name.title()}想去{place.title()}度假。')
# # break 只会彻底终结它当前所在的“当下层级”的循环，它在寻找目标时会无视所有 if 等非循环缩进，
# # 顺着缩进往上找遇到的第一个 while 或 for 就是它唯一的击杀目标，它绝不越级打破外层循环（外层若想结束必须在其内部再写一个 break），
# # 并且打破内层后代码只是跳出内层，依然会留在外层循环体内继续往下执行或自然回滚到外层开头，绝不等于 continue 的仅跳过本次循环。
# # 主要看它到底在哪层循环里面，也要注意看它到底跳出了哪层循环，它在不在那层循环里面.

# 练习8.1: 消息
def display_message():
    """显示学习的内容"""
    print('I learn functions in this chapter.')
display_message()
# 练习8.2: 喜欢的书
def favorite_book(title):
    '''显示喜欢的书籍'''
    print(f'One of my favorite books is {title}.')
favorite_book('Alice in Wonderland')  # 调用函数时，实参是字符串，必须加引号

# 2026.10.5
# 练习8.3: T恤
def make_shirt(size, text):
    print(f'The size of the T-shirt is {size}, and the text on it is "{text}".')
make_shirt('L', 'I love Python')  # 调用函数时，实参是字符串，必须加引号
make_shirt(text='I love Python', size='L')  # 调用函数时，实参是字符串，必须加引号
# Python变量无需声明、赋值即创建、动态类型、可重新绑定，命名须以字母或下划线开头后接字母/数字/下划线，区分大小写且不能用关键字。
# 练习8.4: 大号T恤
make_shirt('M', 'I love Python')  # 调用函数时，实参是字符串，必须加引号
make_shirt(text=10086, size='5XL')  # 调用函数时，实参是数字，不需要加引号
# 练习8.5: 城市
def describe_city(city, country='China'):
    print(f'{city.title()} is in {country.title()}.')
describe_city('beijing')
describe_city('changsha')
describe_city('tokyo', 'japan')

# 2026.10.6
# 练习8.6: 城市名
def city_country(city, country):
    message = f'"{city.title()}, {country.title()}"'  # f放在最前面，且与后面不能又空格
    return message
print(city_country('santiago', 'chile'))
# 练习8.7: 专辑
def make_album(name1, name2, age=None):
    dictionary = {'歌手': name1.title(), '专辑': name2.title()}
    if age:
        dictionary['age'] = age
    return dictionary
a = make_album('mana', 'fase', 18)
print(a)
# 练习8.8: 用户的专辑
# def make_album(name1, name2, age=None):
#     dictionary = {'歌手': name1.title(), '专辑': name2.title()}
#     if age:
#         dictionary['age'] = age
#     return dictionary
# while True:
#     name1_ = input('歌手是谁？\t"q"退出\n')
#     if name1_ == 'q':
#         break
#     name2_ = input('专辑是什么？\t"q"退出\n')
#     if name2_ == 'q':
#         break
#     age = input('年龄？\t"q"退出\n')
#     if age == 'q':
#         break
#     a = make_album(name1_, name2_, age)
#     print(a)
##  函数能不能引用某个变量，看的是“这个变量在函数被调用的时候，是不是已经存在了”，而不是“它在函数的上面还是下面”。

# 2026.10.7
# 练习8.9: 消息
def show_messages(x):
    for message in x:
        print(message)
messages = ['fhsdakj', 'fhaksj', 'dffs', 'vhsd']
show_messages(messages)
# 练习8.10: 发送消息
def show_messages(x):
    for message in x:
        print(message)                   # 看原列表
        sent_messages.append(message)   # 把里面的元素一个个追加，且不改变原来的列表
def send_messages(lists):
    print(lists)
    print(messages)
    if lists == messages:           # 因为是一个个追加，不改变顺序，直接可以做判断对比，不要用reverse()，这个直接原地改变，返回空
        print('消息正确')
sent_messages = []
show_messages(messages)
send_messages(sent_messages)
# 练习 8.10
def show_messages(messages):
    """打印所有消息"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """打印消息，并把它移到 sent_messages"""
    while messages:
        current = messages.pop()
        print(f"发送：{current}")
        sent_messages.append(current)

# 先准备数据
messages = ['fhsdakj', 'fhaksj', 'dffs', 'vhsd']
sent_messages = []

# 调用
send_messages(messages, sent_messages)   # 搬走消息
show_messages(sent_messages)             # 看搬走的结果

print("原列表：", messages)               # 空了
print("新列表：", sent_messages)          # 有内容

# 练习8.11: 消息归档
def show_messages(messages):
    for message in messages:
        print(message)
def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop()        # 因为是pop()下面作比较要用reverse()反转
        print(f"发送：{current}")
        sent_messages.append(current)
# 先准备数据
messages = ['fhsdakj', 'fhaksj', 'dffs', 'vhsd']
sent_messages = []

# 调用
send_messages(messages[:], sent_messages)   # 搬走消息，用副本
show_messages(messages)                  # 看原来的
show_messages(sent_messages)             # 看搬走的结果

print("原列表：", messages)               # 不变
print("新列表：", sent_messages)          # 有内容
sent_messages.reverse()               # 返回空，原地改变列表
if sent_messages == messages:
    print('无误')

# 2026.10.8
# 练习8.12: 三明治
def foods(*food):
    for food_ in food:
        print(f"You want to {food_}?")
foods('pizza')        
foods('pizza', 'egg')
foods('pizza', 'egg', 'hotdog')
# 解包符*
def foods(*food):
    print(f"You want to :",*food, sep=',')  # 不用中间逗号，Python会认为字符串相乘，可以用join()
foods('pizza')        
foods('pizza', 'egg')
foods('pizza', 'egg', 'hotdog')
# join()
def foods(*food):
    print(f"You want to {','.join(food)}")
foods('pizza')        
foods('pizza', 'egg')
foods('pizza', 'egg', 'hotdog')

# 练习8.13: 用户简介
def build_profile(first, last, **user_info):   # **user_info，是搞一个字典定义里面字典名就是它
    """创建一个字典，其中包含我们知道的有关用户的一切"""
# 给实参当一个数据就行了，他能在函数定义里面干很多事
    user_info['first_name'] = first.title()    # 这是新增字典，所以键值在后面
    user_info['last_name'] = last.title()      # 这是新增字典，所以键值在后面
    return user_info     # 把字典返回出去接住
user_profile = build_profile('ma', 'na',
                            location='earth',
                            field='cn')
print(user_profile)
# 字符串方法，只要对象是字符串，随时随地都能调。但换成数字、列表、字典、视图对象，就没这些方法了——方法“长在类型身上”。

# 练习8.14: 汽车
def make_car(name, modle, **others):
    others['name'.title()] = name.title()
    others['modle'] = modle.title()
    return others
car = make_car('subaru', 'outback', color='blue', tow_package=True)  # True是布尔值，不用加引号
print(car)

# 2026.10.8
# 练习8.15: 打印模型
import printing_functions as o
b = []           # 这些变量注意写在调用函数上面
a = ['fdf', 'fds', 'gd']
o.print_(a, b)          # 相当于把模块整个代码引用过来，再在下面调用
o.show_(b)
# 练习8.16: 导入
import pizza
from pizza import make_pizza
from printing_functions import *
import pizza as e
#  from printing_functions import * as p     <--报错* 是通配符，代表“所有名字”，它不是一个具体的名字，所以没法给它起别名。
# as 只能给“具体的名字”改名
from  printing_functions import print_ as p
# 练习8.17: 函数编写指南
pass  # (略)














