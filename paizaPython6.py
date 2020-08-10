#2次元リストとは何かを学ぼう
'''
データ構造とは　データの格納方法。
変数　player = "taro"
リスト　player[0] = "taro"
辞書　chara["yucha"] = "taro"
2次元リスト　party[0][2] = "pikatyu" party[0] = "taro"
'''
'''
2次元リストとは
2次元リストとは、2つのインデックスで要素を指定するリストのこと。
リストにリストを組み合わせて作成し、インデックスを2つ指定してデータを参照する。

多次元リストの用途
- RPGのマップ
- 写真・イラストなどのイメージ
- 3D-CGの空間座標
- ゲームの盤面
- 表形式データ

Python入門(6) リスト
http://www.ic.daito.ac.jp/~mizutani/python/intro6_python.html

5. データ構造 — Python 3.6.4 ドキュメント
https://docs.python.jp/3/tutorial/datastructures.html

リストオブジェクト - リスト - Python入門
https://www.pythonweb.jp/tutorial/list/index1.html
'''

#02:2次元リストを作成する

# coding: utf-8
# Your code here!

# 2次元リストを作成する

list = ["aa", "bb", "cc"]
print(list)
print(list[0])

for i in range(len(list)):
    print(list[i])
    
player = "taro"
team = [player, "ttt", "mafo"]
print(team)

team2 = [team[0], team[1], team[2]]    # element from other list
print("other team")
print(team2)
print(team2[0])

team_a = ["asd", "gagag", "tte"]
team_b = ["ted", "ghshgag", "tttte"]
team_c = ["msj", "hshg", "yhe"]
teams = [team_a, team_b, team_c]
print("lists in list")
print(teams)
print(teams[0])
print(teams[0][1])    # 1st index = 1st elements, 2nd index = element in 1st element

#03:2次元リストを操作する1 
#2次元リストの基本操作を学習します。リストの要素を更新したり、長さを調べたりしてみましょう。

# coding: utf-8
# Your code here!

# 2次元リストの基本操作1
'''要素の変更 - リスト - Python入門
https://www.pythonweb.jp/tutorial/list/index4.html

リストのサイズの取得(len関数) - リスト - Python入門
https://www.pythonweb.jp/tutorial/list/index5.html'''

team_a = ["asd", "gsgs", "ttte"]
team_b = ["assd", "gaasgs", "ettte"]
team_c = ["asxxd", "gsggsgs", "tttsgge"]
teams = [team_a, team_b, team_c]
print(teams)
print(teams[0])
print(teams[0][0])
print(teams[0][1])
print(teams[0][2])

teams2 = [["asd", "gsgs", "ttte"], ["assd", "gaasgs", "ettte"], ["asxxd", "gsggsgs", "tttsgge"]]
teams2[0][0] = "taro"
print(teams2)
print(len(teams2))    # count elements in list
print(len(teams2[0]))    # count elements in list in list

#2次元リストを操作する2 
#要素を追加・削除する基本的な操作を実際に試してみましょう。

# coding: utf-8
# Your code here!

# 2次元リストの基本操作
'''要素の追加と連結(appendメソッド, extendメソッド) - リスト - Python入門
https://www.pythonweb.jp/tutorial/list/index6.html

要素の削除(del文, popメソッド, removeメソッド) - リスト - Python入門
https://www.pythonweb.jp/tutorial/list/index8.html'''

teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
print(teams)
print(len(teams))

teams.append(["gagaga", "ssgsg", "tetaa", "ktte"])    # add element in list
print(teams)
print(len(teams))

teams[3].append("taaa")
print(teams)
print(len(teams))

del teams[1]    # delete element in list
print(teams)
print(len(teams))

del teams[0][1]    # delete element in list in list
print(teams)
print(len(teams))

print("slice")
teams[len(teams):len(teams)] = "slice"    # change elements between last and last = last place to inserted elements list or elements divided
print(teams)

teams[len(teams):len(teams)] = ["slice", "tea"]    # change elements between last and last = last place to inserted elements
print(teams)

teams[len(teams)-1:len(teams)] = ["ahe", "tya"]    # change elements between -1 and last = -1 place to inserted elements
print(teams)

teams[len(teams)-5:len(teams)-1] = ["rice", "rea"]    # change elements between -5 and -1 = -5 and -4 ~ -2 place to inserted elements
print(teams)

