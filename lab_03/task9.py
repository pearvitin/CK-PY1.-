salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 1.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):
    need_money -= salary
    need_money += spend
    spend *= increase

print(round(need_money))

