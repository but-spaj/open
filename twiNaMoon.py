""" based on Murahashi Kuriki, changed by _spaj_ 2020/08/30 """
"""
月齢に対応した絵文字をTwitterの名前に表示するスクリプトをもとに、
好みの地点の潮位データをそこに追記するようなlambda関数として作成しました。
作成にあたり、特に以下の情報を活用させていただきました。
先人の皆様ありがとうございました。

# ユーザー名の@を現在地の天気情報に変更するアプリを作って公開していた山本一成さん(@issei_y)のアイデアを見て、作成を始めた
https://qiita.com/issei_y/items/ab641746be2704db98be

# 自分は🌓だけでいいからPythonでやろう、と思ったらすでに村橋究理基さん(@mkuriki_ )が実装されていたので、そのままいただきました
https://qiita.com/mkuriki1990/items/9c78f285a50f14f31a23

# 初めて使うlambdaに手も足もでなかったところ、Pythonのスクリプトをlambda_functionに追記し、モジュールと合わせてZIPでアップロードするのは「ひろにぃ」さんのコードを参考
https://qiita.com/hirony/items/f63747d5e0326653cc4d

# 指定時刻にlambdaを起動したいときのEventBridge (CloudWatch Events) トリガー設定は、ドキュメントを参考
https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/services-cloudwatchevents-expressions.html

# Twitterの開発者ツールの登録はイッティさんのページを参考
https://www.itti.jp/web-direction/how-to-apply-for-twitter-api/
"""

import json
import sys
import io
import tweepy
import datetime
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
  # TODO implement
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-

  # The MIT License (MIT)
  # 
  # Copyright (c) 2020 Murahashi Kuriki
  # 
  # Permission is hereby granted, free of charge, to any person obtaining a copy
  # of this software and associated documentation files (the "Software"), to deal
  # in the Software without restriction, including without limitation the rights
  # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  # copies of the Software, and to permit persons to whom the Software is
  # furnished to do so, subject to the following conditions:
  # 
  # The above copyright notice and this permission notice shall be included in
  # all copies or substantial portions of the Software.
  # 
  # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  # THE SOFTWARE.


  # 日本語を吐き出すとエラーが出るので追加
  sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

  # OAuth認証部分
  CK      = ""
  CS      = ""
  AT      = ""
  ATS     = ""
  auth = tweepy.OAuthHandler(CK, CS)
  auth.set_access_token(AT, ATS)
  api = tweepy.API(auth)

  sc_name = api.get_user('_spaj_')
  print(sc_name.name)

  # 各月の絵文字
  moons = [
          "🌑", #1 新月
          "🌒", #2 三日月
          "🌓", #3 半月
          "🌔", #4 十三夜月
          "🌕", #5 満月
          "🌖", #6 寝待月
          "🌗", #7 弦月
          "🌘" #8 晦月
  ]

  # 現在の年月日時を int 型で取得
  dt_now = datetime.datetime.now()
  # JSTの年月日時に変換
  dt_jst = dt_now + datetime.timedelta(hours=9)
  timenow = dt_jst.strftime('%H:%M:%S')
  today = dt_jst.strftime('%Y') + "/" + dt_jst.strftime('%m') + "/" + dt_jst.strftime('%d')
  year = int(dt_jst.strftime('%Y'))
  month = int(dt_jst.strftime('%m'))
  day = int(dt_jst.strftime('%d'))
  hour = int(dt_jst.strftime('%H'))

  # 月ごとの定数の計算
  if month == 1 or month == 3:
      month_const = 0
  elif month == 2 or month == 5:
      month_const = 2
  else:
      month_const = month - 2

  # 月齢を計算し, 月齢ごとに emoji を割り振る
  moon_age = (((year - 11) % 19) * 11 + month_const + day) % 30

  if moon_age > 2.0 and moon_age <= 4.2:
      moon_num = 1
  elif moon_age > 4.2 and moon_age <= 8.4:
      moon_num = 2
  elif moon_age > 8.4 and moon_age <= 13.8:
      moon_num = 3
  elif moon_age > 13.8 and moon_age <= 15.8:
      moon_num = 4
  elif moon_age > 15.8 and moon_age <= 19.0:
      moon_num = 5
  elif moon_age > 19.0 and moon_age <= 22.8:
      moon_num = 6
  elif moon_age > 22.8 and moon_age <= 26.8:
      moon_num = 7
  else:
      moon_num = 0

  print("月齢 %d" % moon_age)
  moon = moons[moon_num]
  
# 潮位をスクレイピングするURLを格納
# 気象庁の潮位表から、好きな地点を選択してURLを貼る
load_url = "https://www.data.jma.go.jp/kaiyou/db/tide/suisan/suisan.php?stn=Z1"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 地点名を<h1>から取得する
h1 = soup.find("h1").text.replace("潮位表 ", "")
place = h1[0:h1.find("（")]
# 本日の潮位リスト
tide = []
# 本日日付のtrをtideリストに格納する
for tr in soup.find_all("tr", align="right"):
  if today in str(tr.contents[1]):
    for td in tr.find_all("td"):
      tide.append(td.text.replace(" ",""))
  # 満潮のうち、潮位の高い方をHWとする
  if int(tide[5]) > int(tide[3]):
    tHW = tide[4]
    hHW = tide[5]
  else:
    tHW = tide[2]
    hHW = tide[3]
  # 干潮のうち、潮位の低い方をLWとする
  if int(tide[13]) < int(tide[11]):
    tLW = tide[12]
    hLW = tide[13]
  else:
    tLW = tide[10]
    hLW = tide[11]
  
# Twitterの表示名を設定
nameStr = "_スペアジ!_@" + place + moon + "HHW" + tHW + "," + hHW + "cm, LLW" + tLW + "," + hLW + "cm"
print(nameStr)

# apiで表示名を書き込み
api.update_profile(name = nameStr)