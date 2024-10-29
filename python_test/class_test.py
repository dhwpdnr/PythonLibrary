# Basic Coding
car_company_1 = "Toyota"
car_detail_1 = [{"color": "White"}, {"horsepower": 400}, {"price": 10000}]

car_company_2 = "BMW"
car_detail_2 = [{"color": "Black"}, {"horsepower": 270}, {"price": 50000}]

car_company_3 = "Audi"
car_detail_3 = [{"color": "Silver"}, {"horsepower": 300}, {"price": 60000}]

# List 구조
car_company_list = ["Toyota", "BMW", "Audi"]
car_detail_list = [
    {"color": "White", "horsepower": 400, "price": 10000},
    {"color": "Black", "horsepower": 270, "price": 50000},
    {"color": "Silver", "horsepower": 300, "price": 60000},
]

print("Car company list")
print(car_company_list)
print("Car detail list")
print(car_detail_list)

print()
print()

# BMW 삭제
del car_company_list[1]
del car_detail_list[1]

print("Car company list")
print(car_company_list)
print("Car detail list")
print(car_detail_list)

print()
print()

# Dictionary 구조
car_dicts = [
    {
        "car_company": "Toyota",
        "car_detail": {"color": "White", "horsepower": 400, "price": 10000},
    },
    {
        "car_company": "BMW",
        "car_detail": {"color": "Black", "horsepower": 270, "price": 50000},
    },
    {
        "car_company": "Audi",
        "car_detail": {"color": "Silver", "horsepower": 300, "price": 60000},
    },
]
print("Car company dictionary")
print(car_dicts)

print()
print()

# BMW 삭제
del car_dicts[1]
print("Car company dictionary")
print(car_dicts)

print()
print()


# Class 구조
class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"


car1 = Car("Toyota", {"color": "White", "horsepower": 400, "price": 10000})
car2 = Car("BMW", {"color": "Black", "horsepower": 270, "price": 50000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 60000})

print("Car class instance")
print(f"str method car1 - {car1}")
print(f"repr method car1 - {car1.__repr__()}")
print()
print(f"str method car2 - {car2}")
print(f"repr method car2 - {car2.__repr__()}")
print()
print(f"str method car3 - {car3}")
print(f"repr method car3 - {car3.__repr__()}")
print()
print()
print("__dict__ 확인")
print(f"car1.dict : {car1.__dict__}")
print(f"car2.dict : {car2.__dict__}")
print(f"car3.dict : {car3.__dict__}")
print()
print()

print("dir 확인")
print(dir(car1))

print()
print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print("Car list")
# 이때는 str 메소드가 아닌 repr 메소드가 호출됨
print(car_list)

print()

print("Car list 반복")
for i in car_list:
    # str 메소드가 호출됨
    print(i)
