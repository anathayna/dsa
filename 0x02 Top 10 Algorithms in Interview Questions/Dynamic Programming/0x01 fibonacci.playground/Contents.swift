import Foundation

// Brute force Recursive Approach
// Time complexity: O(2^n)
// Space complexity: O(n)

func fib(_ n: Int) -> Int {
    if n <= 1 {
        return n
    }
    
    return fib(n-1) + fib(n-2)
}

fib(8)

// Memoization Approach
// Time complexity: O(n)
// Space complexity: O(n)

func fibo(_ n: Int) -> Int {
    var mem = [Int:Int]()
    return fibMem(n, mem: &mem)
}

private func fibMem(_ n: Int, mem: inout [Int:Int]) -> Int{
    if n == 0 || n == 1 {
        return n
    }

    if mem[n] == nil {
        mem[n] = fibMem(n - 2, mem: &mem) + fibMem(n - 1, mem: &mem)
    }
    
    return mem[n]!
}

fibo(8)

// Tabulation Approach
// Time complexity: O(n)
// Space complexity: O(n)

func fibTab(_ n: Int) -> Int {
    guard n > 1 else { return n }
    var cache = [0, 1]

    for index in 2...n {
        cache.append(cache[index-1] + cache[index-2])
    }
    return cache[n-1] + cache[n-2]
}

fibTab(8)
