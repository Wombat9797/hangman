# 知識を１つにまとめる

# <ハングマン>
def hangman(word):                                     #入力値(引数)word⇒プレイヤーに当てて欲しい文字列
    wrong = 0                                          #変数wrong⇒プレイヤーが間違った回数を数える
    stages = [
        "",
        "__________          ",
        "|         |         ",
        "|         |         ",
        "|         0         ",
        "|        /|\        ",
        "|        / \        ",
        "|                   "
    ]                                                  #変数stages⇒ハングマンの各パーツを保存したリストオブジェクト

    rletters = list(word)                              #変数rletters⇒プレイヤーが当てなければならない文字列をリストオブジェクトで保存
    board = ["_"] * len(word)                          #変数board⇒プレイヤーの解答状況を表示するリストオブジェクト
    win = False                                        #変数win⇒プレイヤーが勝ったかどうかを記録
    print("ハングマンへようこそ")

    #ゲーム進行するループ処理
    while wrong < len(stages) - 1:                     #whileループ：プレイヤーが間違った回数が「7回以下」の場合、ループ処理を継続
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)                              #変数char⇒プレイヤーが入力した文字を保存

        #正解か不正解かを判定
        if char in rletters:                           #if条件式⇒プレイヤーが入力した文字がrlettersリストに含まれている場合、コードブロックを実行
            cind = rletters.index(char)                #変数cind⇒プレイヤーが入力した文字がrlettersリストの中で最初に現れるインデックス値を取得
            board[cind] = char                         #boardリストの要素を更新⇒変数cindで取得したインデックス値の要素にプレイヤーが入力した文字を再保存
            rletters[cind] = "$"                       #rlettersリストの要素を更新⇒変数cindで取得したインデックス値の要素に「$」マークを再保存(取得するインデックス値の重複を防ぐため)
        else:                                          #if条件式がFalseの場合、プレイヤーが間違った回数を1回増やす
            wrong += 1
        
        #スコアボードを出力
        print(" ".join(board))                         #boardリストの各要素の間に空文字列を結合して文字列型オブジェクトとして出力

        #不正解に応じてハングマンを表示
        e = wrong + 1                                  #変数e⇒stagesリストのスライスの終了インデックスに使用する為、プレイヤーが間違えた回数に「+1」した値を保存
        print("\n".join(stages[0:e]))                  #stagesリストの要素をスライスで切り出して改行文字列を結合して文字列型オブジェクトとして出力

        #プレイヤーが勝ったかを判定
        if "_" not in board:                           #if条件式⇒boardリストにアンダースコア(_)が含まれていない場合、コードブロックを実行
            print(" ".join(board))                     #boardリストの各要素の間に空文字列を結合して文字列型オブジェクトとして出力
            print("あなたの勝ち")
            win =True                                  #変数winにTrueを再保存
            break                                      #breakキーワード⇒whileループ全体を終了して次のプログラムに進む
    
    #プレイヤーが負けた場合
    if win != True:                                    #if条件式⇒変数winにTrueが再保存されていない場合、コードブロックを実行
        print("\n".join(stages[0:wrong+1]))            #stagesリストのインデックス0-7の各要素の間に空文字列を結合して文字列型オブジェクトとして出力
        print("あなたの負け。正解は、{}".format(word))   #書式化文字列をformatメソッドでユーザーに当てて欲しい文字列(word)に置き換える

hangman("cat")

# <チャレンジ>
# 問題1
import random

answer_list = ["cat", "dog", "rabbit", "fox"]           #答えの文字列をリスト型オブジェクトとして保存
answer = random.choice(answer_list)                     #randomモジュールのchoiceメソッドを使用してリスト型オブジェクトanswerからランダムに1つの要素を取り出す

