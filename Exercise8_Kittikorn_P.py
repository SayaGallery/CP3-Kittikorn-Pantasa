usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "operator" and passwordInput == "0000":
    print("Success!")
    print("----  Welcome (:  -----")
    print("Please Select Product")
    print("-----------------------")
    print("No1. Cola can 325ml     = 18 ฿ ")
    print("No2. Water 620ml        = 10 ฿  ")
    print("No3. Sandwich Ham       = 20 ฿  ")
    print("No4. Coffee Can 180 ml  = 15 ฿  ")

    userSelected = int(input("Press No."))
    item = int(input("รับสินค้ากี่ชิ้น  : "))
    if userSelected == 1:
        print("ราคารวมทั้งสิ้น :",18 * item,"฿")
    elif userSelected == 2:
        print("ราคารวมทั้งสิ้น :",10 * item,"฿")
    elif userSelected == 3:
        print("ราคารวมทั้งสิ้น :",20 * item,"฿")
    elif userSelected == 4:
        print("ราคารวมทั้งสิ้น :",15 * item,"฿")
    else:
        print("--------------")
        print("ไม่มีสินค้าที่ระบุ ):")
else:
    print("Wrong password!")






