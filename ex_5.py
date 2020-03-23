Rev = int(input("Введите уровень выручки - "))
Csts = int(input("Введите уровень издержек - "))
Res = Rev - Csts
if Res > 0:
    print(F"Well done! Profit is - {Res}")
    Eff = Res / Rev
    Emp = int(input("Введите кол-во сотрудников - "))
    Rev_p_E = Rev / Emp
    print(F"Рентабельность выручки = {Eff*100}%")
    print(F"Прибыль на человека = {Rev_p_E}")
else:
    if Res == 0:
     print (F"Not bad. The result is - {Res}")
    else:
     print (F"You should work better. The result is - {Res}")