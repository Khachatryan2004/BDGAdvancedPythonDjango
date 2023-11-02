# Generated by Django 4.2.6 on 2023-10-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Publication title')),
                ('publication_type1', models.BooleanField(default=False, verbose_name='Sale')),
                ('publication_type2', models.BooleanField(default=False, verbose_name='Looking for')),
                ('status1', models.BooleanField(default=False, verbose_name='Owner')),
                ('status2', models.BooleanField(default=False, verbose_name='Dialer')),
                ('brand', models.CharField(choices=[('Acura', 'Acura'), ('Alfa Romeo', 'Alfa Romeo'), ('Audi', 'Audi'), ('Bentley', 'Bentley'), ('BMW', 'BMW'), ('Bugatti', 'Bugatti'), ('Buick', 'Buick'), ('Cadillac', 'Cadillac'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Coda', 'Coda'), ('Ferrari', 'Ferrari'), ('Fisker', 'Fisker'), ('Ford', 'Ford'), ('Genesis', 'Genesis'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Infiniti', 'Infiniti'), ('Jaguar', 'Jaguar'), ('Kia', 'Kia'), ('Lamborghini', 'Lamborghini'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Lincoln', 'Lincoln'), ('Lotus', 'Lotus'), ('Maserati', 'Maserati'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Mini', 'Mini'), ('Mitsubishi', 'Mitsubishi'), ('Nikola', 'Nikola'), ('NIO', 'NIO'), ('Nissan', 'Nissan'), ('Pagani', 'Pagani'), ('Polestar', 'Polestar'), ('Porsche', 'Porsche'), ('Rimac', 'Rimac'), ('Rolls-Royce', 'Rolls-Royce'), ('Saab', 'Saab'), ('Subaru', 'Subaru'), ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('Xpeng', 'Xpeng'), ('Zenvo', 'Zenvo')], max_length=13, verbose_name='Car Brand')),
                ('model', models.CharField(max_length=10, verbose_name='Car Model')),
                ('year', models.CharField(choices=[('1900', '1900'), ('1901', '1901'), ('1902', '1902'), ('1903', '1903'), ('1904', '1904'), ('1905', '1905'), ('1906', '1906'), ('1907', '1907'), ('1908', '1908'), ('1909', '1909'), ('1910', '1910'), ('1911', '1911'), ('1912', '1912'), ('1913', '1913'), ('1914', '1914'), ('1915', '1915'), ('1916', '1916'), ('1917', '1917'), ('1918', '1918'), ('1919', '1919'), ('1920', '1920'), ('1921', '1921'), ('1922', '1922'), ('1923', '1923'), ('1924', '1924'), ('1925', '1925'), ('1926', '1926'), ('1927', '1927'), ('1928', '1928'), ('1929', '1929'), ('1930', '1930'), ('1931', '1931'), ('1932', '1932'), ('1933', '1933'), ('1934', '1934'), ('1935', '1935'), ('1936', '1936'), ('1937', '1937'), ('1938', '1938'), ('1939', '1939'), ('1940', '1940'), ('1941', '1941'), ('1942', '1942'), ('1943', '1943'), ('1944', '1944'), ('1945', '1945'), ('1946', '1946'), ('1947', '1947'), ('1948', '1948'), ('1949', '1949'), ('1950', '1950'), ('1951', '1951'), ('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'), ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'), ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'), ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=4, verbose_name='Car Year')),
                ('engine', models.CharField(blank=True, choices=[('Gas', 'Gas'), ('Diesel', 'Diesel')], default='Gas', max_length=6, null=True, verbose_name='Engine Type')),
                ('volumes', models.CharField(choices=[('0.7', '0.7'), ('0.8', '0.8'), ('0.9', '0.9'), ('1.0', '1.0'), ('1.1', '1.1'), ('1.2', '1.2'), ('1.3', '1.3'), ('1.4', '1.4'), ('1.5', '1.5'), ('1.6', '1.6'), ('1.7', '1.7'), ('1.8', '1.8'), ('1.9', '1.9'), ('2.0', '2.0'), ('2.1', '2.1'), ('2.2', '2.2'), ('2.3', '2.3'), ('2.4', '2.4'), ('2.5', '2.5'), ('2.6', '2.6'), ('2.7', '2.7'), ('2.8', '2.8'), ('2.9', '2.9'), ('3.0', '3.0'), ('3.1', '3.1'), ('3.2', '3.2'), ('3.3', '3.3'), ('3.4', '3.4'), ('3.5', '3.5'), ('3.6', '3.6'), ('3.7', '3.7'), ('3.8', '3.8'), ('3.9', '3.9'), ('4.0', '4.0'), ('4.1', '4.1'), ('4.2', '4.2'), ('4.3', '4.3'), ('4.4', '4.4'), ('4.5', '4.5'), ('4.6', '4.6'), ('4.7', '4.7'), ('4.8', '4.8'), ('4.9', '4.9'), ('5.0', '5.0'), ('5.1', '5.1'), ('5.2', '5.2'), ('5.3', '5.3'), ('5.4', '5.4'), ('5.5', '5.5'), ('5.6', '5.6'), ('5.7', '5.7'), ('5.8', '5.8'), ('5.9', '5.9'), ('6.0', '6.0'), ('6.1', '6.1'), ('6.2', '6.2'), ('6.3', '6.3'), ('6.4', '6.4'), ('6.5', '6.5'), ('6.6', '6.6'), ('6.7', '6.7'), ('6.8', '6.8'), ('6.9', '6.9'), ('7.0', '7.0'), ('7.1', '7.1'), ('7.2', '7.2'), ('7.3', '7.3'), ('7.4', '7.4'), ('7.5', '7.5'), ('7.6', '7.6'), ('7.7', '7.7'), ('7.8', '7.8'), ('7.9', '7.9'), ('8.0', '8.0'), ('8.1', '8.1'), ('8.2', '8.2'), ('8.3', '8.3'), ('8.4', '8.4'), ('8.5', '8.5')], max_length=3, verbose_name='Engine Volumes')),
                ('horsepower', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Engine Horsepower')),
                ('transmission', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('cvvt', 'CVT'), ('dct', 'DCT'), ('tiptronic', 'Tiptronic')], max_length=20, verbose_name='Transmission Type')),
                ('unit', models.CharField(choices=[('AWD', 'AWD'), ('FWD', 'FWD'), ('RWD', 'RWD')], max_length=3, verbose_name='Drive Unit')),
                ('mileage', models.PositiveSmallIntegerField(verbose_name='Mileage Value')),
                ('color_of_car', models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('silver', 'Silver'), ('gray', 'Gray'), ('blue', 'Blue'), ('red', 'Red'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('brown', 'Brown'), ('purple', 'Purple'), ('gold', 'Gold')], max_length=20, verbose_name='Car Color')),
                ('wheel_size', models.CharField(blank=True, choices=[('R26', 'R26'), ('R25', 'R25'), ('R24', 'R24'), ('R23', 'R23'), ('R22', 'R22'), ('R21', 'R21'), ('R20', 'R20'), ('R19', 'R19'), ('R18', 'R18'), ('R17', 'R17'), ('R16', 'R16'), ('R15', 'R15'), ('R14', 'R14'), ('R13', 'R13'), ('R12', 'R12'), ('R11', 'R11'), ('R10', 'R10')], max_length=3, null=True, verbose_name='Wheel Sizes')),
                ('color_of_interior', models.CharField(blank=True, choices=[('black', 'Black'), ('gray', 'Gray'), ('beige', 'Beige'), ('brown', 'Brown'), ('white', 'White'), ('cream', 'Cream'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('orange', 'Orange'), ('purple', 'Purple'), ('another', 'Another')], max_length=20, null=True, verbose_name='Interior Color')),
                ('comfort1', models.BooleanField(blank=True, default=False, null=True, verbose_name='AIR Conditioner')),
                ('comfort2', models.BooleanField(blank=True, default=False, null=True, verbose_name='Heated Seats')),
                ('comfort3', models.BooleanField(blank=True, default=False, null=True, verbose_name='Heated Steering Wheel')),
                ('comfort4', models.BooleanField(blank=True, default=False, null=True, verbose_name='Cruise Control')),
                ('comfort5', models.BooleanField(blank=True, default=False, null=True, verbose_name='Tinted Windows')),
                ('price_of_car', models.PositiveSmallIntegerField(verbose_name='Price')),
                ('currency_choose', models.CharField(choices=[('AMD', 'AMD'), ('RUB', 'RUB'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=3, verbose_name='Currency')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo1', models.ImageField(upload_to='media/images/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('photo6', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('mail', models.EmailField(max_length=30, unique=True, verbose_name='Email')),
                ('telephone_number', models.CharField(max_length=20, unique=True, verbose_name='Telephone Number')),
                ('slug', models.SlugField(blank=True, max_length=160, null=True)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]