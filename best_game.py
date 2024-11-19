def find_best_game(games):
    best_g = ''
    best_ev = float('-inf')

    for game in games:
        expected_value = 0
        for probability, reward in game.outcomes:
            expected_value += probability * reward
        
        if expected_value > best_ev:
            best_ev = expected_value
            best_g = game.name

    return best_g