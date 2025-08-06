def rabbit_recurrence(months, offspring):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offspring)
    return child


print(rabbit_recurrence(5, 3))
"""
o - small (children) rabbits. They have to mature and reproduce in the next cycle only.
O - mature (parents) rabbits. They can reproduce and move to the next cycle.


Month 1: [o]
Month 2: [O]
Month 3: [O, o, o]
Month 4: [O, o, o, O, O]
Month 5: [O, o, o, O, O, O, o, o, O, o, o]
Month 6: [O, o ,o, O, O, O, o, o, O, o, o, O, o, o, O, O, O, o, o, O, O ]
"""
