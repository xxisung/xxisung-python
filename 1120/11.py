#버스는 10정거장 미만일 경우에는 각 역의 평균 이동 시간이 2분 소요되며,
#10정가장이 넘으면 4분의 소요 시간이 걸린다.
#버스 정거장 수를 입력하면 소요시간을 계산하여 출력하시어

way = int(input("정거장수를 입력하시오: "))
if way < 10:
    print("총 소요 시간은 %d분 입니다."%(way * 2))
else:
    if way * 4 >=60:
        #100 => 1시간 40분
        hour = (way * 4) // 60 #시간
        min = (way * 4) % 60 #분
        print("총 소요 시간은 %d시간%d분 입니다."%(hour,min))
    else:
            print("총 소요 시간은 %d분 입니다."%(way * 4))