from collections import Counter


class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = []
        all_orders = list(self.data)

        for order in all_orders:
            if order[0] == customer:
                customer_orders.append(order[1])
        return Counter(customer_orders).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        ordered_dishes = []
        unordered = []
        all_orders = list(self.data)
        for order in all_orders:
            if order[0] == customer:
                ordered_dishes.append(order[1])
            else:
                unordered.append(order[1])
        for order in all_orders:
            if order[0] == customer:
                ordered_dishes.append(order[1])
            else:
                unordered.append(order[1])
        return set(unordered) - set(ordered_dishes)

    def get_days_never_visited_per_customer(self, customer):
        days_visited = []
        not_visited = []
        all_orders = list(self.data)
        for order in all_orders:
            if order[0] == customer:
                days_visited.append(order[2])
            else:
                not_visited.append(order[2])
        for order in all_orders:
            if order[0] == customer:
                days_visited.append(order[2])
            else:
                not_visited.append(order[2])
        return set(not_visited) - set(days_visited)

    def get_busiest_day(self):
        days = []
        all_orders = list(self.data)

        for order in all_orders:
            days.append(order[2])
        print(days)
        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = []
        all_orders = list(self.data)

        for order in all_orders:
            days.append(order[2])
        print(days)
        return Counter(days).most_common()[-1][0]
