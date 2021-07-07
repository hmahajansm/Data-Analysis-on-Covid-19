#Code for creating network graph and correlation plots:
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("WTOdata.csv",encoding="latin-1")
top = ["United States of America","India","Brazil","Argentina","Colombia","Mexico"]
#,"Peru","South Africa","Italy","Iran","Chile","Germany","Iraq","Bangladesh","Indonesia","Phillippines"]
data = data[(data['Reporting Economy'].isin(top))&data(['Partner Economy'].isin(top))]
data = data.loc[(data['Year'] == 2018) & (data['Product/Sector Classification']/
                                          == 'HarmonizedSystem')]
data.to_csv("topTrade.csv")
colname = ['Reporting Economy','Partner Economy', 'Import Value','Friendliness']
out = pd.DataFrame(columns = colname)

for i in top:
    total = 0
    for j in top:
        trade = sum(data[(data['Partner Economy']==i) & (data['Reporting Economy']==j)]['Value'])
        trade = int(round(trade/1000000)) #final value in millions USD
        total = total + trade
        out = out.append({'Partner Economy':i,'Reporting Economy':j,'Import Value':trade,'Friendliness':trade}, ignore_index=True)
if total == 0:
    out['Friendliness'].loc[out['Partner Economy']==i] = 0
else:
    out['Friendliness'].loc[out['Partner Economy']==i] = out['Friendliness']/
    .loc[out['PartnerEconomy']==i]/total

out = out.loc[out['Import Value'] !=0]
out.to_csv("Network_Data.csv")
#out = pd.read_csv('Network_Data.csv')
out['Correlation'] = np.nan
growth = pd.read_csv('growth_rate_data.csv')
index = list(growth.drop_duplicates('location')['location'])

for i in index:
    for j in index:
        correlation = np.corrcoef(growth['Growth Rate']/
                                  .loc[growth['location']==i],growth['GrowthRate'].loc[growth['location']==j])
out['Correlation'].loc[(out['Reporting Economy']==i) & (out['Partner Economy']==j)] =
correlation[0,1]
plt.figure(figsize = (20,20))
G = nx.from_pandas_edgelist(out,source = 'Partner Economy',target = 'Reporting
Economy',edge_attr='Friendliness',create_using=nx.DiGraph())
pos = nx.circular_layout(G)
label_pos = {}
countries = list(pos.keys()) #create list of countries to offset label position

for k in countries:
    label_pos[k] = pos[k]*1.08 #node label offset8

nx.draw_networkx_labels(G,label_pos,font_size=25)
imports = nx.get_edge_attributes(G,'Friendliness').values()
cval = np.array(list(imports))
vmin = min(cval)
vmax = max(cval)
cmap = plt.cm.plasma
nx.draw_networkx_nodes(G,pos,node_size = 1000)
edges = nx.draw_networkx_edges(G,pos,width = 5,arrowsize = 15, connectionstyle ='arc3, rad=0.1',alpha = 1,edge_color = cval,edge_cmap = cmap,vmin=vmin,vmax=vmax)
plt.axis('off')
sm = plt.cm.ScalarMappable(cmap = cmap,norm = plt.Normalize(vmin = vmin,vmax = vmax)) #take exponential to map colorbar/
    # to real values
clb = plt.colorbar(sm)
clb.ax.tick_params(labelsize = 28)
clb.set_label('Friendliness Factor',size = 28)
out = out[(out['Friendliness']!=0) & (out['Partner Economy']!='Italy')]
out = out.sort_values('Friendliness',axis = 0,ascending = False,inplace = False)
out = out.drop_duplicates('Correlation')
out2 = out[(out['Reporting Economy']!='United States of America')& /
       (out['PartnerEconomy']!='United States of America')]
plt.show()
plt.figure()
x = out['Correlation']
y = out['Friendliness']
plt.ylabel('Friendliness')
plt.xlabel('Growth Rate Correlation')
plt.scatter(x,y)
plt.show()
plt.figure()
x2 = out2['Correlation']
y2 = out2['Friendliness']
m2,b2 = np.polyfit(x2,y2,1)
plt.scatter(x2,y2)
plt.ylabel('Friendliness')
plt.xlabel('Growth Rate Correlation')



#Code for calculating the moving average of Growth Rate:-

def growt_rate() :
        global y
        y_df=df.drop(['new_deaths','total_cases','total_deaths','weekly_cases','weekly_deaths'/
                         ,'biweekly_cases','biweekly_deaths'],axis =1 )
        #for i in date_array :
        for j in range(0,len(country_array)) :
            y=y_df.loc[df['date'].isin(date_array) & (df['location']==country_array[j]) ]
            new_cases= y['new_cases']
            new_case=new_cases.tolist()9
            a= len(new_case)
            print(type(new_case))
            growth=[]
            moving_average=[]
            for x in range(0,a) :
                if (new_case[x]!=0) and (new_case[x-1]!=0) :
                    gnumbers=round(new_case[x]/new_case[x-1],2)
                    growth.append(gnumbers)
                else:
                    gnumbers=0
                    growth.append(gnumbers)
                #for i in range(0,len(growth)):
            y['Growth']=growth
            sum=0
            for i in range(0,a):
                sum=sum+growth[i]
                moving_average.append(sum/(i+1))
            y['Moving_Average']=moving_average

            print(y)
            print(f'Growth List For Country {country_array[j]} ..')
            print(list(growth))
            print('\n')
            print(len(growth))
            print('\n')



#Code for calculating Error for each m value:-

new_case=df['new_cases_x'].tolist()
def calculate_m(m,n):
    sum=0
    for i in range(n-m,n):
        sum=sum+((new_case[i]-new_case[i-1])/new_case[i-1])
    return sum/m

    m=int(input())
    actual_cases=[]
    error=0
    growth=[]
    for n in range(m,m+11):
        growth_average=calculate_m(m,n)
        predict_cases=new_case[n]*(1 + growth_average)
        error=error+(new_case[n]*(1 + growth_average)-new_case[n+1])
    print(m)
    print(error)