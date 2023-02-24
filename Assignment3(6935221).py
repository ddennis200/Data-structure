#This codes displays a list of cars you are capable of buying with your money
import numpy as np
car=int(input('Please enter the amount you wish to spend on a car from our store: $'))

print()

if car > 1000000:
    print('You are eligible to purchase a toyota corolla')
elif 950000 <= car < 1000000:
    print('You are eligible to purchase a Audi')
elif 850000 <= car < 900000:
    print('You are eligible to purchase a Tesla')
elif 750000 <= car < 850000:
    print('You are eligible to purchase a Volkswagen')
elif 650000 <= car < 750000:
    print('You are eligible to purchase a Range Roner')
elif 550000 <= car < 650000:
    print('You are eligible to purchase a Honda')
elif 450000 <= car < 550000:
    print('You are eligible to purchase a G Wagon')
elif 350000 <= car < 450000:
    print('You are eligible to purchase a Hyundai')
elif 250000 <= car < 350000:
    print('You are eligible to purchase an Peugot')
elif 150000 <= car < 250000:
    print('You are eligible to purchase a Dodge')
elif 100000 <= car < 150000:
    print('You are eligible to purchase a Ford')
elif 95000 <= car < 100000:
    print('You are eligible to purchase a AMG Benz')
elif 90000 <= car < 95000:
    print('You are eligible to purchase a vitz')
elif 85000 <= car < 90000:
    print('You are eligible to purchase a Bugatti')
elif 80000 <= car < 85000:
    print('You are eligible to purchase a Hammer')
elif 75000 <= car < 80000:
    print('You are eligible to purchase a Hilux')
elif 70000 <= car < 75000:
    print('You are eligible to purchase a Mitsubushi')
elif 65000 <= car < 70000:
    print('You are eligible to purchase a Ferrari')
elif 60000 <= car < 65000:
    print('You are eligible to purchase a Elantra')
elif 55000 <= car < 60000:
    print('You are eligible to purchase a Mazda')
elif 50000 <= car < 55000:
    print('You are eligible to purchase a Shelby Cobra')
elif 45000 <= car < 50000:
    print('You are eligible to purchase an Pathfinder')
elif 40000 <= car < 45000:
    print('You are eligible to purchase a Mercedes Benz')
elif 35000 <= car < 40000:
    print('You are eligible to purchase a Kia')
elif 30000 <= car < 35000:
    print('You are eligible to purchase a Honda Civic')
elif 25000 <= car < 30000:
    print('You are eligible to purchase a Volvo')
elif 20000 <= car < 25000:
    print('You are eligible to purchase a Volkswagen')
elif 15000 <= car < 20000:
    print('You are eligible to purchase a Sante fe')
elif 10000 <= car < 15000:
    print('You are eligible to purchase a GLA')
elif 5000 <= car < 10000:
    print('You are eligible to purchase a Pontiac')
elif 1000 <= car < 5000:
    print('You are eligible to purchase a Kantaka')
else:    print('We are sorry but you cannot afford any car from our store but we sell other car accessories if you are interested')
