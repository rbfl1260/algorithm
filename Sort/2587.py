#대표값2
import sys
# 한 번에 입력을 받아 처리
arr = list(map(int, sys.stdin.read().split()))
# arr = [int(input()) for _ in range(5)]

# arr.sort()
# 함수 sort는 TimSort알고리즘 사용함(시간복잡도 O(n log n))

#삽입정렬(시간복잡도 O(n^2)) 차라리 함수 sort를 사용하는것이 더 효율적임.
# for i in range(1,5):
#     for j in range(i):
#         if arr[j]>arr[i]:
#             arr[j],arr[i]=arr[i],arr[j]

#이문제에서 지금 중앙값만 필요하므로 완벽한 정렬이 필요한게 아님. 퀵셀렉트로 중앙값 구할 수 있음

print(sum(arr)//5)
print(arr[2])