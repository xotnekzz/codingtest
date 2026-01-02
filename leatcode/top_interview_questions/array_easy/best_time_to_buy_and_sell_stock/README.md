# 📝 LeetCode 122. Best Time to Buy and Sell Stock II (심화 정리)

## 1. 문제 개요
여러 번의 주식 거래를 통해 얻을 수 있는 **최대 이익**을 구하는 문제입니다.
- 주식은 한 번에 한 주만 보유 가능합니다.
- 같은 날 팔고 다시 사는 것이 가능합니다.

---

## 2. 풀이 방법 1: Greedy (탐욕법) 
'어제보다 오늘 가격이 올랐다면' 무조건 그 차액을 더합니다.

### 💡 핵심 논리
- 전체 그래프에서 저점과 고점을 찾을 필요 없이, **작은 상승 구간(i-1일과 i일의 차이)을 모두 합치면** 결국 전체 상승분의 합과 같아집니다.

### 💻 코드
```python
def maxProfit(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```

- 시간 복잡도 : $O(n) — 배열을 딱 한 번만 순회합니다.
- 공간 복잡도 : $O(1)$ — total_profit 변수 하나만 있으면 됩니다.
---

## 3. 풀이 방법 2: DP (동적계획법)

주식 거래 과정을 **상태(State)**로 정의하고, 매일매일 나의 최적 상태를 갱신해 나가는 정석적인 방법입니다.

💡 핵심 논리: 상태(State) 정의
매일 장이 마감될 때, 다음 두 가지 상태 중 하나여야 합니다.

1. `hold` (주식 보유): 주식 구매함(이미 전에 구매했거나, 오늘 새로 구매했거나)
2. `free` (주식 미보유): 주식 없이 현금을 남김(어제도 미보유, 오늘 팔았거나)

📐 점화식 (Recurrence Relation)
어제의 `베스트 기록`만을 보고 오늘의 `베스트 기록`을 결정합니다.

1. `hold` : max(어제의 hold, 어제의 free - 오늘 가격)
2. `free` : max(어제의 free, 어제의 hold + 오늘 가격)

💻 코드

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: return 0
        
        # 첫날 초기화: 주식을 사거나(-price), 안 사거나(0)
        hold = -prices[0]
        free = 0
        
        for price in prices[1:]:
            # 쉼표(,)를 사용해 어제의 기록만 보고 동시에 업데이트 (Tuple Unpacking)
            hold, free = max(hold, free - price), max(free, hold + price)
            
        # 마지막 날엔 주식(종이조각)보다 현금(free)이 무조건 이득이므로 free 반환
        return free
```

- 시간 복잡도: $O(n) — 각 날짜별로 두 가지 상태(보유/미보유)를 계산합니다.
- 공간 복잡도: $O(n) — 모든 날짜의 최적 수익을 저장할 배열이 필요합니다.비유: 매일매일 "내가 주식을 들고 있을 때의 최대 수익"과 "안 들고 있을 때의 최대 수익"을 커다란 전지에 기록하며 나가는 것.
