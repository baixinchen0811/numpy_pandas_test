import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt

# s = pd.Series([1,2,3,np.nan,4,5])
# print(s)
# dates = pd.date_range('20130101',periods=6)
# print(dates)
# df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
# print(df)
# print(df)
# df.iloc[0,1] = np.nan
# df.iloc[1,2] = np.nan
# print(df)
# print(np.any(df.isnull())== True)
# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
# df3  = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
# print(df1)
# print(df2)
# res=pd.concat([df1,df2,df3],axis=0,ignore_index=)
# print(res)
# res = pd.concat([df1,df2],join='outer',ignore_index=True)
# res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])
# print(res)
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()
