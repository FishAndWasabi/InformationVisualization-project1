# Project1
## 1.  Summary
A new boxplot module named _'boxplots'_ is implemented based on numpy and matplotlib. The module concludes three versions of box plot, a mixed plot( the left half is a box plot, the right half is a horizontal histogram) and a creative box plot. The plots perform well in various kinds of data including real data set, of strong robustness. This report documents the different types of _boxplots_ and explains how to use the methods of the module, illustrating with plots generated.
## 2. Method guide
###  2.1  info_boxplot_v1
method: info_boxplot_v1(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray)

Make a simple box and whisker plot.

Make a box and whisker plot for each dataset in the data list. The box extends from the lower to upper quartile values of the data, with a line at the median. The whiskers extend from the box to show the range of the data. Outliers are those past the end of the whiskers.

Parameters:
| Parameter | Type | Description |
| - | - | - | 
| ax | matplotlib.axes | the axes object to hold the boxplot | 
| data | data: List[np.ndarray or List[int or float]] or np.ndarray |  a list of multiple series of numerical values | 

Returns:
&nbsp; &nbsp; matplotlib.axes
 &nbsp; &nbsp;&nbsp; &nbsp;  the axes object that contains the generated boxplot
  &nbsp; &nbsp;&nbsp; &nbsp;  The plot generated is almost the same as ax.boxplot(data). It shows maximum,  75th  percentile,  median  (50th  percentile),  25th percentile, minimum and outliers of each dataset. It can show whether a data set is symmetric (roughly the same on each side when cut down the middle) or skewed (lopsided).

