import matplotlib.pyplot as plt 
import numpy as np

coffee_names = ['Kirema', 'Aguacate', 'Progreso', 'La Pradera',
                'Palmichal', 'El Apostol', 'Planada', 'Hakuna Matata',
                'Lugmapada', 'Duromina', 'Efrem', 'Kossa', 'Kossa Spro',
                'San Pedro', 'Yara', 'Method', 'Comon Yaj',
                'La Victoria', 'Francisco', 'Cenfrocafe',
                'Technique', 'Kanyenze', 'San Nicholas',
                'Asprocdegua', 'Nueva Esperanza', 'Tero']
ppp = [16, 13.5, 19.5, 13.5, 17.5, 17.5, 19, 19.5, 15.5, 16, 15.5, 15.5,
       13.5, 18.5, 13.5, 13.5, 13.5, 15.5, 13.5, 13.5, 13.5, 19.5, 13.5, 13.5,
       13.5, 13.5]

oct_2018_sales = [70, 48, 108, 76, 40.5, 157.5, 140, 76, 78, 77.5,
                  144, 108.5, 108.5, 108, 74, 54, 54, 81, 93, 94.5,
                  0, 54, 0, 0, 0, 0]

nov_2018_sales = [70, 121.5, 0, 57, 54, 35, 175, 0, 136.5, 46.5, 
                  144, 108.5, 139.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0]

dec_2018_sales = [140, 32, 148.5, 0, 121.5, 87.5, 105, 0, 58.5, 
                  62, 80, 170.5, 108.5, 81, 111, 81, 108, 67.5, 
                  93, 135, 81, 0, 39, 0, 0, 31]



plt.title('2018 Holiday Pouch Sales')
plt.xticks(rotation=80)
plt.bar(coffee_names, oct_2018_sales)
plt.bar(coffee_names, nov_2018_sales)
plt.bar(coffee_names, dec_2018_sales)
plt.tight_layout()
plt.legend(['October', 'November', 'December'])
plt.savefig('2018_monthly_sales.png')
plt.show()

oct_avg = np.mean(oct_2018_sales)
oct_median = np.median(oct_2018_sales)
print(oct_avg, oct_median)
nov_avg = np.mean(nov_2018_sales)
nov_median = np.median(nov_2018_sales)
print(nov_avg, nov_median)
dec_avg = np.mean(dec_2018_sales)
dec_median = np.median(dec_2018_sales)
print(dec_avg, dec_median)
ppp_avg = np.mean(ppp)
ppp_median = np.median(ppp)
print(ppp_avg, ppp_median)

total_holiday_sales = oct_2018_sales + nov_2018_sales + dec_2018_sales
holiday_avg = np.mean(total_holiday_sales)
holiday_median = np.median(total_holiday_sales)
print(holiday_avg, holiday_median)
