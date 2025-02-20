import sys
import markdown

args = sys.argv
markdownFilePath = args[2]
htmlFileName = args[3]

if len(args) != 4:
    print("引数の個数が不正です。再度プログラムを実行してください。")
    print("Usage:python3 file-converter.py markdown inputfileName.md outputfileName.html")
elif args[1] != "markdown":
    print("不正なコマンドです。再度プログラムを実行してください。")
    print("Usage:python3 file-converter.py markdown inputfileName.md outputfileName.html")
else:
    markdownContents = ""
    htmlContents = ""
    with open(markdownFilePath, "r") as f:
        markdownContents = f.read()
    
    #markdown文字列からhtml文字列への変換
    htmlContents = markdown.markdown(markdownContents)

    with open(htmlFileName, "w") as f:
        f.write(htmlContents)

    print("HTMLファイルへの変換が完了しました。")    