__Example:__
```python
import matplotlib.pyplot as plt
import boxplots
data1=[200,200,300,400,500,400,300,400,500,450,780,350,260,160,500,600,-500,1000,-270]
data2=[150,500,400,700,500,800,900,180,670,450,-400]
data = [data1,data2]
fig,ax = plt.subplots()
boxplots.info_boxplot_v1(ax, data) 
```
The result is as follows:
![example1.png](https://i.loli.net/2020/11/10/laAEuVGsIQqoC3z.png)
###  2.2  info_boxplot_v2
method: info_boxplot_v2(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray, facecolor: str = 'white', outliercolor: str = 'steelblue', boxlinecolor: str = 'black', whiskercolor: str = 'black', outlierlinecolor: str = 'white', capcolor: str = 'black', medianlinecolor: str = 'orange')

Make a simple box and whisker plot with colors assignable.

Make a box and whisker plot for each data set in the data list. The box extends from the lower to upper quartile values of the data, with a line at the median. The whiskers extend from the box to show the range of the data. Outliers are those past the end of the whiskers. It allows users to specify the face color of the box and the outliers, the line color of the box, the whisker, the outliers, and the median.

Parameters:
| Parameter | Type | Default | Description |
| - | - | - | -|
| ax | matplotlib.axes | | the axes object to hold the boxplot | 
| data | List[np.ndarray or List[int or float]] or np.ndarray | | a list of multiple series of numerical values | 
| facecolor | str | 'white'| The color of the faces of boxes | 
| outliercolor | str | 'steelblue'| The color of points which represent outliers | 
| outlierlinecolor | str | 'white'| The color of the edges of points which represent outliers| 
| boxlinecolor | str | 'black'| The color of the edges of the boxes| 
| whiskercolor | str | 'black'| The color of whiskers (the vertical lines extending to the most extreme, non-outlier data points)| 
| capcolor | str | 'black'|  The color of caps (horizontal lines at the ends of the whiskers)| 
| medianlinecolor | str | 'orange'|  The color of the median lines in the boxes.| 
Returns:
&nbsp; &nbsp; matplotlib.axes
 &nbsp; &nbsp;&nbsp; &nbsp;  the axes object that contains the generated boxplot
  &nbsp; &nbsp;&nbsp; &nbsp;  The plot shows maximum,  75th  percentile,  median  (50th  percentile), 25th percentile, minimum and outliers of each data set. It can show whether a data set is symmetric (roughly the same on each side when cut down the middle) or skewed (lopsided). The face color of the box and the outliers, the line color of the box, the whisker, the outliers, the caps, and the median are able to be specified by users by assigning the parameters.

Example:
```python
import matplotlib.pyplot as plt
import boxplots
data1=[200,200,300,400,500,400,300,400,500,450,780,350,260,160,500,600,-500,1000,-270]
data2=[150,500,400,700,500,800,900,180,670,450,-400]
data = [data1,data2]
fig,ax = plt.subplots()
boxplots.info_boxplot_v2(ax,data,
                   facecolor='#EDFDFC',
                   outliercolor='#DAFBF9',
                   boxlinecolor='#042524',
                   whiskercolor='#021211',
                   outlierlinecolor='#021211',
                   capcolor='#0B090A',
                   medianlinecolor='#084945')
```
The result is as follows:
![v2.png](https://i.loli.net/2020/11/10/s6YOjHCzBISPrhn.png)

###  2.3  info_boxplot_v3
info_boxplot_v3(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray, facecolor: str = 'white', outliercolor: str = 'steelblue', boxlinecolor: str = 'black', whiskercolor: str = 'black', outlierlinecolor: str = 'white', capcolor: str = 'black', medianlinecolor: str = 'orange', multiplebox: bool = True) 

Make a box and whisker plot with colors assignable, and is able to show every 5%-percentile from the 1st quartile (Q1) until the 3rd quartile (Q3).

Make a box and whisker plot for each data set in the data list. The box extends from the lower to upper quartile values of the data, with a line at the median. The whiskers extend from the box to show the range of the data. Outliers are those past the end of the whiskers. It allows users to specify the face color of the box and the outliers, the line color of the box, the whisker, the caps, the outliers, and the median.  It can also show every 5%-percentile from the 1st quartile (Q1) until the 3rd quartile (Q3).

Parameters:
| Parameter | Type | Default | Description |
| - | - | - | -|
| ax | matplotlib.axes | | the axes object to hold the boxplot | 
| data | List[np.ndarray or List[int or float]] or np.ndarray | | a list of multiple series of numerical values | 
| facecolor | str | 'white'| The color of the faces of boxes | 
| outliercolor | str | 'steelblue'| The color of points which represent outliers | 
| outlierlinecolor | str | 'white'| The color of the edges of points which represent outliers| 
| boxlinecolor | str | 'black'| The color of the edges of the boxes| 
| whiskercolor | str | 'black'| The color of whiskers (the vertical lines extending to the most extreme, non-outlier data points)| 
| capcolor | str | 'black'|  The color of caps (horizontal lines at the ends of the whiskers)| 
| medianlinecolor | str | 'orange'|  The color of the median lines in the boxes| 
| multiplebox | bool | True|  If true, lines which represent every 5%-percentile from the 1st quartile (Q1) until the 3rd quartile (Q3) will be drawn.| 
Returns:
&nbsp; &nbsp; matplotlib.axes
 &nbsp; &nbsp;&nbsp; &nbsp;  the axes object that contains the generated boxplot
  &nbsp; &nbsp;&nbsp; &nbsp;  The plot shows maximum,  75th  percentile,  median  (50th  percentile), 25th percentile, minimum and outliers of each data set. It can show whether a data set is symmetric (roughly the same on each side when cut down the middle) or skewed (lopsided). The face color of the box and the outliers, the line color of the box, the whisker, the outliers, the caps, and the median are able to be specified by users by assigning the parameters. Lines which represent every 5%-percentile from the 1st quartile (Q1) until the 3rd quartile (Q3) can be drawn if the value of parameter _multiplebox_ is True.

Example:
```python
import matplotlib.pyplot as plt
import boxplots
data1=[200,200,300,400,500,400,300,400,500,450,780,350,260,160,500,600,-500,1000,-270]
data2=[150,500,400,700,500,800,900,180,670,450,-400]
data = [data1,data2]
fig,ax = plt.subplots()
boxplots.info_boxplot_v3(ax,data,
                   facecolor='#EDFDFC',
                   outliercolor='#DAFBF9',
                   boxlinecolor='#042524',
                   whiskercolor='#021211',
                   outlierlinecolor='#021211',
                   capcolor='#0B090A',
                   medianlinecolor='#084945',
                   multiplebox=True)
```
The result is as follows:
![v3.png](https://i.loli.net/2020/11/10/H5A3GQdVLsRTD2g.png)
###  2.4  histobox_plot
histobox_plot(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray,
                  bins: int = 10)
                  
Make a plot which is a mix between a box plot and a histogram.

Make a mixed plot for each data set in the data list. The left half is a traditional box plot, while there is a histogram reflecting the distribution on the right half. 

Parameters:
| Parameter | Type | Default | Description |
| - | - | - | -|
| ax | matplotlib.axes | | the axes object to hold the boxplot | 
| data | List[np.ndarray or List[int or float]] or np.ndarray | | a list of multiple series of numerical values | 
| bins | int | 10 | the number of bins of the histogram | 

Returns:
&nbsp; &nbsp; matplotlib.axes
 &nbsp; &nbsp;&nbsp; &nbsp;  the axes object that contains the generated plot
  &nbsp; &nbsp;&nbsp; &nbsp;  For each data set, there is a half of  box plot on the left half, which shows maximum,  75th  percentile,  median  (50th  percentile), 25th percentile, minimum and outliers. The horizontal frequency histogram lies on the right half with the number of bins assigned by the parameter _bins_.

Example:
```python
import matplotlib.pyplot as plt
import boxplots
data1=[200,200,300,400,500,400,300,400,500,450,780,350,260,160,500,600,-500,1000,-270]
data2=[150,500,400,700,500,800,900,180,670,450,-400]
data = [data1,data2]
fig,ax = plt.subplots()
boxplots.histobox_plot(ax,data, bins=10)
```
The result is as follows:
![histo.png](https://i.loli.net/2020/11/10/QFB58yjoJ197xUz.png)
###  2.5  creative_boxplot
creative_boxplot(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray, bins: int = 10,whis: float = 1.5, labelset: list or bool = False, showcaps: bool = True, showfliers: bool = True,showmeans: bool = True, showtrend: bool = True, variawidth: bool = True,curfacecolor: str = 'white', curlinecolor: str = 'black', curalpha: int = 1,outlierlinecolor: str = 'white', outliercolor: str = 'steelblue', outlierlinewidth: int = 1,capcolor: str = 'black', capwidth: int or float = 1,whiskercolor: str = 'black', whiskerwidth: int or float = 1, boxfacecolor: str = 'white', boxedgecolor: str = 'black', boxedgewidth: int or float = 1,mediancolor: str = 'orange', medianwidth: int or float = 1, medianlinestyle: str = '-',meancolor: str = 'green', meanwidth: int or float = 1, meanlinestyle: str = '--',trendcolor: str = 'blue', trendwidth: int or float = 1.5, trendlinestyle: str = ':',rotation: int or float = 0) 


Make a creative mixed plot with various properties assignable, such as color, width and line style. The box plot is on the left half and the frequency area is on the right side.

Make a box and whisker plot for each data set in the data list. The box extends from the lower to upper quartile values of the data, with a line at the median. The whiskers extend from the box to show the range of the data. Outliers are those past the end of the whiskers. It allows users to specify the face color of the box and the outliers, the line color of the box, the whisker, the caps, the outliers, and the median. It also allows users to specify whether to show the caps, outliers, means, and the line among boxes. Users can also set the labels of datasets. There are other properties such as line width and line style that are able to be specified. Besides, users can set the widths of the boxs changeable to make it reflect the size of the samples when comparing grouped data. When used for time series data, dotted line between the boxes can be specified to show the variation trends of the median among the samples.

Parameters:
| Parameter | Type | Default | Description |
| - | - | - | -|
| ax | matplotlib.axes | | the axes object to hold the boxplot | 
| data | List[np.ndarray or List[int or float]] or np.ndarray | | a list of multiple series of numerical values | 
| bins | int | 10 | the number of intervals of the frequency histogram | 
| whis | float | 1.5 | The position of the whiskers | 
| labelset | list | [1,2,3,4,...] |  Labels for each dataset (one per dataset)| 
| showcaps | bool | True |  If True, show the caps on the ends of whiskers | 
| showfliers | bool | True |  If True, show the outliers beyond the caps. | 
| showmeans | bool | True |  If True, show the arithmetic means.| 
| showtrend | bool | True |  If True, show the broken line among medians of datasets| 
| variawidth | bool | True |  If True, change the widths of boxes according to the sizes of datasets| 
| capcolor | color | 'black'|  The color of caps (horizontal lines at the ends of the whiskers)| 
| capwidth | float or int | 1|  The width of caps (horizontal lines at the ends of the whiskers)| 
| whiskercolor | color | 'black'| The color of whiskers (the vertical lines extending to the most extreme, non-outlier data points)| 
| whiskerwidth | float or int | 1| The width of whiskers (the vertical lines extending to the most extreme, non-outlier data points)| 
| boxfacecolor | color | 'white'|  The color of the faces of the boxes| 
| boxedgecolor | color | 'black'|  The color of the edges of the boxes| 
| boxedgewidth | float or int | 1| The width of the edges of the boxes| 
| mediancolor | color | 'orange'|  The color of the median lines in the boxes | 
| medianwidth | float or int | 1| The width of the median lines in the boxes| 
| medianlinestyle | str | '--'|  The line style of the median lines in the boxes| 
| meancolor | color | 'green'|  The color of the mean lines in the boxes | 
| meanwidth | float or int | 1|  The width of the mean lines in the boxes| 
| meanlinestyle | str | '--'|  The line style of the mean lines in the boxes| 
| trendcolor | color | 'blue'|  The color of the line connecting the medians of the boxes| 
| trendwidth | float or int | 1.5| The width of the line connecting the medians of the boxes| 
| trendlinestyle | str | ':'|  The line style of the mean lines in the boxes| 
| curlinecolor | color | 'white'|  The color of edges of the curves|
| curfacecolor | color | 'black'|  The color of edges of the curves|  
| curalpha | int | 1|  The transparency of faces of the curves|  
| outliercolor | color | 'white'| The color of the faces of points represent the outliers| 
| outlierlinecolor | color | 'black'| The color of the edges of points which represent outliers| 
| outlierlinewidth | float or int | 1| The width of the edges of points represent the outliers| 
| rotation | sfloat or {'vertical', 'horizontal'} | 1| The rotation angle in degrees in mathematically positive direction (counterclockwise). 'horizontal' equals 0, 'vertical' equals 90| 
Returns:
&nbsp; &nbsp; matplotlib.axes
 &nbsp; &nbsp;&nbsp; &nbsp;  the axes object that contains the generated boxplot
  &nbsp; &nbsp;&nbsp; &nbsp;  The left half of the plot is a box plot showing the distribution based on quartiles. The right side is a frequency area showing the distribution of the data based on the frequency and its probability density .

Example:
```python
import matplotlib.pyplot as plt
import boxplots
data1=[200,200,300,400,500,400,300,400,500,450,780,350,260,160,500,600,-500,1000,-270]
data2=[150,500,400,700,500,800,900,180,670,450,-400]
data = [data1,data2]
fig,ax = plt.subplots()
boxplots.creative_boxplot(ax,data,labelset=["testdata1","testdata2"],
                       whiskercolor='#021211',
                       capcolor='#0B090A',
                       outliercolor='#DAFBF9',
                       outlierlinecolor='#021211',
                       boxfacecolor = '#EDFDFC',
                       curfacecolor = '#F4F9F0',
                       trendcolor='#084945',
                       mediancolor = 'black',
                       rotation=45)
```
The result is as follows:
![result.png](https://i.loli.net/2020/11/10/GcOvE1D3mPSyBIT.png)
## 3. Design Principle
### 3.1 Avoid chart junk and Non-Data-Ink
The main purpose of the plot is to display the information, so the plot shall be simple and readable. To avoid chart junk, we remove the unnecessary visual elements and grid lines. Unnecessary borders and shadow effects are also ignored. We avoid adding useless decoration which distracts the viewer from the information. The labels are carefully labeled and two‐dimensional designs are used.
### 3.2 Proportion and sizes
The representation of numbers, as physically measured on the surface of the graph itself, is directly proportional to the numerical quantities represented. For instance, the proportions of the bar lengths in the method  histobox_plot() and creative_boxplot()  depend on the proportions of the data in different intervals. We calculate in different sizes of figures and various data, concluding that:
$$ 
Lie factor =\frac{\text{Size of the effect shown in the graph}}{\text{Size of the effect shown in the data}} ≈1
$$
### 3.3 Colorblind-friendly
We mainly use black and grey as default colors ,avoid using red and green together in order to make the plot readable for color blindness. We have tested our image with color blindness simulation tools.
### 3.4 Show comparison and variation
Accoding to  _Tufte’s_  _Principles_,  comparisons between different sets shall be taken into consideration and variation (especially for time series data) shall be showed. Our module shows the distribution of different datasets by drawing them in the same coordinate. for time series data,  a polyline connecting the median of different sets shows the overall trend, which is available in the creative_boxplot() method by setting the parameter _showtrend_ as _True_.
### 3.5 Coding principles
We add the input checking and error message in the module to make it available for users to check what goes wrong when problems occur. We add comments in the code for developers to read and modify. 

## 4. Developing Process
This section records how we implement the methods and the process to solve the problems we meet. For the reason that the creative_boxplot() method involves most functions of the previous methods, we just discuss it as an example. 
### 4.1 Design the style
The first step is to design the style of the plot. Considering the data presentation, we plan to draw the traditional box plot on the left half, displaying the distribution of data based on quartiles and the outliers. On the right half, there is a frequency-curve showing the frequency distribution of the data. The mean of data sets can be optional chosen to draw in the boxes. A polyline connecting the median of different sets is chosen to show the trend of variation, which can be useful for time series data, such as a data set collected in a day is represent in a box and there are data sets for continuous days. The widths of the boxes can be chosen to be changeable, and the width can reflect the size of the various data sets. 
### 4.2 Draw the box and quartiles
Then we start implementing the design. We set 1,2,3,4,... as x-labels if the user do not state real labels. Then we start drawing vertical and horizontal  lines to make up the box. Q1 (25% quartile), Q2 (50% quartile), Q3 (75% quartile) and the oulier bounds are calculated using numpy. After calculating to define the position of the horizontal lines, we decide the default width of the boxes as 0.25 for the reason that each gap between x labels is 1. If the width is specified to be changeable, it is scaled and then modified according to the proportion of data sets' sizes. 
![sub1.png](https://i.loli.net/2020/11/10/r7x534AheRNJ8Og.png)
### 4.3 Draw the outliers
We calculate the range of outliers which are above Q3+1.5IQR or below Q1-1.5IQR (1.5 can be changed by users by setting the value of parameter _whis_ in creative_boxplot() method). then we
get the outliers and remove them from the box. For the purpose of drawing the outliers, we use the _matplotlib.patches.Circle()_. Then we met a serious problem that the radius of the circles is based on the value of data instead of the plot. Therefore, in most cases, the circles are displayed as ellipses rather than circles. We tried many ways such as limiting the gap between labels of x to be the same as y, or getting the gap between y ticks and set a proportion as the radius. Finally, we found the solution by setting the 'transform' parameter. The main thought is to draw circles at (0,0) with a fixed radius and then move it to where outliers locate. This works perfectly. The only thing to notice is that the ranges of x and y have be artificially specified for they can not automatically modified to fit the outliers.
![sub2.png](https://i.loli.net/2020/11/10/4y6eF1Bo5a9EKDu.png)
### 4.4 Draw the frequency area
In order to realize the  frequency-curve and fill the area, we first draw the boxplot, which is shown in histobox_plot() method. The bins with default value as 10 can be stated by users. Then we match the middle point of each bar's right bound. The result is like this one:
![sub3.png](https://i.loli.net/2020/11/10/RmHysF7IcuVbCqK.png)

Then using make_interp_spline() to generate more points to make the line smooth:
![sub5.png](https://i.loli.net/2020/11/10/pIVXR8g2oLDysNW.png)
We can find that some parts of the line go across the vertical line, which is not reasonable. Therefore, we transform these parts to be on the line:
![sub4.png](https://i.loli.net/2020/11/10/rVmtqWUG7BX6CP9.png)
The last thing is to remove the histogram and fill the area with a color:
![result.png](https://i.loli.net/2020/11/10/rpg2nsOoGmEviuZ.png)
### 4.5 Add parameters
After that, we add parameters to the method, allowing users to control the style. For example, users are able to adjust the rotations of x-labels for better visual effects. Then we use various data sets to test the method. It shows great adaptation to various types and sizes of data. We also used a real data set [Android open source dataset](https://github.com/luiscruz/android_test_inspector/blob/master/results_merged.csv) to test the method. The result and explanation are recorded in the jupyter notebook.

