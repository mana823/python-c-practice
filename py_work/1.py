# name = 'ada lovelace'
from dataclasses import field
from importlib.resources import contents
import pathlib


name = 'ada lovelace'
print(name.title())  # .title() 是把首字母换成大写
print(name.upper())  # .upper() 全大写 .lower()全小写

x = "你好"
y = "世界"
a = "你好" "世界"   # ✅ 可以，自动拼接
# b = x y             # ❌ 报错！变量必须用加号
c = x + y           # ✅ 正确

print('\t你好')     # \t制表符
print('你好，\n大家好。')  # \n换行符
# 这些符号可以一起用
变量 = '"你好" '   # 加了空格
print(变量.rstrip())  # 在终端赋值最直观   # strip的英文意思是剥去
# .rstrip()去掉输入内容多余的空格，只删除字符串右边的空格   .lstrip()删左边   .strip()都删

# 删除前缀   .remove()不会改变原来的字符串，字符串不可直接改变，只能用变量接住
url = 'https://douyin.com'
urldemo = url.removeprefix('https://')  # .removeprefix()删除前缀  prefix前缀  suffix后缀 想全部检索用replace
print(urldemo)
urldemo2 = url.removesuffix('douyin.com')
print(urldemo2)

# 加+  减-  乘*  除/  指数(乘方)**    空格不影响运算顺序
# 带小数点的称为浮点数
# 任意两个数相除，结果总是浮点数，其他运算时，如果含浮点数结果也是浮点数
# 下划线'_'可以将数字隔断，便于观看，不过没什么实际用处，打印出来都一样
# 同时给多个数赋值  x, y, z = 0 ,0 ,0    将变量全部初始化  可以当作容器使用
# '常量'是整个周期不变的变量，python里没有内置常量，一般用全大写表示 

# []是列表，可以修改添加内容，用逗号隔开。
car = ['发动机', '方向盘', '反光镜']
print(car)
# 访问列表元素
print(car[0])            # 打印只返回元素，不包含方括号
print(car[0].title())    # .title这种功能接在后面
# 索引是从0开始而不是1
# -1可以返回最后一个元素,以此类推
print(car[-1])
# 使用列表的各个直
message = f'My first car was a {car[0]}.'
print(message)

# 修改列表
列表 = ['a', 'b', 'c']
列表[0] = 'a1'
print(列表)

# 添加元素  使用append()元素追加到列表末尾
列表.append('d')
print(列表)
# 也可以先创建一个空表，再去添加
空表 = []
空表.append('a')
空表.append('b')
空表.append('c')
print(空表)                        # extend的中文意思是扩展，返回None，但是直接修改原对象
# 注意，append只能一次性追加一个元素，，返回None，但是直接修改原对象。而extend()可以追加多个，追加的多个元素也要用'[]'括起来
空表.extend(['d', 'e', 'f', 'g'])
print(空表)
# 也可以拼接
lst = [1, 2, 3]
lst = lst + [4, 5, 6]   # 不修改原列表，返回新列表
print(lst)

# 插入元素  用insert()可在任意位置插入元素，因此需要指定新元素的索引和值
列表 = ['a', 'b', 'c']   # insert意思是插入，返回None，但是直接修改原对象
列表.insert(0, 'a1')   # 指在'索引0'处添加'a1'，也就是说直接占领这个贷方
print(列表)

# 删除元素 用del语句删除元素
del 列表[0]     # [0]代表索引
print(列表)
# 使用pop()方式删除末尾元素并保留元素到非列表  
列表 = ['a', 'b', 'c']
poped_列表 = 列表.pop()   # 'poped_列表'是用来保留末尾元素的
print(poped_列表)
print(列表)              # '列表.pop()'就已经是返回修改内容了，不是返回None，pop()会直接修改内容到原对象
# pop也可以删除列表任意位置的元素，只需要在括号指定索引
列表 = ['a', 'b', 'c']
first_owned = 列表.pop(0)   # 注意是小括号
print(first_owned)
print(列表)
# 根据值删除元素用remove()
列表 = ['a', 'b', 'c']
列表.remove('b')         # remove返回None，但是直接修改原对象
print(列表)

# 管理列表
# 1.使用sort()对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()    # 按英文字母顺序排列，修改表，返回None    'sort'的中文意思是排序
print(cars)
cars.sort(reverse=True)  # reverse=True  按英文字母逆序排列  'reverse'中文意思是反转，默认是reverse=False
print(cars)
# 2.使用sorted()临时排序        # sorted()是一个函数
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))      # 只是临时改变，也就是不改变原表   
print(sorted(cars, reverse=True))
# 3.用reverse()反向打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()           # .reverse()反转直接改变列表
print(cars)
# 4.用len()确定列表长度…………len()为函数
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:   # 将magicians里面的数据一条条装进magician里面
    print(magician)
    print(f'{magician.title()},that was a great trick')  # 先执行一条往下，直到所有程序执行完毕，再循环
# for循环后面没有缩进的程序只执行一次
    print(f"I can't wait to see your next trick, {magician.title()}.\n" )
print('Thank you, everyone')

# 使用range()函数
for value in range(1, 5):   # 打印数字1到4，不会打印5  从第一个数开始，第二个数停止
    print(value)
# 使用range()创建数值列表
# 使用list()函数将range()的结果直接转换为列表,将range()作为list()的参数
numbers = list(range(1,6))   # list()函数转换列表
print(numbers)
# range()还可以指定第三个参数
even_numbers = list(range(1,19,2))   # 第三个参数代表从第一个数开始加那个参数的值，知道第二个参数为止
print(even_numbers)
squares = []    # 拿个盒子去装才能全部列出来，不然要么分散列出来，要么就是只采集到最后一个
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
# 简介写法去掉变量square
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# 对数列进行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(len(digits))
print(sum(digits))
# python内置没有mean()或average()
mean = sum(digits) / len(digits)
print(mean)

# 列表推导式，合并与创建      立方推导式外层看情况加括号 ，列表[]，生成器()，集合字典{}
squares = [value**2 for value in range(1,11)]  # 每次循环先确定value，再执行前面的判别式
print(squares)

# 使用列表的一部分
# 切片   使用方括号[]  
names = ['Tom', 'Bob', 'jack', 'Lisa']
print(names[0:3])
print(names[:4])    # 若没指定第一个索引，将从第一个元素开始
print(names[2:])    # 若没指定第二个，将从第一个索引开始，到最后结束
print(names[-2:])   # 同理
print(names[0:4:2])   # 第三个参数告诉会让Python在这个范围内每隔这个值取一个数
# 遍历切片
names = ['Tom', 'Bob', 'jack', 'Lisa', 'Li Hua']
print('There have my many friends:')
for name in names[2:]:   # 跟在列表后面
    print(name)
# 复制列表
names = ['Tom', 'Bob', 'jack', 'Lisa', 'Li Hua']
friends = names[:]   # 不能直接friends = names,这叫赋值
print(friends)
names.append('Bedy')
friends.append('Tim')
print(names)
print(friends)

# 元组，是不可修改的(tuple) 使用圆括号('注意：元组严格来说是由逗号标识的，圆括号只是看起来更整洁')
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 遍历整个元组
for dimension in dimensions:
    print(dimension)
# 修改元组变量(赋值)
dimensions = (200, 50)
print(dimensions)
dimensions = (111, 22)
print(dimensions)

# 缩进Tab制表符
# 行长
# 空行

# if 语句
cars = ['audi', 'bmw', 'subaru', 'toyata']
for car in cars:
    if car == 'bmw':   # 如果
        print(car.upper())
    else:    # 否则
        print(car.title())    
# if语句核心是值为False & True 的表达式，被称为条件测试
# 检查是否相等
car = 'bmw'
print(car == 'bmw')   # 返回True
print(car == 'audi')  # 返回False

# 忽略大小写
car = 'audi'
print(car == 'Audi')  # 返回False
print(car.title() == 'Audi')  # 返回True
# title(),lower(),upper()都不改变原来的变量

# 检查是否不等…………不等符'!='
requested_topping = 'mushrooms'
if requested_topping != 'anchovies!':
    print('Hold the anchovies')
# 数值比较
age = 18
print(age == 18)
answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')

# 用and & or检查多个条件 (and需要满足所有条件而or只要满足1个条件就行了，也就是返回'True')
age_0 = 22
age_1 = 18
condition = age_0 >= 21 and age_1 >= 21
print(condition)
age_1 = 22
condition = age_0 >= 21 and age_1 >= 21
print(condition)
# 也可以加括号'(age_0 >= 21) and (age_1 >= 21)'

# 用or检查多个条件
age_0 = 22
age_1 = 18
condition = age_0 >= 21 or age_1 >= 21
print(condition)
age_0 = 18
age_1 = 18
condition = age_0 >= 21 or age_1 >= 21
print(condition)

# 用'in'检查特定的值是否在列表里
requested_toppings = ['mushrooms', 'onions', 'pineapple']
condition = 'mushrooms' in requested_toppings
print(condition)  # True
condition = 'pepperoni' in requested_toppings
print(condition)  # False

# 用'not in'检查特定的值是否不在列表里
banned_user = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_user:
    print(f'{user.title()}, you can post a response if you wish.')

# if语句
# 1.简单if语句(一个条件测试和一个操作)
# if conditional_test:     # 一个条件测试
#     do something         # 一个操作(如果为True，执行操作，如果为False，则忽略)
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?') # 这两个操作如果条件测试为Flase，则两个都忽略

# if-else语句(指定未通过时的指令)(总会执行其中一个)
age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:     # 如果为False执行以下指令
    print('Sorry, you are too young in vote.')
    print('Please register to vote as soon as you turn 18!')

