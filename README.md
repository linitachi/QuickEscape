# QuickEscape

你莫名被帶到了奇怪的密室，你能逃出生天嗎!?
## 執行方法
```code=python
python ./main.py
```
或是直接點擊exe檔開始遊戲。
P.S exe檔要與picture在同一個目錄下。

## 玩法介紹

- 輪到你的回合時，玩家會隨機得到三個可以行動的指令，如果不喜歡，可以重新點擊骰子，重骰動作，每個骰子只有一次重骰的機會，可以重骰的骰子邊框會亮黃色。
- 決定完骰子後，點選confirm按鈕，開始行動回合，當重骰骰子的次數都用完時，會自動開始行動回合(也可直接選擇Stay動作結束回合)。
- 已翻開的房間才能旋轉，點擊房間來旋轉，旋轉後點選Rotate按鈕來旋轉完成，旋轉到一開始的位置就不會扣除旋轉次數。
- 要注意，每一輪玩家的回合順序是隨機的，因此第一回合可能順序為:玩家1>2>3，第二回可能是玩家2>3>。
- 每一回合玩家的移動以及旋轉指令都歸零的時候，該玩家回合會自動結束，但如果還有動作未執行，則需要使用Stay動作，主動結束回合。
- 找到出口後，回合結束時待在出口兩個回合的人即是勝利者!
- 當1到3人遊完時，共有12回合，4到6人則有9回合，回合歸零時，代表沒人逃生成功，遊戲結束!

## 玩家的行動

1. 移動:玩家移動到相連的房間，如果房間未翻開，則翻開該房間並移動進去，如果翻開後該房間後，玩家無法移動進去，則玩家待在原地。
2. 旋轉:玩家可以任意旋轉已翻開的房間方向。
3. \>_<:沒有任何事情可以做。
4. 待機:玩家待在目前所在的位置，並捨棄所有未行動的指令。

## 房間效果介紹

- 房間有進入效果、出去效果、待機效果

1. 三面走道:擁有三個路口的房間
2. 直線走道:擁有兩個路口的房間
3. 尖刺房間:擁有四個路口的房間，如果下回合還待在這裡，該玩家立即死亡
4. 加速房間:擁有兩個路口的房間，當玩家進入後，使玩家移動次數+1
5. 超加速房間:擁有兩個路口的房間，當玩家進入後，使玩家移動次數+2(與加速房間的出線機率為1:4)
6. 旋轉房間:擁有三個路口的房間，當玩家進入後，使玩家旋轉次數+1
7. 禁轉房間:擁有三個路口的房間，此房間禁止被旋轉(與旋轉房間的出線機率為1:3)
8. 重力房間:擁有四個路口的房間，當玩家進入後，使玩家移動次數-1
9. 超重力房間:擁有四個路口的房間，當玩家進入後，使玩家移動次數歸零(與重力房間的出線機率為1:5)
10. 交換房間:擁有四個路口的房間，當玩家進入後，與大廳以外的隨機一個房間交換，如果未翻開則翻開該房間，並執行交換後的房間進入效果

## 遊戲實機畫面

- 設定人數畫面
![](https://i.imgur.com/HzSaxk9.png)

- 遊玩畫面
![](https://i.imgur.com/kCcieym.png)

- 遊玩畫面2
![](https://i.imgur.com/PDOcxMH.png)
