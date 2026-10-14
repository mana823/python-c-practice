class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


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


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # 关键：把 Privileges 实例装进来
        self.privileges = Privileges()