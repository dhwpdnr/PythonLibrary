# 클래스 테스트
# 메소드 추가
class Car:
    """
    Car class
    Author: Oh
    Date: 2024.10.29
    """

    # 클래스 변수
    car_count = 0

    def __init__(self, company, details):
        # 인스턴스 변수
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"

    def __del__(self):
        Car.car_count -= 1

    # detail_info 메소드 추가
    def detail_info(self):
        print(f"Current ID: {id(self)}")
        print(f"Car Detail Info: {self._company} {self._details.get('price')}")


car1 = Car("Toyota", {"color": "White", "horsepower": 400, "price": 10000})
car2 = Car("BMW", {"color": "Black", "horsepower": 270, "price": 50000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 60000})

# ID 확인
print("ID of car1: ", id(car1))
print("ID of car2: ", id(car2))
print("ID of car3: ", id(car3))
print()

# dir & __dict__ 확인
print("dir 은 클래스의 모든 속성과 메소드를 보여줍니다.")
print(dir(car1))
print()

print("car1.__dict__ 는 인스턴스의 모든 속성을 보여줍니다.")
print(car1.__dict__)

# Doctring 확인
print("Doctring 확인")
print(Car.__doc__)
print()

# detail_info 메소드 출력
print("detail_info 메소드 출력")
car1.detail_info()
print()
car2.detail_info()
print()
print()

# 비교
print("car1과 car2의 클래스가 같은지 확인")
print(car1.__class__, car2.__class__)
print(f"car1.__class__ == car2.__class__ : {car1.__class__ == car2.__class__}")
print()
print("car1과 car2의 클래스 ID가 같은지 확인")
print(id(car1.__class__), id(car2.__class__))
print(
    f"id(car1.__class__) == id(car2.__class__) : {id(car1.__class__) == id(car2.__class__)}"
)
print()
print()

# 클래스 변수
print("클래스 변수 확인")
print(f"Car.car_count : {Car.car_count}")
print("클래스 변수는 모든 인스턴스가 공유합니다.")
print()
print()

# __del__ 메소드
print("__del__ 메소드 확인")
print("car1 삭제")
del car1
print(f"Car.car_count : {Car.car_count}")
