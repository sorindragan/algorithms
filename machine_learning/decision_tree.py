import math

class DecisionNode:

    def __init__(self, col=-1, value=None, labels=None, lb=None, rb=None):
        self.col = col
        self.value = value
        self.labels = labels
        self.left_branch = lb # true branch
        self.right_branch = rb # false branch

def divide_set(rows, column, value):
    split_function = None
    if isinstance(value, int) or isinstance(value, float):
        split_function = lambda row:row[column] >= value
    else:
        split_function = lambda row: row[column] == value

    set1 = [r for r in rows if split_function(r)]
    set2 = [r for r in rows if not split_function(r)]

    return set1, set2

def count_labels(rows):
    labels = {}
    for row in rows:
        label = row[-1]
        if label not in labels:
            labels[label] = 1
        else:
            labels[label] +=1
    return labels

def entropy(rows):
    labels = count_labels(rows)
    entropy = 0
    for l in labels.keys():
        p = float(labels[l]) / len(rows)
        entropy -= p * math.log2(p)
    return entropy

def construct_tree(rows, score_func=entropy):
    if len(rows) == 0:
        return DecisionNode()
    score = score_func(rows)

    max_gain = 0
    split_criteria = None
    best_sets = None

    column_no = len(rows[0]) - 1
    for col in range(column_no):
        for val in [v[col] for v in rows]:
            set1, set2 = divide_set(rows, col, val)

            p = float(len(set1)) / len(rows)
            gain = score - p * score_func(set1) - (1-p) * score_func(set2)
            if gain > max_gain and set1 and set2:
                max_gain = gain
                split_criteria = col, val
                best_sets = set1, set2
    if max_gain > 0:
        leftBranch = construct_tree(best_sets[0])
        rightBranch = construct_tree(best_sets[1])
        return DecisionNode(col=split_criteria[0],
                            value=split_criteria[1],
                            lb = leftBranch,
                            rb = rightBranch
                            )
    else: return DecisionNode(labels=count_labels(rows))

# TODO:
# def display_tree()

def classify(obsertvation, tree):
    if tree.labels:
        return tree.labels
    else:
        v = obsertvation[tree.col]
        branch = None
        if isinstance(v, float) or isinstance(v, int):
            if v >= tree.value: branch = tree.left_branch
            else: branch = tree.right_branch
        else:
            if v == tree.value: branch = tree.left_branch
            else: branch = tree.right_branch
        return classify(obsertvation, branch)

def main():

    data = [['slashdot', 'USA', 'yes', 18, 'None'],
            ['google', 'France', 'yes', 23, 'Premium'],
            ['digg', 'USA', 'yes', 24, 'Basic'],
            ['kiwitobes', 'France', 'yes', 23, 'Basic'],
            ['google', 'UK', 'no', 21, 'Premium'],
            ['direct', 'New Zealand', 'no', 12, 'None'],
            ['direct', 'UK', 'no', 21, 'Basic'],
            ['google', 'USA', 'no', 24, 'Premium'],
            ['slashdot', 'France', 'yes', 19, 'None'],
            ['digg', 'USA', 'no', 18, 'None'],
            ['google', 'UK', 'no', 18, 'None'],
            ['kiwitobes', 'UK', 'no', 19, 'None'],
            ['digg', 'New Zealand', 'yes', 12, 'Basic'],
            ['slashdot', 'UK', 'no', 21, 'None'],
            ['google', 'UK', 'yes', 18, 'Basic'],
            ['kiwitobes', 'France', 'yes', 19, 'Basic'],
            ]

    tree = construct_tree(data)
    label = classify(['direct', 'USA', 'yes', 5] , tree)
    print(label)
    return


if __name__ == "__main__":
    main()
