def trees(N, x):

    up = 1
    down = 1
    max_up = 1 
    max_down = 1

    for i in range(N - 1):
        if x[i] < x[i + 1]:
            up += 1
            if up > max_up:
                max_up = up
            down = 1
        elif x[i] > x[i+1]:
            down +=1
            if down > max_down:
                max_down = down
            up =1

    print(max_up)
    print(max_down)
trees(4, [1, 3, 4, 2])

