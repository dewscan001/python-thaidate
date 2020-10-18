# Project Thaidate 

## Status : Alpha-0.0.10

## Usage

```
from thaidate import thaidate

'''
    thaidate('วัน เดือน ปี', True/False)
    ex1: 
        ใช้เมื่อปี คือ พ.ศ.
        x = thaidate('1 2 5', True) 
        
    ex2: 
        ใช้เมื่อปี คือ ค.ศ.
        x = thaidate('1 2 5', False) 
        หรือ
        x = thaidate('1 2 5')
        
    ex3:
        สำหรับแสดงวันที่ปัจจุบัน
        x = thaidate()   
        
'''

x = thaidate()
print(x.day)                # x.day แสดงวันที่
print(x.full_month)         # x.full_month แสดงเดือนแบบเต็ม
print(x.short_month)        # x.short_month แสดงเดือนแบบย่อ
print(x.year)               # x.year แสดงปี พ.ศ.
print(x.weekday)            # x.weekday แสดงวันในสัปดาห์

print(x.full_date())        # x.full_date()  แสดงวัน เดือน ปี ในรูปแบบเต็ม 
วัน.......ที่ ..... เดือน...... ปีพุทธศักราช ...... 

print(x.rattanakosin_era)   # x.rattanakosin_era  แสดงปี ร.ศ.

```

## Chengelog
alpha-0.0.10
- เพิ่มแอททริบิวต์สำหรับแสดง วันในสัปดาห์ วันที่ เดือน ปี
- เพิ่มเมธอด สำหรับแสดงวัน เดือน ปี ในรูปแบบเต็ม