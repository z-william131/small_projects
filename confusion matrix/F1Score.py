# The two inputs have the same layout. {news_id: category}

def f1score(actual_result, test_result, category):
    x = recall(actual_result, test_result, category)
    y = precise(actual_result, test_result, category)
    if x == 0 or y == 0:
        print("Recall or precise rate is zero.")
        return 0
    return 2 / ((1 / x) + (1 / y))

# Helper functions

def predicted_positive(test_result, category):
    count = 0
    for value in test_result.values():
        if value == category:
            count += 1
    return count

def predicted_negative(test_result, category):
    return len(test_result) - predicted_positive(test_result, category)

def condition_positive(actual_result, category):
    count = 0
    for value in actual_result.values():
        if value == category:
            count += 1
    return count

def condition_negative(actual_result, category):
    return len(actual_result) - condition_positive(actual_result, category)

#############################

def true_positive(actual_result, test_result, category):
    actual_positive, test_positive = [], []
    count = 0
    for key, value in test_result.items():
        if value == category:
            test_positive.append(key)
    for key, value in actual_result.items():
        if value == category:
            actual_positive.append(key)
    for i in actual_positive:
        if i in test_positive:
            count += 1
    return count

def false_positive(actual_result, test_result, category):
    return predicted_positive(test_result, category) - true_positive(actual_result, test_result, category)

def true_negative(actual_result, test_result, category):
    return condition_positive(actual_result, category) - true_positive(actual_result, test_result, category)

def false_negative(actual_result, test_result, category):
    return condition_negative(actual_result, category) - false_positive(actual_result, test_result, category)

#############################

def precise(actual_result, test_result, category):
    x = true_positive(actual_result, test_result, category)
    y = predicted_positive(test_result, category)
    if y == 0:
        print("There is no predicted positive result.")
        return 0
    return x / y

def recall(actual_result, test_result, category):
    x = true_positive(actual_result, test_result, category)
    y = condition_positive(actual_result, category)
    if y == 0:
        print("There is no condition positive result.")
        return 0
    return x / y