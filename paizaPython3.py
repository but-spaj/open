''' # Python入門編3: ループ処理を学ぶ '''

'''
# 01:数値を繰り返し表示してみよう
for inという、簡単な繰り返し命令について学習します。

繰り返しの回数を指定する
range(10) 0から9まで、10回繰り返す
range(6, 11) 6から10まで繰り返す
'''

# coding: utf-8
# for inによるループ処理

for i in range(1, 11):    # count up from a to b - 1 in range(a, b)
    print(i)    # 1 to 10
print("end with " + str(i))    # end with 10


'''
# 02:条件に合わせてくり返してみよう1
whileの使い方を学びます
'''

# coding: utf-8
# whileによるループ処理

i = 1    # reset counter variable i
while i <= 10:    # i must assigned before use in while
    print(i)
    i += 1    # i = i + 1 counter increase and roop while i <= 10
    print("next " + str(i))
print("end with " + str(i))    # end with 11


'''
# 03:条件に合わせてくり返してみよう2 
whileを使ったループ処理について、もう少し学習します。
そして、数値を10から1までカウントダウン表示させるプログラムを作ります。
さらに、whileの具体例として、RPGの攻撃シーンのようなプログラムを作ってみましょう。
'''

# coding: utf-8
# whileによるループ処理
import random

i = 1    # カウンタ変数を初期化
while i <= 10:
    print("+ " + str(i))    # 繰り返し処理
    i += 2    # カウンタ変数を更新 must be used
print("exp + " + str(i) + ", level up")

hp = i * 5
while hp > 0:
    print("hp = " + str(hp), end = "")
    hit = random.randint(1,5)
    print(" damage " + str(hit))
    hp -= hit
print("hp = " + str(hp) + ", dead")


'''
# 04:繰り返しでHTMLを作成しよう
ループ処理の具体例として、HTMLのプルダウンメニューを作成します。
そして、会員登録の入力フォームで年齢を1歳から100歳まで入力できるようにします。

<select name='age'>
  <option>1才</option>
  <option>2才</option>
  <option>3才</option>
</select>
'''

# coding: utf-8
# 年齢入力のプルダウン作成
print("<select name=\'age\'>")    # ' must ¥ ed between " and " 
for age in range(100):    # for i in range(): colon must be used
    print("<option>" + str(age + 1) + "sai</option>")
print("</select>")

print("<select name=\'aged\'>")
aged = 1
while aged <= 100:
    print("<option>" + str(aged) + "~" + str(aged + 9) +"class</option>")
    aged += 10
print("</select>")
    
print("<select name=\'sex\'>")
print("<option>man</option>")
print("<option>woman</option>")
print("</select>")


'''
# 05:データの読み込み（標準入力）
プログラムの外部からデータを入力する標準入力について学習します。
標準入力を使うと、ファイルのデータを読み込んだり、プログラムの実行時にデータを指定したりできます。

もともとはLINUXなどのUnix系OSで用意されていた仕組みです。
標準入力に対応するようにプログラムを作っておけば、
プログラム実行時に、ファイルを読み込んだり、キーボードからデータを読み込んだり、パラメータを指定したりというように、
入力先を切り替えることができます。
'''

# line = input()

# coding: utf-8
# inputによる入力処理

line = input()    # E0FError occures if no input
print(line * 5)    # input is str, 5 times printed
intline = int(input())    # convert into int 
print(intline + 5)    # intline as int can add 5


'''
# 06:複数データを読み込んでみよう
標準入力を使って、複数のデータを読み込む方法を学びます。
そのために、標準入力にループ処理を組み合わせます。

# データの行末の改行を削除する。
改行が残っていると、その後の処理に悪影響を及ぼすことがあるので、ここで削除しています。
インプットの後に、ドットに続けて記述することで、インプットの戻り値の改行を削除することができます。

line = input().rstrip()
'''

# coding: utf-8
# 標準入力とループ処理
count = int(input())    # only 1st input line, get input data counter
print("data " + str(count))
for i in range(count):    # use input data counter
    line = input().rstrip()    # only an input line # cut line end crlf
    print("hello " + line)


'''
# 07:西暦年と平成年の対応表を作ろう
'''