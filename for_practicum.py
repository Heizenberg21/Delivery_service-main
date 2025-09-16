# Посылка 142281093
def delivery_service(some_list: list, max_weight: int) -> int:
    """Служба доставки."""
    left_pointer = 0
    right_pointer = len(some_list) - 1
    count_of_platforms = 0
    while left_pointer <= right_pointer:
        if some_list[right_pointer] + some_list[left_pointer] <= max_weight:
            count_of_platforms += 1
            left_pointer += 1
            right_pointer -= 1
        else:
            count_of_platforms += 1
            right_pointer -= 1
    return count_of_platforms

if __name__ == '__main__':
    robot_weights = input().split()
    max_weight = int(input())
    robot_weights = sorted([int(weight) for weight in robot_weights])
    print(delivery_service(robot_weights, max_weight))
