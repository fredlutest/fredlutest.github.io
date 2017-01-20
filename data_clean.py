
# coding: utf-8

import pandas as pd
df2 = pd.read_excel('gtd_12to15_0616dist.xlsx', encoding='utf8')
df1 = pd.read_excel('gtd_92to11_0616dist.xlsx', encoding='utf8')
df =pd.concat([df1,df2])


ratio_kill = 0.6
ratio_wound = 1.0 - ratio_kill

df["level"] = df.nkill*ratio_kill + df.nwound*ratio_wound
mask = df.level > 20


df['year_m'] = df.apply(lambda x : x['iyear']+x['imonth']/12,axis=1)
df_new = df[mask]


filter_data = ["eventid",'year_m',"iyear","imonth","iday","region","country_txt","city","latitude","longitude","attacktype1","nkill","nwound","level"]
df_filter = df_new[filter_data]


df_filter.to_csv('dv_data.csv', encoding='utf8', index=True,index_label="case")
