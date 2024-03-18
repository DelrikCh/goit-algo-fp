def greedy_algorithm(items, budget):
    item_list = [(name, item["calories"], item["cost"])
                 for name, item in items.items()]
    item_list.sort(key=lambda x: x[1] / x[2], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, calories, cost in item_list:
        if total_cost + cost <= budget:
            selected_items.append((name, calories, cost))
            total_cost += cost
            total_calories += calories

    return selected_items, total_calories


def dynamic_programming(items, budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (name, item) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            cost = item["cost"]
            calories = item["calories"]
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            name = list(items.keys())[i - 1]
            selected_items.append(
                (name, items[name]["calories"], items[name]["cost"]))
            j -= items[name]["cost"]
        i -= 1

    return selected_items, dp[-1][-1]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    greedy_selected_items, greedy_total_calories = greedy_algorithm(
        items, budget)
    print("Greedy Algorithm:")
    print("Selected Items:", greedy_selected_items)
    print("Total Calories:", greedy_total_calories)

    dp_selected_items, dp_total_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming:")
    print("Selected Items:", dp_selected_items)
    print("Total Calories:", dp_total_calories)


if __name__ == "__main__":
    main()
