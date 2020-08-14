''' # Python入門編8: クラスを理解しよう '''

'''
# 02:クラスを作成しよう
'''
# クラスを作成する
# class クラス名でクラスを作成
class Player0:    # Uppercase classname 1st 
    # メソッドを定義。引数にはselfを使う
    def walk(self):
        print("ゆうしゃは荒野をあるいていた")
    def attack(self, enemy):
        print("ゆうしゃは" + enemy + "を攻撃した")
# 変数に格納してオブジェクトを生成
player1 = Player0() 
# オブジェクト.メソッドで、クラスで定義したメソッドの呼び出し
player1.walk()    # call method with object.method
player1.attack("スライム")


'''
# 03:変数をクラスで管理しよう
変数をクラスで管理する

# 参考URL
クラス — Python 3.6.5 ドキュメント
https://docs.python.org/ja/3/tutorial/classes.html

Pythonのクラス変数とインスタンス変数 | UX MILK
http://uxmilk.jp/41600
'''

class Player:
    # コンストラクターの作成
    # コンストラクターはクラスからオブジェクトを生成するときに最初に自動で実行されるメソッド
    # オブジェクトがもつ変数に初期値を設定できる
    def __init__(self, job):    
        # インスタンス変数は、オブジェクトが存在する限り値が保存される
        # selfは、メソッドが呼び出された際に自身を呼び出す
        self.job = job
        
    def walk(self):
        print(self.job + "は荒野をあるいていた")

player1 = Player("戦士")
player1.walk()

player2 = Player("魔法使い")
player2.walk()

# インスタンス変数を使えば、変数とオブジェクトがセットになっている
player1.walk()

''' 2020/08/10 2nd '''

# coding: utf-8
# 変数をクラスで管理する

class Player():
    #def __init__(self, job):    # constructor called first automatically
    #    self.job = job
        
    def wal(self, job):    # argument of method can be used as variable only in the method
        print(job + " werwrw")

player_1 = Player()
player_1.wal("3333")

player_2 = Player()
player_2.wal("4444")

#player_1.wal()
#--> wal() missing 1 required positional argument: 'job'

#player_3 = Player("2222")
#player_3.wal()
#--> object() takes no parameters

class Player2():
    def __init__(self, job):
        job = 2    # this variable can be used in this method
    
    def ttt(self):
        print(job)    # this variable isnt defined in this method. to use this variable, self.job need to be defined in constructor

#player2_1 = Player2()
#--> __init__() missing 1 required positional argument: 'job'    # this means init starts  automaticaly when class object assigned,  
#player2_1.ttt()

class Test():
    def t(self):
        print(self)
    #def y():
    #    print("y")

test1 = Test()
test1.t()
'''
#--> <__main__.Test object at 0x7f6f6c595ef0>
no arguments used in test1.t(), but print(self) expressed above, so self is above
'''
#test1.y()
'''
#--> TypeError: y() takes 0 positional arguments but 1 was given
 this means self is setted automatically to method, so methods must have a 1st dish to take "self" in arguments
"test1" befor . is 1st argument of y()
'''

test2 = Test()
test2.t()
#-->  <__main__.Test object at 0x7f7397ea0f28>

def www(self):
    print(self)
www(4)
#--> 4


'''
# 04:RPGの敵クラスを作ろう
RPGの敵クラスを作る

# 参考URL
9.クラス — Python 3.6.5 ドキュメント
https://docs.python.org/ja/3/tutorial/classes.html

Python基礎講座(13 クラス)
https://qiita.com/Usek/items/a206b8e49c02f756d636
'''

import random
damage = random .randint(1, 30)

class Enemy:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(self.name + "の攻撃!勇者に" + str(damage) + "のダメージ!")

