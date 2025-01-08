# ファイル操作スクリプト README

このスクリプトは、コマンドラインからの引数を受け取り、さまざまなファイル操作を実行します。次の機能が含まれています。

## 📚 **関数一覧**

| 関数名             | 説明                                                                                 |
|--------------------|--------------------------------------------------------------------------------------|
| `reverse`          | `inputFilePath` にあるファイルを受け取り、`outputFilePath` にその内容を逆にしたファイルを作成します。 |
| `copy`             | `inputFilePath` にあるファイルのコピーを作成し、`outputFilePath` として保存します。     |
| `duplicate-contents` | `inputFilePath` にあるファイルの内容を読み込み、その内容を `count` 回複製します。        |
| `replace-string`   | `inputFilePath` にあるファイルの内容から文字列 `oldWord` を検索し、`newWord` に置き換えます。 |

---

## 🖥️ **使い方**

### **1. スクリプトの実行方法**
```bash
git clone https://github.com/ga-techcraft/file_manipulator_program
cd file_manipulator_program
python main.py <function> <args>
```

- `<function>`: 実行する関数名（`reverse`, `copy`, `duplicate-contents`, `replace-string`）
- `<args>`: 関数に渡す引数

### **2. 各関数の使用例**

#### **① reverse**
ファイルの内容を逆順にして新しいファイルを作成します。

```bash
python main.py reverse input.txt output.txt
```

**引数:**
- `input.txt`: 元のファイル
- `output.txt`: 出力ファイル

#### **② copy**
ファイルのコピーを作成します。

```bash
python main.py copy input.txt output.txt
```

**引数:**
- `input.txt`: 元のファイル
- `output.txt`: 出力ファイル

#### **③ duplicate-contents**
ファイルの内容を複製し、指定された回数だけファイルに追加します。

```bash
python main.py duplicate-contents input.txt 3
```

**引数:**
- `input.txt`: 元のファイル
- `3`: 複製回数（2以上100以下の整数を指定）

#### **④ replace-string**
ファイル内の指定した文字列を別の文字列に置き換えます。

```bash
python main.py replace-string input.txt oldWord newWord
```

**引数:**
- `input.txt`: 元のファイル
- `oldWord`: 置き換えたい文字列
- `newWord`: 新しい文字列

---

## ⚠️ **エラー処理**

スクリプトは、次のようなファイル操作時のエラーを処理します：

| エラータイプ           | 説明                                           |
|----------------------|----------------------------------------------|
| `FileNotFoundError`  | ファイルが見つからない場合に発生します。         |
| `PermissionError`    | ファイルにアクセスする権限がない場合に発生します。 |
| `IsADirectoryError`  | 指定したパスがディレクトリだった場合に発生します。 |
| `OSError`            | OSレベルのエラーが発生した場合に処理されます。    |

エラーが発生すると、適切なエラーメッセージが表示されます。

---

## 📂 **関数の追加方法**

### **関数を追加する手順**
1. スクリプト内に新しい関数を定義します。
2. `funcMap` に新しい関数を追加します。

#### **例: 新しい関数を追加する**
```python
def newFunction(arg1, arg2):
    # 新しい処理を記述
    pass

funcMap = {
    "new-function": newFunction
}
```

---

## ✅ **引数の検証**
スクリプトは、関数の引数の個数を検証し、正しくない場合はエラーメッセージを表示して終了します。

**検証方法:**
- 必要な引数の個数が不足している場合
- 引数の個数が多すぎる場合

---

## 🔧 **エラーメッセージの例**

| シナリオ                          | エラーメッセージ                             |
|---------------------------------|--------------------------------------------|
| 関数名が指定されていない         | `実行する関数名を入力してください。`        |
| 存在しない関数名が指定された     | `<function>は存在しません。`               |
| 引数の個数が合わない             | `<function>の引数の個数が合いません。`     |
| ファイルが見つからない場合        | `エラー: ファイルが見つかりません。`        |
| ファイルへのアクセス権限がない場合 | `エラー: ファイルにアクセスする権限がありません。` |

---

## 📄 **コードの概要**

### **1. ファイル操作関数**
- `reserveFile`: ファイルの内容を逆順にして保存
- `copyFile`: ファイルのコピーを作成
- `duplicateContents`: ファイルの内容を複製
- `replaceString`: ファイル内の文字列を置き換え

### **2. エラーハンドリング関数**
- `handlerFileError`: ファイル操作時のエラーを処理します。

---

## 🧑‍💻 **開発者向け情報**

### **動作環境**
- Python 3.8 以上

### **必要なライブラリ**
- 標準ライブラリのみ使用（`sys`, `os`, `inspect`）

