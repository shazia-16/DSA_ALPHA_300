def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
        
    min_price = prices[0]
    best_profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = prices[i] - min_price
            if profit > best_profit:
                best_profit = profit
                
    return best_profit