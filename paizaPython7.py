''' # Python入門編7: 関数を理解しよう '''

'''
# 01:関数について学習しよう
'''

'''
# 02:関数を作ろう
関数の名前は、次のルールに従って付けます。
・1文字目：英語または、「_」(アンダーバー)
・2文字目以降：英語の大文字・小文字・数字「_」(アンダーバー)

例：
・ hello　 1文字目が、英小文字
・ _attack　 1文字目が、「_」(アンダーバー)
・ move01 2文字目以降に数字
・ move_left 2文字目以降「_」(アンダーバー)
・ moveLeft 2文字目以降に英大文字

慣習として、関数の先頭には大文字を使いません。
また、動詞を表す単語を使うと、コードがわかりやすくなります。
'''

# coding: utf-8
# Your code here!

# 関数を作る
# call any times with function name

def ljljl():    # define function by def
    print(4444)
    print("ggga")   
    i = 9
    i = i ** i
    print(i)

ljljl()


'''
# 03:引数と戻り値を追加しよう
プログラミング言語Pythonの引数と戻り値について学習します。
そして、関数を定義する時、引数と戻り値をどんなふうに記述するのか理解しましょう。

# 参考URL
Python3超入門【第９回】「ユーザー定義関数」 - RURUPI LOGS
http://rurupi.xyz/2016/12/11/introduction-to-python3-9/

Python3系の基礎文法（関数の使い方、クロージャ、ラムダ関数） - Qiita
https://qiita.com/Amtkxa/items/6a74cc5ab42bab131509

組み込み関数
https://docs.python.jp/3/library/functions.html'''

# coding: utf-8
# Your code here!

# 引数と戻り値を追加する

i = 30    # no need

def total(x, y):    # direct argument to chage function calcuration
    #print(x + 20 * y)    # arguments can use like variable
    return x * y    # return means, the result of function is a value and treat like object
    #x + y    # no declare of return make none
    
print(total(40, 3))    # input argument to use needless of variables 

num = total(3, 4)    # function result assigned to variable
print(num)


'''
# 04:スコープを理解しよう
変数の有効範囲であるスコープについて学習します。
スコープは、関数定義などを使いこなすため重要な機能ですので、しっかりと理解しましょう。

# スコープとは
変数の有効範囲が決まっていることです。
Pythonでは、関数定義の中と外ではローカル変数は分離しています。
同じ名前の変数があっても、独立しているので、それぞれ違う変数として扱われます。

# グローバル変数
スコープがなく、関数定義を超えて利用できます。
ただし、どこで値が代入されたのか分かりにくくなるので、あまり奨励されません。
'''

# coding: utf-8
# Your code here!

# スコープを理解する
# range of local variable
# inside of function is isolated from outside of function
message = "pai"
print(message)

a = 10
b = 333


def sum(x, y):
    a = 39    # outside a =/= inside a
    global message    # global variables are basically read only, but "global" declaration activates it to rewrite them
    message += "eee"    
    print(message + str(a))    # inside a is used
    print("scope is useful because create function without thinking of outside variable character")
    return x + y

num = sum(a, b)    # outside a, b is used
print(num)
print(message + str(a))


'''
# 05:RPGの攻撃シーンを作ろう
'''

# coding: utf-8
# Your code here!

# RPGの攻撃シーン
import random

def attack(e):
    print("yusha ha " + e + " wo kougeki")
    r = random.randint(1,10)
    #print(r)
    if r == 1:
        print("sugeeeeee!!" + e + " ni 10000000 damage!!!")
    else:
        print(e + "ni 3 damage")
    print()
    
enemies = ["slime", "dragon", "yush"]
for enemy in enemies:
    #print("yusha ha " + enemy + "wo kougeki")
    attack(enemy)


'''
# 06:引数のデフォルト値
関数で引数を省略した場合に利用できるデフォルト値や、
可変長引数という便利な記述方法について学習します。
'''

# coding: utf-8
# Your code here!

# 引数のデフォルト値
def introduce(greeting, name = "aho"):    
    print(name + " desu" + greeting)
'''
# default arguments
default argument is useful
when function called with blank argument and set default value as argument

# caution
when 2 or more arguments with 1 default argument,
default is arranged in the end of arrangements,
call function with 1 argument value
'''

introduce("aa", "yush")    # 2 arguments
introduce("t")    # 1 argument and 1 default
#--> yush desuaa
#--> aho desut

'''
# variadic arguments
*argument means list
'''
def variad(greeting, *names):    # declare list as argument
    for (i,name) in enumerate(names, 1):    # get index and value by enumerate() and begin index from 2nd argument = 1
        print(name + " da " + greeting + str(i))
variad("halo", "1", "2", "3")    # 1,2,3 used like list
#--> 1 da halo1
#--> 2 da halo2
#--> 3 da halo3

'''
# variadic arguments 2
**argument means dictionary
'''
def variadKey(**peaple):    # declare dictionary as argument
    for (name, greeting) in peaple.items():    # get key and value by items()
        print(name + " desu " + greeting)
    print(peaple)
variadKey(gg="123", kk="34")    # variadic argument ** dont need key ""
#--> gg desu 123
#--> kk desu 34
#--> {'gg': '123' 'kk': '34'}

dict = {"aa":123, "f":233}
print(dict["aa"])
dict["gg"] = 33
print(dict)

# RPGの戦闘シーン

def battle(*enemies):
	for enemy in enemies:
		print("戦士は" + enemy + "と戦った")

battle("スライム", "モンスター", "ドラゴン")
#--> 戦士はスライムと戦った
#--> 戦士はモンスターと戦った
#--> 戦士はドラゴンと戦った

#ballle(enemies):

#battle("スライム")
#--> 戦士はスと戦った
#--> 戦士はラと戦った
#--> 戦士はイと戦った
#--> 戦士はムと戦った


'''
# 07:キーワード引数を理解しよう
キーワード引数は、関数の引数にラベルを付ける機能です。
'''

# coding: utf-8
# Your code here!

# キーワード引数

def say(greeting = "ho", tar = "wo"):
    print(greeting + tar + " ttttaaaa")
    
say()
#--> howo ttttaaaa
say("tt", "44")
#--> tt44 ttttaaaa
say("gg ")    # omited 2nd argument, 2nd is filled with default
#--> gg wo ttttaaaa
say(greeting = "aaaa", tar = "1234")    # keyword argument
#--> aaaa1234 ttttaaaa
say(tar = "1234", greeting = "aaaa")    # keyword argument
#--> aaaa1234 ttttaaaa
say(greeting = "aaaa")    # keyword argument, omit 2nd argument
#--> aaaawo ttttaaaa
say(tar = "1234")    # keyword argument, omit 1st argument
#--> ho1234 ttttaaaa



