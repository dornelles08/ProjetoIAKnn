import csv


def load_dataset() -> list[list[str]]:
    with open("player_classifier/recursos/dataset.csv") as csvfile:
        dataset = list(csv.reader(csvfile))

    return dataset


def split_train_test(dataset:list[list[str]]):
    train_X = [data[:7] for data in dataset]
    train_Y = [[data[7], data[8]] for data in dataset]

    return train_X, train_Y


def euclidean_distance(point_p, point_q):
    # função que calcula o quadrado da diferença entre dois pontos
    def square_diffs(p_i, q_i): return (float(q_i) - float(p_i)) ** 2
    distance = list(map(square_diffs, point_p, point_q))

    return sum(distance)**0.5


def knn(train_set, test_instance, k=1) -> list[int]:
    distance = [euclidean_distance(X, test_instance) for X in train_set]
    return sorted(range(len(distance)), key=lambda i: distance[i])[:k]


def predict(train_y, k_n):
    knn_labels = [train_y[i][0] for i in k_n]
    return max(set(knn_labels), key=knn_labels.count)


def classifier(attributes: str):
    train_x, train_y = split_train_test(load_dataset())

    instance: list[float] = []

    attributes: list[str] = attributes.split(",")
    for attribute in attributes:
        instance.append(float(attribute))

    k_n = knn(train_x, instance, 11)
    position = predict(train_y, k_n)
    overall = train_y[k_n[0]][1]

    return {'position': position,
            'overall': overall}
