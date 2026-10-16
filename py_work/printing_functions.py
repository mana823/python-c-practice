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



def print_(unprinted, completed):
    while unprinted:
        current_design = unprinted.pop()
        print(f"printing model {current_design}")
        completed.append(current_design)
def show_(completeds):
    for completed in completeds:
        print(completed.title())

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
































