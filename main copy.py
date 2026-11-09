# # 클래스 정의(선언) : 붕어빵 틀
# class User:
#     def __init__ (self, name): # 생성자 : 클래스가 처음 생성될 때 자동으로 호출
#         self.name = name # 변수를 초기화

#     def show(self): #메서드(Method)
#         return f"회원 이름: {self.name}"

# # 인스턴스 생성 : 붕어빵 만들기
# user_a = User("손흥민")
# user_b = User("이강인")

# # user 클래스로 생성한 인스턴스 (메모리에 생성)

# # 클래스의 인스턴스 변수
# print(user_a.name)
# print(user_b.name)

# # 클레스의 메서드 접근
# print(user_a.show())
# print(user_b.show())

# print(type(user_a))
# print(user_a is user_b)
# print(id(user_a))
# print(id(user_b))


# # =============================

# class Monitor:
#     def display_info(self):
#         # 인스턴스 변수
#         self.resolution = "1920X1080"
#         self.size = "27인치"
#         print(f"모니터 정보\n해상도: {self.resolution}\n크기: {self.size}\n객체 ID: {id(self)}")

# monitor = Monitor() # 인스턴스 생성 (모니터 객체 생성)
# print(id(monitor))  # 모니터 인스턴스의 ID 출력

# monitor.display_info()

# # ===================================
# class SmartPhone:
#     def __init__(self, model):
#         self.model = model # 속성 (Attribute)
#         self.battery = 50 # 속성 (Attrubute)

#     def charge(self, amount):
#         self.battery += amount
#         if self.battery > 100:
#             self.battery = 100
#             print(f"배터리 충전 완료 : {self.battery}%")
#         else:
#             print(f"배터리 충전 중 ... : {self.battery}%")
            
# phone_a = SmartPhone("아이폰")
# print(phone_a.model)
# phone_a.charge(30)
# phone_a.charge(30)


# phone_b = SmartPhone("갤럭시")
# print(phone_b.model)
# phone_b.charge(18)
# phone_b.charge(18)
# phone_b.charge(18)

# 은행 계좌 클래스

class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = owner          # 계좌 예금주
        self.balance = balance      # 잔액

    def __str__(self):
        return f"예금주 : {self.owner}, 잔액: {self.balance:,} "

    def __repr__(self):
        return f"예금주 : {self.owner}, 잔액: {self.balance:,} "
    
    
    #입금 처리 메서드
    def deposit(self, amount):
        self.balance += amount # 입금처리
        print(f"{amount:,} 입금완료 / 잔액 : {self.balance:,}원")

    #출금 매서드
    #잔액 확인 => 잔액부족 메시 출력
    def withdraw(self, amount):
        # psudo code
        # 잔액 확인
            if self.balance < amount:
                print("잔액이 부족합니다.")
                return 0
            
            self.balance -= amount # 출금처리
            print(f"{amount:,} 출금완료") 
            return self.balance # 춯금후 잔액 리턴

account_a = BankAccount("배유성", 100_000)
print(account_a)
account_a.deposit(500_000)

account_a.withdraw(1_000_000)

print(f"잔액:{account_a.withdraw(200_000):,}")

print(f"잔액:{account_a.withdraw(300_000):,}")


account_b = BankAccount("홍길동1", 200_000)

account_c = BankAccount("홍길동", 200_000)

print(f"잔액:{account_c.withdraw(200_000):,}")

print([account_a, account_b, account_c])

print(account_a)


# shopping cart 클래스 생성
# 상품 목록 저장 기능
# 메서드
# - 장바구니 담기
# - 장바구니 빼기
# - 상품 목록 조회
class ShoppingCart:
    def __init__(self):
        self.bucket = []
    # 장바구니 넣기
    def add_item(self, item):
        self.bucket.append(item)
    # 장바구니 빼기
    def remove_item(self, item):
        self.bucket.remove(item)
    # 상품 목록 조회
    def show_items(self):
        return self.bucket


# 상품 클래스
# 속성
# - 제품명 
# - 가격
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 쇼핑 카트 생성
cart = ShoppingCart()

# 상품 3개 생성
item_a = Item("초코파이", 5000)
item_b = Item("새우깡", 2000)
item_c = Item("빅파이", 3000)

# 상품 1개 장바구니 담기
cart.add_item(item_a)
# 상품 1개 장바구니 담기
cart.add_item(item_b)
# 상품 1개 장바구니 담기
cart.add_item(item_c)
# 상품 1개 장바구니에서 빼기
cart.remove_item(item_b)
# 장바구니에 담긴 상품 목록 조회
for item in cart.show_items():
    print(item.name, item.price)
