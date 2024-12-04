def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    # Find the most likely sequence
    (prob, state) = max((V[len(obs) - 1][y], y) for y in states)
    return (prob, path[state])


states = ['Sunny', 'Rainy', 'Cloudy']
observations = ['Walk', 'Shop', 'Clean']

start_probability = {
    'Sunny': 0.4,
    'Rainy': 0.3,
    'Cloudy': 0.3
}

transition_probability = {
    'Sunny': {'Sunny': 0.6, 'Rainy': 0.2, 'Cloudy': 0.2},
    'Rainy': {'Sunny': 0.3, 'Rainy': 0.5, 'Cloudy': 0.2},
    'Cloudy': {'Sunny': 0.3, 'Rainy': 0.3, 'Cloudy': 0.4}
}

activity_probability = {
    'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1},
    'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5},
    'Cloudy': {'Walk': 0.3, 'Shop': 0.4, 'Clean': 0.3}
}

# Observed activities for a week
week_activities = ['Walk', 'Shop', 'Clean', 'Clean', 'Walk', 'Shop', 'Walk']

# Run Viterbi algorithm
prob, path = viterbi(week_activities, states, start_probability, transition_probability, activity_probability)

print(f"The most likely weather sequence is: {' -> '.join(path)}")
print(f"Probability of this sequence: {prob}")