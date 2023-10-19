import database as db

def employee_update():
    designation=input("enter your designation:")
    salary=input("Enter your salary:")
    db.car.execute(f"insert into employee(designation,salary) values('{designation}','{salary}')")
    print("Your data feed successfully")

def ticket_booking():
    start_point=input("Enter your start point: ").casefold()
    end_point=input("Enter your end point:").casefold()
    journey=start_point+"-"+end_point
    db.car.execute(f"select start_end from fair where start_end='{journey}'")
    available_destination=[i for i in db.car][0][0]
    if journey == available_destination:
        pclass=input("enter your class:") 
        name=input("Enter you name:")
        db.car.execute(f"select 1st,2nd,chrage from fair where start_end='{journey}'")
        print([i for i in car])
        
        if 700.50<=amount and amount<2000 and pclass=="3rd":
            amount=eval(input("Enter your amount:"))    
            total=ticket_amount_3rd=700.50
            total=amount-ticket_amount_3rd
            print("collect amount",total)
            db.car.execute(f"insert into trip(name,amount,class) values('{name}',700.50,'3rd')")
            db.krishna.commit()
            print(f"ticket confirm 700.50 and {pclass}")
        elif 1400.00<=amount and amount<2000 and pclass=="2nd":
            amount=eval(input("Enter your amount:"))
            ticket_amount_2nd=1400.00
            total=amount-ticket_amount_2nd
            print("collect amount",total)
            db.car.execute(f"insert into trip(name,amount,class) values('{name}',1400.50,'2nd')")
            db.krishna.commit()
            print(f"ticket confirm 1400.00 and {pclass}")
        elif amount>=2900.50 and pclass=="1st":
            amount=eval(input("Enter your amount:"))
            ticket_amount_1st=2900.50
            total=amount-ticket_amount_1st
            print("collect amount",total)
            db.car.execute(f"insert into trip(name,amount,class) values('{name}',2900.50,'1st')")
            db.krishna.commit()
            print(f"ticket confirm 2900.50 and {pclass}")
        else:
            print("Paise muh per marenge tumhare")
            print("Your ticket is not confirmed")
    else:
        print("destination is not available")