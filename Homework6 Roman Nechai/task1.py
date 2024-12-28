import abc
import random
import time


class Bank:

    initial_capital = 1000
    profit = 0


class Factory(abc.ABC):
    """Абстрактная фабрика"""

    def __init__(self, name, products):
        self.name = name
        self.products = products

    @abc.abstractmethod
    def __str__(self):
        pass


class BeerFactory(Factory):
    """Завод по производству пива"""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name:
            self.__name = name

    def __str__(self):
        return f'На заводе {self.name} производят лучшее пиво.'


class BrewHouse(BeerFactory):
    """Варочный цех"""

    ingredients = True
    batch_number = 0
    beer_barrels = []

    def __init__(self, name, products, vol, alc, kind, price, cost):
        super().__init__(name, products)
        self.vol = vol
        self.alc = alc
        self.kind = kind
        self.price = price
        self.bank = cost
        self.all = [self.name, self.vol, self.alc, self.price]

    def brew_beer(self):
        if self.ingredients:
            if self.bank.initial_capital >= self.price:
                self.bank.initial_capital -= self.price
                BrewHouse.batch_number += 1
                self.beer_barrels.append((
                    f'Партия {BrewHouse.batch_number}', self.vol, self.alc
                ))
                return (f'После варки у вас осталось'
                        f' {self.bank.initial_capital} у.е.')
            else:
                return 'Вы не можете сварить пиво, отсутствует капитал'
        else:
            return 'Проверьте ингредиенты'

    def __getitem__(self, item):
        return self.beer_barrels[item]

    def __add__(self, other):
        if type(other) is BrewHouse:
            return self.vol + other.vol
        raise TypeError(
            f'Unsupported operator + between ({type(other)} and {BrewHouse})'
        )

    def __eq__(self, other):
        if type(other) is BrewHouse:
            return self.alc == other.alc
        raise TypeError(
            f'Unsupported operator == between ({type(other)} and {BrewHouse})'
        )

    def __iter__(self):
        return iter(self.all)

    def __next__(self):
        if self.beer_barrels == []:
            raise StopIteration
        item = self.beer_barrels[0]
        del self.beer_barrels[0]
        return item

    def __str__(self):
        return f'В цеху {self.name} варится пиво.'


class QualityControl(BeerFactory):
    """Цех проверки качества товара"""

    def __init__(self, name, products, test):
        super().__init__(name, products)
        self.test = test

    def sample_for_analysis(self):
        ex = random.randrange(0, len(self.test.beer_barrels))
        fin_ex = self.test[ex]
        part, volume, alc = fin_ex
        if 4.5 < alc < 6:
            return f'{part} объемом {volume} литров проверку прошла'
        self.test.beer_barrels.pop(ex)
        print(f'Удалена партия {part}')
        return f'{part} объемом {volume} литров не прошла проверку'

    def __str__(self):
        return f'В цеху {self.name} проверяется качество напитков.'


class Packaging(BeerFactory):
    """Цех розлива пива"""

    def __init__(self, name, products, size, count, price, beer, cost):
        super().__init__(name, products)
        self.size = size
        self.count = count
        self.price = price
        self.beer = beer
        self.bank = cost

    def packaged_in_bottles(self):
        if self.count * self.size == self.beer.vol:
            if self.bank.initial_capital >= self.price:
                self.bank.initial_capital -= self.price
                return (f'Пиво {self.beer.name} упаковано в емкости'
                        f' объемом {self.size} л в количестве'
                        f' {self.count} шт.')
            else:
                return 'Вы не можете упаковать продукт, отсутствует капитал'
        else:
            return ('Проверьте, что объем и количество емкостей'
                    ' соответствуют объему сваренного пива')

    def __str__(self):
        return f'В цеху {self.name} пиво фасуется.'


class MarketingDepartment(BeerFactory):
    """Маркетинговый отдел"""

    def __init__(
            self, name, products, filename, mode, part, retailer, cost, bottle
    ):
        super().__init__(name, products)
        self.filename = filename
        self.mode = mode
        self.part = part
        self.retailer = retailer
        self.bank = cost
        self.pack = bottle

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.file.close()
        except ValueError:
            return True

    def sell_beer(self):
        if self.retailer:
            self.bank.initial_capital += self.part.price * 1.3
            self.bank.profit = (self.part.price * 1.3
                                - self.part.price - self.pack.price)
            return (f'{time.asctime()} Партия успешно продана,'
                    f' выручка составила {self.bank.profit}')
        return 'Покупателю не нужен ваш товар'

    def buy_bottles(self):
        if self.part.beer_barrels:
            self.bank.initial_capital -= self.pack.price
            return 'Бутылки приобретены'
        return 'Пиво еще не сварино'

    def __str__(self):
        return 'Здесь происходят финансовые махинации'


class Retailer:
    """Компания, скупающая готовый продукт"""

    def __init__(self, name, buy):
        self.name = name
        self.buy = buy

    def __bool__(self):
        return self.buy


bank = Bank()

brew = BrewHouse('Brew', 'Lager', 100, 4.0, 'white', 100, bank)
brew2 = BrewHouse('Brew', 'Porter', 100, 5.0, 'white', 200, bank)
brew3 = BrewHouse('Brew', 'Ale', 100, 4.6, 'white', 200, bank)
qual = QualityControl('Qual', 'Beer', brew)
pack = Packaging('Pack', 'bottles', 1.0, 100, 1.0, brew, bank)
pack2 = Packaging('Pack', 'bottles', 1.0, 90, 1.0, brew, bank)

retail = Retailer('Store', True)
market = MarketingDepartment(
    'Marketing', 'Pack beer', 'reporting.txt', 'w', brew3, retail, bank, pack
)

print(brew.name)
# brew.ingredients = False
print(brew.brew_beer())
print(brew.beer_barrels)
print(brew.beer_barrels)
print(brew2.brew_beer())
print(brew2.beer_barrels)
print(brew3.brew_beer())
print(brew3.beer_barrels)
print(brew[0] == brew2[0])
print(qual.sample_for_analysis())
print(brew + brew2)
print(brew == brew3)
print(pack.packaged_in_bottles())
print(pack2.packaged_in_bottles())
print(brew.beer_barrels)
print(qual.sample_for_analysis())
print(brew.beer_barrels)

print(market.sell_beer())
print(bank.initial_capital)

with market as my_file:
    my_file.write(market.sell_beer())

for i in brew:
    print(i)

iter(brew)
print(next(brew))
print(next(brew))
print(next(brew))
# print(next(brew))

print(brew.beer_barrels)
