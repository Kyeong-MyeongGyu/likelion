class Student: # 파이썬에서 클래스란 객체를 찍어내는 틀과 같다.
    def __init__(self, name, grade, student_number, sex, address, phone_number, year): # __init__ 함수는 초기화를 자동으로 시켜주는 메소드이다.
        self.name = name # 입력받은 name의 매개변수 값을 (Class_name).name인 인스턴트 변수에 저장한다.
        self.grade = grade # 입력받은 grade의 매개변수 값을 (Class_name).grade인 인스턴트 변수에 저장한다.
        self.student_number = student_number # 입력받은 student_number의 매개변수 값을 (Class_name).student_number인 인스턴트 변수에 저장한다.
        self.sex = sex # 입력받은 sex의 매개변수 값을 (Class_name).sex인 인스턴트 변수에 저장한다.
        self.address = address # 입력받은 address의 매개변수 값을 (Class_name).address인 인스턴트 변수에 저장한다.
        self.phone_number = phone_number # 입력받은 phone_number의 매개변수 값을 (Class_name).phone_number인 인스턴트 변수에 저장한다.
        self.year = year # 입력받은 year의 매개변수 값을 (Class_name).year인 인스턴트 변수에 저장한다.

    def introduce(self): # Student 클래스 내에 introduce 메소드를 생성한다.
        print("이름은 %s 이다." %self.name) # 저장된 (Class_name).name의 값을 출력한다.
        print("학년은은 %s 학년이다." %self.grade) # 저장된 (Class_name).grade의 값을 출력한다.
        print("학번은 %s 이다." %self.student_number) # 저장된 (Class_name).student_number의 값을 출력한다.
        print("성별은 %s 이다." %self.sex) # 저장된 (Class_name).sex의 값을 출력한다.
        print("주소는 %s 이다." %self.address) # 저장된 (Class_name).address의 값을 출력한다.
        print("전화번호는 %s 이다." %self.phone_number) # 저장된 (Class_name).phone_number의 값을 출력한다.
        if self.year == '1' : # 조건문을 통해, 저장된 (Class_name).year의 값이 1인지 검사한다.
            print("멋사 1년차") # (Class_name).year의 값이 1일 경우 이 값이 출력된다.
            print("우와 아기사자다!") # 이하동문
        else :
            print("멋사 %s년차" %self.year) # (Class_name).year의 값이 1이 아닐 경우 이 값이 출력된다.
            print("우와 운영진이다!") # 이하동문
        print("\n") # 반복문이 실행될 때매다 마지막에 한 줄이 띄어지도록 한다.

while True : # 반복문을 통해 Class_name에 '종료'를 입력하지 않는다면 무한하게 프로그램을 실행할 수 있도록 한다.
    Class_name = str(input("객체 명을 입력하시오. (단, 영문으로): ")) # 객체 명을 영문으로 입력받아서 Class_name에 저장한다.
    if Class_name == '종료' : # 조건문을 통해, 입력받은 객체 명이 '종료'인지 검사한다.
        break # 객체 명이 '종료'일 경우, 반복문이 종료된다.
    else :
        pass # 객체 명이 '종료'가 아닐 경우, 반복문이 계속 실행된다.
    name = str(input("이름을 입력하시오. (단, 한글로): ")) # 이름을 한글로 입력받아서 name에 저장한다.
    grade = int(input("학년을 입력하시오. (단, 숫자로): ")) # 학년을 숫자로 입력받아서 grade에 저장한다.
    student_number = int(input("학번을 입력하시오. (단, 숫자로): ")) # 학번을 숫자로 입력받아서 student_number에 저장한다.
    sex = str(input("성별을 입력하시오. (모를 때는 모른다 라고 입력.): ")) # 성별을 입력받아서 sex에 저장한다.
    if sex == '모른다' : # 조건문을 통해, 입력받은 성별의 값이 '모른다'인지 검사한다.
        sex = 'None' # 성별의 값이 '모른다'일 경우, sex에 'None'을 저장한다.
    else :
        pass # 성별의 값이 '모른다'가 아닐 경우, 입력받은 성별의 값이  sex에 그대로 저장된다.
    address = str(input("주소를 입력하시오. (~시까지만): ")) # 주소를 ~시까지만 입력받아서 address에 저장한다.
    phone_number = input("전화번호을 입력하시오. (모를 때는 모른다 라고 입력.): ") # 전화번호를 입력받아서 address에 저장한다.
    if phone_number == '모른다' : # 조건문을 통해, 입력받은 전화번호의 값이 '모른다'인지 검사한다.
        phone_number = 'None' # 전화번호의 값이 '모른다'일 경우, phone_number에 'None'을 저장한다.
    else :
        pass # 전화번호의 값이 '모른다'가 아닐 경우, 입력받은 전화번호의 값이 phone_number에 그대로 저장된다.
    year = int(input("멋사 몇년차인가요? (단, 숫자로): ")) # 멋사 몇년차인지 숫자로 입력받아서 year에 저장한다.

    Class_name = Student(name, grade, student_number, sex, address, phone_number, year) # 앞에서 입력받은 값들을 이용해서 인스턴스를 생성한다.
    Class_name.introduce() # introduce 메소드를 사용해 입력했던 값들을 출력받는다.