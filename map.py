#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.base import DataError
from pandas.core.frame import DataFrame

# file paths
weather_path = 'data/sunshine_total_backup.csv'
df = pd.read_csv(weather_path, parse_dates=["time_date"])
df.sort_values(by='time_date', ascending=False, inplace=True)

# %%
# numbers
condition = df.apply(lambda x: True if x['sun_hourly'] >= 0 else False, axis=1)
count_hourly = len(condition[condition == True].index)
condition = df.apply(lambda x: True if x['sun_daily'] >= 0 else False, axis=1)
count_daily = len(condition[condition == True].index)
condition = df.apply(lambda x: True if x['condition_code'] >= 0 else False, axis=1)
count_coco = len(condition[condition == True].index)
print('Datasets containing hourly sunshine: ', count_hourly)
print('Datasets containing daily sunshine: ', count_daily)
print('Datasets containing condition codes: ', count_coco)

coco = df.groupby('condition_code').count()
coco.rename(columns={'city' : 'count'}, inplace=True)
print(coco['count'])

#%%
# hourly_suntime
plt.figure(figsize=(16,9))
plt.plot(df.time_date, df.sun_hourly, '.r-')
plt.title('Sonnenminuten pro Stunde je Sichtung')
plt.ylabel('Sonnenminuten/Stunde')
plt.xlabel('Datum')
plt.savefig('img/hourly_suntime.png', dpi=(1920/16))
plt.show()

#%%
# daily_suntime
plt.figure(figsize=(16,9))
plt.plot(df.time_date, df.sun_daily, 'b.-')
plt.title('Sonnenminuten pro Tag je Sichtung')
plt.ylabel('Sonnenminuten/Tag')
plt.xlabel('Datum')
plt.savefig('img/daily_suntime.png', dpi=(1920/16))
plt.show()

#%%
# condition_codes
plt.figure(figsize=(16,9))
plt.plot(df.time_date, df.condition_code, 'g.-')
plt.title('Condition Code je Sichtung')
plt.ylabel('Conditioncode')
plt.xlabel('Datum')
plt.savefig('img/condition_codes.png', dpi=(1920/16))
plt.show()

#%%
# histogram
bins = range(28)
plt.figure(figsize=(16,9))
plt.hist(df.condition_code, bins=np.arange(29)-0.5, edgecolor='black')
plt.xticks(bins)
plt.title('Absolute Anzahl Condition Codes')
plt.savefig('img/condition_codes_hist.png', dpi=(1920/16))
plt.show()

# %%
# pie chart
coco = df.groupby('condition_code').count()
coco.rename(columns={'city' : 'count'}, inplace=True)
labels = coco['count']
font = {'size' : '18'}

# Beschriftung relativer Verteilung
def autopct_more_than_1(pct):
    return ('%1.f%%' % pct) if pct > 1 else ''

plt.figure(figsize=(16,9))
plt.pie(labels, labels=labels, autopct=autopct_more_than_1, pctdistance=0.8, startangle=90)
plt.legend(labels.index.tolist(), title='Legende', bbox_to_anchor=(1,1))
plt.title('Verteilung der Condition Codes', fontdict=font)
plt.axis('equal')
plt.savefig('img/condition_codes_pie.png', dpi=(1920/16))
plt.show()

#%%
# boxplots
# hourly_sun
box_hourly = df.boxplot(column='sun_hourly')
plt.title('Boxplot Sonnenminuten in Stunde der Sichtung')
box_hourly.get_figure().savefig('img/hourly_suntime_boxplot.png', dpi=(1920/16))

# daily_sun
box_daily = df.boxplot(column='sun_daily')
plt.title('Boxplot Sonnenminuten am Tag der Sichtung')
box_daily.get_figure().savefig('img/daily_suntime_boxplot.png', dpi=(1920/16))