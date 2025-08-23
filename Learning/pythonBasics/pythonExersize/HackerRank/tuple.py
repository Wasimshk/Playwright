if __name__ == '__main__':
    n = int(input())
    my_t = map(int, input().split())
    # assert len(my_t) == n, f"Expected {n} numbers"
    # t = my_t[0] + my_t[1]
    print(hash(my_t))
