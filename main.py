# 쇼핑몰 프로젝트
class Item:
    def __init__(self, item, price, stock):
        self.item = item           # 상품명
        self.price = price         # 가격
        self.stock = stock         # 재고수량

    def __str__(self):
        return f"상품 : {self.item}, 가격 : {self.price:,}, 재고수량{self.stock}"

    def __repr__(self):
        return f"상품 : {self.item}, 가격 : {self.price:,}, 재고수량{self.stock}"

    # 판매 후 재고감소
    def decrease(self, amount):
        if amount <= 0:
            print("수량은 1개 이상이어야 합니다.")
            return False
        
        if self.stock < amount:
            print("재고가 부족합니다.")
            return False

        self.stock -= amount

        if self.stock == 0:
            print("품절되었습니다.")

        return True


class ShoppingCart:
    def __init__(self):
        self.bucket = {}
 
    # 장바구니 넣기
    def add_item(self, item, amount):
        if amount <= 0:
            print("수량은 1개 이상이어야 합니다.")
            return

        # 기존 상품인지 확인
        current_amount = self.bucket.get(item, 0)

        # 재고 확인
        if current_amount + amount > item.stock:
            print(f"재고가 부족합니다. (담을 수 있는 수량: {item.stock - current_amount}개)")
            return
        
        # 수량 추가
        self.bucket[item] = current_amount + amount
        print(f"{item.item} {amount}개를 담았습니다.")  

    # 장바구니 빼기
    def remove_item(self, item):
        if item in self.bucket:
            del self.bucket[item]
            print(f"{item.item}을(를) 장바구니에서 제거했습니다.")
        else:
            print("장바구니에 없는 상품입니다.")

    
    # 상품 목록 조회
    def show_item(self):
        return self.bucket

    #상품 합계
    def get_total(self):
        total = 0
        for item, amount in self.bucket.items():
            total += item.price * amount

        return total

# 할인 쿠폰 클래스 추가
class Discount:
    def discount_amount(self, total):
        return 0

# 10% 할인
class RateDiscount(Discount):
    def discount_amount(self, total):
        discount = int(total*0.1)
        return min(discount, 5000)

# 3,000원 할인
class FixedDiscount(Discount):
    def discount_amount(self, total):
        if total >= 20_000:
            return 3000
        else:
            return 0
        


# 상품 생성
item_1 = Item("무선 이어폰", 89_000, 3)
item_2 = Item("텀블러", 15_000, 10)
item_3 = Item("보조배터리", 32_000, 5)
item_4 = Item("마우스패드", 9_000, 0)
item_5 = Item("USB 허브", 18_000, 4)

# 장바구니 생성
cart = ShoppingCart()

cart.add_item(item_3, 3)
cart.add_item(item_2, 2)

print(f"상품 합계: {cart.get_total():,}원")

