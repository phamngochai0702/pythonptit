def generate_palindromes(limit):
    res = []
    digits = ['0', '2', '4', '6', '8']
    max_len = len(str(limit))

    for length in range(2, max_len + 1, 2):
        half = length // 2

        def backtrack(pos, cur):
            if pos == half:
                if cur[0] == '0':
                    return
                pal = int(cur + cur[::-1])
                if pal <= limit:
                    res.append(pal)
                return

            for d in digits:
                backtrack(pos + 1, cur + d)

        backtrack(0, "")

    return sorted(res)


# ===== MAIN =====
t = int(input())

# sinh trước 1 lần với giới hạn lớn nhất
limits = []
for _ in range(t):
    limits.append(int(input()))

max_n = max(limits)
palindromes = generate_palindromes(max_n)

for n in limits:
    for x in palindromes:
        if x > n:
            break
        print(x, end=' ')
    print()