# オブジェクトをリストに追加
# オブジェクトはクラスを変数やリストに格納して生成する
enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("半魚人"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:
    # 共通のメソッドが使える
    # メソッドを呼び出すには、for文内で格納するenemy変数を使う
    enemy.attack()

''' 2020/08/10 2nd '''

# coding: utf-8
# RPGの敵クラスを作る


class Enemy():
    def __init__(self, e):
        self.e = e     # define instance variable to use other methods
            
    def atta(self):
        print(self.e + " wo attak")    # use instance variable not argument to omit input argument many timase 

#slime = Enemy("slime")
#slime.atta()

enemies = []
enemies.append("asd")    # input elements in list then attend object to each of them
enemies.append("sdf")
enemies.append("dfg")
for enemy in enemies:
    enemy = Enemy(enemy)
    enemy.atta()    # indirectly
#--> same

enemies2 = []
enemies2.append(Enemy("asd"))    # input instances in list directly
enemies2.append(Enemy("sdf"))
enemies2.append(Enemy("dfg"))
for enemy2 in enemies2:
    enemy2.atta()    # directly
#--> same


'''
# 05:引数と戻り値のあるメソッドを作ろう
クラスで、引数と戻り値のあるメソッドを作る

# 参考URL 
9.クラス — Python 3.6.5 ドキュメント
https://docs.python.org/ja/3/tutorial/classes.html

Python基礎講座(13 クラス)
https://qiita.com/Usek/items/a206b8e49c02f756d636
'''

class Item:
    # クラス変数はすべてのインスタンスで共通で使用できる
    tax = 1.1
    
    def __init__(self, price, quantity):
        # 2つのインスタンス変数に引数を代入
        self.price = price
        self.quantity = quantity
    
    # クラス変数はクラス名.変数名で使用できる
    # 整数にするためにint()関数を使用する
    def total(self):
        return int(self.price * self.quantity * Item.tax)
    
apple = Item(100, 10)
total = apple.total()
# total関数の戻り値を文字列と組み合わせるためにstr()関数を使う
print("合計金額は" + str(total) + "円です")

orange = Item(150, 10)
print("合計金額は" + str(orange.total()) + "円です")
print("消費税込の金額は、元の金額に" + str(Item.tax) + "倍したものです")

''' 2020/08/10 2nd '''

# coding: utf-8
# クラスで、引数と戻り値のあるメソッドを作る

class Item:
    tax = 1.1    # class.variable can be used in all instance which has the same class
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def sum(self):
        return int(self.price * self.quantity * Item.tax)

fruit = []
fruit.append(Item("apple", 2, 3))
fruit.append(Item("orange", 4, 1))
fruit.append(Item("banana", 5, 6))

try:
    for fru in fruit:
        print(fru.name + " wa " + str(fru.sum()) + " en desu")
except Exception as e:
    print(e)
    

'''
# 06:文字列とリストのメソッドを使ってみよう
文字列とリストのメソッドを使ってみよう
すでにPythonで用意されたメソッドを使う

# 参考URL
4.7.1. 文字列メソッド
https://docs.python.jp/3/library/stdtypes.html#string-methods

5.1. リスト型についてもう少し
https://docs.python.jp/3/tutorial/datastructures.html#more-on-lists
'''
# 文字列で使用できるメソッド

text = "pYthon"
print(text)
# 先頭の1文字を大文字、他を小文字
print(text.capitalize())
# すべて大文字
print(text.upper())

# 文字列をリストに変換するメソッド

players = "勇者,戦士,魔法使い,忍者"
# 引数で指定した文字で文字列を分割してリストを返す
list = players.split(",")
print(list)

# リストで使用できるメソッド

# 引数で指定した文字をリストから削除
list.remove("忍者")
print(list)
# リストに追加する
list.append("霧島")
print(list)


# 演習問題
msg = input()
# msgが小文字の場合はTrue、大文字の場合はFalse
print(msg.islower())
# リストのインデックスiに要素xを挿入する
# team.insert(3, "盗賊")

''' 2020/08/14 2nd '''

# coding: utf-8
# 文字列とリストのメソッドを使ってみよう

text = input()
print(text)
#--> jlEEEE
print(text.capitalize())
#--> Jleeee
print(text.upper())
#--> JLEEEE

players = "we,ggg,shsh,rte"
list = players.split(",")
print(list)
for player in list:
    print(player)
list.remove("we")
print(list)
list.append("aaa")
print(list)
list[1:2] = "lll"
print(list)


'''
# 07:アクセス制限を理解しよう
アクセス制限を理解する

メソッドや変数に対する外部からのアクセスを制限する
完全にアクセス不可にできるわけではないが、変数を管理しやすくできる

# 参考URL
プライベートメンバ - Python学習講座
http://www.python.ambitious-engineer.com/archives/323

9.6. プライベート変数
https://docs.python.jp/3/tutorial/classes.html#private-variables
'''

class Player2:
    def __init__(self, job, weapon):
        self.job = job
        # プライベート変数orプライベートプロパティ：変数名の前に__を付けるとクラスの外では呼び出せない変数
        self.__weapon = weapon

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        # 
        self.__attack("スライム")

    # プライベートメソッド：メソッド名の前に__を付けるとクラスの中でしか呼び出せないメソッドになる
    def __attack(self, enemy):
        print(self.__weapon + "で" + enemy + "を攻撃")


player1 = Player2("戦士", "剣")
player1.walk()
# player1.__attack("スライム")
# print(player1.__weapon)


''' 2020/08/14 2nd '''

# coding: utf-8
# アクセス制限を理解する

class Player:
    def __init__(self, job, weapon):
        self.job = job
        self.__weapon = weapon    # def private variable __

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        self.__attack("slime")    # call private method

    def __attack(self, enemy):    # def private method __
        print(self.__weapon + "で" + enemy + "を攻撃")    # call private variable


player1 = Player("戦士", "剣")
player1.walk()
#player1.__attack("スライム")    # private method cant use outside
#print(player1.__weapon)    # private variable cant use outside
