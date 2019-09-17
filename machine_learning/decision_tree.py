import math
import operator
from pprint import pprint

class None:
    def __init__(self, feature, children):
        self.feature = feature
        self.children = children

class Leaf:
    def __init__(self, class):
        self.class = class

# TODO: implement a decision tree

def initial_entropy(data):
    neg = len([t for t in data if t[1] == 0])
    poz = len(data) - neg
    e1 = -(poz/len(data)) * math.log2(poz/len(data))
    e2 = -(neg/len(data)) * math.log2(neg/len(data))
    return e1 + e2

def calculate_entropy(data, feature, values):
    entropy = 0
    for val in values:
        neg = len([t for t in data if t[1] == 0 and val in t[0]])
        poz = len([t for t in data if t[1] == 1 and val in t[0]])
        all = poz + neg
        if poz == 0:
            e1 = 0
        else:
            e1 = -(poz/all) * math.log2(poz/all)

        if neg == 0:
            e2 = 0
        else:
            e2 = -(neg/all) * math.log2(neg/all)
        entropy += e1 + e2
    return entropy


def calculate_gain(data, feature, values, level_entropy):
    return level_entropy + calculate_entropy(data, feature, values)


def train(data, feature_values, level_entropy, tree):
    # if len(set([d[1] for d in data
    #             if any([True for v in feature_values.values() if v in d[0]])
    #             ])
    #        ) == 1:
    if not feature_values:
        return

    gain_score = {}
    for feature in feature_values.keys():
        gain_score[feature] = calculate_gain(data, feature, feature_values[feature], level_entropy)

    split_feature, level_entropy = max(gain_score.items(), key=operator.itemgetter(1))
    tree.feature = split_feature
    pprint(gain_score)
    print(split_feature, level_entropy)

    next_values = feature_values[split_feature]
    del feature_values[split_feature]
    for value in next_values:
        examples = [d[1] for d in data if value in d[0]]
        if len(set(examples)) == 1:

        train(data, feature_values, level_entropy)

def predict():
    pass

def main():

    feature_values = {"outlook": ["sunny", "overcast", "rain"],
                      "humidity": ["high", "normal"],
                      "wind": ["strong", "weak"],
                      }

    # 0: no, 1: yes
    data = [(["sunny", "high", "strong"], 0),
            (["sunny", "normal", "weak"], 1),
            (["sunny", "normal", "strong"], 1),
            (["sunny", "high", "weak"], 0),
            (["overcast", "normal", "weak"], 1),
            (["overcast", "high", "weak"], 1),
            (["overcast", "normal", "strong"], 1),
            (["overcast", "high", "strong"], 1),
            (["rain", "normal", "strong"], 0),
            (["rain", "normal", "weak"], 1),
            (["rain", "high", "strong"], 0),
            ]

    print(initial_entropy(data))

    train(data, feature_values, initial_entropy(data), Node(None, None))

if __name__ == "__main__":
    main()
