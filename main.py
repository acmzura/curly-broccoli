import os
import random

days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

for i in range(180, 360):
    year = '2024'
    month = random.randint(1, 12)
    max_day = days_in_month[month]
    day = random.randint(1, max_day)
    
    year = str(year)
    if len(str(month)) == 1:
        month = '0'+str(month)
    else:
        month = str(month)
        
    if len(str(month)) == 1:
        day = '0'+str(day)
    else:
        day = str(day)
        
    commit_date = year+'-'+month+'-'+day
    f'{year}-{month:02}--{day:02}'
    d = f'{i} days ago'

    with open('test'+day+'.txt', 'a') as f:
        f.write(d + '\n')
        os.system('git add test'+day+'.txt')
        os.system(f'git commit --date="{commit_date}" -m "Commit number {i+1}"')

os.system('git push -u origin main')
