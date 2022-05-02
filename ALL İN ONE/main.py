#
#
#      tarzımız farkımız aşko
#
#


import os
from platform import system
from traceback import print_exc






def clear_screen():
    if system() == "Linux":
        os.system("clear")
    if system() == "Windows":
        os.system("cls")


clear_screen()

print("   ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄██████▄           ███      ▄██████▄   ▄██████▄   ▄█       ")
print("  ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███      ▀█████████▄ ███    ███ ███    ███ ███       ")
print("  ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀          ▀███▀▀██ ███    ███ ███    ███ ███       ")
print(" ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███                 ███   ▀ ███    ███ ███    ███ ███       ")
print("▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄           ███     ███    ███ ███    ███ ███       ")
print("  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███          ███     ███    ███ ███    ███ ███       ")
print("  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███          ███     ███    ███ ███    ███ ███▌    ▄ ")
print("  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀          ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ ")
print("                                   made by strAgont     instagram=poyrazss                                                      ")
print("                                   simsiyah bir gencenin , öfkesiydi sözlerin                                                   ")

print("İNSTAGRAM HACKİNG (1)")
print("FACEBOOK HACKİNG (2)")
print("PROXY ?! (3)")
print("PHİSHİNG TOOL (4)")

main = int(input("WHİCH OPTİONS ? ="))


if main == 1:
   if system() == "Linux":
      os.system("cd ALL İN ONE")
      os.system("python3 insta.py")
   if system() == "Windows":
      os.system("cd ALL İN ONE")
      os.system("python insta.py")

elif main == 2:
   if system() == "Linux":
      os.system("cd ALL İN ONE")
      os.system("python3 face.py")
   if system() == "Windows":
      os.system("cd ALL İN ONE")
      os.system("python face.py") 

elif main == 3:
   print("knks senin pc çöp .")
   
elif main == 4:
   if system() == "Linux":
      os.system("bash phisher.sh")
   if system() == "Windows":
      os.system("bash phisher.sh")