from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

input_data = [
    [6, 4],
    [7, 4],
    [8, 4],
    [9, 4],
    [10, 4],
    [11, 4],
    [12, 4],

    [6, 6],
    [7, 6],
    [8, 6],
    [9, 6],
    [10, 6],
    [11, 6],
    [12, 6],
]

output_data = [
    2.5,
    5.1,
    6.9,
    9.9,
    7,
    4,
    2,

    1,
    2,
    3,
    4,
    6,
    8,
    9
]

# model 1: linear model
model = linear_model.LinearRegression()
model.fit(input_data, output_data)
res = model.predict([[10, 4], [8.5, 4], [12, 4], [15, 4]])
print(res)
res = model.predict([[10, 6], [8.5, 6], [12, 6], [15, 6]])
print(res)


# model 2: polynomial model
model2 = make_pipeline(PolynomialFeatures(2), linear_model.LinearRegression())
model2.fit(input_data, output_data)
res2 = model2.predict([[10, 4], [8.5, 4], [12, 4], [15, 4]])
print(res2)
res2 = model.predict([[10, 6], [8.5, 6], [12, 6], [15, 6]])
print(res2)

# 1. Dataset: size, feature set
# 2. Model