print("extend")
teams.extend(teams)    # elongate list, not add as list
print(teams)

print("+")
num = ["123", "234"]
adin = teams + num
print(adin)
adon = adin + ["444", "4221"]
print(adon)

print("-")
adon[1:22] = ""
print(adon)
adon[1:2] = []
print(adon)

print("*")
adonn = adon * 3
print(adonn)
adonnn = [adon] * 3
print(adonnn)

print("remove")
print(adonnn.remove(adon))    # remove all elements matched with argument
print(adonnn)
inin = ["1", "2", "3"]
ininn = inin * 3
print(ininn)
print(ininn[0:2])
innin = [inin] * 2
print(innin)

print("pop")
print(innin.pop())    # get ()elements and remove
print(innin)

#05:ループでリストを処理する
#2次元リストから離れて、ループを使ってリストを処理する方法について、さらに理解を深めます。たくさんのデータを持つリストを処理するには、ループ処理が欠かせません。2次元リストを使う時にも活躍します。

'''enumerate関数でインデックスつきループを行う - Python Tips
http://www.gesource.jp/programming/python/code/0022.html

Python, enumerateの使い方: インデックスを1から開始 | Python / note.nkmk.me
https://note.nkmk.me/python-enumerate-start/'''

# coding: utf-8
# Your code here!

# ループでリストを処理する
team = ["yusha", "sensi", "mahotsu"]
print(team)
print(team[0])

for (i,person) in enumerate(team):    # output index with value, like items of dictionary
    print(str(i + 1) + " ninn no " + person + "ga, slime to tatta")    # index starts 0 + 1
    
numbers = [3, 1, 3 ,4, 5]
result = []    # create list before insert
results = []
for (j,item) in enumerate(numbers):
    results.append((j + 1) ** item)
print(results)
print(len(results))
results[0:len(results)] = []
print(results)

for k in range(0, 10):
    for l in range(0, 10):
        # print(str(k) + " ** " + str(l) + " = " + str(k ** l))
        result.append(k ** l)
        # print("result = " + str(result))
        print(str(k) + ", " + str(l))
    print(result)
    results.append(result)    # add list into 2d list
print(results)

#06:2次元リストをforで作成する
#forを使って2次元リストを作成してみましょう

'''for文 - 繰り返し - Python入門
https://www.pythonweb.jp/tutorial/for/index3.html
繰返し処理 - for, while 等 - Python 入門
http://python.keicode.com/lang/control-flow-loop-for-while.php
【Python入門】for文の使い方総まとめ | 侍エンジニア塾ブログ | プログラミング入門者向け学習情報サイト
https://www.sejuku.net/blog/24766'''

# coding: utf-8
# Your code here!

# 2次元リストをforで作成する

numbers = []
numbers2 = [[1]]
print(numbers2[0])

for i in range(10):
    print(i)
    #numbers2[i].append(1)
    for j in range(10):
        print(numbers2[0])
        #numbers2.append(j)
        #numbers2[i][j] = [j]
        print(numbers2)
    #numbers[len(numbers):len(numbers)] = [numbers2]
    #numbers2.append([1,2,3,4,5,6,7,8,9])

#print(numbers2)
#sum = i + sum for i in range(10)    # invalid syntax
#print(sum)

numbers3 = [i + i for i in range(1, 11)]    # insert elements for i times 
print(numbers3)

numbers4 = [[i + 1 for i in range(3)] for j in range(4)]    # repeat A for j times ; A is code berfore (2nd for)
numbers4[0][2] = 2
print(numbers4)

#07:ドット絵を表示する
#2次元リストで、簡単なドット絵を表示してみましょう。元になるイラストのドットの有無を、数字のゼロイチで表して、テキストで表示します。

# coding: utf-8
# Your code here!

# ドット絵を表示する

enemy_img = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]]


for line in enemy_img:
    for dot in line:
        #print(dot)
        if dot == 1:
            print("#", end = "")    # end="" means dont crlf
        else:
            print(" ", end = "")
    print()    # this do crlf

#08:3次元リストで複数のドット絵を表示する
#複数のドット絵を表示するために、3次元リストを使ってみます。ドット絵のパターンごとに、リストを切り替えて表示してみましょう。

