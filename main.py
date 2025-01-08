import sys
import os
import inspect

# ------------------------------------------定義部分------------------------------------------
# 関数一覧
# ①reverse inputFilePath outputFilePath: inputFilePath にあるファイルを受け取り、outputFilePath に inputFilePath の内容を逆にした新しいファイルを作成します。
# ②copy inputFilePath outputFilePath: inputFilePath にあるファイルのコピーを作成し、outputFilePath として保存します。
# ③duplicate-contents inputFilePath count: inputFilePath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputFilePath に count 回複製します。
# ④replace-string inputFilePath oldWord newWord: inputFilePath にあるファイルの内容から文字列 'oldWord' を検索し、'oldWord' の全てを 'newWord' に置き換えます。

# 関数の追加方法
# 以下に関数を定義し、ハッシュマップに追加する。

# ファイル操作時の例外処理の関数
def handlerFileError(e):
  if isinstance(e, FileNotFoundError):
    print('エラー: ファイルが見つかりません。')
  elif isinstance(e, PermissionError):
    print('エラー: ファイルにアクセスする権限がありません。')
  elif isinstance(e, IsADirectoryError):
    print('エラー: 指定したパスがディレクトリです。')
  elif isinstance(e, OSError):
    print('エラー: OSエラーが発生しました。')
  else:
    print(f'予期しないエラーが発生しました: {e}')

# ①inputFilePath にあるファイルを受け取り、outputFilePath に inputFilePath の内容を逆にした新しいファイルを作成します。
def reserveFile(inputFilePath, outputFilePath):
  try:
    with open(inputFilePath, 'r') as inputD:
      inputText = inputD.read()
      inputTextReversed = ''.join(reversed(inputText))

    with open(outputFilePath, 'w') as outputD:
      outputD.write(inputTextReversed)
      print(f'{inputFilePath}のテキストを反転させて{outputFilePath}に書き込みました。')
  except Exception as e:
    handlerFileError(e)

# ②inputFilePath outputFilePath: inputFilePath にあるファイルのコピーを作成し、outputFilePath として保存します。
def copyFile(inputFilePath, outputFilePath):
  try:
    with open(inputFilePath, "r") as inputD:
      inputText = inputD.read()
    
    with open(outputFilePath, "w") as outputD:
      outputD.write(inputText)
      print(f'{inputFilePath}のテキストを{outputFilePath}に書き込みました。')
  except Exception as e:
    handlerFileError(e)

# ③inputFilePath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputFilePath に count 回複製します。
def duplicateContents(inputFilePath, count):
  try:
    count = int(count)
    if count < 2 or count > 100:
      print(f'{sys.argv[1]}の第２引数(複製回数)には２以上100以下の数字を入力してください。')
      return

    with open(inputFilePath, 'r') as inputD:
      inputText = inputD.read()

    with open(inputFilePath, 'a') as inputD:
      for i in range(count - 1):
        inputD.write('\n' + inputText)
    print(f'{inputFilePath}のテキストを{count}個複製しました。')

  except ValueError:
    print(f'{sys.argv[1]}の第２引数(複製回数)には数字を入力してください。')
    return
  except Exception as e:
    handlerFileError(e)

# ④inputFilePath にあるファイルの内容から文字列 'oldWord' を検索し、'oldWord' の全てを 'newWord' に置き換えます。
def replaceString(inputFilePath, oldWord, newWord):
  try:
    with open(inputFilePath, 'r') as inputD:
      inputText = inputD.read()
      updateText = inputText.replace(oldWord, newWord)
    
    with open(inputFilePath, 'w') as inputD:
      if inputText == updateText:
        print(f'{inputFilePath}には文字{oldWord}が存在しません。')
      else:
        print(f'{inputFilePath}の文字{oldWord}を文字{newWord}に変換しました。')
      inputD.write(updateText)
  except Exception as e:
    handlerFileError(e)

# キーは関数名で、値は関数のハッシュマップ
funcMap = {
  "reverse": reserveFile,
  "copy": copyFile,
  "duplicate-contents": duplicateContents,
  "replace-string": replaceString
}

# --------------------------------------------------------------------------------------------

# 関数名が入力されているかどうか確認する
if len(sys.argv) < 2:
  print('実行する関数名を入力してください。')
  sys.exit()

# 入力された関数を取得する
inputFunc = sys.argv[1]

# 入力された関数が存在するかどうか確認する
if not inputFunc in funcMap:
  print(f'{inputFunc}は存在しません。')
  sys.exit()

# 引数の個数を確認する
NumsParameters = len(inspect.signature(funcMap[inputFunc]).parameters) 
if NumsParameters != len(sys.argv) - 2:
  print(f'{inputFunc}の引数の個数が合いません。')
  sys.exit()

# 関数を実行する
funcMap[inputFunc](*sys.argv[2:])