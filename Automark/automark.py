def mark_start():
    def mark_start_answer():
        print('まずは答えを入力してください。')
        mark_answer = input('>>> ') #答え入力
        mark_start_answer_check(mark_answer)

    def mark_start_answer_check(mark_answer):
        if mark_answer.isdecimal() != True:
            print('数字で入力してください。')
            mark_answer = mark_start_answer()
        else:
            mark_start_suggest(mark_answer)

    def mark_start_suggest(mark_answer):
        print('次にあなたの解答を入力してください。')
        mark_suggest = input('>>> ') #解答入力
        mark_start_suggest_check(mark_suggest, mark_answer)

    def mark_start_suggest_check(mark_suggest, mark_answer):
        if mark_suggest.isdecimal() != True:
            print('数字で入力してください。')
            mark_suggest = mark_start_suggest(mark_answer)
        else:
            mark_start_do(mark_suggest, mark_answer)

    def input_end():
        print('\n終了するにはyを入力してください。\nもう一度採点するにはnを入力してください。')
        input_user = input('>>> ')
        if input_user == 'y':
            exit()
        if input_user == 'n':
            mark_start()
        else:
            input_end()

    def mark_start_do(mark_suggest, mark_answer):
        if len(mark_suggest) != len(mark_answer):
            print('問題数が違います。')
            mark_start_answer()
        else:
            mark_suggest_list = list(mark_suggest)
            mark_answer_list = list(mark_answer)

            mark_time = len(mark_answer)

            list_num = 0 #リストの参照番号
            mark_point = 0 #テストの得点の定義
            mark_num = 1

            print('>>採点を開始します<<')

            while mark_time != 0:
                if mark_answer_list[list_num] == mark_suggest_list[list_num]:
                    print('第{0}問 : 正解！'.format(mark_num))
                    mark_num += 1
                    mark_point += 1
                else:
                    print('第{0}問 : 不正解！'.format(mark_num))
                    mark_num += 1
                list_num += 1
                mark_time -= 1

            print('正解数は{0}問でした。'.format(mark_point))
            input_end()

    mark_start_answer()

print('======================================================\n\nAutomark - オートマーク（マークテスト自動採点ソフト）\nby Minato86\n\n======================================================')
mark_start()
