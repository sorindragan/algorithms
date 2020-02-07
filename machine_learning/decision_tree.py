import math

class DecisionNode:

    def __init__(self, col=-1, value=None, labels=None, lb=None, rb=None):
        self.col          = col
        self.value        = value
        self.labels       = labels
        self.left_branch  = lb # true branch
        self.right_branch = rb # false branch

def divide_set(rows, column, value):
    split_function = None
    if isinstance(value, int) or isinstance(value, float):
        split_function = lambda row: row[column] >= value
    else:
        split_function = lambda row: row[column] == value

    set1 = [r for r in rows if split_function(r)]
    set2 = [r for r in rows if not split_function(r)]

    return set1, set2

def create_labels_dict(rows):
    labels = {}
    for row in rows:
        label = row[-1]
        if label not in labels:
            labels[label] = 1
        else:
            labels[label] += 1
    return labels

def entropy(rows):
    labels = create_labels_dict(rows)
    entropy = 0
    for l in labels.keys():
        p = float(labels[l]) / len(rows)
        entropy -= p * math.log2(p)
    return entropy

def construct_tree(rows, score_func=entropy):
    if len(rows) == 0:
        return DecisionNode()
    
    # calculate entropy before split
    score = score_func(rows)

    max_gain = 0
    split_criteria = None
    best_sets = None

    for col in range(len(rows[0]) - 1):
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
        return DecisionNode(col   = split_criteria[0],
                            value = split_criteria[1],
                            lb    = leftBranch,
                            rb    = rightBranch
                            )
    
    else: return DecisionNode(labels=list(create_labels_dict(rows).keys())[0])


def get_node_height(tree, node, height):
    if not tree:
        return 0
    
    if tree == node:
        return height
    
    level = get_node_height(tree.left_branch, node, height + 1)

    if level:
        return level
    
    return get_node_height(tree.right_branch, node, height + 1)


# level traversal
def display_tree(tree):
    
    if not tree:
        return
    
    order_q = []
    order_q.append(tree)

    while order_q:
        node = order_q.pop(0)
        if node.labels:
            print(
                f"Level {get_node_height(tree, node, 1)} : Leaf Node with Label {node.labels}")
        else :
            print(
                f"Level {get_node_height(tree, node, 1)} : Split Node on column: {node.col} by value {node.value}")


        if node.left_branch:
            order_q.append(node.left_branch)
        
        if node.right_branch:
            order_q.append(node.right_branch)


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
    
    display_tree(tree)
    
    print("--------------------------------------------")
    new_data_point = ['direct', 'USA', 'yes', 5]
    label = classify(new_data_point, tree)
    print(new_data_point, label)

    return 0


if __name__ == "__main__":
    main()
