# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Tue Jul  3 14:18:29 2018)---
pwd
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
runfile('C:/Users/Administrator/.spyder-py3/read_txt.py', wdir='C:/Users/Administrator/.spyder-py3')
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
s1  = Series(range(4),list('dabc'))
s1
s1.sort_index()
d1 = DataFrame(range(12).reshape(3,4),index=list('abc'),columns=list('one','two','three','four'))
d1 = DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('one','two','three','four'))
d1 = DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list(('one','two','three','four')))
d1.sort_index()
d1.columns=['o','t','th','f']
d1
d1.sort_index()
d1.sort_index(axis=1)

## ---(Wed Jul  4 10:52:36 2018)---
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
s1=Series(np.arange(3))
s1[-1]
s1[3]
s1.get_value(2)
s1.iget_value(2)
s1.get_value(0)
s1.at[2]
d1 = DataFrame(s1,index=[list('abc')])
d1
d1 = DataFrame(s1,names=[list('abc')])
d1 = DataFrame(s1,columns=[list('abc')])
d1
s1
d1 = DataFrame(s1)
d1
d1 = DataFrame(s1,columns=[list('abc')])
d1[['b','c']]=np.nan
d1['B']=np.nan
d1.columns = list('ABC')
d1['c'] = None
d1
d2=DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=['xx','yy','xy','xd'])
d1.clear()
d2['a]=[0,0,1,1]
d2['a']=[0,0,1,1]
d2['a']
d2[:,'a']
d2.ix['a']
d2.loc['a']
d2.iloc(2)
d2.iloc(1)
list(d2.iloc(1))
d2.loc('a')
d2.loc('a',axis=0)
d2.loc('xx',axis=0)
d2.loc('xx')
?d2.loc()
d2['a':'c']
d2['a']
d2[['a','b']]
d2[2]
d2.columns=[2,'x','y','d']
d2[2]
d2[:,2]
d2[:2]
d2[:2,2]
d2[2,'a']
d2[2]['a']
d2['x']['a']
d2.loc
d2.loc()
?d2.loc()
 de2
d2
?d2.stack()
d2.stack()
d2.sort()
d2s = d2.stack(
)
d2s.sort()
d2s.order()
? d2s.sort_index()
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
?pd.MultiIndex
?pd.MultiIndex.from_arrays
 ?d2s.sort_index
d2s.sort_index()
d2s.sort_index(level=1)
 d2s.loc['a'].sort_index()
 d2sa = d2s.loc['a']
d2sa.sort_index()
d2sa.sort_values()
d2s.rank()
d2.sort_index(by=y,ascending=False)
d2.sort_index(by='y',ascending=False)
?d2s .dropna(

## ---(Wed Jul  4 15:40:35 2018)---
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
pd.read_excel('D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/在售商品数据统计表（20180702）.xlsx',index_col=0)
onsells = pd.read_excel('D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/在售商品数据统计表（20180702）.xlsx',index_col=0)
filt_onsells = onsells.dropna()
onsells.dropna()
onsells.dropna(axis=1)
onsells.dropna(axis=0)
onsells.dropna(axis=1).dropna(axis=0)

## ---(Wed Jul  4 15:51:35 2018)---
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
junesells= pd.read_excel('D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/销售数据-（20180601-20180630） - 副本.csv',index_col=0)
ord('F')-97
ord('F')-65
ord('L')-65
junesells= pd.read_excel('D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/销售数据-（20180601-20180630） - 副本.csv',index_col=0,usecols=[0,1,4,7,11])
junesells= pd.read_csv('D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/销售数据-（20180601-20180630） - 副本.csv',index_col=0,usecols=[0,1,4,7,11])
pd.read_csv('D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/销售数据20180601-20180630.csv')
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
print(pwd)
file = ''D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/销售数据20180601-20180630.csv'
file = 'D:/Documents/Tencent Files/3365737608/FileRecv/近50天销售数据统计和FBA库存情况/销售数据20180601-20180630.csv'
pwd
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
os.path.dirname(trainFile)
os.path.basename(trainFile)
pwd

## ---(Wed Jul  4 16:14:51 2018)---
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
june_sells=pd.read_csv(trainFile,index_col=0,usecols=[0,1,4,7,11],engine='python')
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
june_sells.describe()
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
june_sells[['Title','Page Views']]
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
x = '$23,037.42'
to_num(x)
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
to_num(x)
product_sells = june_sells['Ordered Product Sales'].applymap(to_num)
product_sells = june_sells['Ordered Product Sales'].map(to_num)
june_sells['Ordered Product Sales']=product_sells
june_sells.describe()
june_sells['Page Views'].sum()
june_sells['Page Views'].max()/june_sells['Page Views'].sum()
june_sells['Units Ordered'].idxmax()
june_sells.sum()
trans_rate = (june_sells['Units Ordered']/june_sells['Page Views']).sort
trans_rate = (june_sells['Units Ordered']/june_sells['Page Views']).sort_values()
trans_rate = (june_sells['Units Ordered']/june_sells['Page Views']).sort_values(ascending=False)
filtered_tr = trans_rate[[june_sells['Units Ordered']>5]]
filtered_tr = trans_rate[june_sells['Units Ordered']>5]
filtered_=june_sells['Units Ordered'] >5
filtered_sells = june_sells[filtered_]
tr = (filtered_sells['Units Ordered']/filtered_sells['Page Views']).sort_values()
tr.head()
tr = (filtered_sells['Units Ordered']/filtered_sells['Page Views']).sort_values(ascending=False)
tr.head()
len(tr[tr >0.1])
product_sells.describe()
june_sells.describe()
june_sells['Ordered Product Sales'].idxmax()
june_sells['Page Views'].idxmax()
june_sells['Units Ordered'].idxmax()
june_sells.loc['B01N2TD63']
june_sells.loc['B01N2TD63I']
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
x='$23,037.42'
to_num(x)
?pd.read_csv()

## ---(Mon Jul  9 17:20:17 2018)---
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')
?pd.read_csv()
runfile('C:/Users/Administrator/.spyder-py3/imort.py', wdir='C:/Users/Administrator/.spyder-py3')

## ---(Tue Jul 10 09:35:14 2018)---
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
_
_=ax2.plot(np.random.randn(20))
_
ax3.plot(np.linspace(20,30))
fig
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
fig
axe
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
plt.xlim()
f = plt.plot(s1)
f.set_xticks([0,10,20])
f 
f[0].set_xticks([0,10,20])
type(axe[0])
type(axe)
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
plt.xlim()
plt.xticks()
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
plt.xticks()
?plt.scatter(
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
~matplotlib.markers
import matplotlib
~matplotlib.markers
matplotlib.markers
matplotlib.markers.__doc__
?matplotlib.markers
?matplotlib.colors.Colormap
?plt.hist
?plt.plot
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
axe
?plt.plot
 %colors
axe[0,0].plot(s1,s2,linestyle=':',color='g',marker='^')
axe[0,0].plot(s1,s2[10],linestyle=':',color='g',marker='^')
axe[0,0].plot(s1[:10],s2,linestyle=':',color='g',marker='^')
axe
plot(range(10))
plt.plot(range(10))
runfile('C:/Users/Administrator/.spyder-py3/template.py', wdir='C:/Users/Administrator/.spyder-py3')
plot(range(10))