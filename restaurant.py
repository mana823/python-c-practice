class Restaurant:    # 分类
    def __init__(self, restaurant_name, cuisine_type):   # 特殊方法
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}.")   # 内部调用只要用self(变量)
    def open_restaurant(self):
        print("正在营业")