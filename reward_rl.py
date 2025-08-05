def simulate_rl_feedback(original, modified):
    print("Original Summary:", original[:200])
    print("Modified Summary:", modified[:200])
    try:
        reward = float(input("Rate this version from -1 (bad) to +1 (excellent): "))
        return reward
    except:
        return 0.0
