from user1 import User
class Privileges:
    def __init__(self):
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
        ]   # 可以不加在__init__()中用默认值，直接后面自己加就行

    def show_privileges(self):
        print("管理员权限：")
        for p in self.privileges:
            print(f"- {p}")


class Admin(User):   # 因为是子类，所以必须导入父类才行
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # 关键：把 Privileges 实例装进来
        self.privileges = Privileges()
# 子类文件里，必须自己 from 父类文件 import 父类。
# 不能指望“第三个文件导入了”，子类就能用。