def main():
    r,D,x = [int(element) for element in input().split(" ")]
    for i in range(10):
        x = r*x - D
        print(x)

if __name__ =='__main__':
    main()
