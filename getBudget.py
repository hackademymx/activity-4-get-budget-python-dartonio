def getTotalBudget(people):
    pass
    '''Your amazing code here'''
    totalBudget = 0
    for i in people:
        totalBudget += i['budget']
    return totalBudget