#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 김채영
#  작성일: 2025-09-29
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################
import time

def factorial_iter(n):
    # 반복문 기반 n!
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    # 재귀적으로 문제 해결 n! -> 재귀함수 정의
    # 1. base case (재귀함수 정의)
    if n == 1:
        return 1
    
    # 2. 재귀 분할
    return n * factorial_rec(n-1)

def run_with_time(func, n):
    start = time.time()
    end = time.time()
    result = func(n)
    result_time = end - start
    return result, result_time

def user_menu():
    print("\n================ Factorial Tester ================")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")
    print("------------------------------------------------")
    return input("선택: ").strip()

def user_n_input():
    while True:
        user_input = input("n 값(정수, 0이상)을 입력하세요: ").strip()
        if user_input.lower() == ('q', 'quit'):
            return None
        try:
            n = int(user_input)
            
            if n < 0:
                print("정수(0 이상의 숫자)만 입력하세요.")
                continue
            
            return n
        
        except ValueError:
            print("정수(0 이상의 숫자)만 입력하세요.")

def compare_result(n):
    try:
        iter_result, iter_time = run_with_time(factorial_iter, n)
        print(f"[반복] {n}! = {iter_result}")
                
        rec_result, rec_time = run_with_time(factorial_rec, n)
        print(f"[재귀] {n}! = {rec_result}")
                
        is_same = iter_result == rec_result
        if is_same:
            print("결과 일치 여부 : 일치")
        else:
            print("결과 일치 여부 : 불일치")
                    
        print(f"[반복] 시간 : {iter_time}s | [재귀] 시간 : {rec_time}s ")
    except:
        print("오류 발생!")

def test_data():
    Test_Data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]
    print("\n[테스트 데이터 실행]")
    
    for n in Test_Data:
        try:
            iter_result, iter_time = run_with_time(factorial_iter, n)
            rec_result, rec_time = run_with_time(factorial_rec, n)
            is_same = iter_result == rec_result
            
            print(f"n = {n} | same = {is_same} | iter = {iter_time}s | rec = {rec_time}s")
            print(f"    {n}! = {iter_result}")
        except RecursionError:
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

def main():
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 를 입력하세요.")
    while True:
        choice = user_menu()
        if choice == '1':
            n = user_n_input()
            if not n == None:
                print(f"[반복] {n}! = {factorial_iter(n)}")
        elif choice == '2':
            n = user_n_input()
            if not n == None:
                try:
                    print(f"[재귀] {n}! = {factorial_rec(n)}")
                except RecursionError:
                    print("입력값이 너무 커서 재귀 계산은 불가능합니다.")
        elif choice == '3':
            n = user_n_input()
            if not n == None:
                compare_result(n)
        elif choice == '4':
            test_data()
        elif choice.lower() in ('q', 'quit'):
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효한 메뉴를 선택해주세요.")

if __name__ == "__main__":
    main()