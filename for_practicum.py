# Посылка 143008589
def delivery_service(robot_weights: list, max_weight: int) -> int:
    """Служба доставки."""
    robot_weights = sorted(robot_weights)
    left_pointer = 0
    right_pointer = len(robot_weights) - 1
    count_of_platforms = 0
    while left_pointer <= right_pointer:
        if robot_weights[right_pointer] + robot_weights[left_pointer] <= max_weight:
            left_pointer += 1 
        right_pointer -= 1
        count_of_platforms += 1
    return count_of_platforms


if __name__ == '__main__':
    robot_weights = [int(weight) for weight in input().split()]
    max_weight = int(input())
    print(delivery_service(robot_weights, max_weight))
