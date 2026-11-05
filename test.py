def tree(N, values):
    increase = 1
    decrease = 1
    max_increase = 1
    max_decrease = 1
    for i in range(N-1):
        if values[i] < values[i+1]:
            increase +=1
        else:
            if increase > max_increase:
                max_increase = increase
            increase = 1
    for i in range(N-1):
        if values[i] > values[i+1]:
            decrease += 1
        else:
            if decrease > max_decrease:
                max_decrease = decrease
            decrease = 1
    print(max_increase)
    print(max_decrease)

tree(4, [1,3,4,2])

    