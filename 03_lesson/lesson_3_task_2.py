from smartphone import Smartphone

catalog = [Smartphone('Sumsung', 'A51', '+79119792032'),
           Smartphone('Nokia', 'M53', '+79217685375'),
           Smartphone('Iphone', 'E3', '+79347654321'),
           Smartphone('LG', 'S65', '+78128548643'),
           Smartphone('Sumsung', 'S21', '+79119792754')]

for i in catalog:
    print(f'{i.brand} - {i.model}. {i.phone_number}')
