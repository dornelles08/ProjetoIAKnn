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

    test_ratio = int(len(dataset)*split_ratio)
    train_ratio = len(dataset) - test_ratio

    test_data = dataset[test_ratio:]
    train_data = dataset[:train_ratio]

    train_X = [data[:7] for data in dataset]
    train_Y = [[data[7], data[8]] for data in dataset] 

    return train_X, train_Y

def euclidean_distance(point_p, point_q):
    square_diffs = lambda p_i, q_i: (float(q_i) - float(p_i)) ** 2 #função que calcula o quadrado da diferença entre dois pontos
    distance = list(map(square_diffs, point_p, point_q))

    return sum(distance)**0.5

def knn(train_set, test_instance, k=1):
    distance = [euclidean_distance(X, test_instance) for X in train_set]
    return sorted(range(len(distance)), key=lambda i: distance[i])[:k]

def predict(train_y, k_n):
    knn_labels = [train_y[i][0] for i in k_n]
    return max(set(knn_labels), key=knn_labels.count)

def detail(request, attributes):
    train_x, train_y = split_train_test(load_dataset())

    instance = []

    attributes = attributes.split(",")
    for attribute in attributes:
        instance.append(float(attribute))

    k_n = knn(train_x, instance)
    position = predict(train_y, k_n)
    overall = train_y[k_n[0]][1]

    response = {}
    response['position'] = position
    response['overall'] = overall

    return JsonResponse(response)