from thaidate import thaidate
from datetime import date

'''
    thaidate(date(ปี, เดือน, วัน), True/False)
    ex1: 
        ใช้เมื่อปี คือ พ.ศ. เช่น วันที่ 1 เดือนกุมภาพันธ์ ปี พ.ศ. 5
        x = thaidate(date(5 2 1), True) 
        
    ex2: 
        ใช้เมื่อปี คือ ค.ศ. เช่น วันที่ 1 เดือนกุมภาพันธ์ ปี ค.ศ. 5
        x = thaidate(date(5 2 1), False) 
        หรือ
        x = thaidate(date(5 2 1))
        
    ex3:
        สำหรับแสดงวันที่ปัจจุบัน
        x = thaidate()   
        
'''

x = thaidate()
print(x.day)                # x.day แสดงวันที่ เช่น วันที่ 1
print(x.full_month)         # x.full_month แสดงเดือนแบบเต็ม เช่น มกราคม
print(x.short_month)        # x.short_month แสดงเดือนแบบย่อ เช่น ม.ค.
print(x.year)               # x.year แสดงปี พ.ศ.
print(x.weekday)            # x.weekday แสดงวันในสัปดาห์ เช่น วันอาทิตย์

print(x.date)               # x.date แสดงวันที่ เดือน ปีพุทธศักราช เช่น 5 พฤศจิกายน 2536
print(x.short_date)         # x.date แสดงวันที่ เดือน ปีพุทธศักราช เช่น 5 พ.ย. 2536

print(x.full_date)          # x.full_date  แสดงวัน เดือน ปี ในรูปแบบเต็ม 
#วัน.......ที่ ..... เดือน...... ปีพุทธศักราช ...... 

print(x.rattanakosin_era)   # x.rattanakosin_era  แสดงปี ร.ศ.
