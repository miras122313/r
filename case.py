#место для твоего кода
import pandas as examen
import matplotlib.pyplot as plt
examen = examen.read_csv('StudentsPerformance .csv')
examen.info()



female_math = examen[examen['gender']=='female']['math score'].mean()
male_math = examen[examen['gender']=='male']['math score'].mean()
female_reading = examen[examen['gender']=='female']['reading score'].mean()
male_reading = examen[examen['gender']=='male']['reading score'].mean()
female_write = examen[examen['gender']=='female']['writing score'].mean()
male_write = examen[examen['gender']=='male']['writing score'].mean()

female_free = 0
female_standart = 0

def lunch_counter(row):
    global female_free, female_standart
    if fow['gender'] == 'femali' and row['lunch'] == 'standart':
        female_standart+=1
    if fow['gender'] == 'femali' and row['lunch'] == 'free/reduced':
        female_free+=1
    return False

examen.apply(lunch_counter, axis = 1)
print(female_free, female_standart)

print('Результаты по математике:', 'Девочки:', round(female_math, 2), 'Мальчики:', round(male_math, 2))
print('Результаты по чтению:',  'Девочки:', round(female_reading, 2), 'Мальчики:', round(male_math, 2))
print('Результаты по письму:', 'Девочки:',  round(female_write, 2), 'Мальчики:', round(male_math, 2))

print('Девочки сильнее в гуманитарных науках, а мальчики в точных науках')


reading = (examen['reading score'].value_counts())
reading_mean = examen['reading score'].mean()
writing = (examen['writing score'].value_counts())
writing_mean = examen['writing score'].mean()
math = (examen['math score'].value_counts())
math_mean = examen['math score'].mean()
print('у учеников средние результаты по алгебре ниже чем результаты по другим тестам?')
math_reading = math_mean / reading_mean
math_writing = math_mean / writing_mean
if math_reading > 1 :
    print(math_reading)
    print('по матиматике больше чем по чтению')
else:
    print(math_reading)
    print('по математике меньше чем по чтению')
if math_writing > 1 :
    print(math_writing)
    print('по матиматике больше чем по писанию')
else:
    print(math_writing)
    print('по математике меньше чем по писанию')

print('Теория подверждена что у учеников средние результаты по алгебре ниже чем результаты по другим тестам ')


