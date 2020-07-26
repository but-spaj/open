#01:数値が一致した場合、メッセージを表示

# coding: utf-8
# if文による条件分岐

import random

a = random.randint(1,5)
if a > 2: #if jadge :
    b = 10
    print(b)
else: #else:
    print(a * 10)
    
#02:複数の条件を組み合わせてみよう
#if文で、複数の条件式を指定する「elif」について学習します。

# coding: utf-8
# if文による条件分岐　elif文
import random, sys

number = random.randint(1,3)
if number == 1:
	print( "スキ！")	#条件式が成立したときの処理
elif number == 2:
    sys.stderr.write("2") #std must be str
    sys.stdout.write("1")
else:
	print( "キライ")	#条件式が成立しなかったときの処理


#03:比較演算子で条件分岐してみよう
# coding: utf-8
# if文による条件分岐　比較演算子
import random

number = random.randint(1,5)
if number > 3:
	print("スキ！")	#条件式が成立したときの処理
elif number == 3:
    print(2)
else:
    print(1)

# a >= b
# a > b
# a == b
# a < b
# a <= b

#04:おみくじを作ってみよう
'''デバッグ (debug) とは、プログラムの不具合・欠陥を発見および修正し、
正常に動作させるための作業全般のことです。このような、プログラム上の
不具合・欠陥をバグ(bug)と呼びます。

動画の中では、デバッグとして、
randint関数で何の値がomikuji変数に代入されたかを出力して、
omiokuji変数の値に対して、if文が期待通りに動いているか確認しています。'''

# coding: utf-8
# おみくじを作る
# 比較演算子 == > < >= <= !=
# 大吉  中吉  小吉  凶  大凶

import random

omikuji = random.randint(1,10)

if omikuji % 2 == 0:
    print(omikuji)
    print(2)
elif omikuji >= 6:
    print(omikuji)
    print(6)
elif omikuji <= 3:
    print(omikuji)
    print(1)
else:
    print(omikuji)
        
#05:RPGのクリティカルヒットを再現 
#06:西暦から平成何年かを求めてみよう 
'''・today関数：現在の日付を返します。
https://docs.python.org/ja/3/library/datetime.html#date-objects'''

# coding: utf-8
# 西暦年から平成年を求める

import datetime
seireki = datetime.date.today().year
print("now is " + str(seireki) + " de ", end = "")
print(seireki - 1988)

