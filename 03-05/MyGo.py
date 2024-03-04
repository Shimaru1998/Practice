#################################
# 請只在這個區段寫 code
Mygo = ["高松燈", "千早愛音", "要樂奈", "長崎爽世", "椎名立希"]

def is_my_go(m):
    if m in Mygo:
        return True
    else: 
        return False
#################################

# 請寫一個 function is_my_go() 來判斷 person 的英文名字是不是 MyGo 成員
# P.S 可以嘗試用 Set 來實作
# 例如: is_my_go("豐川祥子") 回傳 False
#      is_my_go("高松燈") 回傳 True
print(is_my_go(input("輸入 MyGo 成員名字: ")))