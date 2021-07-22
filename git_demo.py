# This is Git Demo

# ユーザー名を設定する。

# git config --global user.name "ユーザー名"
# メールアドレスを設定する。

# git config --global user.email メールアドレス



# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/AISTARWORKS/git-demo2.git
# git push -u origin main

# 1つ前のcommitに戻す
# git reset --hard HEAD

# 任意のcommitに戻す
# git log
# commit XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# // ３，git logでどこの部分まで戻したいかを確認できたらcommitの隣に書いてあるID的なものを入力
# git reset --hard <commitID>

# // ４（ここでエラー発生したら手順６へ），現在連携しているリポジトリを削除する
# git remote rm <現在接続しているリポジトリのURL>

# // ５，新しく連携するリモートリポジトリを登録する
# git remote add <本来のリポジトリのURL>

# // ６（５ができたらここはやる必要無し），しかし今回の場合はGithub上から元々連携していたリポジトリが削除されていたので（絶対やっちゃダメ）URLを変更することで対処
# git remote set-url origin <本来のリポジトリのURL>

# // ７，最後は強引にmain or masterブランチにpushして内容を反映させる
# git push -f origin main or master

print('This is Git Demo....')
print('This is Git Demo....')
print('6th commit')
