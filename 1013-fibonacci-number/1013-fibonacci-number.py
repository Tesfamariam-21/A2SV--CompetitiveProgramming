class Solution:
    def fib(self, n: int) -> int:
        first, second = 0, 1

        for i in range(n):
            temp = first
            first = second + first
            second = temp

        return first  

        # dict_ = defaultdict(int)

        # def f(n):
        #     if n < 2:
        #         dict_[n] = n
        #         return n
        #     if n not in dict_:
        #         dict_[n] = f(n-1) +f(n-2)
            
            
        #     return dict_[n]

    
#         f(n)

#         return dict_[n]          
        
#         or
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
        
#         return self.fib(n-1) + self.fib(n-2)


# class Solution:
#     @functools.cache
#     def fib(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return n
#         else:
#             return self.fib(n-1) + self.fib(n-2)