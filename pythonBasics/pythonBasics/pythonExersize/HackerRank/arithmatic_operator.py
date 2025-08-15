if __name__ == '__main__':
    a = int(input())
    b = int(input())
    try:
        if 1 <= a <= 10**10 and 1 <= b <= 10**10:
            print(a+b)
            print(a-b)
            print(a*b)

        else:
            raise Exception("Number out of range!")
    except Exception as e:
        print(e)
