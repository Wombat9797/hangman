# 知識を１つにまとめる

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