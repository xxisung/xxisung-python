#일어나니 시간이 많이 지났다. 버스탈지, 택시를 탈지 고민하는 코드
#지하철과 버스 사이에서도 고민을 할 수 있다.
print("지각이다, 대중교통과 택시 중 무얼 탈까?")
money = input("택시 탈 돈이 있나?[y/n]:")

if money == 'n' :
    print("할 수 없다. 지하철과 버스 중 멀 타지?")
    time = input("지금이 러시아워인가[y/n]:")
    if time == 'y':
        print("지하철이 낫겠다.")
    else:
        print("버스 타고 가야지")

else:
    print("그냥 택시타고 편하게 가야지")
        