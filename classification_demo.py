from sklearn import svm

input_data = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    [4.6, 3.1, 1.5, 0.2],

    [7.0, 3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5],
    [6.9, 3.1, 4.9, 1.5],
    [5.5, 2.3, 4.0, 1.3],
    
    [6.3, 3.3, 6.0, 2.5],
    [5.8, 2.7, 5.1, 1.9],
    [7.1, 3.0, 5.9, 2.1],
    [6.3, 2.9, 5.6, 1.8],    
]

output_data = [
    "setosa",
    "setosa",
    "setosa",
    "setosa",  

    "versicolor",
    "versicolor",       
    "versicolor",
    "versicolor",

    "virginica",
    "virginica",    
    "virginica",
    "virginica",
]

model = svm.SVC()
model.fit(input_data, output_data)
res = model.predict([[5.1,3.8,1.5,0.3], [5.6,2.7,4.2,1.3], [6.7, 3.0, 5.2, 2.3]])
print(res)