# if-elif-else语句(依次检查每个条件测试)(依次检查，直到遇到True，执行对应指令，剩下全部跳过)
age = 12
if age < 4:
    print('Your admission cost 0$.')
elif age < 18:    # elif后面也要加条件
    print('Your admission cost 25$.')
else:             # else后面不加条件，放到最后与一切条件相反
    print('Your admiddion cost 40$.')    
# 简写(不打印门票，只说明价格)
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f'Your admiddion cost {price}$.')    

# 使用多个elif代码块(同组里面，if必须开头，else可以写，要写就写结尾，elif可在中间多次出现) <--一定是同组里面
age = 88
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'Your admiddion cost {price}$.')    

# 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f'Your admiddion cost {price}$.')    

# 测试多个条件(使用多个if)
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinished making your pizza!')
# 为什么不能用if-elif-else语句？(如要测试多个条件并执行相关命令，这个语句导致后面内容被跳过)
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:   # 条件通过，下面的条件检测直接跳过
    print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinished making your pizza!')

# 使用if语句处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':  # 如果处理一个元素，优先将它作为条件测试
        print('Sorry we are out of green prpprts right now.')
    else:
        print(f'Adding {requested_topping}.')
print('\nFinished making your pizza!')

# 确定列表非空,要先确定列表非空再执行相应操作
requested_toppings = []
if requested_toppings:   # 用if判断列表是否非空，(空'列表、元组、字典'、单双引号空字符串、数值0、空值None)在布尔上下文被视为False
    for requested_topping in requested_toppings:
        print(f'Adding{requested_topping}')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperone', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:      # for in 循环逐个打印元素，每个元素都会去判断
    if requested_topping in available_toppings:   # 有if-elif可能不执行，只要有else,必定执行一条命令
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry, we don't have {requested_topping}")    
print('\nFinished making your pizza!')

# 字典(dictionary)
alien_0 = {'color': 'green', 'points': 5}   # 存储了
print(alien_0['color'])        # 找到拿出来
print(alien_0['points'])

# 在python中，字典(dictionary)是一系列键值对(key-value pair)，键与值相关联，
# 可将任意python对象作为字典的值(数、字符串、列表、字典…………)
# 字典用放在花括号的一系列键值对表示
alien_0 = {'color': 'green', 'points':5}  # 键值对包含两个相互关联的值，键与值用冒号(:)隔开，键值对用逗号(,)隔开
# alien_0 = {'color': 'green', 'points':5}    'color'是键，'green'是值

# 访问字典里面的值
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0['color'])  # 指定字典名，并把键放在后面方括号里面

new_points = alien_0['points']   # 获取值并赋予变量
print(f'You just earned {new_points} points!')

# 添加键值对 
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0)

alien_0['x_position'] = 0      # 依次指定字典名、用方括号括起来的键和与该键的关联值
alien_0['y_position'] = 25
print(alien_0)                 # 字典排列数序与添加顺序相同

# 从创建一个空字典开始
alien_0 = {}   # 创建一个空字典，常用于(存储、编写能自动生成大量键值对的代码)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# 修改字典中的值(依次指定字典名、用方括号括起来的键和该键关联的新值)
alien_0['color'] = 'green'
print(f'The alien is now {alien_0["color"]}')

alien_0['color'] = 'yellow'      # 依次指定字典名、用方括号括起来的键和该键关联的新值
print(f'The alien is now {alien_0["color"]}')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position: {alien_0["x_position"]}')
# 向右移动外星人(根据速度去判断移多远)
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment  # 键始终是x_position， 主要改值

print(f'New position: {alien_0["x_position"]}')
# 这样我们修改字典里面的值就可以对应最后位置

# 删除键值对(用del语句删除，必须指定字典名和要删除的键)  注意：删除的键值永远消失
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)

del alien_0['points']    # 指定字典名和要删除的键
print(alien_0)

# 由类似的对象组成的字典
favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python',    # 在最后一个键值对也打上逗号，这样为以后添加键值对做好准备
        }      # 先打完花括号后回车，再缩进，写完一组键值对之后打逗号再回车；本编辑器自动缩进后续键值对，且缩进量与第一个相同。

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite languages is {language}")

# 使用get()来访问值
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) <--  KeyError: 'points'   可使用get()指定键不存在时返回一个默认值
point_value = alien_0.get('points', 'No point value assigned')  # 两个参数，一个key,一个没找到信息(默认返回None)
print(point_value)

# 遍历字典
# 用items()遍历所有键值对
# 视图对象不是列表，不能用列表的方法调用它,且转换列表"list()"后就与字典无关了，字典改变他不会变，不转变就与字典油管
user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
        }
for key, value in user_0.items():   # .items()返回一个字典视图对象(sict_items)包含键值对(元组形式)
    print(f'\nKey: {key}')
    print(f'Value: {value}')

favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python', 
        }
for name , language in favorite_languages.items():
    print(f'{name.title()} favorite language is {language}')
# 用key()方法遍历字典的所有键
favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python', 
        }
for name in favorite_languages.keys():
    print(name.title())
# 在遍历字典时会默认遍历键，所以以下代码等同于上面代码
for name in favorite_languages:     # 不加key()也一样，默认遍历键
    print(name.title())

favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python', 
        }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'Hi {name}')
    if name in friends:
        language = favorite_languages[name]
        print(f'\t{name.title()}, I see you love {language}!')
if 'erin' not in favorite_languages.keys():  # key()方法并非只能遍历，它会返回一个视图对象(dict_keys)
    print('Erin ,please take our poll!')

# 按特定顺序遍历字典中的所有键   sorted()函数
favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python', 
        }
for name in sorted(favorite_languages.keys()):    # 用sorted()，永远输出列表，只看能不能比较
    print(f'{name.title()}, thank you for taking the poll.')
print(sorted(favorite_languages.keys()))   # 返回列表

# 遍历字典里面的所有值
favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python', 
        }
print('The following languages have been mentioned:')
for language in favorite_languages.values():    # values()返回视图对象(dict_values)
    print(language.title())      # 这种方法不考虑重复可以使用集合(set)
# 通过将包含重复的列表传入set()      set()返回集合用的是花括号,不过不是字典的意思
favorite_languages = {
        'jen': 'python',
        'sarah' :'c',
        'edward': 'rusr',
        'phil': 'python', 
        }
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())

# 2026.9.24
# 嵌套:有时候，需要将多个字典存储在列表中或将列表作为值存储在字典中，称为嵌套。
# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:     # 把字典从列表取出来赋给alien
    print(alien)

# 创建一个装外星人的空列表 
aliens = []
# 创建30个绿色外星人
for alien_number in range(30):    # 告诉python循环多少次，alien_number变量直接丢掉
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)   # 每一次都是一个新的字典给aliens列表，不过键值一样
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
# 显示创建了多少外星人
print(f'Total number of aliens: {len(aliens)}')

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:4]:
    if alien['color'] == 'green':   # '=='是比较
        alien['color'] = 'yellow'   # '='是赋值
        alien['points'] = 10
        alien['speed'] = 'medium'
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')

# 用if-elif来通过颜色判断来改变外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'   
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'   
        alien['points'] = 15
        alien['speed'] = 'fast'

# 在字典中储存列表(当一个键关联到多个值时)
# 储存客人的比萨饼信息
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],
         }
print(pizza['toppings'])   # 可以将列表打印出来
# 概述客人点的比萨
print(f'You ordered a {pizza["crust"]}-crusht pizza '  # <--这里拼接了
      'with the following toppings:')
for topping in pizza['toppings']:
    print(f'\t{topping}')

favorite_languages = {
        'jen': ['python', 'rust'],
        'sarah': ['c'],
        'edward': ['rust', 'go'],
        'phil': ['python', 'haskell'],
        }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}' favorite languages are:")
    for language in languages:      # 下一层级会跟着循环
        print(f'\t{language.title()}')

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}' favorite languages are:")
    print(*languages, sep='\n')    # *languages把里面的每个元素拆包成独立参数,sep='\n'每个参数用换行符隔开

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}' favorite languages are:")
# 'join'用分隔符把一堆字符串粘成一个大字符串，'join'前必须写引号，里面的符号可加可不加，只能用于元素全是字符串的可迭代对象
    print('\t' + '\n\t'.join(languages))   
# '\t' + '\n\t'.join(languages)  让格式变为前面空格且换行

# 在字典中储存字典(较复杂)
users = {'aeinstein':{
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
        },

        'mcurie':{
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
        }

}

for username, user_info in users.items():    # 对字典循环是一个键值对一个键值对循环,其中user_info拿到字典
    print(username, user_info)   # 这里的","是分隔参数,其中空格是默认sep=' '
    print(f'\nUsername: {username}')
    full_name = f'{user_info["first"]} {user_info["last"]}'    # 相当于查找user_info字典里面的值
    location = user_info['location']

    print(f'\tFull name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')

# · 列表套字典 = 排队点名（关注一条条记录），键统一，按键批量筛选查找，因为外层是字典，所以遍历的是字典，只要一个变量去取
# · 字典套字典 = 按号找人（关注精确匹配），键不统一，精准查找键里面的键值对，其中里面的键可能统一
# · 字典套列表 = 按类分堆（关注分类汇总），将值集中


# 在input()章节，基本都要注释掉，不然影响下面学习的体验，但如果是做笔记，我会再写一个‘#’号
# 2026.9.26
# input()函数的工作原理（让程序暂停运行，等待用户输入一些文本。输入完毕后，其值赋给变量）
# message = input('Tell me something, and I will repeat it back to you: ')     # 先打印，再让input输入
# print(message)     # 先注释掉，不然后面每次都要输入

