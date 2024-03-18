import random


def simulate_dice_rolls(num_rolls):
    # Створюємо словник для зберігання кількості випадіння кожної суми
    results = {i: 0 for i in range(2, 13)}

    # Кидаємо кубики num_rolls разів
    for _ in range(num_rolls):
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        total = roll_1 + roll_2
        results[total] += 1

    # Обчислюємо ймовірність кожної суми
    probabilities = {key: value / num_rolls *
                     100 for key, value in results.items()}

    return probabilities


def print_probabilities(probabilities):
    expected_probabilities = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }
    print("Сума\tІмовірність\tОчікувана імовірність")
    for key, value in probabilities.items():
        print(f"{key}\t{value:.2f}%\t\t{expected_probabilities[key]:.2f}%")


def main():
    num_rolls = 10000000  # Кількість кидків кубиків
    probabilities = simulate_dice_rolls(num_rolls)
    print_probabilities(probabilities)


if __name__ == "__main__":
    main()
