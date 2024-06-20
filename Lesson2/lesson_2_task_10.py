def bank(X, Y):
    total_amaunt = X
    for i in range(1, Y+1):
        total_amaunt += total_amaunt / 10
    print(total_amaunt)

bank(1500, 5)