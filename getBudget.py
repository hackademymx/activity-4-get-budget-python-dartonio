def getTotalBudget(people):
    '''Your amazing code here'''
     # with list comprehension
    list_1 = [i['budget'] for i in people]

    return sum(list_1)