# 2026.9.28
# 编写清晰的提示
# name = input('Please enter your name: ')    # 在末尾空格将提示和用户输入区分开
# print(f'\nHello, {name}!')

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"    # '+='是追加，追加在后面，这样子，提示词过长可以这样分开写
# name = input(prompt)     # 你输入的内容，会在终端紧跟着句子后面，prompt只是变量，实际还是先打印再在最后输入
# print(f"\nHello, {name}")

# 使用int()来获取数值输入，（在使用；input()函数时，Python会将用户输入解读为字符串
# 以下为模拟终端
# >>> age = input()  
# 21     # 输入21
# >>> age
# '21'   # 显示'21'  是字符串
# >>> age >= 18   # 报错 # 这样如果打印的话没问题，但如果是将其作为数来使用就会引发错误
# >>> age = int(age)    # 转为整数
# >>> age >= 18         # 再做比较，顺序不能反
# True

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# 求模运算符(%)将两数相除返回余数
# 以下模拟终端
# >>> 4 % 3
# 1            # 返回余数
# >>> 6 % 3
# 0            # 0也能被返回

# 利用这个特性检验奇数偶数
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f'\nThe number {number} is even.')
# else:
#     print(f'\nThe number {number} is odd.')


# #  2026.9.28
# 循环章节和input()章节，基本都要注释掉，不然影响下面学习的体验，但如果是做笔记，我会再写一个‘#’号
# while循环简介(不断运行，直到指定的条件不再满足为止)
# current_number = 1
# while current_number <=5:    # 只要current_number <=5,就一直循环
#     print(current_number)
#     current_number += 1
# # 用户选择何时退出
# prompt = "\nTell me something, and I will repeat it bavd to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""  # 这里必须写，给while提供可检查对象
# while message.lower() != 'quit':
#     message = input(prompt)    # 这里已经把prompt带入循环里面了，因为要先打印，再输入
#   # print(message)             # input只返回用户输入的信息给变量
#     if message != 'quit':      # 这里做一个判断，就不会把quit打印出来
#         print(message)

# # 使用标志(flag)在while循环中管理程序状态,标志为True时，程序继续运行，为False时，程序停止运行
# prompt = "\nTell me something, and I will repeat it bavd to you:"
# prompt += "\nEnter 'quit' to end the program."
# active = True   # 先让active为True，while循环就会一直运行
# while active:
#     message = input(prompt)
#     if message == 'quit':   # 给出条件,为下面的active = False提供条件
#         active = False      # 这样可以让while循环停止运行，同时也可以在if语句中使用break语句直接退出循环
#     else:
#         print(message)      # 不输入'quit'，就会打印输入的内容

# # 使用break退出循环
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:       # 这里的True是一个条件测试，永远为True，所以while循环会一直运行，直到遇到break语句
#     city = input(prompt)
#     if city == 'quit':
#         break     # 使用break语句直接退出循环
#     else:
#         print(f"I'd love to go to {city.title()}!")
# # 在python中，break语句用于控制循环语句的执行。它可以用来提前退出循环，无论循环条件是否仍然为真。

# 在循环中使用continue(跳过本次循环剩余的代码，直接进入下一次循环判断)
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:   # 如果是偶数
        continue                  # 跳过本次循环剩余的代码，直接进入下一次循环判断
    print(current_number)         # 只打印奇数
# 避免无限循环
# x = 1
# while x <= 5:
#     print(x)   # 只要x <= 5,就一直循环，所以就一直打印，这是个例子，应该避免，我们给他注释掉，避免影响下面代码
# 按Ctrl + C可以强制退出程序


# 2026.10.3
# 使用while循环来处理列表和字典
# 在列表之间移动数据

# 首先创建一个待验证的用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']   # 待验证的用户列表
confirmed_users = []   # 已验证的用户列表

# 验证每个用户，直到没有未验证的用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:   # 只要unconfirmed_users列表非空，就一直循环
    current_user = unconfirmed_users.pop()   # pop()方法删除列表末尾的元素，并返回该元素的值
    print(f'Verifying user: {current_user.title()}')   # 打印验证信息
    confirmed_users.append(current_user)   # 将已验证的用户添加到已验证用户列表中
# 显示所有已验证的用户
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:   # 遍历已验证用户列表
    print(confirmed_user.title())   # 打印已验证用户的名字
print(f'The following users have been confirmed: {", ".join(confirmed_users).title()}.')   # 打印已验证用户的名字，使用join()方法将列表转换为字符串，并用逗号分隔
# 这里title()必须放在join()后面，因为join()返回的是一个字符串，title()方法只能用于字符串

# 删除为特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:   # 只要列表中还有'cat'，就一直循环
    pets.remove('cat')   # remove()方法删除列表中第一个出现的指定值
print(pets)   # 打印删除后的列表

# # 使用用户输入来填充字典
# responses = {}   # 创建一个空字典，用于存储用户的回答
# polling_active = True   # 设置一个标志，用于控制循环
# while polling_active:   # 只要polling_active为True，就一直循环
#     name = input('\nWhat is your name? ')   # 获取用户的名字
#     response = input('Which mountain would you like to climb someday? ')   # 获取用户的回答
#     responses[name] = response   # 将用户的名字和回答存储到字典中
#     repeat = input('Would you like to let another person respond? (yes/no) ')   # 询问是否有其他人要回答
#     if repeat == 'no':   # 如果没有其他人要回答，就将polling_active设置为False，退出循环
#         polling_active = False
# # 显示调查结果
# print('\n--- Poll Results ---')
# for name, response in responses.items():
#     print(f"{name}: {response}")


# 2026.10.4
# 函数的定义和调用
# 定义函数
def greet_user():   # 定义一个函数，函数名为greet_user，括号内为空，表示没有参数，以冒号收尾
    """显示简单的问候语"""   # 文档字符串(docstring)的注释，描述函数的功能，缩进三个引号括起来，放在函数定义的下一行
    print("Hello!")   # 打印问候语
# 调用函数
greet_user()

# 向函数传递信息
def greet_user(username):   # 定义一个函数，函数名为greet_user，括号内有一个参数username，以冒号收尾
    """显示简单的问候语"""   # 文档字符串(docstring)的注释，描述函数的功能，缩进三个引号括起来，放在函数定义的下一行
    print(f"Hello, {username.title()}!")   # 打印问候语，使用f-string格式化字符串，将username变量的值插入到字符串中，并将其首字母大写

greet_user('jesse')   # 调用函数，传递一个实参'jesse'给参数username，这种没有默认值的参数称为必备参数(positional argument)，调用函数时必须传递实参，否则会报错

# 实参和形参
# 形参(parameter)是函数定义中括号内的变量名，用于接收调用函数时传递的实参(argument)，实参是调用函数时传递给形参的值
def describe_pet(animal_type, pet_name):   # 定义一个函数，函数名为describe_pet，括号内有两个参数animal_type和pet_name，以冒号收尾
    """显示宠物的信息"""   # 文档字符串(docstring)的注释，描述函数的功能，缩进三个引号括起来，放在函数定义的下一行
    print(f"\nI have a {animal_type}.")   # 打印宠物类型，使用f-string格式化字符串，将animal_type变量的值插入到字符串中
    print(f"My {animal_type}'s name is {pet_name.title()}.")   # 打印宠物名字，使用f-string格式化字符串，将pet_name变量的值插入到字符串中，并将其首字母大写 
describe_pet('dog', 'da huang')   # 要输入两个实参

# 传递实参
# 位置实参(positional argument)是按顺序传递给函数的实参，调用函数时必须按照形参的顺序传递实参，否则会报错
# 关键字实参(keyword argument)是通过指定形参的名称来传递给函数的实参，调用函数时可以不按照形参的顺序传递实参

# 位置实参
def describe_pet(animal_type, pet_name):   # 定义一个函数，函数名为describe_pet，括号内有两个参数animal_type和pet_name，以冒号收尾
    """显示宠物的信息"""   # 文档字符串(docstring)的注释，描述函数的功能，缩进三个引号括起来，放在函数定义的下一行
    print(f"\nI have a {animal_type}.")   # 打印宠物类型，使用f-string格式化字符串，将animal_type变量的值插入到字符串中
    print(f"My {animal_type}'s name is {pet_name.title()}.")   # 打印宠物名字，使用f-string格式化字符串，将pet_name变量的值插入到字符串中，并将其首字母大写 
describe_pet('dog', 'da huang')   # 要按顺序输入两个实参
describe_pet('cat', 'da bai')     # 可以多次调用函数，传递不同实参

# 关键字实参
def describe_pet(animal_type, pet_name):   # 定义一个函数，函数名为describe_pet，括号内有两个参数animal_type和pet_name，以冒号收尾
    """显示宠物的信息"""   # 文档字符串(docstring)的注释，描述函数的功能，缩进三个引号括起来，放在函数定义的下一行
    print(f"\nI have a {animal_type}.")   # 打印宠物类型，使用f-string格式化字符串，将animal_type变量的值插入到字符串中
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')   # 关键字实参，调用函数时可以不按照形参的顺序传递实参
# 注意:在使用关键字实参时，务必准确地指定函数定义的形参名

# 默认值
# 可以给每个形参指定默认值，如果调用函数时给形参提供了实参，Python将使用指定的实参；否则，将使用形参的默认值
def describe_pet(pet_name, animal_type='dog'):   # 给animal_type指定默认值'dog'
    '''显示宠物的信息'''
    print(f"\nI have a {animal_type}.")   # 打印宠物类型，使用f-string格式化字符串，将animal_type变量的值插入到字符串中
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')   # 调用函数时只传递了pet_name实参，使用animal_type的默认值'dog'
describe_pet('willie')   # 也可以只传递一个实参，使用    
describe_pet('willie', 'cat')   # 调用函数时传递了两个实参，覆盖了animal_type的默认值

