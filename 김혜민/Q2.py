'''
[Question 2] = (20점)
<이달의 우수 영업 사원 선발>
영업팀 팀원들의 이름과 이번 달 매출 실적(만원)이 담긴 2차원 리스트가 주어집니다.
이번 달에 가장 높은 매출을 기록한 영업 사원의 이름을 출력하시오.
'''

sales_performance = [
    ['Kim', 1500], ['Lee', 2400], ['Park', 850], ['Choi', 4100],
    ['Jung', 5500], ['Kang', 3200], ['Cho', 4800], ['Yoon', 1200],
    ['Jang', 6200], ['Lim', 8900], ['Han', 400], ['Oh', 7500],
    ['Seo', 4400], ['Shin', 4100], ['Kwon', 1010], ['Hwang', 1240]
]
a =sorted(sales_performance, key = lambda x : -x[1])
print(a[0])
# sales_performance[]



# 로직 작성
# def sales_good(sales):
#     for s in sales_performance:
    
    

