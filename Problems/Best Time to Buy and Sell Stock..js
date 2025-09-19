var maxProfit = function(prices) {
    let profit = 0;
    let lowest = Number.MAX_VALUE;
    for (let i = 0; i < prices.length; ++i) {
        lowest = Math.min(lowest, prices[i]);
        profit = Math.max(profit, prices[i] - lowest)
    }
    return profit;
};
