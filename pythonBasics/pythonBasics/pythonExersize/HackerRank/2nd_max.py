if __name__ == '__main__':
    n = int(input())
    assert 2 <= n <= 10

    A = list(map(int, input().split()))
    assert len(A) == n, f"Expected {n} numbers"

    winner = runner_up = float('-inf')
    for i in A:
        if i > winner:
            runner_up = winner
            winner = i
        elif i > runner_up and i != winner:
            runner_up = i
    print(runner_up)