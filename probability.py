import random


def die_probability():
    total = 6
    count = 0

    for x in range(1, 7):
        if x > 4:
            count += 1

    return count / total


def dice_sum_probability(target=7):
    total = 0
    count = 0

    for x in range(1, 7):
        for y in range(1, 7):
            total += 1

            if x + y == target:
                count += 1

    return count / total


def coin_probability():
    outcomes = ["HH", "HT", "TH", "TT"]
    count = 0

    for result in outcomes:
        if "H" in result:
            count += 1

    return count / len(outcomes)


def expected_die_value():
    total = 0

    for x in range(1, 7):
        total += x

    return total / 6


def lottery_expected_value():
    prizes = [10, 50, 0]
    probs = [0.2, 0.1, 0.7]

    total = 0

    for prize, prob in zip(prizes, probs):
        total += prize * prob

    return total


def uniform_probability(samples=100000):
    count = 0

    for _ in range(samples):
        x = random.uniform(5, 15)

        if 8 <= x <= 12:
            count += 1

    return count / samples


def soccer_probability():
    boys = 0.6
    girls = 0.4
    boys_soccer = 0.3
    girls_soccer = 0.5

    p_boys = boys * boys_soccer
    p_girls = girls * girls_soccer

    return p_girls / (p_boys + p_girls)


def machine_probability():
    machine_a = 0.8
    machine_b = 0.2
    defect_a = 0.05
    defect_b = 0.1

    p_a = machine_a * defect_a
    p_b = machine_b * defect_b

    return p_b / (p_a + p_b)


def main():
    print("Probability Solver")
    print()

    print("Die result greater than 4:", round(die_probability(), 4))
    print("Two dice sum equal to 7:", round(dice_sum_probability(), 4))
    print("At least one head:", round(coin_probability(), 4))
    print("Expected die value:", round(expected_die_value(), 4))
    print("Expected lottery winnings: $", round(lottery_expected_value(), 2))
    print("Uniform probability:", round(uniform_probability(), 4))
    print("Soccer probability:", round(soccer_probability(), 4))
    print("Machine B probability:", round(machine_probability(), 4))


main()