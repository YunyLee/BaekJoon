import sys
sys.stdin = open('input_10951.txt', 'r')

# 백준 단계별 풀이 - while문 - 10951문제
# 입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요.
# EOF : 파일 끝(End of File, EOF)는 데이터 소스로부터 더 이상 읽을 수 있는 데이터가 없음을 나타낸다.
# EOFError: EOF when reading a line

while True:
    try:
        NUM1, NUM2 = map(int, input().split())
        print(NUM1 + NUM2)
    except:
        break

