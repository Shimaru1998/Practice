bands = [
    ["Takamatsu Tomori", "Chihaya Anon", "Kaname Rana", "Shiina Takki", "Nagasaki Soyo"], # Mygo
    ["Misumi Uika", "Wakaba Mutsumi", "Youtenji, Nyamu", "Yahada Umiri", "Togawa Sakiko"]  # Ave Mujica
]
# 使用巢狀/雙重迴圈 每一個元素都檢查一遍
# 如果是Mygo 回傳 0
# 如果是Ave Mujica 回傳 1
# 如果都不是 回傳 -1
def which_band(name) -> int:
    for i in range(len(bands)):
        for j in range(len(bands[i])):
            if name == bands[i][j] and i == 0:
                return 0
            elif name == bands[i][j] and i == 1:
                return 1
            else:
                continue
    return -1


print(which_band("Rinrinko"))
print(which_band("Togawa Sakiko"))
print(which_band("Ako"))
print(which_band("Kaname Rana"))