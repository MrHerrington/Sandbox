class Postman:
    """Класс описывает почтальона"""
    def __init__(self):
        """delivery_data — изначально пустой список адресов,
        по которым следует доставить письма"""
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        """Метод принимает в качестве аргументов улицу, дом и квартиру,
        и добавляет в список адресов эти данные в виде кортежа"""
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        """Метод принимает в качестве аргумента улицу и возвращает список всех домов
        на этой улице, в которые требуется доставить письма """
        all_results = map(lambda x: x[1], filter(lambda y: y[0] == street, self.delivery_data))
        return list(dict.fromkeys(all_results))

    def get_flats_for_house(self, street, house):
        """Метод принимает в качестве аргументов улицу и дом и возвращает список
        всех квартир в этом доме, в которые требуется доставить письма"""
        all_results = list(map(lambda x: x[-1],
                               filter(lambda y: y[0] == street and y[1] == house, self.delivery_data)))
        return list(dict.fromkeys(all_results))


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
