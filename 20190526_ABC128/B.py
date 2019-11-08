from pprint import pprint
from operator import itemgetter
def main():
    N = int(input())
    book_l = []
    for i in range(N):
        line=input().split(" ")
        book_l.append([line[0],int(line[1]),i])

    book_l = sorted(book_l,key=itemgetter(0),reverse=True)
    print(book_l)
    book_l = sorted(book_l,key=itemgetter(1),reverse=True)
    print(book_l)
    for name,score,ans in sorted(book_l,key=itemgetter(1),reverse=True):
        print(ans+1)

if __name__ == '__main__':
    main()
