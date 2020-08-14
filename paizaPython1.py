''' # Python入門編1:プログラミングを学ぶ '''

'''
# 02:Pythonでプログラムを書いてみよう
関数名が、全て半角小文字で記述されていない。
（× Print、　○ print）
'''

# coding: utf-8
# hello worldと表示する

try:
    Print("hello")    # Upper is NameError
except NameError as e:
    print(e)
finally:
    print("fin")


'''
# 03:コメントでプログラムを見やすく！
Pythonでは、「#」から行末までがコメントになります。

複数の行をコメントアウトするときは、次のようにします。
・各行の先頭に「#」を記述する。
・3つの連続したシングルクォート「'」で囲む
'''

# coding: utf-8  #japanese character direction for python
# コメントを入力する
print("hel#lo")    # comment
# comment
#print("comment out ed")
'''
#-->
c
o
m
m
e
n
t
'''


'''
# 04:HTMLを表示してみよう
'''
'''print('''''''<h1>hello world</h1>
<p>世界の皆さん、
<b>こんにちは</b></p>'''''')'''

# coding: utf-8
# HTMLを表示する

print(1)
print("hello world")

print(2)    # in html output, between 1 and 2 as 1 line 
print('''<h1>asdf</h1><p>qwer</p><p>tyui</p>''')    # in html output, lines crlf ed by end tag 
print('''<h1>asdf</h1>,<p>qwer</p>,<p>tyui</p>''')    # in html output, lines crlf ed by end tag and , 

print(3)
print("asdf")
print("asdf")

print("asdf")    # in text output, crlf in code dont sence #in html output, crlf and , in code used as halfspace
print(4)
print("hello world")
print("hello world", "世界の皆さん、", "こんにちは")
print("asdf""asdf",     "asdf")    # in text and html output, , in () used as halfspace. but halfspace dont sence

print(5)
print("hello world", end="")
print("世界の皆さん、", end="")
print("こんにちは", end="")
'''print("hello world", end="")
print("世界の皆さん、", end="")
print("こんにちは", end="")
=
print("asdf""asdf""asdf")
print("hello world" "世界の皆さん、" "こんにちは")'''

print(6)
print("<h1>hello world</h1>" "<p>世界の皆さん、" "<b>こんにちは</b></p>")
print("<h1>hello world</h1>", "<p>世界の皆さん、", "<b>こんにちは</b></p>")
print("<h1>hello world</h1>""," "<p>世界の皆さん、""," "<b>こんにちは</b></p>")
print(7)
print("<h1>hello world</h1>", end="")    # end="" used to continue next as 1 line
print("<p>世界の皆さん、", end="")    # start tag interrupts line # end="" used to continue next as 1 line
print("<p>世界の皆さん、")    # start tag interrupts line
print("<p>世界の皆さん、", end="")    # start tag interrupts line # end="" used to continue next as 1 line
print("世界の皆さん、,", end="")    # end="" used to continue next as 1 line
print("世界の皆さん、", )    # , used to continue next as 1 line
print("世界の皆さん、")
print("世界の皆さん、")
print("<b>こんにちは</b></p>", end="")
print("<p>世界の皆さん、</p>", end="")
print("<p><b>こんにちは</b></p>", end="")

# text: 1print 1line. but , and end="" as crlf. 
# html: text on browser biew


'''
# 05:変数を使えるようになろう

× 1player 1文字目に数字は使えない
× class 重複
文字データを格納した変数と文字列は、「+」記号で連結できます。
'''

# coding: utf-8
# 変数を使う

import sys

try:
    player = "yusha"
    print(plaayer + "は、荒野を歩いていた")
    print(player + "は、モンスターと戦った")
    print(player + "は、モンスターをたおした")
except NameError as e:
    print(e)
    sys.stdout.write("e")    # stdout


'''
# 06:サイコロを作ろう
関数とは、Pythonが持つ特別な機能を呼び出す方法です。
print関数のように標準で利用できる関数と、
モジュールを組み込み(インポート)してから利用する関数があります。

# 参考URL
str()：数値を、数を表す文字に変換する関数です。
https://docs.python.org/ja/3/library/functions.html#func-str

randomモジュール
https://docs.python.org/ja/3/library/random.html

・random関数：0から1までの間で、ランダムな数値を返す
・randint関数：指定した引数の範囲で、ランダムな整数の値を返す
'''

# coding: utf-8
# 数の表示とサイコロ

import random

number = random.random() * 100
number2 = random.randint(1,10)
print("slime is " + str(number))


'''
# 07:演算子で計算してみよう
'''

# coding: utf-8
# 計算する
import random

number = 100 
print(number + 30 + random.randint(1,5))
print("slime is " + str(30))


'''
# 08:値段を計算してみよう 
'''


'''
# 09:データの型を覚えよう

# 参考URL
GoogleスタイルのPython Docstringの入門
https://qiita.com/11ohina017/items/118b3b42b612e527dc1d
'''