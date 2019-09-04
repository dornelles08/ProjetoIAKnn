from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.db.models.functions.math import Sqrt
import csv
import random
import datetime
import json
# Create your views here.


def load_dataset():
    with open("polls/recursos/dataset.csv") as csvfile:
        dataset = list(csv.reader(csvfile))

    return dataset

def split_train_test(dataset, split_ratio=0.2):
    dataset = random.sample(dataset, len(dataset))

    test_ratio = int(len(dataset)*split_ratio)
    train_ratio = len(dataset) - test_ratio

    test_data = dataset[test_ratio:]
    train_data = dataset[:train_ratio]

    test_X = [data[:7] for data in test_data]
    test_Y = [data[7] for data in test_data]
    train_X = [data[:7] for data in train_data]
    train_Y = [data[7] for data in train_data]

    return train_X, train_Y, test_X, test_Y

def euclidean_distance(point_p, point_q):
    square_diffs = lambda p_i, q_i: (float(q_i) - float(p_i)) ** 2 #função que calcula o quadrado da diferença entre dois pontos
    distance = list(map(square_diffs, point_p, point_q))

    return sum(distance)**0.5

def knn(train_set, test_instance, k=1):
    distance = [euclidean_distance(X, test_instance) for X in train_set]
    return sorted(range(len(distance)), key=lambda i: distance[i])[:k]

def predict(train_y, k_n):
    knn_labels = [train_y[i] for i in k_n]

    return max(set(knn_labels), key=knn_labels.count)

def evaluate(predictions, test_y):
    #for idx, prediction in enumerate(predictions):
        #print(f' > Predicted = {prediction}, Actual = {test_y[idx]}')

    accuracy = sum(i == j for i, j in zip(predictions, test_y)) / len(test_y) * 100.0

    #print(f'Model accuracy: {accuracy:.2f}%')
    return accuracy


def detail(request, attributes):
    train_x, train_y, test_x, test_y = split_train_test(load_dataset())

    predictions = []

    #for instamce_test in test_x:
        #k_n = knn(train_x, instamce_test)
    instance = []

    attributes = attributes.split(",")
    for attribute in attributes:
        instance.append(float(attribute))

    k_n = knn(train_x, instance)
    predictions.append(predict(train_y, k_n))

    response = {}
    response['position'] = predictions[0]

    #response["Access-Control-Allow-Origin"] = "*"
    #response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    #response["Access-Control-Max-Age"] = "1000"
    #response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return JsonResponse(response)
        
    
    #return HttpResponse(instance)
    #return HttpResponse(test_x[0])
    #return HttpResponse(predictions[0])
    #return HttpResponse(evaluate(predictions, test_y))