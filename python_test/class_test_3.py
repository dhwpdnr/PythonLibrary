class Car:
    """
    Car class
    Author: Oh
    Date: 2024.10.29
    Description: Class, Static, Instance Method
    """

    # 클래스 변수
    price_per_raise = 1.0

    def __init__(self, company, details):
        # 인스턴스 변수
        self._company = company
        self._details = details

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"

    # detail_info 메소드 추가 (Instance Method)
    def detail_info(self):
        print(f"Current ID: {id(self)}")
        print(f"Car Detail Info: {self._company} {self._details.get('price')}")

    # Instance Method
    def get_price(self):
        return f"Before Car Price -> company: {self._company}, price: {self._details.get('price')}"

    # Instance Method
    def get_price_calc(self):
        return f"After Car Price -> company: {self._company}, price: {self._details.get('price') * Car.price_per_raise}"

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        print("Succeed! Price increased.")

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "BMW":
            return "OK! This car is BMW."
        return "Sorry. This car is not BMW."


car1 = Car("Toyota", {"color": "White", "horsepower": 400, "price": 10000})
car2 = Car("BMW", {"color": "Black", "horsepower": 270, "price": 50000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 60000})

# 전체 정보
car1.detail_info()
car2.detail_info()
car3.detail_info()

# 가격 정보
print("직접 접근 가격 정보")
print(car1._details.get("price"))
print(car2._details["price"])

print()
print()

print("메소드를 통한 가격 정보")
print("가격 정보 인상 전")
print(car1.get_price())
print(car2.get_price())

print()

Car.price_per_raise = 1.4

print("가격 정보 인상 후")
print(car1.get_price_calc())
print(car2.get_price_calc())

print()

print("가격 인상 메소드에 1 입력")
Car.raise_price(1)

print()

print("가격 인상 클래스 메소드에 1.6 입력")
Car.raise_price(1.6)

print()

print("가격 정보 인상 후")
print(car1.get_price_calc())
print(car2.get_price_calc())

print()
print()

print("Static Method is_bmw 사용")
# 인스턴스로 호출
print(f"car1 is_bmw (instance) : {car1.is_bmw(car1)}")
print(f"car2 is_bmw (instance) : {car2.is_bmw(car2)}")

print()

# 클래스로 호출
print(f"car1 is_bmw (class) : {Car.is_bmw(car1)}")
print(f"car2 is_bmw (class) : {Car.is_bmw(car2)}")
