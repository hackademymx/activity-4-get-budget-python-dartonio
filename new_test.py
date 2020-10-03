import getBudget

get_1 = getBudget.getTotalBudget(
    [{
        'name': "John",
        'age': 21,
        'budget': 23000
    },
    {
        'name': "Steve",
        'age': 32,
        'budget': 40000
    },
    {
        'name': "Martin",
        'age': 16,
        'budget': 2700
    }])
print(get_1)

get_2 = getBudget.getTotalBudget(
    [{
        'name': "John",
        'age': 21,
        'budget': 29000
    },
    {
        'name': "Steve",
        'age': 32,
        'budget': 32000
    },
    {
        'name': "Martin",
        'age': 16,
        'budget': 1600
    }])
print(get_2)

get_3 = getBudget.getTotalBudget(
    [{
        'name': "John",
        'age': 21,
        'budget': 19401
    },
    {
        'name': "Steve",
        'age': 32,
        'budget': 12321
    },
    {
        'name': "Martin",
        'age': 16,
        'budget': 1204
    }])
print(get_3)

get_4 = getBudget.getTotalBudget(
    [{
        'name': "John",
        'age': 21,
        'budget': 10234
    },
    {
        'name': "Steve",
        'age': 32,
        'budget': 21754
    },
    {
        'name': "Martin",
        'age': 16,
        'budget': 4935
    }])
print(get_4)