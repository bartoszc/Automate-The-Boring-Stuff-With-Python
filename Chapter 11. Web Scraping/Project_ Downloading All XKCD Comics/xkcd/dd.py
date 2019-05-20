def featureScaling(arr):
    return [float((i - min(arr))) / (max(arr) - min(arr)) for i in arr]


data = [115, 140, 175]
print(featureScaling(data))