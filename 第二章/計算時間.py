#題目:從地球到月球距離為384400公里 火箭速度為每小時1225公里 需要多久時間才能抵達
km=384400
speed=1225
total_hours=km//speed
days=total_hours//24
hours=total_hours%24
print("需要%d天又%d小時"%(days,hours))