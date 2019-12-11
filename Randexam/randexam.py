import random
import os

if os.path.exists('exam_suggest.txt'):
    os.remove('exam_suggest.txt') #ファイルのクリーンアップ

f = open('exam_answer.txt', 'r') #回答ファイルの読み込み
exam_answer = f.read()
f.close()

exam_answer = exam_answer.replace('\n','') #改行対策
exam_answer = exam_answer.replace('\r','')

print(exam_answer)
print(len(exam_answer))

exam_time = len(exam_answer) #繰り返し回数を文字数から取得

print('>>解答を開始します<<')

while exam_time != 0:
    exam_suggest = random.randint(1,4) #解答作成
    print(exam_suggest) #解答の表示
    f = open('exam_suggest.txt', 'a') #解答の書き込み
    f.write(str(exam_suggest))
    f.close()
    exam_time -= 1 #回数の変更

f = open('exam_suggest.txt', 'r') #解答ファイルの読み込み
exam_suggest = f.read()
f.close()

exam_suggest_list = list(exam_suggest) #問題のリスト化
exam_answer_list = list(exam_answer)

exam_time = len(exam_answer) #繰り返し回数を文字数から取得
list_num = 0 #リストの参照番号
exam_point = 0 #テストの得点の定義
exam_num = 1

print('>>採点を開始します<<')

while exam_time != 0:
    if exam_answer_list[list_num] == exam_suggest_list[list_num]:
        print('第{0}問 : 正解！'.format(exam_num))
        exam_num += 1
        exam_point += 1
    else:
        print('第{0}問 : 不正解！'.format(exam_num))
        exam_num += 1
    list_num += 1
    exam_time -= 1

print('正解数は{0}問でした。'.format(exam_point))

def input_end():
    print('終了するにはyを入力してください。')
    input_user = input('>>> ')
    if input_user == 'y':
        exit()
    else:
        input_end()

input_end()
