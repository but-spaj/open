# coding: utf-8
# Python入門編8 クラスを理解しよう 02:クラスを作成しよう
# クラスを作成する

# class クラス名でクラスを作成
class Player:
    # メソッドを定義。引数にはselfを使う
    def walk(self):
        print("ゆうしゃは荒野をあるいていた")
    def attack(self, enemy):
        print("ゆうしゃは" + enemy + "を攻撃した")
# 変数に格納してオブジェクトを生成
player1 = Player() 
# オブジェクト.メソッドで、クラスで定義したメソッドの呼び出し
player1.walk()
player1.attack("スライム")
