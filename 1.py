# name = 'ada lovelace'
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
cars.sort(reverse=True)  # reverse=True  按英文字母逆序排列  'reverse'中文意思是反转，默认是reverse=Falsa
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






