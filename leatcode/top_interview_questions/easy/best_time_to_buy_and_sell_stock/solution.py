class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += (prices[i] - prices[i-1])
        return profit   

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices: return 0
        
        # -inf(무한대)로 초기화하는 것도 좋은 습관입니다 (첫날 반드시 사게 유도)
        hold = -float('inf')
        free = 0
        
        for price in prices:
            # 어제의 상태를 기준으로 오늘 상태를 동시에 갱신
            hold, free = max(hold, free - price), max(free, hold + price)
            print(f"hold(매수): {hold}")
            print(f"free(매도): {free}")
            
        return free

if __name__ == "__main__":
    #prices = [7,6,4,3,1]
    prices = [7,1,5,2,6]
    #prices = [1,2,3,4,5]
    print(Solution().maxProfit2(prices))
