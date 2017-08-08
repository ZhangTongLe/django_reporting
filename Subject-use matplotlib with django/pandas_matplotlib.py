from pandas import Series,DataFrame
import matplotlib.pyplot as plt
d={'1.htldxhzj.duapp.com': 9398,
 'gtxapi.cdn.duapp.com': 79496,
 'www.xxx.com': 2477070,
 'www.baidu.com': 1465,
 'www.bing.com': 777,
 'www.aaa.com': 1113101,
 'www.ccc.net.cn': 922,
 'www.zhanimei.ga': 29847,
 'www.zhanimei.ml': 40155,
 'www.zhasini.ml': 373436}
plt.figure(figsize=(8,6), dpi=80)
ts = Series(d)
ts.plot(kind='barh')
plt.savefig('./static/images/log.png')