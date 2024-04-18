import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.DataFrame({'col1': (1, 2), 'col2': (3, 4)})
df2 = pd.Series((10, 100), index=['col3', 'col4'])
df3 = pd.DataFrame(((1000, 2000, 3000, 4000),
                    (5000, 6000, 7000, 8000),
                    (9000, 10000, 11000, 12000),
                    (13000, 14000, 15000, 16000)), columns=['col5', 'col6', 'col7', 'col8'],
                   index=['row1', 'row2', 'row3', 'row4'])
# print(df1, df2, df3, sep='\n\n')
# print(df1.columns)
# print(df3.index)

table_props = {
    'bbox': [0.1, 0.1, 0.8, 0.8]
}

plt.table(cellText=df3.values, rowLabels=df3.index, colLabels=df3.columns, loc='center',
          bbox=table_props['bbox'], rowLoc='center', colLoc='center', cellLoc='center',
          colColours=['lightblue', 'lightgreen', 'lightblue', 'lightgreen'], colWidths=[0.2, 0.2, 0.2, 0.2])
# plt.savefig(r'C:\Users\user\Desktop\stick_finger.png')
plt.show()
# data1 = df3['col5'].to_numpy()
# data2 = df3['col5'].to_numpy().reshape(-1, 1)
# print(data1, data2, sep='\n\n')
