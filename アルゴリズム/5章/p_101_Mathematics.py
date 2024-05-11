K=int(input())
A,B=map(int,input().split())

#Kの倍数がA以上B以下の範囲の中にあるかどうかを記録する変数
ok=False

x=A//K
u=B//K

#x<uならばKの倍数がA以上B以下の範囲の中にある
if x<u:
    ok=True


if A%K==0:
    ok=True


#Kで割り切れる数があればOKを出力する
if ok:
    print("OK")
else:
    print("NG")