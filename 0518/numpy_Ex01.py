"""
    파이썬 numpy 라이브러리를 활용하여 행렬의 곱(dot product) 처리하기
"""
import numpy as np

A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[10,20],
              [30,40],
              [50,60]])

C = np.dot(A,B)

print(C)

# 실행결과
# [[220 280]
#  [490 640]]