print("What bank do you want to transfer to? ")
print("1. Access Bank")
print("2. First Bank")
print("3. Polaris Bank")
print("4. Opay")
print("5. Zenith Bank")
print("6. FCMB")
print("7. Other banks")
response = str(input(" "))
if response == "1" or response == "Access Bank":
    #Transfer to Access Bank
    recipient_account_number = int(input("Enter recipient's account number "))
    print("Confirming account name...")
    amount = int(input("Enter the amount to be transferred:#"))
    print(f"Transferring #{amount} to Access Bank account number {recipient_account_number}....")
    print("Transfer Processing...")
    print("Transfer Successful👍👍👍 \nThank you for banking with us!❤")
elif response == "2" or response == "First Bank":
    #Transfer to First Bank
    recipient_account_number = int(input("Enter recipient's account number "))
    print("Confirming account name...")
    amount = int(input("Enter the amount to be transferred:#"))
    print(f"Transferring #{amount} to First Bank account number {recipient_account_number}....")
    print("Transfer Processing...")
    print("Transfer Successful👍👍👍 \nThank you for banking with us!❤")
elif response == "3" or response == "Polarris Bank":
    #Transfer to Polaris Bank
    recipient_account_number = int(input("Enter recipient's account number "))
    print("Confirming account name...")
    amount = int(input("Enter the amount to be transferred:#"))
    print(f"Transferring #{amount} to Polaris Bank account number {recipient_account_number}....")
    print("Transfer Processing...")
    print("Transfer Successful👍👍👍 \nThank you for banking with us!❤")
elif response == "4" or response == "Opay":
    #Transfer to Opay
    recipient_account_number = int(input("Enter recipient's account number "))
    print("Confirming account name...")
    amount = int(input("Enter the amount to be transferred:#"))
    print(f"Transferring #{amount} to Opay account number {recipient_account_number}....")
    print("Transfer Processing...")
    print("Transfer Successful👍👍👍 \nThank you for banking with us!❤")
elif response == "5" or response == "Zenith Bank":
    #Transfer to Zenith Bank
    recipient_account_number = int(input("Enter recipient's account number "))
    print("Confirming account name...")
    amount = int(input("Enter the amount to be transferred:#"))
    print(f"Transferring #{amount} to Zenith Bank account number {recipient_account_number}....")
    print("Transfer Processing...")
    print("Transfer Successful👍👍👍 \nThank you for banking with us!❤")
elif response == "6" or response == "FCMB":
    #Transfer to Opay
    recipient_account_number = int(input("Enter recipient's account number "))
    print("Confirming account name...")
    amount = int(input("Enter the amount to be transferred:#"))
    print(f"Transferring #{amount} to FCMB account number {recipient_account_number}....")
    print("Transfer Processing...")
    print("Transfer Successful👍👍👍 \nThank you for banking with us!❤")
elif response == "7" or response == "Other banks":
    #Transfer to Other banks
    bank_name = str(input("Search bank name: "))
    recipient_account_number = int(input("Enter recipient's account number "))
    print("Confirming account name...")
    amount = int(input("Enter the amount to be transferred:#"))
    print(f"Transferring #{amount} to {bank_name} account number {recipient_account_number}....")
    print("Transfer Processing...")
    print("Transfer Successful👍👍👍 \nThank you for banking with us!❤")
else:
    print("INVALID REQUEST!")

#For Airtime Recharge
print("Select Network Provider")
print("1. MTN \n2. GLO \n3.AIRTEL \n4. 9MOBILE")
reply = str(input(" "))
#MTN Recharge
if reply == "1" or reply == "MTN":
    Phone_Number = int(input("Enter MTN phone number "))
    print("Select Amount")
    print("1. 100")
    print("2. 200")
    print("3. 500")
    print("4. 1000")
    print("5. 5000")
    print("6. Others")
    answer = str(input(" "))
    if answer == "1" or answer == "100":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "2" or answer == "200":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "3" or answer == "500":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "4" or answer == "1000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "5" or answer == "5000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    else:
        enter_amount = int(input("Enter the amount#"))
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
#GLO Recharge
elif reply == "2" or reply == "GLO":
    Phone_Number = int(input("Enter GLO phone number "))
    print("Select Amount")
    print("1. 100")
    print("2. 200")
    print("3. 500")
    print("4. 1000")
    print("5. 5000")
    print("6. Others")
    answer = str(input(" "))
    if answer == "1" or answer == "100":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "2" or answer == "200":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "3" or answer == "500":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "4" or answer == "1000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "5" or answer == "5000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    else:
        enter_amount = int(input("Enter the amount#"))
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
#AIRTEL Recharge
elif reply == "3" or reply == "AIRTEL":
    Phone_Number = int(input("Enter AIRTEL phone number "))
    print("Select Amount")
    print("1. 100")
    print("2. 200")
    print("3. 500")
    print("4. 1000")
    print("5. 5000")
    print("6. Others")
    answer = str(input(" "))
    if answer == "1" or answer == "100":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "2" or answer == "200":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "3" or answer == "500":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "4" or answer == "1000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "5" or answer == "5000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    else:
        enter_amount = int(input("Enter the amount#"))
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
#9MOBILE Recharge
elif reply == "4" or reply == "(9MOBILE)":
    Phone_Number = int(input("Enter 9MOBILE phone number "))
    print("Select Amount")
    print("1. 100")
    print("2. 200")
    print("3. 500")
    print("4. 1000")
    print("5. 5000")
    print("6. Others")
    answer = str(input(" "))
    if answer == "1" or answer == "100":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "2" or answer == "200":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "3" or answer == "500":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "4" or answer == "1000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    elif answer == "5" or answer == "5000":
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
    else:
        enter_amount = int(input("Enter the amount#"))
        print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us❤")
else:
    print("INVALID REQUEST! \nCheck options and try again.")
    