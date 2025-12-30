'''
[Question 3] = (30점)
<누락된 결제 내역 확인>
회계 팀에서는 결제 내역을 대조하고 있습니다. 
정상적인 거래는 승인 번호가 한 쌍(승인-확정, 2개)씩 존재해야 하지만, 
시스템 오류로 인해 단 하나의 승인 번호만이 짝 없이 혼자 기록되었습니다.
전체 승인 번호 리스트가 주어질 때, 짝이 없는 '미확정 결제 번호'를 찾아 반환하는 함수를 완성하시오.
'''

auth_codes1 = [1010, 2020, 3030, 1010, 4040, 5050, 2020, 5050, 4040]
auth_codes2 = [7, 101, 25, 13, 1, 101, 77, 7, 13, 1, 25]
# print(auth_codes1.count(1010))
# x = []
# y = []

def find_unconfirmed_code(codes):
    for codes in auth_codes1:
        if auth_codes1.count(codes) == 2:
            print(find_unconfirmed_code)

        
            
    # for codes in auth_codes2:
        # 

# print(find_unconfirmed_code(auth_codes1))  # 3030 출력
# print(find_unconfirmed_code(auth_codes2))  # 77 출력
