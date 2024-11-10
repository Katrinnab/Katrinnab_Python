class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        lst = ['Отправление', self.track, 'из', self.to_address.index,
               self.to_address.city, self.to_address.street,
               self.to_address.home_number, '-', self.to_address.flat_number,
               'в', self.from_address.index, self.from_address.city,
               self.from_address.street, self.from_address.home_number,
               '-', self.from_address.flat_number, 'Стоимость',
               self.cost]

        return ' '.join(lst)
