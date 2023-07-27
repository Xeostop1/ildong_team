from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mn
from sklearn.neighbors import LocalOutlierFactor


# 1차원
d1 = np.loadtxt("./appliedStatistics/Outliers/outlier_1d.txt")
# 2차원
d2 = np.loadtxt("./appliedStatistics/Outliers/outlier_2d.txt")
# 곡선 그래프
d3 = np.loadtxt("./appliedStatistics/Outliers/outlier_curve.txt")

# print(d1.shape, d2.shape)
# plt.scatter(d1, np.random.normal(7, 0.2, size=d1.size), s=1, alpha=0.5)
# plt.scatter(d2[:, 0], d2[:, 1])
# plt.show()
# plt.plot(d3[:, 0], d3[:, 1])

# 그래프를 보면 위쪽에 10개정도의 이상치값 존재 확인
# 초록색은 산점도 표시 그래서 끝쪽에 있는 뭉쳐지지 않는 값은 이상치로 확인 가능

# 이상치 처리(1차원 데이터)
# 1. 데이터를 분석함수로 모델링하기(ex 정규분포 가우스)
# 여기서 이상치를 찾고 확률임계값을 사용하여 원하느 만큼 해당과정 반복
# 지금 이데이터에서는 정규분포를 따른다고 가정하고 시작(아니라면 변경하거나 다른 방법으로 사용)

# 평균, 표준편차
mean, std = np.mean(d1), np.std(d1)
# 정규분포라서 z인덱스 구하기
# 거리의 평균값으로 z인덱스 사용 → z_score: 현재 평균에서 벗어난 표준편자의 수
z_score = np.abs((d1-mean)/std)
# 이후 3개 이상의 배열 모두 제거 threshold: 한계점 여기서 범위를 조정할 필요가 있음!
threshold = 3
good_val = z_score < threshold

# 그래프로 확인하기
# print(f"Rejection{(~good_val).sum()} points")
# print(
#     f"z-score of 3 corresponds to a proib of {100*2*norm.sf(threshold):0.2f}%")
# visual_scatter = np.random.normal(size=d1.size)
# plt.scatter(d1[good_val], visual_scatter[good_val],
#             s=2, label="Good", color="#4caf50")
# # ~ not 연산자 판다스에서는 부정이나 not으로 해석 블리언값 반전 "틸드"!
# plt.scatter(d1[~good_val], visual_scatter[~good_val],
#             s=2, label="Bad", color="#F44336")
# plt.legend()
# plt.show()
# 임계값이 3이고 낮은 값들은 버리기 때문에 5개 삭제 0.27% 조금 그래프가 다른데 5개 이상치 확인했고
# y축값이 다름 확인 필요!


# 이상치 처리(2차원 데이터) → 2차원배열을 가우스로 정량화
# 2차원 데이터의 평균(mean)과 공분산(cov)을 계산
# mean2, cov = np.mean(d2, axis=0), np.cov(d2.T)
# # 굳이 z스코어를 사용하지 않고 라이브러리(mn)사용 multivariate_normal: 다변량 정규밀도(2차원이라서)
# # 가우시안 확률 밀도 함수를 사용하여 각 데이터 포인트에 대한 확률 값을 계산
# prob_threshold = 0.01/100
# good = mn(mean2, cov).pdf(d2) > prob_threshold
# plt.scatter(d2[good, 0], d2[good, 1], s=2, label="Good", color="#4caf50")
# # ~ not 연산자 판다스에서는 부정이나 not으로 해석 블리언값 반전
# plt.scatter(d2[~good, 0], d2[~good, 1], s=2, label="Bad", color="#F44336")
# plt.legend()
# # 범례(legend)추가
# plt.show()

# 이상치를  빼서 정규화 하는방법 곡선그래프 와오아ㅘ오아ㅓㅗ아ㅣ 너무 어려운데요??????
# xs, ys = d3.T
# # deg=5 5차 다항식이 되도록 세팅
# p = np.polyfit(xs, ys, deg=5)
# ps = np.polyval(p, xs)
# plt.plot(xs, ys, ".", label="Data")
# plt.plot(xs, ps, ".", label="Bad poly fit")
# plt.legend()
# # 범례(legend)추가
# plt.show()

# 지금까지 한거(수동)를 어떤 또또깡 한놈이 알고리즘 패키지로 만들어 놨데! 그거 사용하면 된데
# LocalOutlierFactor 이상치 제거 알고리즘 라이브러리
# contamination 임계값 수정 contamination:오염
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.005)
good = lof.fit_predict(d2) == 1
plt.scatter(d2[good, 0], d2[good, 1], s=2, label="Good", color="#4caf50")
plt.scatter(d2[~good, 0], d2[~good, 1], s=2, label="Bad", color="#F44336")
plt.legend()
plt.show()
