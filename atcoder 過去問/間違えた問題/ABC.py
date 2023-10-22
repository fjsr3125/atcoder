s = input()

flag = "flag"

# for i in range(len(s)):
#   if i == 0:
#     if s[i].isupper():
#       continue
#     else:
#       break
#   elif i != 0 and i != len(s):
#     if 100000 <= int(s[1:len(s)-1]) <= 9999999 and len(s[1:len(s)-1]) == 6:
#       continue
#     else:

if s[0].isupper():
  flag = "Yes"
else:
  flag = "No"
  print(flag)
  exit()

def isint(c):  # 整数値を表しているかどうかを判定
    try:
        int(c, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False  # 例外が発生＝変換できないのでFalseを返す
    else:
        return True 

if not isint(s[1:len(s)-1]):
  flag = "No"
  print(flag)
  exit()
if 100000 <= int(s[1:len(s)-1]) <= 999999 and len(s[1,len(s)-1]) == 7:
  flag = "Yes"
else:
  flag = "No"
  print(flag)
  exit()

if s[len(s)].isupper():
  flag = "Yes"
else:
  flag = "No"
  print(flag)
  exit()

print(flag)
