import datetime
name = 'Avarice'
age = 32
relationship_status = 'single'

relationship_status = 'it \'s complicated'

birth_year = input('what year were you born?')


today_date = datetime.date.today()
age_calc = today_date.year - int(birth_year)
print(f'your age is: {age_calc}')