# coding: utf-8
# Your code here!

# 3次元リストでドット絵を表示する

enemy_img = [[[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]],
             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1],
             [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
             [0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]],
             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1],
             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]]]

for img in enemy_img:
    for line in img:
        for dot in line:
            if dot == 1:
                print("#", end = "")
            else:
                print(" ", end = "")
        print()
        
#09:enumerateで2次元リストを操作する
#Pythonのenumerateを使って、2次元リストを出力します。具体的な例として、RPGの簡単なマップを作って、城と町の間を道路で接続します。

# coding: utf-8
# Your code here!

# 2次元リストで地図を表示する

map = [["森" for i in range(20)] for j in range(10)]
map[0][0] = "城"
map[0][19] = "町"
map[9][19] = "町"

for i,line in enumerate(map):
    print(str(i) + "; ", end = "")
    line[5] = "川"
    for dot in line:
        print(dot, end = "")
    print()
    
#10:2次元リストのマップに道を追加する
# coding: utf-8
# Your code here!

# 2次元リストで地図を表示する

landmap = [["森" for i in range(20)] for j in range(10)]
landmap[0][0] = "城"
landmap[0][19] = "町"
landmap[9][19] = "町"
for i,line in enumerate(landmap):
    print(str(i) + ":", end="")
    for (j,area) in enumerate(line):
        if (i % 2 == 0 or j % 3 == 0) and area == "森":    # control and
        #if (j % 3 == 0 or i % 2 == 0) and area == "森":    # control and
        #if i % 2 == 0 or j % 3 == 0 and area == "森":    # control and
        #if j % 3 == 0 or i % 2 == 0 and area == "森":    # control and
        #if j % 3 == 0 or (i % 2 == 0 and area == "森"):    # control and
        #if i % 2 == 0 or (j % 3 == 0 and area == "森"):    # control and
    
            print("＋", end="")
        else:
            print(area, end="")
    print()


#11:標準入力から2次元リスト
#標準入力から2次元リストを読み込んでみます。複数行のカンマで区切ったデータを用意して、それを2次元リストに割り当てます。

# coding: utf-8
# Your code here!

# 標準入力から2次元リスト

enemy_imag = []
while True:
    line = input()
    if line == "_":    # while need to declare an end point
        break
    #print(line.split(","))
    enemy_imag.append(line.split(","))    # capture input to use as 2d liset
#print(enemy_imag)

for line in enemy_imag:
    for dot in line:
        if int(dot) == 1:
            print("#", end = "")
        else:
            print(" ", end = "")
    print()

# 標準入力から、2次元リストを読み込む

# 標準入力のデータ
# 0,0,1,1,0,0
# 0,1,0,0,1,0
# 1,0,0,0,0,1
# 1,1,1,1,1,1
# 1,0,0,0,0,1
# 1,0,0,0,0,1
# _

letter_A = []
letter_B = []

while True:
    line = input()
    if line == "_":
        break
    else:
        letter_A.append(line.split(","))

print(letter_A)
    # ここに、読み込んだデータをリストに追加するコードを記述する
letter_B = [[str(dot) for dot in line] for line in letter_A]
print(letter_B)

#12:2次元リストで画像を配置
#標準入力から読み込んだ2次元リストデータに合わせて、RPGのキャラクターを配置して表示してみます。将棋のコマの初期状態のような感じで、画像を表示してみましょう

'''Python入門編3: ループ処理を学ぶ「データの読み込み（標準入力）」 | プログラミング学習ならpaizaラーニング
https://paiza.jp/works/python3/primer/beginner-python3/4024

文字列を分割する！Pythonでsplit関数を使う方法 | TechAcademyマガジン
https://techacademy.jp/magazine/15553'''

# coding: utf-8
# Your code here!

# 2次元リストで画像を配置

# 画像用リスト
players_img = [
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Empty.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Dragon.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Crystal.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Hero.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Heroine.png"]

# load rayout data

team = []
while True:
    line = input()
    if line == "_":
        break
    else:
        team.append(line.split(","))    # split divides element into  elements
        #print(line)
#print(team)

# display along rayout
print("<table>")
for line in team:
    print("<tr>")
    for person in line:
        print("<td><img src='" + players_img[int(person)] + "'></td>")
    print("</tr>")
print("</table>")

