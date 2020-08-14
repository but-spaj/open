''' # Python入門編4: リストの基礎 '''

'''
# 01:リストとは何かを学ぼう 
リストとは、まとまったデータを便利に扱うことができるデータ構造。
インデックスと呼ばれる番号で、それぞれのデータを区別します。

他のプログラミング言語では「配列」と呼ばれる機能が、Pythonでは「リスト」という名前で提供されています。
1.並び順管理が必要なデータ処理
 出席番号、座席順、パーティの並び順
 トランプや将棋などのゲームデータ
2.Webフォームの選択肢
 年齢、都道府県など
3.エクセルのような複数行データ
 CSVデータの処理

# 参考URL
リスト - Python入門 (注:printなど一部にPython2系が前提の記述があります。)
http://www.pythonweb.jp/tutorial/list/

リスト - Python入門から応用までの学習サイト (注:printなど一部にPython2系が前提の記述があります。)
http://www.python-izm.com/contents/basis/list.shtml

Python 言語リファレンス
https://docs.python.org/ja/3/reference/index.html

Python3系 基礎文法 - Qiita
http://qiita.com/rohinomiya/items/aab6b16d1a470871713c
'''


'''
# 02:リストを作ろう
'''

# coding: utf-8
# リストを作成する

player_1 = "hero"
player_2 = "wizzard"

print(player_1)
print(player_2)

team = [player_1, player_2, 100]    # use [] for list
print(team)


'''
# 03:リストの要素を取り出してみよう
リストでは、番号を使って要素を取り出します。また、その番号を変数で指定したり、計算して指定できます。

# 参考URL
リストの範囲外のインデックスにアクセスしたときにどうなるか? | hydroculのメモ
https://hydrocul.github.io/wiki/programming_languages_diff/list/index-out-of-bounds-exception.html

リストのサイズの取得(len関数) - リスト - Python入門 (注:printなど一部にPython2系が前提の記述があります。)
http://www.pythonweb.jp/tutorial/list/index5.html
'''

# coding: utf-8
# リストの要素を取り出す
import random

team = ["勇者", "魔法使い", 100]
print(team)

for j in team:
    i = random.randint(0,2)
    print(team[i])
print(team[i + 1])
print(len(team))    # len() used to count elements in list


'''
# 04:リストを操作しよう
リストの便利な機能を試します。そして、Pythonを使って、要素の追加、上書き、削除といった機能を使ってみましょう。

# append関数　リストの末尾に要素を追加
team.append("戦士")

# リストの要素を上書き
team[0] = "ドラゴン"

# リストの要素を削除
team.pop(0)

# 参考URL
素の追加と連結(append関数, extend関数) - リスト - Python入門 (注:printなど一部にPython2系が前提の記述があります。)
http://www.pythonweb.jp/tutorial/list/index6.html

要素の変更 - リスト - Python入門 (注:printなど一部にPython2系が前提の記述があります。)
http://www.pythonweb.jp/tutorial/list/index4.html

Pythonのリスト(配列)の削除のまとめ。先頭、末尾、指定の位置、複数、一致する値、全削除 - python入門 - python3系からのまとめ
http://coderoid.hatenablog.com/entry/2016/02/12/083000
'''

# coding: utf-8
# リストの要素を操作する

team = ["勇者", "魔法使い"]
print(team)
print(team[0])
print(len(team))

team.append("warrier")    # add an element to the last of list
print(len(team))
print(team)

team[1] = "dragoon"    # change element by assign
print(len(team))
print(team)

team.pop(0)    # pop can drop an element from list
print(len(team))
print(team)


'''
# 05:ループでリストを処理しよう
Pythonのfor inとリストを組み合わせて、HTMLのプルダウンリストを作成します。

# 参考URL
配列(リスト)の要素を1つずつ処理するには (for / foreach) | hydroculのメモ
https://hydrocul.github.io/wiki/programming_languages_diff/list/foreach.html

覚えるだけでPythonのコードが少し綺麗になる頻出イディオム - タオルケット体操
http://hachibeechan.hateblo.jp/entry/Python-idiom-101
'''

# coding: utf-8
# ループでリストを操作する

team = ["勇者", "戦士", "魔法使い"]    # list use []
print(team[0])    # [index]

for i in range(5):
    print(i)

print("<select name = 'job'>")
for i in team:    # assign each element in list for len
    print(i)    # assign 0,1,2,,, element 
    print(team[0])
    print("<option>" + i + "</option>")
    team.pop(0)
team.append(1)

print("</select>")
print(len(team))


'''
# 06:カンマ区切りデータを、splitで分割しよう 
標準入力から取り込んだデータをリストに格納する方法を学びます。
そのために、カンマで区切られた1行データを、区切りごとに分割してリストに格納します。
'''

# coding: utf-8
# 取り込んだデータをリストに格納する

line = input().rstrip().split(",")    # divide input with agg andget as list
print(line)
print(len(line))

for enemy in line:    # no need to get len of list
    print(enemy)


'''
# 07:複数行データを、リストに格納しよう
標準入力から読み込んだ複数の行のデータをリストに格納します。
その時に、読み込む行数が事前に分からなくても、きちんと対応できるようにしましょう。

# 参考URL
ファイルの中身を1行ずつテキスト処理するには | hydroculのメモ
https://hydrocul.github.io/wiki/programming_languages_diff/io/each-line.html

python: ファイルの読み込み–read()、readlines()、readline() (Python 入門) | OpenBook
https://openbook4.me/projects/147/sections/885
'''

# coding: utf-8
# 複数行データをリストに格納する
line = input().rstrip()    # use standard input with input().rstrip()
print(line)

import sys, random

try:
    array = []
    for line in sys.stdin.readlines():    # read some stdin lines by readlines()
        array.append(line.rstrip())    # add each lines to []
        print(array)
except Exception as e:
    print(e)
finally:
    print(array)


'''
# 08:リストを使ったランダムくじ 
# randrange関数 ランダムな値を生成します。
引数を1つ指定した場合は、ゼロから引数以下の値をランダムに生成します

# 参考URL
random — 擬似乱数を生成する
http://docs.python.jp/3/library/random.html

ライブラリ：random - Life with Python
http://www.lifewithpython.com/2013/04/random.html
'''

# coding: utf-8
# リストを使ったランダムくじ
# スライム,モンスター,ドラゴン,魔王

import random, sys
try:
    line = input().rstrip().split(",")    # use divide line with split(",")
    for enemy in line:    # each diveded lines added to [] 
        print(enemy + " !!!")
    
    #print(len(line))    # count line elements by len()
    
    #chooseEnemy = random.randint(0,len(line) - 1)
    chooseEnemy = random.randrange(len(line))    # randrange used to choose from len(line)
    damage = random.randint(1,10)
    print("you attacked " + line[chooseEnemy])
    print("!!!!!")
    print(line[chooseEnemy] + " " + str(damage * 10) + " damaged!")

except Exception as e:
    print(e)
    sys.stdout.write("error")
finally:
    print("you killed it !")