# 2026.10.5
# 等效的函数调用
def describe_pet(pet_name, animal_type='dog'):  # 这种定义任何时候都必须传递pet_name实参，在指定实参时，既可用位置实参，也可用关键字实参
    print(f"\nI have a {animal_type}.")   # 打印宠物类型，使用f-string格式化字符串，将animal_type变量的值插入到字符串中
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# 一条名为Willie的狗
describe_pet('willie')  # 位置实参
describe_pet(pet_name='willie') # 关键字实参
# 一条名为Harry的仓鼠
describe_pet('harry', 'hamster')  # 位置实参,不必在意有默认值的形参，直接写就行
describe_pet(pet_name='harry', animal_type='hamster')  # 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')  # 关键字实参，顺序可以颠倒

# 避免实参错误
# traceback首先指出错误类型，再指出错误出现在什么地方，然后指出错误的函数调用，最后指出函数调用缺少的实参

# 2026.10.6
# 返回值，函数并非总是直接显示输出，他还可以处理一些数据，并返回一个或一组值，这被称为返回值。可以使用return直接调用函数的那行代码
# 返回简单的值
def get_formatted_name(first_name, last_name):
    '''返回标准格式的名字'''
    full_name = f'{first_name.title()} {last_name.title()}'
    return full_name.title()    # return语句让函数返回一个值，并结束函数的执行。返回值可以赋给变量，也可以直接使用
musician = get_formatted_name('jimi', 'hendrix')   # 调用函数，并将返回值赋给变量musician
print(musician)   # 打印变量musician的值

# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):   # 给middle_name指定默认值为空字符串，因为下面调用函数时可能没有传递middle_name实参
    '''返回标准格式的名字'''
    if middle_name:   # 如果middle_name不为空字符串，就将其加入到full_name中
        full_name = f'{first_name.title()} {middle_name.title()} {last_name.title()}'
    else:   # 如果middle_name为空字符串，就只返回first_name和last_name
        full_name = f'{first_name.title()} {last_name.title()}'  # 就算if没用到middle_name,下面调用函数的时候还是会在定义去找，所以必须middle_name=''，不然没实参报错
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')   # 调用函数时只传递了first_name和last_name实参，使用middle_name的默认值为空字符串
print(musician)   # 打印变量musician的值
musician = get_formatted_name('john', 'hooker', 'lee')   # 调用函数时传递了三个实参，覆盖了middle_name的默认值为空字符串
print(musician)   # 打印变量musician的值

# 返回字典
def build_person(first_name, last_name):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first': first_name, 'last': last_name}   # 创建一个字典，包含first_name和last_name,不加引号是因为可以把形参看为变量，后面给实参时加上就行了
    return person   # 返回字典
musician = build_person('jimi', 'hendrix')   # 调用函数，并将返回值赋给变量musician
print(musician)
# · return 一执行，函数立即结束 → 后面写什么都白搭
# · 想打印返回值 → 在调用处打印（用变量接，或直接塞进 print）
# · 在函数体里 return 后面打印 → 永远轮不到

# 补充字典添加用法(.update()方法)
# update 传字典
d = {'a': 1}
d.update({'b': 2})          # d = {'a': 1, 'b': 2}

# update 传关键字参数
d = {'a': 1}
d.update(b=2, c=3)          # d = {'a': 1, 'b': 2, 'c': 3}

# update 传可迭代的键值对（列表/元组）
d = {'a': 1}
d.update([('b', 2), ('c', 3)])   # d = {'a': 1, 'b': 2, 'c': 3}
[('b', 2), ('c', 3)]      # 列表，里面装元组
(('b', 2), ('c', 3))      # 元组，里面装元组

# update 直接传 zip
d = {'a': 1}
d.update(zip(['b', 'c'], [2, 3]))   # d = {'a': 1, 'b': 2, 'c': 3}
keys   = ['b', 'c']
values = [2, 3]
zip(keys, values)   # 配出来是 ('b', 2) 和 ('c', 3) ，讲究一个对一个，短的直接舍弃

# update 不覆盖已有的写法（配合循环判断）
d = {'a': 1}
d.update({'a': 99})         # d = {'a': 99}，同名会被覆盖


# 扩展函数，修改存储年龄
def build_person(first_name, last_name, age=None):  # 由于可能不填age，而且age一般填数字，所以给一个None既可判断又不会因为没写实参报错
    '''返回一个字典其中包含一个人的信息'''
    person = {'first': first_name, 'last': last_name}
    if age:   # 做判断，如果age不为空则进行下一步加入字典
        person['age'] = age      # 标准的加入字典
    return person
musician = build_person('jimi', 'hendrix', age=34)
print(musician)

# 函数内部定义的局部变量（含形参）只活在函数里、外面看不见，想送出去必须用 return；而函数外部定义的全局变量，函数内可以直接读，但要修改它必须加 global 声明。


# # 结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
#     '''返回规范格式的姓名'''
#     full_name = f'{first_name.title()} {last_name.title()}'
#     return full_name.title()
# # 这是一个无限循环
# while True:
#     print('\nPlease tell me your name:')
#     f_name = input("First name:(按'exit'退出)\n")
#     if f_name == 'exit':
#         break
#     l_name = input("Last name:(按'exit'退出)\n")
#     if l_name == 'exit':
#             break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f'Hello , {formatted_name}')

# 2026.10.7
# 传递列表
def greet_users(names):    # 拿到列表实参
    '''向列表中的用户发出简单的问候'''
    for name in names:     # 相当于把列表中元素一个个提取出来
        msg = f"Hello, {name.title()}"
        print(msg)
user_names = ['mana', 'li hua', 'tom']    # 这是列表
greet_users(user_names)                   # 实参直接传递列表，整体是一个实参

# 在函数中修改列表
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
while unprinted_designs:     # unprinted_designs不被搬空，就一直循环
    current_design = unprinted_designs.pop()            # current中文意思当前的
    print(f"Printing model: {current_design}")   
    completed_models.append(current_design)           # 将pop()的元素追加至新列表
# 显示打印好的所有模型
print(f"\nThe following models have been printed:")
for completed_model in completed_models:
# 这里的completed_model后不能用title(),for 后面的变量，作用是挨个接住序列里的元素，它是一个赋值位置，不是一个“可以运算的表达式”。    
    print(completed_model.title())

