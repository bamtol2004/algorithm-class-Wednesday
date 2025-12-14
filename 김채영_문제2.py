# 문제 2. 여행 짐 꾸리기 최적 패킹 프로그램
# <문제 설명> 7일 동안 해외여행을 떠나려고 한다. 배낭의 최대 용량은 W(kg) 이며, 가져갈 수 있는 짐은 다음과 같다:
# 각 물건은 하나만 선택 가능한 0/1 배낭 문제이다. 여행의 만족도를 최고로 만들기 위해, 배낭 용량을 넘지 않는 범위에서 만족도의 합이 최대가 되도록 짐을 선택하시오.
# <요구사항>
# - 사용자에게 다음 데이터를 입력받으시오: 배낭 용량 W
# - 선택된 물건 목록 출력하시오.
# - 총 만족도 출력하시오.
# - 동적계획법의 테이블 Bottom-up (A[i][w]) 방식으로 구현하시오.
# - 선택한 물건을 역추적 하는 기능을 포함하시오.

def knapSack_dp(W, wt, val, n):
    # 1. DP 테이블 초기화 : (n+1) X (W + 1)
    A = []
    for i in range(n + 1):          # 행 생성 (0 ~ n)
        row = []
        for w in range(W + 1):      # 열 생성 (0 ~ W)
            row.append(0)           # 모든 값을 0으로 초기화
        A.append(row)

    # 2. DP 테이블 채우기
    for i in range(1, n + 1):       # 물건 index 1~n - 위에서 아래로 진행
        for w in range(1, W + 1):   # 배낭 용량 1~W - 좌에서 우로 진행
            if w < wt[i-1]:         # i번째 물건이 용량 초과해서  넣을 수 없으므로 위 값 복사
                A[i][w] = A[i-1][w]
            else:                   # i번째 물건을 넣을 수 있으면
                valWith = val[i-1] + A[i-1][w - wt[i-1]]  # 넣는 경우
                valWithout = A[i-1][w]                    # 빼는 경우
                A[i][w] = max(valWith, valWithout)        # 더 큰 값을 선택
    
    # 3. 최대 가치와 DP테이블 A 둘 다 반환
    return A[n][W], A


# 테스트 
items = [("노트북", 3, 12), 
         (" 카메라", 1, 10),
         ("책", 2, 6),
         ("옷", 2, 7), 
         ("휴대용 충전기", 1, 4)]

W = int(input("배낭 용량을 입력 하세요 : "))
wt = [item[1] for item in items]
val = [item[2] for item in items]
n = len(items)

max_value, A = knapSack_dp(W, wt, val, n)

print("최대 만족도 =", max_value)
selected = []
w = W

for i in range(n, 0, -1):            # DP 테이블을 거꾸로 올라가며 선택된 물건을 하나씩 찾아내는 과정이 필요
    if A[i][w] != A[i-1][w]:         # i번째 물건은 선택되어 가방에 들어감
        name, wt, val = items[i-1]   # i번째 물건을 리스트에 추가
        selected.append(name)  
        w -= wt                      # i번째 물건을 배낭에 넣었으므로 배낭의 용량에서 그 무게만큼 줄어든다.
                                     # 줄어든 나머지 용량 w에서 앞선 물건(i-1번째까지)으로 최대 가치를 만드는 방법 고려
    else:
        pass

selected.reverse()
print("선택된 물건 :", selected)