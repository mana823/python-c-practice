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