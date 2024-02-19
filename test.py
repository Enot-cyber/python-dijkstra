import math

def calculate_distance(point1, point2):
    
    # Расчет расстояния между двумя точками по их гео-координатам.
    
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def assign_orders(orders, couriers):
    
    # Распределение заказов между курьерами с приоритетом на скорость доставки.
    
    for order in orders:
        min_distance = float('inf')
        closest_courier = None
        
        for courier in couriers:
            distance = calculate_distance(order['from'], courier['location'])
            if distance < min_distance:
                min_distance = distance
                closest_courier = courier
        
        closest_courier['orders'].append(order)
        closest_courier['location'] = order['to']  # Обновляем координаты курьера
        
    return couriers

# Пример входных данных
# Список заказов
orders = [
    {'from': (10, 20), 'to': (30, 40)},
    {'from': (15, 25), 'to': (35, 45)},
    {'from': (20, 30), 'to': (40, 50)},
    {'from': (25, 35), 'to': (45, 55)},
    {'from': (30, 40), 'to': (50, 60)},
    {'from': (35, 45), 'to': (55, 65)},
    {'from': (40, 50), 'to': (60, 70)},
    {'from': (45, 55), 'to': (65, 75)},
    {'from': (50, 60), 'to': (70, 80)},
    {'from': (55, 65), 'to': (75, 85)},
]

# Список курьеров
couriers = [
    {'id': 1,'location': (5, 15), 'orders': []},
    {'id': 2,'location': (20, 30), 'orders': []},
    {'id': 3,'location': (40, 50), 'orders': []},
]

# Распределение заказов между курьерами
assigned_couriers = assign_orders(orders, couriers)

# Вывод результата
for courier in assigned_couriers:
    print("Курьер ", courier['id'], " доставляет заказы:", courier['orders'])

