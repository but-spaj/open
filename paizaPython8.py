# coding: utf-8


# Python入門編8 クラスを理解しよう 02:クラスを作成しよう
# クラスを作成する

# class クラス名でクラスを作成
class Player0:
    # メソッドを定義。引数にはselfを使う
    def walk(self):
        print("ゆうしゃは荒野をあるいていた")
    def attack(self, enemy):
        print("ゆうしゃは" + enemy + "を攻撃した")
# 変数に格納してオブジェクトを生成
player1 = Player0() 
# オブジェクト.メソッドで、クラスで定義したメソッドの呼び出し
player1.walk()
player1.attack("スライム")


# Python入門編8 クラスを理解しよう 03:変数をクラスで管理しよう
# 変数をクラスで管理する

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

# 参考URL
# 9.クラス — Python 3.6.5 ドキュメント
# https://docs.python.org/ja/3/tutorial/classes.html

# Pythonのクラス変数とインスタンス変数 | UX MILK
# http://uxmilk.jp/41600


# Python入門編8 クラスを理解しよう 04:RPGの敵クラスを作ろう
# RPGの敵クラスを作る

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

# 9.クラス — Python 3.6.5 ドキュメント
# https://docs.python.org/ja/3/tutorial/classes.html

# Python基礎講座(13 クラス)
# https://qiita.com/Usek/items/a206b8e49c02f756d636


# Python入門編8 クラスを理解しよう 05:引数と戻り値のあるメソッドを作ろう
# クラスで、引数と戻り値のあるメソッドを作る

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

# 9.クラス — Python 3.6.5 ドキュメント
# https://docs.python.org/ja/3/tutorial/classes.html

# Python基礎講座(13 クラス)
# https://qiita.com/Usek/items/a206b8e49c02f756d636


