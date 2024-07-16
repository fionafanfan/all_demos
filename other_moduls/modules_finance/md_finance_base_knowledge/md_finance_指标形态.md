# 形态指标 （起指导意义：购买信号 or 售出信号； 说到底是一种趋势追踪的工具）
参考资料
* talib（51cto博客，均线指标实现教程）： https://blog.51cto.com/u_16213338/7272531
* 半小时股票漫画： https://read.douban.com/reader/ebook/139832326/?from=book

1. ma： ma多头排列、ma空头排列
2. ema
3. macd
4. boll
5. sar
6. kdj
7. mavol
8. rsi
9. arbr
10. bias
11. psy
12. cci
13. dmi
14. dma
15. vr
16. wmsr
17. nine_turn_sequence

专业词：
1. 平仓
2. 加仓 
3. 做空 
4. 反向做空

talib所有指标：https://codeleading.com/article/49013187313/
ma均线：http://www.360doc.com/content/12/0121/07/15913066_1081938559.shtml(利用talib和matplot绘图)
1. ma（等同sma）移动平均线：
2. sma最简单移动平均线: https://baike.baidu.com/item/SMA%E5%9D%87%E7%BA%BF/7238642?fr=ge_ala (ma是统称，sma就是最基础的简单ma)
3. wma加权移动平均线（加权方式：末日、线性、梯形、平方系数）: 
4. ema（expma, exp原单词exponential指数的意思，代表增长得越来越快的意思）指数移动平均线（也可以看作时WMA的一种特殊形式，以指数形式进行加权）：
5. dema(DEMA = EMA1 + ( EMA1 - EMA2 )): DEMA其实就是普通的指数移动平均线EMA1加上EMA1 与EMA2的差值，和之前介绍的赫尔均线计算方法类似: https://baijiahao.baidu.com/s?id=1778083107684819027&wfr=spider&for=pc
DEMA的优势在于，通过计算两个指数移动平均线的差值，能够更敏锐地捕捉到价格的快速波动和趋势转折点，减少了指标的滞后性，同时能保持较好的平滑性https://baijiahao.baidu.com/s?id=1778083107684819027&wfr=spider&for=pc （带公式说明，易懂）
6. tema（等同T3）三指数移动平均线：https://baijiahao.baidu.com/s?id=1778083107684819027&wfr=spider&for=pc （带公式说明，易懂）
7. trima三角异动平均线(): https://www.cnblogs.com/wintalau/p/11616277.html
8. kama考夫曼自适应均线: https://baijiahao.baidu.com/s?id=1772380549617827193&wfr=spider&for=pc
9. mama（也同AMA，MAMA自适应移动平均线，MESA Adaptive）:

SAR:
1. sar: 又叫抛物线指标或停损转向操作点指标，其全称叫“Stop and Reverse，缩写SAR”; 
属于价格与时间并重的分析工具;由于组成SAR的点以弧形的方式移动，故称“抛物转向”。
https://baike.baidu.com/item/SAR%E6%8C%87%E6%A0%87/6329095?fr=aladdin
(https://baike.baidu.com/item/SAR%E6%8C%87%E6%A0%87/6329095?fr=aladdin)

KDJ：
1. kdj： KDJ中文名又叫随机指标，英文名叫Stochastic oscillator，由乔治·莱恩（George Lane）于20世纪50年代首创，最早用于期货市场。
它主要是利用价格波动的真实波幅来反映价格走势的强弱和超买超卖现象，在价格尚未上升或下降之前发出买卖信号
（https://zhuanlan.zhihu.com/p/523967712）


形态理解：
1. 五线顺上: close > MA5 > MA10> MA20 > MA60> MA60
2. 一阳穿三线（阳线，收盘价>开盘价）：open < MA5、MA10、MA30 < close
3. 三金叉: MACD金叉P1死叉S1、kdj金叉P2死叉S2、MA金叉P1死叉S3  满足条件: P1> (S1、 S2 、S3) & P2> (S1、 S2 、S3) & P3> (S1、 S2 、S3) 
4. w底： https://zhuanlan.zhihu.com/p/558793135
5. 上升九转： closeX> (closeX-X4), close价格大于前4个中的任意一个，就开始从1开始计数，如果后面9个都满足要求，就完成上升九转，否则重新就开始计数。
是卖出信号，任务都完成了上升九转，后面可能就会降下来了。

# 百度百科了解 股票形态指标
1. ma：https://baike.baidu.com/item/MACD%E6%8C%87%E6%A0%87/6271283?fr=ge_ala#1
移动平均线能够反应出价格趋势走向，所谓移动平均线，就是把某段时间的股价加以平均，再依据这个平均值作出平均线图像