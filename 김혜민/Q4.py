'''
[Question 4] = (40점, 부분점수 있음)
<쇼핑몰 고객 및 주문 데이터 분석>
쇼핑몰의 고객 정보 데이터 crm_data와 최근 주문 내역 orders 데이터가 주어질 때 다음 질문에 답하시오.
단, 상품 카테고리(Category)는 1~5까지의 자연수만 있다고 가정한다.

(1) 전체 고객 데이터 crm_data에서 등록된 총 고객 인원수를 구하시오. (고객 정보는 customers) (10점)
(2) 최근 주문 내역(orders)의 평균 결제 금액을 구하시오. (10점)
(3) 최근 주문 내역(orders) 중 가장 많이 주문된 상품 카테고리를 구하시오. (10점)
(4) 가장 많이 주문된 카테고리의 고객들 중, CRM 데이터(customers)에서 고객 등급 점수(score)가 가장 높은 고객의 이름을 출력하시오. (10점)
'''

# 쇼핑몰 고객 데이터 (CRM)
crm_data = {
    'store_name': 'Green-Market',
    'location': 'Seoul',
    'customers': [
        {'name': 'Alice', 'category': 2, 'score': 1.423},
        {'name': 'Bob', 'category': 3, 'score': 5.225},
        {'name': 'Charlie', 'category': 1, 'score': 6.814},
        {'name': 'David', 'category': 2, 'score': 7.137},
        {'name': 'Eva', 'category': 2, 'score': 5.576},
        {'name': 'Frank', 'category': 3, 'score': 6.754},
        {'name': 'Grace', 'category': 1, 'score': 8.339},
        {'name': 'Henry', 'category': 3, 'score': 9.127},
        {'name': 'Ivy', 'category': 2, 'score': 8.934},
        {'name': 'Jack', 'category': 1, 'score': 5.147},
        {'name': 'Kelly', 'category': 2, 'score': 2.996},
        {'name': 'Liam', 'category': 2, 'score': 3.842},
        {'name': 'Mona', 'category': 2, 'score': 7.123},
        {'name': 'Noah', 'category': 5, 'score': 5.465},
        {'name': 'Olivia', 'category': 2, 'score': 8.846},
        {'name': 'Peter', 'category': 4, 'score': 3.157},
        {'name': 'Quinn', 'category': 3, 'score': 8.752},
        {'name': 'Rose', 'category': 4, 'score': 6.936},
        {'name': 'Steve', 'category': 2, 'score': 9.998},
        {'name': 'Tom', 'category': 2, 'score': 5.246},
        {'name': 'Ursula', 'category': 2, 'score': 2.502},
        {'name': 'Vince', 'category': 3, 'score': 4.478},
    ]
}
# print(sorted(crm_data['customers']))
# 최근 주문 내역
orders = [
    {'category': 1, 'amount': 72260},
    {'category': 3, 'amount': 24420},
    {'category': 2, 'amount': 86830},
    {'category': 2, 'amount': 96760},
    {'category': 3, 'amount': 42130},
    {'category': 2, 'amount': 37240},
    {'category': 2, 'amount': 55530},
    {'category': 4, 'amount': 91550},
    {'category': 3, 'amount': 46670},
    {'category': 5, 'amount': 59720},
    {'category': 5, 'amount': 63740},
    {'category': 1, 'amount': 38260},
    {'category': 2, 'amount': 17320},
    {'category': 1, 'amount': 79450},
    {'category': 2, 'amount': 13370},
]

order_sorted = sorted(orders, key = lambda x : -x['amount'])
print(order_sorted)
# # 1번 풀이
# (1) 전체 고객 데이터 crm_data에서 등록된 총 고객 인원수를 구하시오. (고객 정보는 customers) (10점)
# print(crm_data['customers'])
customer_count = 0
for _ in crm_data['customers']:
    customer_count += 1
print(f"(1) 등록 고객 수: {customer_count}")

# # 2번 풀이
# (2) 최근 주문 내역(orders)의 평균 결제 금액을 구하시오. (10점)
# avg_amount = 0
# for a, b in orders:
#      print(b)
# print(sorted(orders, lambda x : (-x['amount'])))
# print(f"(2) 평균 결제 금액: {avg_amount}")

# # 3번 풀이
# (3) 최근 주문 내역(orders) 중 가장 많이 주문된 상품 카테고리를 구하시오. (10점)
# top_category = 
# print(f"(3) 최다 주문 카테고리: {top_category}")

# # 4번 풀이
# (4) 가장 많이 주문된 카테고리의 고객들 중, CRM 데이터(customers)에서 고객 등급 점수(score)가 가장 높은 고객의 이름을 출력하시오. (10점)
# best_customer = 
# print(f"(4) 등급 점수가 가장 높은 고객: {best_customer}")