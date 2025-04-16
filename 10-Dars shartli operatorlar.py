# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Apr 15 08:46:09 2025

# @author: dm
# """

# yosh=int(input("Yoshingizni kiriting: "))
# if yosh<=4 or yosh>=60:
#     print("Sizga Kirish bepul!")
# elif yosh<=18:
#     print("Sizga kirish 10 ming so'm ! ")
# else:
#     print("Sizga kirish 20 ming so'm! ")



# kun=str(input("Bugun nima kun? >>>"))
# if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#     print("Bugun dam olish kuni! ")
# else:
#     print("Bugun ish kuni!")

# menu=["osh","manti","kabob","shashlik"]
# buyurtma=str(input("Ovqat nomini kiriting.>>> "))
# if buyurtma.lower() in menu:
#     print("Buyurtmangiz qabul qilindi! ")
# else:
#     print("Uzur,bizda bunday taom yo'q!")


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")


# son=int(input("Juft son kiriting.>>> "))

# if son%2:
#   print("Bu son juft emas!")
# else:
#     print("Raxmat")


# x=float(input("Birinchi sonni kiriting>>> "))
# y=float(input("Ikkinchi sonni kiriting>>> "))
# if x>y:
#     print(f"{x}>{y}")
# else:
#     print(f"{x}<{y}")


# mahsulotlar=["olma","shaftoli","nok","qulupnay","olkcha"]
# savat=[]
# for n in range(5):
#     savat.append(str(input(f"{n+1}-mahsulotni kiriting.>>> ")))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")


# foydalanuvchilar=["anvar","ali","karim","ulugbek"]
# admin=(str(input("Loginingizni kiriting.>>> ")))
# if admin.lower() in foydalanuvchilar:
#     print("Bu login band.Iltimos boshqa login tanlang")
# else:
#     print(f" {admin.title()} Hush kelibsiz!")
# son=int(input("Istalgan bitta butun sonni kiriting.>>> "))
# for n in range(2,10):
#     if not son%n:
        
        
#       print(f"{son} {n}ga qoldiqsiz bo'linadi") 