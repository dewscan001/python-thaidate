from thaidate import thaidate, thaidatetime
from datetime import date

'''
    thaidate(date(ปี, เดือน, วัน), True/False)
    ex1: 
        ใช้เมื่อปี คือ พ.ศ. เช่น วันที่ 1 เดือนกุมภาพันธ์ ปี พ.ศ. 5
        x = thaidate(date(5, 2, 1), True) 
        
    ex2: 
        ใช้เมื่อปี คือ ค.ศ. เช่น วันที่ 1 เดือนกุมภาพันธ์ ปี ค.ศ. 5
        x = thaidate(date(5, 2, 1), False) 
        หรือ
        x = thaidate(date(5, 2, 1))
        
    ex3:
        สำหรับแสดงวันที่ปัจจุบัน
        x = thaidate()   
        
'''

x = thaidate()              # ใช้คำสั่งนี้ สำหรับการแสดงวันเดือนปี
print(x.day)                # x.day แสดงวันที่ เช่น วันที่ 1
print(x.full_month)         # x.full_month แสดงเดือนแบบเต็ม เช่น มกราคม
print(x.short_month)        # x.short_month แสดงเดือนแบบย่อ เช่น ม.ค.
print(x.year)               # x.year แสดงปี พ.ศ.
print(x.weekday)            # x.weekday แสดงวันในสัปดาห์ เช่น วันอาทิตย์

# x.date แสดงวันที่ เดือน ปีพุทธศักราช เช่น 5 พฤศจิกายน 2536
print(x.date)
# x.date แสดงวันที่ เดือน ปีพุทธศักราช เช่น 5 พ.ย. 2536
print(x.short_date)

print(x.full_date)          # x.full_date  แสดงวัน เดือน ปี ในรูปแบบเต็ม
# วัน.......ที่ ..... เดือน...... ปีพุทธศักราช ......

print(x.rattanakosin_era)   # x.rattanakosin_era  แสดงปี ร.ศ.


#####################################################################
y = thaidatetime()          # ใช้คำสั่งนี้ สำหรับการแสดงวันเดือนปี ชั่วโมงนาทีวินาที
print(y.hour)               # แสดงชั่วโมง
print(y.minute)             # แสดงนาที
print(y.fulltime)           # แสดงเวลา ในรูปแบบ 'เวลา ... นาฬิกา ... นาที ... วินาที'
print(y.datetime)           # แสดงวันและเวลา ในรูปแบบ '5 พฤศจิกายน 2536 เวลา ... นาฬิกา ... นาที ... วินาที'
print(y.fulldatetime)       # แสดงวันและเวลา ในรูปแบบ 'วัน.......ที่ ..... เดือน...... ปีพุทธศักราช ......  เวลา ... นาฬิกา ... นาที ... วินาที'
print(y.short_datetime)       # แสดงวันและเวลา ในรูปแบบ 'วันที่ เดือน(ตัวย่อ) ปี  เวลา ... นาฬิกา ... นาที ... วินาที'
