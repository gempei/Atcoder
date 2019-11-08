def main():
    P,Q,R = map(int,input().split(" "))
    print(min([P+Q,Q+R,P+R]))

if __name__ == "__main__":
    main()
