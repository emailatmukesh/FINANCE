import glob
import pandas as pd
import matplotlib.pyplot as plt
# get data file names
#st1=input('enter the strike with PE OR CE:--')
#st2=input('enter the strike with PE OR CE:--')
PATH =r'C:\Users\mukesh\Downloads\Compressed\Expiry 01st October\CSV 14-09-20 to 01-10-20 (Expiry Day)'
filenames = glob.glob(PATH + "/*.csv")

#file2 = glob.glob(PATH + "/*20002")#
#rint(filenames)


collect=pd.DataFrame()

#st=input('enter a strike with pe/ce')
p = list(map(str, input("Enter a multiple value with ce/pe: ").split()))



d={}

for filename in filenames:
      x=filename.split('BANKNIFTYWK')[-1]
      y=x.split('.')[0]
      for i in range(len(p)):
          if y==p[i]:
              df = pd.read_csv(filename)
              
              col=[y,'date','time','open','high','low','close','lot1','lot2']
              df.columns=col
              df['time-date']=pd.to_datetime(df['date'] + ' ' + df['time'])
              plt.xticks(fontsize=8, rotation=65)
              plt.plot(df['time-date'],df['close'],label=y)
              
     
plt.legend(loc='upper left', frameon=False, prop={'size': 10})

plt.rcParams["figure.figsize"] = (20,7)
plt.grid()
plt.show()
             

plt.savefig("sample1.jpg")

