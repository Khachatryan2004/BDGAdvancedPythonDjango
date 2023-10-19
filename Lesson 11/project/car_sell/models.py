from django.db import models


class CarSell(models.Model):
    car_brands = (
        ('Acura', 'Acura'),
        ('Alfa Romeo', 'Alfa Romeo'),
        ('Audi', 'Audi'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Bugatti', 'Bugatti'),
        ('Buick', 'Buick'),
        ('Cadillac', 'Cadillac'),
        ('Chevrolet', 'Chevrolet'),
        ('Chrysler', 'Chrysler'),
        ('Coda', 'Coda'),
        ('Ferrari', 'Ferrari'),
        ('Fisker', 'Fisker'),
        ('Ford', 'Ford'),
        ('Genesis', 'Genesis'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Infiniti', 'Infiniti'),
        ('Jaguar', 'Jaguar'),
        ('Kia', 'Kia'),
        ('Lamborghini', 'Lamborghini'),
        ('Land Rover', 'Land Rover'),
        ('Lexus', 'Lexus'),
        ('Lincoln', 'Lincoln'),
        ('Lotus', 'Lotus'),
        ('Maserati', 'Maserati'),
        ('Mazda', 'Mazda'),
        ('McLaren', 'McLaren'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mini', 'Mini'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nikola', 'Nikola'),
        ('NIO', 'NIO'),
        ('Nissan', 'Nissan'),
        ('Pagani', 'Pagani'),
        ('Polestar', 'Polestar'),
        ('Porsche', 'Porsche'),
        ('Rimac', 'Rimac'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Saab', 'Saab'),
        ('Subaru', 'Subaru'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
        ('Xpeng', 'Xpeng'),
        ('Zenvo', 'Zenvo')
    )
    body_types = (
        ('sedan', 'Sedan'),
        ('wagon', 'Wagon'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('suv', 'SUV'),
        ('crossover', 'Crossover'),
        ('minivan', 'Minivan'),
        ('pickup', 'Pickup'),
        ('limousine', 'Limousine'),
        ('van', 'Van'),
        ('targa', 'Targa'),
        ('sports_car', 'Sports Car'),
        ('truck', 'Truck')
    )
    years = (
        (str(year), str(year)) for year in range(1900, 2024)
    )

    engine_type = (
        ('Gas', 'Gas'),
        ('Diesel', 'Diesel'),
    )
    engine_volumes = (
        (str(volume / 10), str(volume / 10)) for volume in range(7, 86, 1)
    )
    transmission_types = (
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('cvvt', 'CVT'),
        ('dct', 'DCT'),
        ('tiptronic', 'Tiptronic'),
    )
    drive_unit = (
        ('AWD', 'AWD'),
        ('FWD', 'FWD'),
        ('RWD', 'RWD')
    )
    car_color = (
        ('black', 'Black'),
        ('white', 'White'),
        ('silver', 'Silver'),
        ('gray', 'Gray'),
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('brown', 'Brown'),
        ('purple', 'Purple'),
        ('gold', 'Gold'),
    )
    wheel_sizes = (
        ('R26', 'R26'),
        ('R25', 'R25'),
        ('R24', 'R24'),
        ('R23', 'R23'),
        ('R22', 'R22'),
        ('R21', 'R21'),
        ('R20', 'R20'),
        ('R19', 'R19'),
        ('R18', 'R18'),
        ('R17', 'R17'),
        ('R16', 'R16'),
        ('R15', 'R15'),
        ('R14', 'R14'),
        ('R13', 'R13'),
        ('R12', 'R12'),
        ('R11', 'R11'),
        ('R10', 'R10')
    )
    interior_colors = (
        ('black', 'Black'),
        ('gray', 'Gray'),
        ('beige', 'Beige'),
        ('brown', 'Brown'),
        ('white', 'White'),
        ('cream', 'Cream'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('another', 'Another')
    )
    currency = (
        ('AMD', 'AMD'),
        ('RUB', 'RUB'),
        ('EUR', 'EUR'),
        ('USD', 'USD')
    )

    title = models.CharField('Publication title', max_length=40, unique=True)

    publication_type1 = models.BooleanField('Sale', default=False)
    publication_type2 = models.BooleanField('Looking for', default=False)

    status1 = models.BooleanField('Owner', default=False)
    status2 = models.BooleanField('Dialer', default=False)

    brand = models.CharField('Car Brand', choices=car_brands, max_length=13)
    model = models.CharField('Car Model', max_length=10)
    year = models.CharField('Car Year', choices=years, max_length=4)

    engine = models.CharField('Engine Type', choices=engine_type, max_length=6, default='Gas', blank=True, null=True)
    volumes = models.CharField('Engine Volumes', choices=engine_volumes, max_length=3)
    horsepower = models.PositiveSmallIntegerField('Engine Horsepower', default=0, blank=True, null=True)

    transmission = models.CharField('Transmission Type', choices=transmission_types, max_length=20)
    unit = models.CharField('Drive Unit', choices=drive_unit, max_length=3)
    mileage = models.PositiveSmallIntegerField('Mileage Value')

    color_of_car = models.CharField('Car Color', choices=car_color, max_length=20)
    wheel_size = models.CharField('Wheel Sizes', choices=wheel_sizes, max_length=3, blank=True, null=True)
    color_of_interior = models.CharField('Interior Color', choices=interior_colors, max_length=20, blank=True,
                                         null=True)

    comfort1 = models.BooleanField('AIR Conditioner', default=False, blank=True, null=True)
    comfort2 = models.BooleanField('Heated Seats', default=False, blank=True, null=True)
    comfort3 = models.BooleanField('Heated Steering Wheel', default=False, blank=True, null=True)
    comfort4 = models.BooleanField('Cruise Control', default=False, blank=True, null=True)
    comfort5 = models.BooleanField('Tinted Windows', default=False, blank=True, null=True)

    price_of_car = models.PositiveSmallIntegerField('Price')
    currency_choose = models.CharField('Currency', choices=currency, max_length=3)
    description = models.TextField('Description')

    photo1 = models.ImageField(upload_to='media/images/')
    photo2 = models.ImageField(upload_to='media/images/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='media/images/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='media/images/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='media/images/', blank=True, null=True)
    photo6 = models.ImageField(upload_to='media/images/', blank=True, null=True)

    mail = models.EmailField('Email', max_length=30, unique=True)
    telephone_number = models.CharField('Telephone Number', max_length=20, unique=True)

    slug = models.SlugField(max_length=160, blank=True, null=True)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

