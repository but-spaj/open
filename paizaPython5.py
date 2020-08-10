#01:辞書とは何かを学ぼう
#連想配列のこと
#リストの箱に名前をつけることができる
'''辞書(ディクショナリ) - Python入門
https://www.pythonweb.jp/tutorial/dictionary/

Python - 辞書（ディクショナリ）の使い方 - ざっくりん雑記
http://azuuun-memorandum.hatenablog.com/entry/2015/05/01/075000

Pythonで辞書（ディクショナリ）型を使う方法【初心者向け】 | TechAcademyマガジン
https://techacademy.jp/magazine/15639'''

#02:辞書を作る
# coding: utf-8
# Your code here!

# リストのおさらい
enemyArray = ["a","b","c"]
print(enemyArray)
print(enemyArray[0])
num = 2
print(enemyArray[num])
print(len(enemyArray))

# dictionary
enemyDictionary = {"za":"a","ch":"b","la":"c"}
print(enemyDictionary)
print(enemyDictionary["ch"])
try:
    level = "la"
    print(enemyDictionary[level])
except KeyError as e:
    print(e)
    
#03:辞書の基本操作
#Pythonを使って辞書の追加、上書き、削除といった機能を試してみましょう。
# coding: utf-8
# Your code here!

# 辞書の基本操作
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["ザコ"])
print(len(enemies))
print(enemies["ザコ"])
enemies["123"] ="asdf"    #add element to dictionary
print(enemies["123"])
enemies["ザコ"] = 123    #change element in dictionary

del enemies["ザコ"]    #delete element from dictionary
print(len(enemies))

#04:辞書をループで処理する
#Pythonのitemsと辞書を組み合わせてみましょう。
'''【Python入門】for文を使った繰り返し文の書き方 | プロスタ
http://programming-study.com/technology/python-for/

Python: 辞書の全てのキーと値をたどる – items(), keys(), values()メソッド
http://www.yukun.info/blog/2008/06/python-dict2.html

キーと値のリストを取得(keysメソッド, valuesメソッド, itemsメソッド) - 辞書 - Python入門
https://www.pythonweb.jp/tutorial/dictionary/index8.html'''

# coding: utf-8
# Your code here!

# 辞書をループで処理する

# list: how to use
enemiesList = []
enemiesList.append("qwe")
enemiesList.append(123)
enemiesList.append("34g")
enemiesList.append("1515")
print(enemiesList)
print(enemiesList[2])
for ene in enemiesList:
    print(ene)
print("----")
for enemies in range(len(enemiesList)):
    print(enemies)
    print(enemiesList[enemies])

# 辞書のおさらい
print("---dictionary---")
enemiesDictionary = {"123":"13", "234":"24", "345":"35"}
enemiesDictionary["qwe"] = "gagaga"
print(enemiesDictionary)
for i in enemiesDictionary:
    print(i)
    print(enemiesDictionary[i] + " appeared !!")
for (j, k) in enemiesDictionary.items():    # items can put key and value in variables
    print(j + ", who is " + k + " is coming !!")
    
# ループで辞書のキーと値を出力しよう

skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# この下で、ハッシュの値をループで出力してみよう

for (lank, skill) in skills.items():
    print(lank + "は" + str(skill) + "です")
    
# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう

for i in points:
    sum = sum + int(points[i])
print(sum)

sum2 = 0
for (j, k) in points.items():
    sum2 = sum2 + k
print(sum2)

#05:リストの整列 
#リストのソートについて学習しましょう。リストをソートすると、データをアイウエオ順・数字順といった具合に整列することができます
'''[Python] コレクション型をソート - Qiita
https://qiita.com/ysk24ok/items/b546471c37b2f443f4c7#%E8%BE%9E%E6%9B%B8

Python sortのまとめ (リスト、辞書型、Series、DataFrame) - Qiita
https://qiita.com/shizuma/items/40f1fe4702608db40ac3

【Python入門】list sortでリストの中身を効率的にソートする方法 | プロスタ
http://programming-study.com/technology/python-list-sort/'''

# coding: utf-8
# Your code here!

# リストの整列
weapons = ["うして", "いうと", "そそい", "たとい"]
print(weapons)

print(sorted(weapons))    #sort hiragana
print(sorted(weapons, reverse = True))    #sort reverese

weapons2 = ["4.うして", "2.いうと", "20.そそい", "89.たとい"]
print(sorted(weapons2))    # sorted by numbers

weapons3 = ["蘇うして始祖", "い得うと", "そそ足そい", "た憂ううとい"]
print(sorted(weapons3))    # sorted by some utf-8

#06:辞書の整列
'''[Python] コレクション型をソート - Qiita
https://qiita.com/ysk24ok/items/b546471c37b2f443f4c7#%E8%BE%9E%E6%9B%B8

Python sortのまとめ (リスト、辞書型、Series、DataFrame) - Qiita
https://qiita.com/shizuma/items/40f1fe4702608db40ac3

【Python入門】list sortでリストの中身を効率的にソートする方法 | プロスタ
http://programming-study.com/technology/python-list-sort/'''

# coding: utf-8
# Your code here!

# 辞書の整列
weapons = {"sord":30, "tea":21, "apple":225 }
print(weapons)
print(sorted(weapons))    # sorted by keys and output is list
print(sorted(weapons.items()))    # sorted by keys and output is taple list

print(weapons.items())    #dict_items has no index

#07:RPGのアイテム一覧を再現
# coding: utf-8
# Your code here!

# 画像用ハッシュ
item_images = {
    "剣":"http://paiza.jp/learning/images/sword.png",
    "盾":"http://paiza.jp/learning/images/shield.png",
    "回復薬":"http://paiza.jp/learning/images/potion.png",
    "クリスタル":"http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順配列
items_order = ["クリスタル", "盾", "剣", "回復薬", "回復薬", "回復薬"]

# print(item_images)
# print(items_order)

# アイテム名を取り出す
for item_name in items_order:
# 画像ファイル名を取り出す
    print("<img src = '" + item_images[item_name] + "'>")
    print(item_name + "<br>")
    
# 画像用辞書
items_img = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
items_order = ["剣", "盾", "回復薬", "クリスタル"]

# ここから下を記述しよう

# call items_img by items_order order

for item in items_order:
    # print(item)
    # print(items_img[item])
    # set html for img
    print("<img src = '" + items_img[item] + "'><br>")

# 画像用辞書
items_img = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# ここから下を記述しよう

line_count = int(input())
print(line_count)
for i in range(line_count):
    # print(input())
    print("<img src = '" + items_img[input().rstrip()] + "'>")
    
    