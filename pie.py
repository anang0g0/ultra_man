# クラスの作成
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    
    def info(self):
        print("====================")
        print(f"名前：{self.name}\n性別：{self.sex}\n年齢：{self.age}")
        
# インスタンスを作成
p1 = Person("太郎", "男性", 50)
p1.info()

p2 = Person("花子", 60, "女性") # 順番が違う？
p2.info()