# 重新组织这些代码，编写两个函数，让每个都做具体的工作
def print_models(unprinted_designs, completed_models):
    '''模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到completed_models中'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()            # current中文意思当前的
        print(f"Printing model: {current_design}")   
        completed_models.append(current_design)      # 调用加入的是外部变量，改的是‘可变对象内部’，所以外部会变。不用加global     
# 可变对象：能把里面的内容原地改了，变量还指着原来那个。
# 不可变对象：改不了内部，想变只能让变量指个新的。
# 后者看起来就像“普通变量”那样，赋值一次换一个。
def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
# 这里的completed_model后不能用title(),for 后面的变量，作用是挨个接住序列里的元素，它是一个赋值位置，不是一个“可以运算的表达式”。    
        print(completed_model.title())

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs, completed_models)    # 先注释掉，下面的副本调用要用到
# show_completed_models(completed_models)              # 先注释掉，下面的副本调用要用到
# 1. 先想清楚：这个函数要从外面拿什么（输入），要还给外面什么（输出）
# 2. 从外面拿的 → 写进形参
# 3. 自己内部用的临时变量 → 不用写形参，直接在函数体里定义
# 4. 要给外面的 → 用 return 送出去
# 形参不是“函数里用到啥就写啥”，而是“从外面传进来的才写”。名字不能乱起，要让人一眼看懂。
# 先把事写出来，再整理成函数，最后把定义挪上去——这是非常正规的写代码流程。你一上来就想“先定义好函数”，反而会卡死，因为你还没想清楚下面要干嘛。

# 禁止函数修改变量
# function_name(list_name[:])   #将列表的副本传给函数   function意思是函数

# 如果不想清空未打印的设计列表，可以像下面这样调用print_models()
print_models(unprinted_designs[:], completed_models)    # unprinted_designs[:]用的是副本，不会改变原来的列表
show_completed_models(completed_models)
print(unprinted_designs)              # 无变化
print(completed_models)               # 有变化,如果也传的副本就没变化
print(unprinted_designs[:])            # 看不到被pop()搬空的列表了
# 副本就是为了不改变原件，而把数据传给形参。
# 形参定流程，实参填值，填进去就走那套流程。

# 2026.10.8
# 传递任意数量的实参
def make_pizza(*toppings):   # 形参名*toppings让Python创建一个名为toppings的元组，该元组包含函数收到的所有值
    """打印顾客点的所有配料"""
    print(toppings)         # print()函数可以处理元组
make_pizza('pepperoni')   # ('pepperoni',)  把实参封装到元组中，即便一个函数只收到一个值也是如此
make_pizza('mushrooms', 'green peppers', 'extra cheese')   # ('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:    # 因为把元组里面的元素一个个取出来了，所以打印没引号和方括号
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接受任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，
# 再将余下的实参都收集到最后一个形参中。
def make_pizza(size, *toppings):   # 两个形参，接受任意数量实参的形参放在最后(*toppings)
    '''概述要制作的比萨'''
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')    # 如果不是for……in……取了元素，'pepperoni'照样打印元组  
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
# 可将函数编写成能够接受任意数量的键值对————调用语句提供了多少就接受多少
def build_profile(first, last, **user_info):   # **user_info，是搞一个字典定义里面字典名就是它
    """创建一个字典，其中包含我们知道的有关用户的一切"""
# 给实参当一个数据就行了，他能在函数定义里面干很多事
    user_info['first_name'] = first    # 这是新增字典，所以键值在后面
    user_info['last_name'] = last      # 这是新增字典，所以键值在后面
    return user_info     # 把字典返回出去接住
user_profile = build_profile('albert', 'eistein',
                             location='printceton',
                             field='physics')   # location='printceton', field='physics'任意数量字典实参
print(user_profile)
# location='princeton' 里的 location 是“参数名”，不加引号；它作为键进到字典里时，Python 自动把它变成字符串 'location'。
# 你不能写 'location'='princeton'，因为字符串不能当参数名。
# location='princeton' 就是关键字实参；**user_info 专门用来“收集任意多个关键字实参，打包成字典”。
# 参数名（location）自动变成字典的键，不带引号；值（'princeton'）是字符串，带引号。

# * 收“一堆位置实参” → 元组；** 收“一堆关键字实参” → 字典。
# 传几个收几个，专门处理“不知道会传多少”的情况。


# 2026.10.8
# 将函数存储在模块中(用import语句)
# 导入整个模块。模块是扩展名为.py的文件，包含要导入程序的代码，现在我创建一个(pizza.py),在同目录
import pizza     # 导入pizza.py   用pizza. 可以调用它的代码函数
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# · pizza：导入的模块名（pizza.py）
# · make_pizza：模块里的函数
# · . ：点号，表示“到 pizza 这个模块里找”
# · (...)：调用这个函数，把参数传进去
# 模块名.函数名(参数) = 调用“某个模块里的某个函数”。pizza. 就是“到 pizza 模块里找”。

# 导入特定的函数
# 可以只导入模块中特定的函数
# from pizza import function_name    # 没有的函数会报错
from pizza import make_pizza
# from pizza import function_name   <-- 在pizza模块中导入function_name函数
# 用逗号分隔函数名，可根据需要从模块中导入任意数量的函数: from pizza import function_0, function_1, function_2
# 如果只想导入要使用的函数，代码类似这样:
from pizza import make_pizza
make_pizza(16, 'pepperoni')   # 这样导入模块特定函数，不需要再点出模块名了，直接用函数就行了
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给函数指定别名，指定独一无二的别名(alias)
# 下面给make_pizza()函数指定了别名mp()
from pizza import make_pizza as mp   
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# import 模块 as 别名 = 给整个模块起新名字。
# from 模块 import 函数 as 别名 = 给某个函数起新名字。
# 都能用 as，看你想改谁的名。

# 使用as给模块指定别名
import pizza as p   # 把模块加载进来，只用p这个名字引用它，所以不能用原来模块名字，除非再调用一次
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 可以同时改两个，只建议模块调用函数，直接调用特定函数本来就不用写模块名

# 使用(*)导入模块中的所有函数，写大模型不建议，会有重名的函数，Python会互相覆盖
from pizza import *      # 可再次调用pizza(原模块)，*代表调用所有，在这里是通配符
make_pizza(16, 'pepperoni')   # 这样导入模块所有函数，不需要再点出模块名了，直接用函数就行了
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 蟒蛇书第8.7节“函数编写指南”要求给函数起描述性名字且仅用小写字母和下划线，在def行后紧跟文档字符串注释，
# 形参默认值和关键字实参赋值时等号两边不加空格，程序内用两个空行分隔相邻函数，所有import语句置于文件开头，并建议函数精简以不超过50行为宜。
# def function_name(parameter_0, parameter_1='default value')  <--这里的默认形参等号不空格
# function_name(value_o, parameter_1='value')   <--这里的关键字实参等号不空格


# 2026.10.9
# 第九章: 类
# 面向对象编程(OOP)，编写现实情景的类(class)，并基于这些来创建对象(object)
# 9.1 创建和使用类
# 9.1.1 创建Dog类   赋予每条小狗坐下(sit())和打滚(roll_over())的能力
class Dog:    # 定义一个名为Dog的类,约定上，我们再python中类名称首字母大写,但小写一样合法
    """一次模拟小狗的简单尝试"""     # 同样是用三个引号注释提示
    def __init__(self, name, age):  # 这个self(当然也只是一个名称)必不可少，且位于其他形参前面，这个形参是Python传递实例用的
        """初始化属性name和age"""
        self.name = name    # 把右边的实参name传递存入(被引用)到实例的name(变量)属性里去
        self.age = age    # 这两个在__init__方法内定义的变量都有前缀self，可供类中所有方法使用(使用时用完整变量名)，可通过任意实例来访问
    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting." )
    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
# __init__()方法
# 类中的函数称方法，与前面的唯一重要差别是调用的方法的方式
# __init__()是一个特殊方法，每当你根据Dog类创建新实例时，Python都会自动运行它
# 在这种方法名称中开头和结尾的两个下划线是一种约定，避免Python默认方法与普通方法发生名称冲突
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):     # 这里的第一个形参self也是被塞进实例
        print(f"{self.name} 在叫")   # 这里的self.name可供类中所有方法使用(使用时用完整变量名)

my_dog = Dog('旺财')     # 造实例，装进变量，后面的调用函数用这个变量调用
my_dog.name              # 访问属性 → '旺财'  必须先存进实例，才能访问 --> self.name = name
my_dog.bark()            # 访问方法 → 打印“旺财 在叫”
# 类主要是防止在这一段函数下参数过多且要频繁的去传递，所以把它用class分类，用__init__打包，
# 之后实例赋给变量后用它去调用方法，class和init只是工具，真正还是给def函数方法铺路

# 所以class和__init__只要出现一次就行了，当然，你多次打包也没问题，多次分类也没问题，不过在一个函数运作体系中没必要

# 根据类创建实例
class Dog:    # 定义一个名为Dog的类,约定上，我们再python中类名称首字母大写,但小写一样合法
    """一次模拟小狗的简单尝试"""     # 同样是用三个引号注释提示
    def __init__(self, name, age):  # 这个self(当然也只是一个名称)必不可少，且位于其他形参前面，这个形参是Python传递实例用的
        """初始化属性name和age"""
        self.name = name    # 把右边的实参name传递存入(被引用)到实例的name(变量)属性里去
        self.age = age    # 这两个在__init__方法内定义的变量都有前缀self，可供类中所有方法使用(使用时用完整变量名)，可通过任意实例来访问
    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting." )
    def roll_over(self, number):  # 在类函数方法中，第一个形参必须是接实例的位置
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled {number}!")
my_dog = Dog('willie', 6)      # 开始造实例，用变量my_dog引用
print(f"My dog's name is {my_dog.name}.")   # 调用,(self.name = name是把实参name传入实例名叫name的变量中。my_dog.name只是在实例里面提取name)
print(f"My dog is {my_dog.name}")
# · self：定义里第一个形参，代表“当前实例”，Python 自动传
# · name（右边）：形参名，接住外面传进来的值，比如 '旺财'
# · self.name（左边）：你给实例起属性名叫 name，把右边的值存进去
# my_dog.name = 从 my_dog 这个实例里，取出之前存进去的 name 属性。
# 不是“把 my_dog 当 self”，是“从实例身上取属性”。

# 1.访问属性
print(my_dog.name)   # 先找到实例my_dog，再查找与这个实例相关的属性name
# 2.调用方法
my_dog.sit()         # 指定实例名和想调用的方法，并用句号分隔
my_dog.roll_over(3)  # (self, number)这两个形参，一个留给实例，拿到__init__实参，一个自己补充
# 实例 = 调用类里方法的通行证，同时自带 __init__ 存好的数据，还不能直接自己下面去调用。方法用实例的数据，方法必须在类里定义好，新参数自己补。
# 3.创建多个实例
your_dog = Dog('Lucy', 3)    # 开始搞新的实例了，里面的实参不一样了，存入的数据方式一样，但是内容不同
print(f"My dog's name is {your_dog.name}.")
# 一旦存进实例，只要实例还在，没被改，实例.属性 取出来永远是那个值。
# 这就是实例属性的“持久性”。
# 但注意：能跨代码访问的是 your_dog.name，不是光写 name。
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over(4)  # 和上面是一样的,实例没有的额外形参自己去补

# 2026.10.10
# 使用类和实例
# 使用car类
# ============================================================
# 第一部分：位置实参和关键字实参混用
# ============================================================

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        # __init__ 不能变，Python 只认这个
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):       
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', year=2025, model='a4')
# 第一个位置实参，后两个关键字实参，且位置调换
# 位置实参和关键字实参可以混用
# 但位置实参必须全部写在前面，关键字实参写在后面
# 反过来（关键字在前、位置在后）会报错
# 这是语法硬规定，跟“覆不覆盖”无关

print(my_new_car.get_descriptive_name())
# 不写括号，打印的是方法对象本身，不是返回值

# return 的值，你可以接，也可以不接
# 不接，直接 print 能看到；接了，才能继续用
# “看到”和“拿到”，是两回事


# ============================================================
# 第二部分：给属性指定默认值
# ============================================================

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        # __init__ 不能变，Python 只认这个
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        # 创建一个变量，用默认值存储到实例
        # 下面的方法可以用 self.odometer_reading 访问

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# ============================================================
# 第三部分：修改属性的值
# 方法一：直接修改属性的值
# ============================================================

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
# 这里用“实例.变量名”直接修改属性值

my_new_car.read_odometer()
# 调用含改变属性值的方法看效果


# ============================================================
# 方法二：通过方法修改属性的值
# ============================================================

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # 加入 mileage 主要是为了调用时用实参修改
        # 没有它，就只能写死在方法里改
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage
        # 相当于重新存储（被引用）了一个值
        # 这个值可以在调用时自己给实参


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
# 先运行这个函数，改变属性的值

my_new_car.read_odometer()
# 最后调用含改变属性值的方法看效果

# 同一个实例，改了就一直是改后的值，除非你再改
# 新实例是新的，跟旧实例互不影响
# “只要不添新实例，这个变量就一直改”
# 注意：这句话只对“同一个实例”有效，不是对所有实例有效
# 每个实例有自己的一份属性，互不干扰

# __init__ 跑一次，属性存住
# 后面 self 就是调用者本身
# 只有 self 的方法：不能从外面拿到新值，但能给实例加/改属性


# ============================================================
# 方法二加强版：禁止回调
# ============================================================

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            # 改的值不能小于以前的值
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


# ============================================================
# 方法三：通过方法让属性的值递增
# ============================================================

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # 原来写的是 increment_odometer(a, miles)，第一个形参用 a
        # 第一位形参叫什么都行，照样能接实例、能存属性
        # 但为了别人看懂，还是写 self 最稳
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car('subaru', 'outback', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23_500)
# 更改默认属性，23_500 = 23500
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
# 增加里程数
my_new_car.read_odometer()
# 再读取里程数


# ============================================================
# 重点总结
# ============================================================

# 1. 位置实参和关键字实参可以混用
#    但位置实参必须在前面，关键字实参在后面
#    反过来会报错

# 2. 方法调用要加括号
#    my_car.get_descriptive_name()   ← 调用，拿返回值
#    my_car.get_descriptive_name     ← 不调用，只是方法对象

# 3. 属性可以三种方式改：
#    - 直接改：my_car.odometer_reading = 23
#    - 通过方法改：my_car.update_odometer(23)
#    - 通过方法递增：my_car.increment_odometer(100)

# 4. self 就是当前实例的入口
#    方法里靠 self 来读、存、改这个实例的数据
#    第一位形参叫什么都行，但写 self 是约定，最稳

# 5. __init__ 只跑一次，属性存到实例上
#    后面所有方法都通过 self 访问这些属性
#    每个实例有自己独立的一份属性，互不影响

# 6. 同一实例改了就一直是改后的值
#    新实例是新的，跟旧实例互不影响
#    “只要不添新实例就一直改”这句话只对同一个实例成立

# 2026.10.11
# 9.3 继承
# 如果要编写的类是一个既有类的特殊版本，可使用继承(inheritance)。当一个类继承一个类时，将自动获得后者的所有属性和方法。
# 原有的叫父类(parent class)，而新类称为子类(child class)。子类不仅继承所有属性方法，还可以自己定义
# 9.3.1 子类的__init__()方法
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        # __init__ 不能改名，Python 只认这个
        # self 是当前实例，make/model/year 是形参
        # 属性全挂在 self 上，没有父子之分
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year

        # 创建一个变量，用默认值存储到实例
        # 下面的方法可以用 self.odometer_reading 访问
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # 加入 mileage 是为了调用时用实参修改
        # 没有它，就只能写死在方法里改
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            # 改的值不能小于以前的值
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # 原来写的是 (a, miles)，第一个形参必须是 self
        # 原来函数体也没写，补上
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles


# ============================================================
# 子类 ElectricCar
# ============================================================

# 创建子类时，父类必须已经定义或导入
# 同文件时放在子类前面；不在同文件要先 import
class ElectricCar(Car):
    # 必须在括号里指定父类名称
    """电动汽车的独特之处"""

    def __init__(self, make, model, year, battery=75):
        # 子类可以自己加参数，自己初始化新属性
        # 多出来的参数放在父类参数后面
        # 前面几个对应父类，后面几个是自己扩展

        # 子类形参不能比父类必需参数少接
        # 父类必需参数 = make, model, year
        # 子类就至少要接住这三个，否则 super() 里没变量可用
        # 父类有默认值的参数，子类也可以少接、少传

        # super() 是子类手里的对讲机，用来呼叫父类
        # super().__init__(...) 就是调用父类的 __init__
        # 父类需要的必需参数一个都不能少，少了报 TypeError
        # 父类有默认值的参数可以少传

        # 传参两种都行：
        #   位置实参：super().__init__(make, model, year)
        #   关键字实参：super().__init__(make=make, model=model, year=year)
        #     等号左边是父类形参名，必须和父类 def 里的名字一致
        #     等号右边是子类变量名，必须和子类 def 里的形参一致

        super().__init__(make, model, year)

        # 父类执行完返回子类，子类继续往下走
        # self 还是同一个实例，父类属性已经挂好了
        # 这行是子类自己新增的属性，父类没有
        self.battery = battery
        # 子类新增属性写在哪都行，只要它的值不依赖父类属性。
        # 依赖父类属性，就必须放 super() 后面；不依赖，前后都行。



# ============================================================
# 实例化和调用
# ============================================================

my_leaf = ElectricCar('nissan', 'leaf', 2024)

# 调用父类的方法
# 父类方法里的 self 就是 my_leaf
# 能取到 make/model/year，因为 super().__init__ 已经挂好了
print(my_leaf.get_descriptive_name())

# 子类自己的属性也能用
print(f"Battery: {my_leaf.battery}-kWh")


# ============================================================
# 完整执行顺序（针对 my_leaf = ElectricCar('nissan', 'leaf', 2024)）
# ============================================================

# 1. Python 调用 ElectricCar.__new__(ElectricCar) 造一个空实例 my_leaf
#    此时 my_leaf 什么属性都没有
#
# 2. Python 调用 ElectricCar.__init__(my_leaf, 'nissan', 'leaf', 2024)
#    my_leaf 是 Python 自动作为第一个实参传进去的，对应 self
#
# 3. 进入子类 ElectricCar.__init__（就是子类 def __init__()）
#    形参接住值：
#       self    = my_leaf
#       make    = 'nissan'
#       model   = 'leaf'
#       year    = 2024
#       battery = 75（默认值）
#
# 4. 执行 super().__init__(make, model, year)
#    相当于 Car.__init__(my_leaf, 'nissan', 'leaf', 2024)
#    my_leaf 自动作为父类的 self 传进去
#
# 5. 进入父类 Car.__init__
#    形参接住值：
#       self  = my_leaf（同一个实例）
#       make  = 'nissan'
#       model = 'leaf'
#       year  = 2024
#    执行：
#       self.make = make        → my_leaf.make = 'nissan'
#       self.model = model      → my_leaf.model = 'leaf'
#       self.year = year        → my_leaf.year = 2024
#       self.odometer_reading = 0 → my_leaf.odometer_reading = 0
#    父类执行完，返回子类
#
# 6. 回到子类，继续执行 super() 后面的代码：
#       self.battery = battery → my_leaf.battery = 75
#
# 7. 子类 __init__ 结束，返回
#
# 8. my_leaf 初始化完成，身上有：
#       my_leaf.make             = 'nissan'
#       my_leaf.model            = 'leaf'
#       my_leaf.year             = 2024
#       my_leaf.odometer_reading = 0
#       my_leaf.battery          = 75
#    全部挂在同一个 my_leaf 上


# ============================================================
# 重点总结
# ============================================================

# 1. 属性全是实例自己的，都挂在同一个 self 上
#    “父类属性”只是口语，指“写在父类 __init__ 里的那几行 self.xxx = xxx”

# 2. 创建子类实例时，Python 先 __new__ 造空壳，再调用子类 __init__ 初始化

# 3. 子类 __init__ 只负责设置子类自己的属性
#    父类属性需要子类主动调 super().__init__(...) 才会被设置

# 4. 不写 super().__init__() 的后果：
#    父类属性不存在，父类方法一调用就 AttributeError
#    （除非你完全不需要父类方法，那可以不写）

# 5. super() 里的变量就是子类 __init__ 的形参
#    变量名必须和子类 def 里的形参名一致
#    如果按关键字写，关键字名必须是父类的形参名

# 6. 子类 def __init__ 的参数不能比父类少接：
#    - 父类必需参数，子类必须接住并传过去，少一个就报错
#    - 父类有默认值的参数，可以少接也可以少传
#    - 子类可以多接自己的参数（比如 battery）

# 7. def 定义时只写形参名，没有“关键字”一说
#    调用函数时才能用关键字参数，关键字名匹配被调用函数的形参名

# 8. 继承不是复制粘贴，是实时引用父类
#    父类的方法改了，子类立刻用新的

# 9. super() 不是把父类代码复制过来
#    而是让父类用当前这个 self 把父类那部分属性设置一遍


# 9.3.2 给子类定义属性和方法
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()   # 有return返回的long_name.title()可以直接打印，也可以接住

    def read_odometer(self):
        """打印一个句子，指出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        先初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)   # 后面没":"，记得super()这要加"()"
        # 这里在def __init__()下面要缩进
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

my_leaf = ElectricCar('nisssan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

# 重写父类中的方法
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        先初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)   # 后面没":"，记得super()这要加"()"
        # 这里在def __init__()下面要缩进
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print(f"This car doesn't have a tank!")
# 这时如果有人对电动汽车调用fill_gas_tank()方法,Python将忽略Car类中的fill_gas_tank()方法，转而运行上述代码
# 父类没有、子类有，叫新增，子类实例只能跑子类的，父类实例压根没这个方法。
# 父类有、子类也有且同名，叫重写，子类实例跑子类的，父类实例跑父类的，互不干扰。

# 9.3.4 将实例用作属性
# 发现自己给类添加了太多细节:属性和方法越来越多，文件越来越长。可能需要提取一部分，作为一个独立的类。
# 将大型类拆分为多个协同工作的小类，这种方法称为组合(composition)
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()   # 有return返回的long_name.title()可以直接打印，也可以接住

    def read_odometer(self):
        """打印一个句子，指出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles

class Battery:   # 定义一个新类，没有继承任何类
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size   # 把默认属性存入实例如果没给它供值，那值就是40

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        先初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)   # 后面没":"，记得super()这要加"()"
        # 这里在def __init__()下面要缩进
        self.battery = Battery(30)   # 不加就是默认值，加了就是30,有几个形参就传几个，默认值可不传
# 添加一个名为self.battery的属性,每当__init__()被调用时，都执行操作
# 因此现在每个ElectricCar实例都包含一个自动创建的Battery实例，调用的是Battery.__init__()

my_leaf = ElectricCar('nissan', 'leaf', 2024)   # 创建实例,实参填什么看自己的def __init__()
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

# 现在再给Battery类添加一个方法，它根据电池容量报告汽车的续航里程
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()   # 有return返回的long_name.title()可以直接打印，也可以接住

    def read_odometer(self):
        """打印一个句子，指出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles

class Battery:   # 定义一个新类，没有继承任何类
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size   # 把默认属性存入实例如果没给它供值，那值就是40

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):    # 新增方法
        """打印一条信息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        先初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)   # 后面没":"，记得super()这要加"()"
        # 这里在def __init__()下面要缩进
        self.battery = Battery(65)   # 不加就是默认值，加了多少就是多少,有几个形参就传几个，默认值可不传

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()   # 新增方法也通过汽车属性battery调用

# 9.3.5 模拟实物
# 略  --snip--

# 2026.10.12
# 导入类(允许将类存储在模块中，然后在主程序中导入所需的模块)
# 9.4.1 导入单个类
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        # __init__ 不能改名，Python 只认这个
        # self 是当前实例，make/model/year 是形参
        # 属性全挂在 self 上，没有父子之分
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year

        # 创建一个变量，用默认值存储到实例
        # 下面的方法可以用 self.odometer_reading 访问
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # 加入 mileage 是为了调用时用实参修改
        # 没有它，就只能写死在方法里改
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            # 改的值不能小于以前的值
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # 原来写的是 (a, miles)，第一个形参必须是 self
        # 原来函数体也没写，补上
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles
# 此类以复制粘贴至文件car.py

# 下面创建另一个文件——my_car.py，在其中导入Car类并创建其实例:
from car import Car   # 这里相当于调用car.py中的Car类函数(相当于搬过来)

my_new_car = Car('audi', 'a4', '2024')   # 创建实例
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23    # 改存入属性
my_new_car.read_odometer()          # 调用方法

# 9.4.2 在一个模块中存储多个类
# 由于代码过多，将要调用的多个类放进了car1.py文件里面
from car1 import ElectricCar

my_leaf = ElectricCar('nissam', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
# self.battery = Battery(65) 这行写在 car1.py 里
# 这里通过 import 把 ElectricCar 导进来用
# 如果要改 Battery 实例是怎么创建的，要改调用Battery实例中的实参"65"得回 car1.py 改
# 这种写法本就是写函数的时候自己定，现在调用就改不了
my_leaf.battery.get_range()

# 9.4.3 从一个模块中导入多个类
from car1 import Car, ElectricCar   # 可同时导入一个文件中的多个类,用逗号(","分隔)
# from...import... 拿的是类，不是函数集合。
# 类里怎么调别的类、怎么创建实例、值写没写死，都是类内部的事。
# 你导入之后只能用，改不了内部实现。想改就回源文件，或者覆盖实例属性。
my_mustang = Car('ford', 'mustang',2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# 9.4.4 导入整个模块
import car1    # 导入整个模块
my_mustang = car1.Car('ford', 'mustang', 2024)   # 直接导入模块，每次调用指明模块名，再调用方法
print(my_mustang.get_descriptive_name())   # 创建实例后照常掉用变量就行
# car1. 前缀只在“从模块里取东西”时用，比如 car1.Car、car1.Battery。
# 实例一旦创建出来，它自己就知道是哪个类的，后面直接用变量点方法/属性就行，不用再写模块名。
my_leaf = car1.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# 9.4.5 导入模块中的所有类
from car1 import *
# 优点就一个字：省事。
# 缺点全是坑：看不出来源、容易撞名、难排查。

# 9.4.6 在一个模块中导入另一个模块
# 在 Python 中，一个模块导入另一个模块，通常是为了使用另一个模块中定义的对象，
# 并建立清晰的模块/包依赖关系。把类分散到多个模块、避免模块过大或职责混杂，是常见的工程组织动机之一，但导入机制本身更广泛。
# 已创建electric_car.py
from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# 如此代码不冗杂，就是每个模块中的类的函数方法要记得

# 9.4.7 使用别名用(as)
from electric_car import ElectricCar as EC   # 给模块中的类指定别名
my_leaf = EC('nissan', 'leaf', 2024)

import electric_car as ec     # 给模块指定别名
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)

# 9.4.8 找到合适的工作流程
# 略  --snip--

# 有关字符串格式化的补充
# ============================================================
# Python 字符串格式化：格式说明符全解
# 语法: f"{值:[填充字符][对齐][符号][#][0][宽度][,][.精度][类型]}"
# 方括号 [] 表示可选，实际写代码时不写方括号。
# 顺序基本固定，不能乱写。
# ============================================================

# ============================================================
# 一、整体语法与分隔符
# ============================================================
# f"{值:格式说明符}"
# 冒号 : 是分隔符，左边是值，右边是格式说明符。
print(f"{42:5d}")          # 输出: '   42'  冒号左边42，右边5d

# ============================================================
# 二、填充字符：宽度不够时用什么填
# ============================================================
# 写在对齐符号前面，可以是任意字符。
print(f"{'A':*<5}")        # 'A****'   用 * 填充
print(f"{'A':0>5}")        # '0000A'   用 0 填充
print(f"{'A':-^5}")        # '--A--'   用 - 居中填充

# ============================================================
# 三、对齐：决定值在宽度里靠哪边
# ============================================================
# <  左对齐
print(f"{'A':<5}")         # 'A    '
# >  右对齐（数字默认）
print(f"{'A':>5}")         # '    A'
# ^  居中
print(f"{'A':^5}")         # '  A  '
# =  符号后对齐（符号单独占左边）
print(f"{-42:=5d}")        # '-  42'

# ============================================================
# 四、符号：正数怎么显示
# ============================================================
# +  正数也显示 +
print(f"{42:+d}")          # '+42'
# -  只负数显示 -（默认）
print(f"{42:-d}")          # '42'
# 空格  正数前留一个空格
print(f"{42: d}")          # ' 42'

# ============================================================
# 五、#  进制前缀
# ============================================================
# 显示 0b / 0o / 0x
print(f"{255:#b}")         # '0b11111111'
print(f"{255:#o}")         # '0o377'
print(f"{255:#x}")         # '0xff'

# ============================================================
# 六、0  补零
# ============================================================
# 写在宽度前面，数字前补 0
print(f"{42:05d}")         # '00042'
print(f"{3.14:08.2f}")     # '00003.14'

# ============================================================
# 七、宽度：最小占几个字符
# ============================================================
print(f"{42:5d}")          # '   42'   不足 5 位补空格
print(f"{42:2d}")          # '42'      超过宽度不截断

# ============================================================
# 八、,  千分位
# ============================================================
print(f"{1234567:,}")      # '1,234,567'

# ============================================================
# 九、.精度：小数位 / 有效数字 / 字符串截断
# ============================================================
# 浮点：小数位数
print(f"{3.14159:.2f}")    # '3.14'
# 浮点：有效数字（用 g）
print(f"{3.14159:.3g}")    # '3.14'
# 字符串：截断到几个字符
print(f"{'Hello, World':.5}")   # 'Hello'

# ============================================================
# 十、类型代码：决定怎么解释这个值
# ============================================================
# d  十进制整数
print(f"{42:d}")           # '42'
# f  浮点数
print(f"{3.14:f}")         # '3.140000'
# s  字符串
print(f"{'abc':s}")        # 'abc'
# b  二进制
print(f"{255:b}")          # '11111111'
# o  八进制
print(f"{255:o}")          # '377'
# x  十六进制小写
print(f"{255:x}")          # 'ff'
# X  十六进制大写
print(f"{255:X}")          # 'FF'
# e  科学计数法
print(f"{12345.678:e}")    # '1.234568e+04'
# g  通用数字（自动选 f 或 e）
print(f"{0.00001:g}")      # '1e-05'
# %  百分比（乘 100 加 %）
print(f"{0.25:.1%}")       # '25.0%'
# c  字符（整数转 ASCII）
print(f"{65:c}")           # 'A'

# ============================================================
# 十一、完整拆解几个例子
# ============================================================
# 例 1: f"{42:05d}"
#   42    值
#   :     开始格式说明
#   0     补零
#   5     宽度至少 5 位
#   d     十进制整数
print(f"{42:05d}")         # '00042'

# 例 2: f"{3.14159:*<+10.2f}"
#   3.14159   值
#   :         开始格式说明
#   *         填充字符用 *
#   <         左对齐
#   +         正数显示 +
#   10        宽度 10
#   .2        保留 2 位小数
#   f         浮点数
print(f"{3.14159:*<+10.2f}")   # '+3.14*****'

# 例 3: f"{255:#08x}"
#   255    值
#   :      开始格式说明
#   #      显示进制前缀 0x
#   0      补零
#   8      宽度 8
#   x      十六进制小写
print(f"{255:#08x}")       # '0x0000ff'

# 例 4: f"{'Hello, World':.5}"
#   'Hello, World'   值
#   :                开始格式说明
#   .5               只取前 5 个字符
print(f"{'Hello, World':.5}")   # 'Hello'

# ============================================================
# 十二、三种写法对照（同样效果）
# ============================================================
val = 3.14159
print("%.2f" % val)              # 3.14        % 格式化
print("{:.2f}".format(val))      # 3.14        format
print(f"{val:.2f}")              # 3.14        f-string

# ============================================================
# 十三、常见坑
# ============================================================
# 补零时别加左对齐，否则 0 跑到右边
print(f"{42:<05d}")        # '42000'  错误示范
print(f"{42:05d}")         # '00042'  正确

# % 格式化遇到 % 要转义
print("%d%%" % 50)         # '50%'

# format 花括号转义
print("{{}}".format())     # '{}'

# f-string 不能解包 *args / **kwargs
args = [1, 2]
# print(f"{*args}")        # ❌ 语法错误
print("{} {}".format(*args))  # ✅ '1 2'

# f-string 不能放语句
# print(f"{x = 1}")        # ❌ 赋值不是表达式

# 类型不匹配会炸
# print(f"{'abc':d}")      # ❌ ValueError

# ============================================================
# 十四、总结口诀
# ============================================================
# {值 : [填充][对齐] [符号] [#] [0] [宽度] [,] [.精度] [类型]}
# 对齐: > 右, < 左, ^ 中
# 类型: d 整数, f 浮点, s 字符串, b/o/x 进制, % 百分比
# 补零: 宽度前加 0，如 05d, 08.2f
# 千分位: 加 ,
# 调试: f"{变量=}"  (Python 3.8+)

# ============================================================
# 十五、选哪个？
# ============================================================
# % 格式化   : 老代码、老教材、C 风格习惯。能用但别主动写。
# format()   : 动态模板、需要解包、需要复用模板时用。
# f-string   : 日常首选，可读性最好、性能最高。
# 新代码无脑 f-string，遇到动态模板/解包再退回 format。

# 9.5 Python标准库
from random import randint
print(randint(1, 6))  # 生成一个1和6之间的随机数字

from random import choice  # 都属于random库里面
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)  # choice将列表或元组作为参数，并返回其中一个元素
print(first_up)

# 9.6 类编码风格（规范）

# 这一节没有任何新语法，全是写代码时的格式约定，目的是让代码易读、符合行业标准。

# 类名：ElectricCar —— 大驼峰，首字母大写，没下划线 ✅
# 实例名/模块名：my_leaf —— 小写 + 下划线；car.py（这里用 from car import Car 隐式体现）
# 类内部格式：
# 类定义下一行就是 """电动汽车的独特之处。""" 文档字符串 ✅
# 在 class 和实例化代码 my_leaf = ... 之间，留了空行隔开 ✅

# 导入顺序：
# import random（标准库）在最上面 ✅
# 空了一行
# from car import Car（自己写的模块）在下面 ✅
#   · 推荐使用绝对导入，结构清晰。

# 9.7 小结（章节收尾）

# 这一节是对整个第 9 章的回顾，没有新知识点。
# · 回顾了本章学到的核心能力：定义类、初始化属性、实例化对象、修改属性、继承、super() 调用父类、导入模块、使用 Python 标准库。
# · 承上启下：指出下一章（第 10 章）将学习文件和异常，让程序能够持久化保存数据和优雅地处理错误。


# 2026.10.19
# 第十章:文件和异常
# 10.1: 读取文件

# 10.1.1: 读取文件的全部内容
# 要读取文件，许要一个包含多干行文本的文件。下面创建一个文件，包含精确到小数点后30位的圆周率值，且在小数点后每10位处换行:
# pi_digits.txt   <-- 已保存为同一目录,在这个文件夹里面打开
# 3.1415926535
#   8979323846
#   2643383279

# 下面的程序打开并读取这个文件，再将其内容显示到屏幕上:
from pathlib import Path    # 标准库模块，首先从中导入Path类，Path对象指向一个文件，可以做很多事，核实文件存在，读取内容，将新数据写入等。
path = Path('pi_digits.txt')  # 这里创建一个表示文件pi_digits.txt的Path对象，并赋值给变量path
contents = path.read_text()   # 由于这个文件与当前编写的.py文件位于同一个目录中，因此Path只需要知道其文件名就能访问它
print(contents)   # 相比与源文件，末尾多输出了一行，因为read_text()到达文件末尾时会返回一个空字符串，其会被显示一个空行，可以对contents调用rstrip()(已经被修复，现在的版本已经不会再多一行了)
# 路径(path)指的是文件或文件夹在系统的准确位置。pathlib模块，让我们轻松在各种操作系统中处理文件和目录。提供功能的模块通常称为库(librery)
# 注意，VS Code会在最近打开的文件夹中查找文件，因此需要先打开本章程序所在的文件夹

# 相对文件路径和绝对文件路径
# 相对路径让Python到相对于当前运行程序的所在目录的指定位置去查找。若filename.txt位于python_work中的text_files中，则如下:
# path = Path('text_files/filename.txt')  # 路径之间，使用/隔开每一层级(Windows系统使用\)

# 绝对路径将文件精准位置告诉Python，在相对路径行不通的时候，可以使用绝对路径。假如text.files并不在python_work中，则向Path传递相对路径行不通，因为只能在python_work(当前文件夹)中寻找
# 绝对路径比相对路径更长，因为它们以系统的根文件为起点:
# path = Path('/home/eric/data_files/text_files/filename.txt')
# 使用绝对路径，可以读取系统中任何地方的文件。

# 注意: 在显示文件路径时，Windows系统使用反斜杠(\)，而不是斜杠(/)。但在代码中始终用斜杠，在与你或其他用户的系统交互时，pathlib库会自动使用正确的路径表达方式。


# 10.1.3 访问文件中的各行
# 可以使用splitlines()方法将冗长的字符串转换为一系列行，在使用for循环以每次一行的方式检查文件中的各行:
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()   # sokutkubes()方法返回一个列表，其中包含文件的所有行，把每一行切割下来并且作为列表中的一个元素
for line in lines:
    print(line)
# 【splitlines() 的底层本质】
# 1. 切割标准：只认换行符（\n, \r\n, \r 等跨平台换行），遇到就切。“其实就是各个系统的换行符不一样，有的夹带私货，它能识别照样切。”
# 2. 去除内容：只吃掉换行符本身。
# 3. 保留内容：行首、行尾的空格、制表符（\t）【绝对原样保留】。
# 4. 如果要去掉行首尾的空白字符，必须手动套用 .strip() 或 .strip('\t')。

# 【\r (Carriage Return) 的本质】
# 1. 动作：将光标移动到当前行的最开头（不换行）。
# 2. 跨平台：Windows 使用 \r\n 换行；Linux/macOS 使用 \n。
# 3. 进度条原理：结合 print(..., end="")，用 \r 回到行首覆盖刷新。
# 4. 安防警告：恶意脚本利用 \r 覆盖屏幕输出，伪造密码提示框；Web 漏洞中常见 CRLF 注入。


# 10.1.4 使用文件的内容
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)        # 打印字符串
print(len(pi_string))   # 打印长度

from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()  # 删掉左边的空格
print(pi_string)        # 打印字符串
print(len(pi_string))   # 打印长度

# 注意: 在读取文本时，Python将其中的所有文本都解释为字符串。如果读的是数，要将其作为数值使用，用int()或float()

# 10.1.5 包含100万位的大型文件
from pathlib import Path
path = Path('pi_million_digits.txt')   # 导入文件
contents = path.read_text()     # 读取文本,调用类里面的函数
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

# 10.1.6 圆周率包含你的生日吗
# 可以先将生日表示为一个由数字组成的字符串再检查这个字符串是否位于pi_string中
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your ...")
# else:
#     print("No!")

# 2026.10.20
"""
============================================================================
【Python f-string 对齐与补位法则：为什么只有浮点数非要用 'f'？】
============================================================================

在 f-string 的大括号 {变量:格式} 中，冒号后面的规则有一个“极简特例”：

1. 整数与字符串（极度宽容）：
   - 进行对齐、补位、补零时，不需要写 'd' 或 's'。
   - 例如：
     num = 42
     text = "Hello"
     f"{num:>10}"   # 右对齐，补空格（不需要写 >10d）
     f"{num:05}"    # 左补零（不需要写 05d）
     f"{text:<10}"  # 左对齐，补空格（不需要写 <10s）

2. 浮点数（必须带 'f' 的例外）：
   - 只要涉及到控制“小数点后保留几位”，必须带上 'f'。
   - 如果不带 'f' 只写 .2，Python 会报错，因为解释器分不清你是要切字符串，还是要切小数。
   - 例如：
     pi = 3.1415926
     f"{pi:>10.2f}"  # 右对齐，保留2位小数（输出 '      3.14'）
     f"{pi:010.2f}"  # 占10位，左补零，保留2位小数（输出 '0000003.14'）

3. 进阶骚操作（百分比与千分位）：
   - 用 '%' 代替 'f'：自动乘以100并加百分号。
     f"{0.75:>10.1%}" # 输出 '     75.0%'
   - 用 ',' 加千分位逗号：
     f"{1234567:,}"   # 输出 '1,234,567'

【底层原理差异】：
Python 的 f-string 是“动态解释”，解释器知道变量的类型，所以能容忍你不写 d/s；
而 C 语言的 printf 是“静态盲读”，全靠 %d/%f 去内存里抠字节，少一个字符都会导致底层错乱。
============================================================================
"""