#Program name: Ebill.py

#Unit Consumed    Charge per Unit
#--------------     -------------

#Upto 100units      Rs.1.50
#101 to 300units    Rs.2.50
#301 and above      Rs. 3.50


#An extra of Rs.50 is charged towards the reconnection of electricity meter used by the customer after default


name = input("Enter Name:")
Units = int(input('Enter Number of Units:'))


if Units <= 300:
    amount_to_pay = Units*1.50
    print(amount_to_pay)

elif Units <= 300:
    amount_to_pay =150 + (Units-100) * 2.50
    print(amount_to_pay)
else:
    amount_to_pay=650 + (Units-300) * 3.50

print("Name:", name)
print("Units Consumed:", Units)
print("Electricity Bill:%0.2f"%amount_to_pay )
print('Extra charges for reconnect is Rs 50')


