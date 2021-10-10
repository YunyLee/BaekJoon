import sys
sys.stdin = open('input_2775.txt', 'r')

# 부녀회장이 될테야

TC = int(input())
for test_case in range(1, TC+1):
    K = int(input()) # K층
    N = int(input()) # N호

    # 2층 1  4 10 20 35 56
    # 1층 1  3  6 10 15 21
    # 0층 1  2  3  4  5  6

    # a층의 b호 = a층의 b-1호(누적) +  a-1층의 b호(새로 추가)
    # ARR[a][b] = ARR[a][b-1]       +  ARR[a-1][b]

    # 배열 만들기
    ARR = [[0]*N for _ in range(K+1)]
    for k in range(K+1):
        for n in range(N):
            if k == 0: # 0층이면
                ARR[k][n] += n+1
            elif k >= 1: # k가 1층 이상이면
                ARR[k][n] = ARR[k][n-1] + ARR[k-1][n]

    print(ARR[k][n])

# TC = int(input())
# for test_case in range(1, TC+1):
#     K = int(input())
#     N = int(input())
#     result = 0
#
#     n_list = []
#     n_list2 = []
#     if K >= 1 :
#         for i in range(1, N+1):
#             n_list.append(i)
#         result = sum(n_list)
#     if K >= 2:
#         for j in range(len(n_list)):
#             result += sum(n_list[:j])
#             n_list2.append(sum(n_list[:j]))
#     if K >= 3:
#         for k in range(len(n_list2)):
#             result += sum(n_list2[:k])
#
#     print(result)