A = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    A.append(row)
M = [
    [False, False, False],
    [False, False, False],
    [False, False, False],
]  # テーブルを用意

# 選ばれた数字がビンゴカードに書かれているかを確認する。
for _ in range(0, N):
    b = int(input())
    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                M[i][j] = True

# ビンゴを達成しているかどうかを調べる。

# ビンゴを記録しているかを記録する変数
bingo = False
# 行を検査
for i in range(0, 3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

# 列を検査
for i in range(0, 3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

# 左上から右下に書けて斜めに3つ印がついているかを調べる。
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

# 右上から左下に書けて斜めに3つ印がついているかを調べる。
if M[0][2] and M[1][1] and M[2][0]:
    bingo = True


# 最終結果を出力
if bingo:
    print("Yes")
else:
    print("No")
