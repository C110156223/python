hr,min,sec=input("請輸入時間1(時:分:秒):").split(':')
time2=int(input("請輸入時間2(秒):"))
hr=int(hr)*60*60
min=int(min)*60
sec=int(sec)
time1=(sec+hr+min)

hr2=int(time2/60/60)
min2=int((time2-(hr2*60*60))/60)
sec2=int(time2-(hr2*60*60)-(min2*60))
print("時間1轉換為:",time1,"秒")
print("時間2轉換為:",hr2,":",min2,":",sec2)