def hangman(answer):                                    #入力値(引数)answer⇒プレイヤーに当てて欲しい文字列
    #プログラムに使用する部品を用意
    wrong = 0                                           #変数wrong⇒プレイヤーが間違った回数を数える
    stages = [
        "",
        "__________          ",
        "|         |         ",
        "|         |         ",
        "|         0         ",
        "|        /|\        ",
        "|        / \        ",
        "|                   "
    ]                                                    #変数stages⇒ハングマンの各パーツをリスト型オブジェクトとして保存
    rletters = list(answer)                              #変数rletters⇒答えの文字列をリスト型オブジェクトとして保存
    board = ["_"] * len(answer)                          #変数answer⇒プレイヤーの解答状況をリスト型オブジェクトとして保存
    win = False                                          #変数win⇒プレイヤーの勝ち負けをブール型オブジェクトとして保存
    print("ハングマンへようこそ!")

    #ゲーム進行のループ処理
    while wrong < len(stages) - 1:                       #whileループ処理⇒プレイヤーの間違った回数が「7回以下」の場合、ループ処理を続ける
        print("\n")
        msg = "1文字を予想してね。"
        char = input(msg)                                #変数char⇒プレイヤーが入力した文字を保存

        #正解か不正解かを判定
        if char in rletters:                             #if条件式⇒プレイヤーが入力した文字がrlettersリストに含まれている場合、コードブロックを実行
            cind = rletters.index(char)                  #変数cind⇒プレイヤーが入力した文字がrlettersリストの中で最初に現れるインデックス値を取得
            board[cind] = char                           #boardリストの要素の更新⇒インデックス値cindに該当する要素にプレイヤーが入力した文字を再保存
            rletters[cind] = "$"                         #rlettersリストの要素を更新⇒インデックス値cindに該当する要素に「$」マークを再保存(取得するインデックス値の重複を防ぐ)
        else:                                            #if条件式がFalseの場合⇒プレイヤーが間違った回数を1回増やす
            wrong += 1
        
        #現在の解答状況を出力
        print(" ".join(board))                           #boardリストの各要素の間に空白文字列を結合して文字列型オブジェクトとして出力

        #ゲーム進行に応じてハングマンを出力
        e = wrong + 1                                    #変数e⇒プレイヤーの間違えた回数に応じてstagesリストをスライスする時の終了インデックス値として使用
        print("\n".join(stages[0:e]))                    #スライスを使用してstagesリストから要素を切り出して改行文字列を結合して文字列型オブジェクトとして出力

        #勝ったかを判定
        if "_" not in board:                             #if条件式⇒boardリストにアンダースコア(_)の要素が含まれていない場合、コードブロックを実行
            print(" ".join(board))                       #boardリストの各要素の間に空文字列を結合して文字列型オブジェクトとして出力
            print("あなたの勝ちです!!")
            win = True                                   #変数winにブール型オブジェクトTrueを再保存(=負け判定の条件式に使用)
            break                                        #breakキーワード⇒whileループ全体を終了
    
    #負けたかを判定
    if win != True:                                      #if条件式⇒変数winが「True」で無い場合、コードブロックを実行
        print("\n".join(stages[0:wrong+1]))              #スライスを使用してstagesリストの全要素(=インデックス0-7)の間に改行文字列を結合して文字列型オブジェクトとして出力
        print("あなたの負け!! 正解は、{}".format(answer))  #formatメソッドを使用して書式化文字列を入力値(引数)の値に置き換える

hangman(answer)

# <チャレンジ>
# 解答1
import math                                              #mathモジュールをインポート

def hangman():
    #解答候補を用意
    word_list = [
        "Python",
        "java",
        "computer",
        "hacker",
        "painter"
    ]                                                     #変数word_list⇒解答候補の文字列をリスト型オブジェクトとして保存
    random_number = random.randint(0, 4)                  #変数random_number⇒randomモジュールのrandintメソッドを使用して「0-4」の間で乱数を生成(インデックス値として使用)
    word = word_list[random_number]                       #変数word⇒変数random_numberに該当するインデックス値の要素をword_listリストから取得する

    #ゲームに使用する部品を用意
    wrong_guesses = 0
    stages = [
        "",
        "__________          ",
        "|         |         ",
        "|         |         ",
        "|         0         ",
        "|        /|\        ",
        "|        / \        ",
        "|                   "
    ]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("Welcome to Hanman!!")

    #ゲームを進行するループ処理
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter..")

        #正解か不正解かを判定
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = "$"
        else:
            wrong_guesses += 1
    
        #現在のスコアボードを表示
        print(" ".join(letter_board))

        #解答状況に応じてハングマンを表示
        print("\n".join(stages[0:wrong_guesses+1]))

        #勝ったかを判定
        if "_" not in letter_board:
            print("You win! The word was :")
            print(" ".join(letter_board))
            win = True
            break
    
    #負けたかを判定
    if win != True:
        print("\n".join(stages[0:wrong_guesses+1]))
        print("You lose! The word was {}.".format(word))

hangman()