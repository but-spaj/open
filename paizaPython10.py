''' # Python入門編10: 例外処理を理解しよう '''

'''
# 01:例外処理の概要を理解しよう
実行時に発生する様々な問題に対してプログラムで対応する、例外処理について学習します。
プログラムを安定して動作させることでシステムの品質を高める、例外処理について理解を深めましょう。

NameError: name 'b' is not defined 変数が定義されていない実行時エラー(→ 例外:exception)

# 例外処理
try : バグ検出の範囲を予め決めておいて、例外を捕まえる
except : 捕まえた例外への対応方法を定める
raise : その場で対応しない　← は？
以上が適切に行われなければ、例外でプログラムが止まる。
'''


'''
# 02:簡単な例外処理してみよう

answer = 100 / number
ZeroDivisionError: division by zero

# 参考URL
エラーと例外 — Python 3.6.5 ドキュメント
https://docs.python.jp/3/tutorial/errors.html

これでマスター！try-exceptの使い方を学ぼう！ | 侍エンジニア塾ブログ
https://www.sejuku.net/blog/23044
'''

# coding: utf-8
# Your code here!

print(1)
try:    # try block
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:    # if except occurs in try block use error object as e variable
    print(e)
finally:    # どっちでもやってほしいコード
    print(2)

# coding: utf-8
# 例外処理を定義しよう

enemies = ["スライム", "ドラゴン", "魔王"]

number = 0
print("勇者は敵に遭遇した")
try:
    print("勇者は" + enemies[2 / number] + "と戦った")
except ZeroDivisionError as e:
    print(e)
finally:
    print("勇者は勝利した")



#03:いろいろな形式で例外に対応しよう 
#例外情報を表示するだけでなく、分かりやすいエラーメッセージを追加してみましょう

# coding: utf-8
# Your code here!
import traceback, sys

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("you cant divide by 0")
    #print(traceback.format_exc()) #get error as string
    sys.stderr.write(traceback.format_exc()) #standard error output
finally:
    print(2)
    
#traceback — スタックトレースの表示または取得 — Python 3.6.5 ドキュメント
#https://docs.python.jp/3/library/traceback.html

#sys — システムパラメータと関数 — Python 3.6.5 ドキュメント
#https://docs.python.jp/3/library/sys.html

# coding: utf-8
# 例外メッセージを指定しよう

import sys

enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[2 / number] + "と戦った")
except ZeroDivisionError as e:
    #print(e)
    sys.stderr.write("その敵は表示できません")
finally:
    print("勇者は勝利した")

#04:発生させる例外を変えてみよう
#ZeroDivisionErrorだけでなく、それ以外の例外についても捕まえましょう。

# coding: utf-8
# Your code here!

print(1)
try:
    number = 1
    answer = 100 / number
    print(answer2)
#except ZeroDivisionError as e: #used only when zeroDivison
#    print("0では割り算できません")
except NameError as e: #used only when undefined variable 
    print("assigned undefined variable")
    print(e)
finally:
    print(2)

# coding: utf-8
# 例外の種類を変更しよう その１

import sys

enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number1 = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[number2] + "と戦った")
except NameError as e:
    sys.stderr.write("未定義の変数を呼び出しています")
finally:
    print("勇者は勝利した")

#05:複数の例外を捕捉してみよう
#tryブロック内で発生する可能性のある複数の例外に対応できるよう、プログラムを改良していきましょう。
# coding: utf-8
# Your code here!

print(1)
try:
    number = 1
    answer = 100 / number
    print(answer2)
except ZeroDivisionError as e: #subclass of exception 1st read
    print("cant divide by 0")
    print(e)
except NameError as e: #subclass of exception 2nd read
    print("未定義の変数を呼び出しています")
    print(e)
except TypeError:
    print("typerr")
except SyntaxError as e: #didnt work why?
    print("syntax error")
    print(e)
except Exception as e: #superclass of all exception other read
    print("unexpected error")
    print(e)
else: #lf no except occured 
    print("ok")
finally:
    print(2)

#動画では、Exceptionクラスは、全ての例外クラスのスーパークラスと説明しました。ただ、Exceptionは、BaseExceptionクラスを継承しているので、全ての例外クラスのスーパークラスは、「BaseException」となります。BaseExceptionを継承していて、Exceptionを継承していない例外は、技術的な例外です。技術的な例外が発生した場合は、原則、プログラムを終了させる必要があるため、意図的に捕捉しないようにします。そのため、みなさんが全ての例外を捕捉したい時は、「Exception」を使うようにします。
#組み込み例外 — Python 3.6.5 ドキュメント
#https://docs.python.jp/3/library/exceptions.html#exception-hierarchy

#06:raiseで意図的に例外を投げよう
#例外を意図的に投げるraiseについて学習します。
#raiseを使うと、意図的に例外処理を起こすことが出来ます。また、exceptと組み合わせることで、メソッドの呼び出し元にある例外処理を利用できます。

# coding: utf-8
# Your code here!

print(1)
try:
    print(2)
    raise Exception("purposely exception")
    print(3) #raise skipps this, and go to except
except Exception as e: #must much raise and except
    print("予期せぬエラーが発生しました")
    print(e)
finally:
    print(4)

#Pythonで例外を発生させる：raise | UX MILK
#https://uxmilk.jp/39845

#07:例外は伝わる
#処理中に、例外が発生した場合、呼び出し元へその例外が伝わることを学習します。

# coding: utf-8
# Your code here!

def test_exception(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e: #catch exception
        print(5)
        raise e #use exception object as e then returns to call
    #finally:
        print(6) #if without finally, skipped by raise
    
print(1)
try:
    answer = test_exception(0) #interrupted by exception between 3 and 5 then raise go to exception
    print(7) #skipped by raise
except ZeroDivisionError as e: #raise e return here
    print(8)
    print(e)

# coding: utf-8
# 呼び出し元へ例外を伝えよう

import sys

def calc():
    return 100 / 0

try:
    print(calc())
except ZeroDivisionError as e:
    sys.stderr.write("0で割り算はできません")
    
#08:finallyをもっと理解しよう

# coding: utf-8
# Your code here!

def test_exception(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e:
        print(5)
        raise e
    finally: #can interrupt return answer
        print(6)

print(1)
try:
    answer = test_exception(0)
    print(7)
except ZeroDivisionError as e:
    print(8)
    print(e)

