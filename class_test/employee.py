class Employee:
    # 클래스 변수 (모든 인스턴스에서 공유)
    total_employees = 0

    def __init__(self, name, position, salary):
        # 인스턴스 변수 (각 직원별로 개별 저장)
        self.name = name
        self.position = position
        self.salary = salary

        # 새로운 직원이 생성될 때마다 증가
        Employee.total_employees += 1

    def display_info(self):
        """사원의 정보를 출력하는 메서드"""
        print(f"이름: {self.name}, 직무: {self.position}, 연봉: {self.salary:,.0f}원")

    @classmethod
    def get_total_employees(cls):
        """현재 직원 수를 반환하는 클래스 메서드"""
        return f"현재 총 직원 수: {cls.total_employees}명"

    def remove_employee(self):
        """직원 삭제 메서드"""
        print(f"{self.name} 직원이 퇴사 처리되었습니다.")

        # 직원 수 감소
        Employee.total_employees -= 1

        # 객체 삭제
        del self


# 직원 객체 생성 (인스턴스)
emp1 = Employee("김철수", "소프트웨어 엔지니어", 60000000)
emp2 = Employee("이영희", "데이터 분석가", 65000000)
emp3 = Employee("박지성", "프로젝트 매니저", 75000000)

# 직원 정보 출력
emp1.display_info()
emp2.display_info()
emp3.display_info()

# 총 직원 수 확인 (클래스 메서드 호출)
print(Employee.get_total_employees())
