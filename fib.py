def mem_fib(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n
sum = 0
for i in range(1, 101):
    sum = sum + mem_fib(i)
print(sum)
