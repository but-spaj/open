''' # Python入門編9:さらにクラスを理解しよう '''

'''
# 02:クラスを継承する
RPGで使うアイテムが入る宝箱クラスを作り、そこから宝石箱クラスを継承で作ってみましょう。

# 参考URL
クラス — Python 3.6.5 ドキュメント
https://docs.python.jp/3/tutorial/classes.html

【Python入門】オブジェクト指向とclassの作り方
https://www.sejuku.net/blog/28182

Python基礎講座(13 クラス)
https://qiita.com/Usek/items/a206b8e49c02f756d636
'''

# 親クラスと、そこから継承した子クラス

class Box:
    def __init__(self, item):
        self.item = item
    
    def open(self, __mimi):
        self.__mimi = __mimi
        print("宝箱を開いた。" + self.item + " を手に入れた。")
        print(self.__mimi)
        self.__mimick(__mimi)
        
    def __mimick(self, __mimi):    # private propertyはどこでもprivateに合わせる
        print(self.__mimi + "が襲ってきた")
        
class JeweryBox(Box):    # super classのコンストラクタを使う
    def look(self):
        print("宝石はキラキラと輝いている。")
box = Box("鋼鉄の剣")
box.open("mi")
# box.mimick("mi")

jewerybox = JeweryBox("魔法の指輪")
jewerybox.look()
jewerybox.open("mim")    # subclassにないメソッドはsuperclassを使う
# jewerybox.__mimick("mmmm")    # private methodなので呼べない

# coding: utf-8
# クラスにメソッドを定義しよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

class Hello(Greeting):
    # この下に、say_helloメソッドを記述する
    def say_hello(self):
        print(self.msg + " " + self.target)

player = Hello()
player.say_hello()

# coding: utf-8
# クラスを継承しよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

# この下に、Greetingクラスを継承した、Helloクラスを定義する。
# そこに、say_hello()メソッドの定義を記述する。

class Hello(Greeting):
    def say_hello(self):
        print(self.msg + " " + self.target)

player = Hello()
player.say_hello()

''' 2020/08/14 2nd '''

class Box():
    def __init__(self, item):
        self.item = item
        
    def open(self):
        print("open " + self.item)
        
box1 = Box("qwee")    # class() used for arguments
box1.open()

class JBox(Box):    # def super class using class name ()
    
    def look(self):
        print("look")

box2 = JBox("ttt")
box2.look()
box2.open()    # call open, but JBox doesnt have open method, then call method from super class


'''
# 03:メソッドのオーバーライド
ここでは、クラスを継承したときに利用できる、メソッドのオーバーライドについて学習します。
オーバーライドを使うと、スーパークラスが持つメソッドを、サブクラスで再定義できます。

# 参考URL
クラス — Python 3.6.5 ドキュメント
https://docs.python.jp/3/tutorial/classes.html

Pythonで学ぶ 基礎からのプログラミング入門(25) オブジェクト指向について学ぼう(7)
https://news.mynavi.jp/article/python-25/
'''

class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

class MagicBox(Box):
    def look(self):
        print("宝箱は怪しく輝いている")
    def open(self):
        print("宝箱を開いた。" + self.item + "が襲ってきた")

box = Box("鋼鉄の剣")
box.open()

magicbox = MagicBox("モノマネモンスター")
magicbox.look()
magicbox.open()

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    def say_hello(self, target):
        self.target = target
        print(self.msg + " " + self.target)


player = Hello()
player.say_hello("python")

''' 2020/08/14 2nd '''

class Box:
    def __init__(self, item):
        self.__item = item
        
    def open(self):
        print("宝箱を開いた。" + self.__item + "を手に入れた。")

box = Box("鋼鉄の剣")
box.open()

class SBox(Box):
    def look(self):
        print("suspicious")
    
    def open(self):
        print(self.__item + " attacked!!")    # cant use private variable
        
sbox = SBox("ttt")
sbox.look()
sbox.open()
'''
#--> Traceback (most recent call last):
  File "Main.py", line 20, in <module>
    sbox.open()
  File "Main.py", line 16, in open
    print(self.__item + " attacked!!")
AttributeError: 'SBox' object has no attribute '_SBox__item'
'''


'''
# 04:RPGのプレイヤーを継承で記述１
クラスを継承する具体例として、RPGのPlayerクラスとWizardクラスを記述します。
はじめに、スーパークラスとなる、Playerクラスから記述していきます。 

# 参考URL
クラス — Python 3.6.5 ドキュメント
https://docs.python.jp/3/tutorial/classes.html
'''

class Player:
    def __init__(self, name):
        self.name = name    # for using attribute at other method
        print(name)    # can use attribute as variable in using method
        
    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")    # attribute in other method must be used as variable

