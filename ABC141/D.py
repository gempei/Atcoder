import bisect
import sys

def main():
  input = sys.stdin.readline
  N,M = map(int,input().split())
  a_l = list(map(int,input().split()))
  a_l.sort()

  for _ in range(M):
    discount = a_l[-1]//2
    a_l.pop()
    bisect.insort(a_l,discount)

  print(sum(a_l))

if __name__ == "__main__":
  main()
