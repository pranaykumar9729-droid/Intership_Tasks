problem : Symmetric Difference
link : https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = input()
X = set(map(int,input().split()))
N = input()
Y = set(map(int,input().split()))
out = X.symmetric_difference(Y)
for num in sorted(out):
    print(num)