print("== attack slime with party ===")
hero = Player("hero")
# hero.attack("slime")

warrior = Player("worrior")

party = [hero, warrior]
for member in party:
    member.attack("slime")

''' 2020/08/14 2nd '''


'''
# 05:RPGのプレイヤーを継承で記述２
'''

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizzard(Player):
    def attack(self, enemy):
        print("wryyyyyy")
        print(self.name + "は" + enemy + "に炎を放った")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")

wizard = Wizzard("wizard")

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

# coding: utf-8
# RPGの攻撃シーン

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")

class Warrior(Player):
    def attack(self, enemy):
        print(self.name + "は" + enemy + "を猛攻撃した")


team = []
team.append(Player("勇者"))
team.append(Player("魔法使い"))
team.append(Warrior("戦士"))

for person in team:
    person.attack("スライム")


'''
# 06:クラスからメソッドを呼び出してみよう

# 参考URL
【Python入門】クラスのインスタンス変数を隠す(プライベート変数)
https://pycarnival.com/mangling/

プライベートメンバ - Python学習講座（__変数名による隠蔽）
http://www.python.ambitious-engineer.com/archives/323

クラス — Python 3.6.5 ドキュメント（プライベート変数・名前マングリング）
https://docs.python.jp/3/tutorial/classes.html#private-variables
'''

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    def __init__(self):
        self.name = "wizard" #引数を使わないだけなら、コンストラクタのオーバーライドでインスタンス変数を定数にするだけでもできる。
        #super().__init__("wizard") #super classからメソッドを呼び出し
        
    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")
        
    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

wizard._Wizard__spell() #name mangling


# coding: utf-8
# クラスの中のメソッドを呼び出す

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)
        self.__say_yeah()

    def __say_yeah(self):
        print("YEAH YEAH YEAH!")


player = Greeting()
player.say_hello()

# coding: utf-8
# 親クラスのメソッドを呼び出す

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)
        
class Hello(Greeting):
    def say_hello(self):
        print(self.msg + " " + self.target)
        print("YEAH YEAH YEAH!")


player = Hello()
player.say_hello()

'''
# 07:クラス変数とクラスメソッド 
ここでは、Pythonのクラス変数とクラスメソッドを使います。
クラス変数とクラスメソッドは、オブジェクトで共通して利用できる変数です。

# 
オブジェクト間で共通して利用できるメソッドのこと。
動画では、2つの方法でクラスメソッドを作成しましたが、デコレータを使用する方法が推奨されています。

# 参考URL
クラスメソッド | Python-izm
https://www.python-izm.com/advanced/class_method/

# デコレータ
すでに定義されている関数に、新たに機能を追加できる仕組みのこと。
デコレータは、すでに用意されていたり、自分で作成したりすることができます。
動画では、@classmethodを使用しました。

@classmethod
def summary(cls):
    print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")

def summary(cls):
    print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")

summary = classmethod(summary)

上の2つのコードは、同じ処理をします。

# 参考URL
Pythonのデコレータの使い方 - Life with Python
https://www.lifewithpython.com/2014/12/python-decorator-syntax.html

Pythonのデコレータについて
https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e

クラス — Python 3.6.5 ドキュメント
https://docs.python.jp/3/tutorial/classes.html

Python のクラス変数とインスタンス変数って何？
http://nihaoshijie.hatenadiary.jp/entry/2018/01/15/225346
'''

class Player:
    __charactor_count = 0
    
    @classmethod #decoratorでclassmethod関数に追加
    def summary(cls):
        print(str(Player.__charactor_count) + "ninde slime wo attack")
        
    def __init__(self, name):
        self.name = name
        Player.__charactor_count += 1
        print(str(Player.__charactor_count) + " banme" + self.name + "gatoujoa")

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

    #summary = classmethod(summary)
    
class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")

    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

Player.summary()



'''
# 08:標準ライブラリを読み込んでみよう

# 参考URL
8.1. datetime — 基本的な日付型および時間型
https://docs.python.jp/3/library/datetime.html#module-datetime

協定世界時 (UTC)とは
https://wa3.i-3-i.info/word11831.html

10. 標準ライブラリミニツアー
https://docs.python.jp/3/tutorial/stdlib.html

11. 標準ライブラリミニツアー — その2
https://docs.python.jp/3/tutorial/stdlib2.html
'''

from datetime import datetime, timedelta, timezone

jst = timezone(timedelta(hours=9))
today = datetime.now(jst) #now is a classmethod, so no need to use variable
print(today)
print(today.year)
print(today.month)
print(today.day)

day = datetime.strptime("2030/01/10 06:02:19", "%Y/%m/%d %H:%M:%S")
print(day)

