import sys
from itertools import combinations_with_replacement
n,m,l,k = map(int,input().split())

stars = []


for _ in range(k):
    x,y = map(int,input().split())
    stars.append((x,y))

stars_comb = list(combinations_with_replacement(stars,2))

zone = [(l,l),(-l,-l)] 

# 우주로 튕겨나간 별 갯수
def cnt_starts(x_range, y_range):
    tmp_cnt = 0
    for star_x, star_y in stars:
        # 별이 트램펄린 범위 안에 있으면, 우주로 튕겨나간다.
        if x_range[0]<=star_x<=x_range[1] and y_range[0]<=star_y<=y_range[1]:
            tmp_cnt +=1
    
    return tmp_cnt


min_cnt =  sys.maxsize
# 별의 총 갯수는 100개

for s1_x, s1_y in stars:
    for s2_x,s2_y in stars:
        nx = min(s1_x,s2_x)
        ny = min(s1_y,s2_y)
        
        x_range = [nx, nx + l]
        y_range = [ny, ny + l]
    
        min_cnt = min(min_cnt, k-cnt_starts(x_range, y_range))
        

# for star1, star2 in stars_comb :
    
#     s_x = min(star1[0], star2[0])
#     s_y = min(star1[1], star2[1])
    
#     x_range = [s_x, s_x + l]
#     y_range = [s_y, s_y + l]
    
#     min_cnt = min(min_cnt, k-cnt_starts(x_range, y_range))
   
print(min_cnt)