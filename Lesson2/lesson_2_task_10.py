def bank(X, Y):
    total_amaunt = 0
    for i in range(1, Y+1):
        total_amaunt += X
        total_amaunt += total_amaunt / 10
    print(total_amaunt)

bank(100, 4)