def getTotalBudget(people):
    '''Your amazing code here'''
    # totalBudget = 0
    # for i in people:
        # totalBudget += i['budget']

    # with list comprehension
    list_1 = [i['budget'] for i in people]

    return sum(list_1)