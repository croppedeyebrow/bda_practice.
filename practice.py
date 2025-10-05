# 데이터 리스트 정의
a = [15,46,78,24,56]

# a 리스트에서 최솟값을 구해서 x 변수에 저장
x = min(a) 
# a 리스트에서 최댓값을 구해서 y 변수에 저장
y = max(a) 

# 범위를 계산하는 함수 정의 (x, y를 매개변수로 받음)
def name(x,y):

   gap = y-x # 최댓값 - 최솟값
    # 함수 내부의 gap (지역 변수수)
   # 계산된 범위 값을 반환
   return gap


# 전역 변수 result에 함수 호출 결과 저장
result = name(x,y)

# 계산된 범위 값을 출력
print(result)