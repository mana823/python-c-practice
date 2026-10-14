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