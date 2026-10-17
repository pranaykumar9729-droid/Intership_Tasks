problem : Set .add()
https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
dist_countries = set()
for _ in range(n):
    country = input()
    dist_countries.add(country)
print(len(dist_countries))
    

