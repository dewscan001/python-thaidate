# Project Thaidate 

## Status : 0.1.5 - alpha

## Installation
```
    pip install thaidate
```
## Usage

```
from thaidate import thaidate
from datetime import date

'''
    thaidate('วัน เดือน ปี', True/False) หรือ thaidate('ปี เดือน วัน', True/False)
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
วัน.......ที่ ..... เดือน...... ปีพุทธศักราช ...... 

print(x.rattanakosin_era)   # x.rattanakosin_era  แสดงปี ร.ศ.

```

## Chengelog
```
0.1.5
- แก้ไข bug แสดงผลไม่ถูกต้อง


ตั้งแต่เวอร์ชัน 0.1.0 ลงไป มีบัคการแสดงผลไม่ถูกต้อง ควรใช้ เวอร์ชัน 0.1.5 ขึ้นไป

0.1.0  
- เปลี่ยนวิธีการแสดงผลวัน วันที่ เดือน ปี ในรูปแบบเต็ม จากเดิมต้องเรียกในรูปแบบเมธอด [x.full_date()] เป็น [x.full_date] ได้เลย
- เพิ่มแอททริบิวต์สำหรับแสดงวันที่ เดือน ปี 
       [x.date] =>  [x.day] [x.full_month] [x.year]
       [x.short_date] =>  [x.day] [x.short_month] [x.year]

0.0.1b
- เพิ่มแอททริบิวต์สำหรับแสดง วันในสัปดาห์ [x.weekday] วันที่ [x.day] เดือน [x.full_month] [x.short_month] ปี [x.year]
- เพิ่มแอททริบิวต์สำหรับปี ร.ศ. [x.rattanakosin_era]
- เพิ่มเมธอด สำหรับแสดงวัน วันที่ เดือน ปี ในรูปแบบเต็ม [x.full_date()]
        [x.full_date()] => วัน [x.weekday] ที่ [x.day] เดือน [x.month] ปีพุทธศักราช [x.year]

```