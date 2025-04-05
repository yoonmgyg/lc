class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1
        last_span = 0
        while self.stack and price >= self.stack[-1][0]:
            value, last_span = self.stack.pop() #getting span of the element on top of the stack
            span += last_span
        self.stack.append((price, span)) # In the end we have the span for current price and we add it to the stack.
        return span
