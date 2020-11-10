#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module provides 5 methods to plot boxplot
------------------------------------------------------------------------------------------------------------------------
Overview
1. info_boxplot_v1
This is the 1st version of info_boxplot which satisfies the requirement 1.
1.1 The box plot will be drawn
1.2 In this box plot, the quartile 1, median, quartile 3, the lower fence (sometimes called “minimum”), and upper fence
    will be included.
1.3 The outliers will be drawn as pointers on the plot.
------------------------------------------------------------------------------------------------------------------------
2. info_boxplot_v2
This is the 2nd version of info_boxplot which satisfies the requirement 2.
2.1 The box plot will be drawn
2.2 In this box plot, the quartile 1, median, quartile 3, the lower fence (sometimes called “minimum”), and upper fence
    will be included
2.3 The outliers will be drawn as pointers on the plot
2.4 The color of the boxplot's components can be changed
------------------------------------------------------------------------------------------------------------------------
3. info_boxplot_v3
This is the 3rd version of info_boxplot which satisfies the requirement 3.
3.1 The box plot will be drawn
3.2 In this box plot, the quartile 1, median, quartile 3, the lower fence (sometimes called “minimum”), and upper fence
    will be included
3.3 The outliers will be drawn as pointers on the plot
3.4 The color of the boxplot's component can be changed
3.5 Every 5%-percentile from the 1st quartile (Q1) until the 3rd quartile (Q3) will be drawn
------------------------------------------------------------------------------------------------------------------------
4. histobox_plot
Drawing function for plot which is a mix between a box plot and a histogram
------------------------------------------------------------------------------------------------------------------------
5. creative_boxplot
Make a creative mixed plot with various properties assignable, such as color, width and line style.
The box plot is on the left half and the frequency area is on the right side.
------------------------------------------------------------------------------------------------------------------------

"""

__author__ = "Group No.18 in DSP of Lanzhou University: Yuming Chen, Huiyi Liu"
__copyright__ = "Copyright 2020, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__maintainer__ = "Yuming Chen"
__email__ = ["chenym18@lzu.edu.cn", "liuhuiyi18@lzu.edu.cn"]
__status__ = "Experimental"

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes
import matplotlib.patches
import matplotlib.transforms as transforms
from typing import List
from tools import input_checking
from matplotlib.path import Path
import matplotlib.patches as patches


def info_boxplot_v1(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray) -> matplotlib.axes:
    """
    Drawing function for box plots.

    This is the 1st version of info_boxplot which satisfies the requirement 1.
    The box plots will be drawn by this function and the quartile 1, median, quartile 3,
    the lower fence (sometimes called “minimum”), and upper fence will be included.
    The outliers will be drawn as pointers on the plot.

    Parameters
    ----------
    ax: matplotlib.axes.Axis

    data: list(list()), ...)
          consists in a list of list and each item of data is a list containing multiple series of numerical values

    Returns
    -------
    matplotlib.axes

    """

    # input checking
    if isinstance(data, np.ndarray):
        assert len(data.shape) == 2, "The input should be 2-D array"
        assert data.dtype != '<U11', "The element in 2-D array should be numerical values"
    else:
        data = input_checking(data)

    # set x-axis and y-axis
    labels = [i + 1 for i in range(len(data))]
    y_min = min(min(data[i]) for i in range(len(data)))
    y_max = max(max(data[i]) for i in range(len(data)))
    ax.set_ylim(y_min - 0.1 * (abs(y_max)), y_max + 0.1 * (abs(y_max)))
    ax.set_xlim(0, len(labels) + 1)
    ax.set_xticks(labels)

    # set a box for each list of data
    for index in range(len(data)):
        # set the width of the box and caps
        width = 0.2
        # get the quantiles
        quantiles = np.percentile(data[index], (25, 50, 75))
        iqr = quantiles[2] - quantiles[0]
        # the lower bound of the box
        low_bound = quantiles[0] - 1.5 * iqr
        # the upper bound of the box
        up_bound = quantiles[2] + 1.5 * iqr

        # pick out and draw the outliers
        outliers = np.concatenate((data[index][low_bound > data[index]], data[index][up_bound < data[index]]))
        for o in outliers:
            trans = (ax.figure.dpi_scale_trans + transforms.ScaledTranslation(labels[index], o, ax.transData))
            circle = matplotlib.patches.Circle((0, 0), 0.04, edgecolor='black', facecolor='white',
                                               transform=trans)
            ax.add_patch(circle)
            # do not consider outliers when drawing the boxplot
            data[index] = data[index][~np.isin(data[index], o)]

        # draw the whisker,caps and box
        # define the top of box
        box_top = min(max(data[index]), up_bound)
        # define the bottom of box
        box_bottom = max(min(data[index]), low_bound)
        # draw the bottom of box
        ax.hlines(quantiles[0], labels[index] - width, labels[index] + width, linewidth=1)
        # draw the median of box
        ax.hlines(quantiles[1], labels[index] - width, labels[index] + width, color='orange', linewidth=1)
        # draw the top of box
        ax.hlines(quantiles[2], labels[index] - width, labels[index] + width, linewidth=1)
        # draw the high cap
        ax.hlines(box_top, labels[index] - width / 2, labels[index] + width / 2, linewidth=1)
        # draw the low cap
        ax.hlines(box_bottom, labels[index] - width / 2, labels[index] + width / 2, linewidth=1)
        # draw the low whisker
        ax.vlines(labels[index], ymin=box_bottom, ymax=quantiles[0], linewidth=1)
        # draw the high whisker
        ax.vlines(labels[index], ymin=quantiles[2], ymax=box_top, linewidth=1)
        # draw the left bound of whisker
        ax.vlines(labels[index] - width, ymin=quantiles[0], ymax=quantiles[2], linewidth=1)
        # draw the right bound of whisker
        ax.vlines(labels[index] + width, ymin=quantiles[0], ymax=quantiles[2], linewidth=1)
    return ax


def info_boxplot_v2(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray,
                    facecolor: str = 'white', outliercolor: str = 'steelblue', boxlinecolor: str = 'black',
                    whiskercolor: str = 'black', outlierlinecolor: str = 'white', capcolor: str = 'black',
                    medianlinecolor: str = 'orange') -> matplotlib.axes:
    """
    Drawing function for box plots.

    This is the 2nd version of info_boxplot which satisfies the requirement 2.Based on the previous `info_boxplot`,
    the `info_boxplot_v2` can change the color of box plots' components.

    Parameters
    ----------
    ax: matplotlib.axes.Axis

    data: List[np.ndarray or List[int or float]] or np.ndarray
        consists in a list of list and each item of data is a list containing multiple series of numerical values.

    facecolor: str, default: 'white'
        The color of the faces of boxes.

    outliercolor: str, default: 'steelblue'
        The color of points which represent outliers.

    outlierlinecolor: str, default: 'white'
        The color of the edges of points which represent outliers.

    boxlinecolor: str, default: 'black'
        The color of the edges of the boxes.

    whiskercolor: str, default: 'black'
        The color of whiskers (the vertical lines extending to the most extreme, non-outlier data points).

    capcolor: str, default: 'black'
        The color of caps (horizontal lines at the ends of the whiskers).

    medianlinecolor: str, default: 'orange'
        The color of the median lines in the boxes.

    Returns
    -------
    matplotlib.axes

    """

    # input checking
    if isinstance(data, np.ndarray):
        assert len(data.shape) == 2, "The input should be 2-D array"
        assert data.dtype != '<U11', "The element in 2-D array should be numerical values"
    else:
        data = input_checking(data)

    # set x-axis and y-axis
    labels = [i + 1 for i in range(len(data))]
    y_min = min(min(data[i]) for i in range(len(data)))
    y_max = max(max(data[i]) for i in range(len(data)))
    ax.set_ylim(y_min - 0.1 * abs(y_max), y_max + 0.1 * (abs(y_max)))
    ax.set_xlim(0, len(labels) + 1)
    ax.set_xticks(labels)

    # set a box for each list of data
    for index in range(len(data)):
        # set the width of the box and caps
        width = 0.2
        quantiles = np.percentile(data[index], (25, 50, 75))  # get the quantiles
        iqr = quantiles[2] - quantiles[0]
        low_bound = quantiles[0] - 1.5 * iqr  # the lower bound of the box
        up_bound = quantiles[2] + 1.5 * iqr  # the upper bound of the box

        # pick out and draw the outliers
        outliers = np.concatenate((data[index][low_bound > data[index]], data[index][up_bound < data[index]]))
        for o in outliers:
            trans = (ax.figure.dpi_scale_trans + transforms.ScaledTranslation(labels[index], o, ax.transData))
            circle = matplotlib.patches.Circle((0, 0), 0.04, edgecolor=outlierlinecolor, facecolor=outliercolor,
                                               transform=trans)
            ax.add_patch(circle)
            # do not consider outliers when drawing the boxplot
            data[index] = data[index][~np.isin(data[index], o)]

        # draw the whisker,caps and box
        # define the top of box
        box_top = min(max(data[index]), up_bound)
        # define the bottom of box
        box_bottom = max(min(data[index]), low_bound)
        # draw the bottom of box
        ax.hlines(quantiles[0], labels[index] - width, labels[index] + width, linewidth=1, color=boxlinecolor)
        # draw the median of box
        ax.hlines(quantiles[1], labels[index] - width, labels[index] + width, color=medianlinecolor, linewidth=1)
        # draw the top of box
        ax.hlines(quantiles[2], labels[index] - width, labels[index] + width, linewidth=1, color=boxlinecolor)
        # draw the high cap
        ax.hlines(box_top, labels[index] - width / 2, labels[index] + width / 2, linewidth=1, color=capcolor)
        # draw the low cap
        ax.hlines(box_bottom, labels[index] - width / 2, labels[index] + width / 2, linewidth=1, color=capcolor)
        # draw the low whisker
        ax.vlines(labels[index], ymin=box_bottom, ymax=quantiles[0], linewidth=1, color=whiskercolor)
        # draw the high whisker
        ax.vlines(labels[index], ymin=quantiles[2], ymax=box_top, linewidth=1, color=whiskercolor)
        # draw the left bound of whisker
        ax.vlines(labels[index] - width, ymin=quantiles[0], ymax=quantiles[2], linewidth=1, color=boxlinecolor)
        # draw the right bound of whisker
        ax.vlines(labels[index] + width, ymin=quantiles[0], ymax=quantiles[2], linewidth=1, color=boxlinecolor)

        # define the color of the box's face
        rect = plt.Rectangle((labels[index] - width, quantiles[0]), 2 * width, quantiles[2] - quantiles[0],
                             color=facecolor)
        ax.add_patch(rect)
    return ax


def info_boxplot_v3(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray,
                    facecolor: str = 'white', outliercolor: str = 'steelblue', boxlinecolor: str = 'black',
                    whiskercolor: str = 'black', outlierlinecolor: str = 'white', capcolor: str = 'black',
                    medianlinecolor: str = 'orange', multiplebox: bool = True) -> matplotlib.axes:
    """
    Drawing function for box plots.

    This is the 3rd version of info_boxplot which satisfies the requirement 3. Based on the previous `info_boxplot`,
    the `info_boxplot_v3` can show every 5%-percentile from the 1st quartile (Q1) until the 3rd quartile (Q3).

    Parameters
    ----------
    ax: matplotlib.axes.Axis

    data: List[np.ndarray or List[int or float]] or np.ndarray
        consists in a list of list and each item of data is a list containing multiple series of numerical values.

    facecolor: str, default: 'white'
        The color of the faces of boxes.

    outliercolor: str, default: 'steelblue'
        The color of points which represent outliers.

    outlierlinecolor: str, default: 'white'
        The color of the edges of points which represent outliers.

    boxlinecolor: str, default: 'black'
        The color of the edges of the boxes.

    whiskercolor: str, default: 'black'
        The color of whiskers (the vertical lines extending to the most extreme, non-outlier data points).

    capcolor: str, default: 'black'
        The color of caps (horizontal lines at the ends of the whiskers).

    medianlinecolor: str, default: 'orange'
        The color of the median lines in the boxes.

    multiplebox: bool, default: True
        If true, lines which represent every 5%-percentile from the 1st quartile (Q1) until the 3rd quartile (Q3)
        will be drawn.

    Returns
    -------
        matplotlib.axes

    """

    # input checking
    if isinstance(data, np.ndarray):
        assert len(data.shape) == 2, "The input should be 2-D array"
        assert data.dtype != '<U11', "The element in 2-D array should be numerical values"
    else:
        data = input_checking(data)

    # set x-axis and y-axis
    labels = [i + 1 for i in range(len(data))]
    y_min = min(min(data[i]) for i in range(len(data)))
    y_max = max(max(data[i]) for i in range(len(data)))
    ax.set_ylim(y_min - 0.1 * abs(y_max), y_max + 0.1 * (abs(y_max)))
    ax.set_xlim(0, len(labels) + 1)
    ax.set_xticks(labels)

    # set a box for each list of data
    for index in range(len(data)):
        width = 0.2  # set the width of the box and caps
        quantiles = np.percentile(data[index], (25, 50, 75))  # get the quantiles
        iqr = quantiles[2] - quantiles[0]
        low_bound = quantiles[0] - 1.5 * iqr  # the lower bound of the box
        up_bound = quantiles[2] + 1.5 * iqr  # the upper bound of the box

        # pick out and draw the outliers
        outliers = np.concatenate((data[index][low_bound > data[index]], data[index][up_bound < data[index]]))
        for o in outliers:
            trans = (ax.figure.dpi_scale_trans + transforms.ScaledTranslation(labels[index], o, ax.transData))
            circle = matplotlib.patches.Circle((0, 0), 0.04, edgecolor=outlierlinecolor, facecolor=outliercolor,
                                               transform=trans)
            ax.add_patch(circle)
            # do not consider outliers when drawing the boxplot
            data[index] = data[index][~np.isin(data[index], o)]

        # draw the whisker,caps and box
        # define the top of box
        box_top = min(max(data[index]), up_bound)
        # define the bottom of box
        box_bottom = max(min(data[index]), low_bound)
        # draw the bottom of box
        ax.hlines(quantiles[0], labels[index] - width, labels[index] + width, linewidth=1, color=boxlinecolor)
        # draw the median of box
        ax.hlines(quantiles[1], labels[index] - width, labels[index] + width, color=medianlinecolor, linewidth=1)
        # draw the top of box
        ax.hlines(quantiles[2], labels[index] - width, labels[index] + width, linewidth=1, color=boxlinecolor)
        # draw the high cap
        ax.hlines(box_top, labels[index] - width / 2, labels[index] + width / 2, linewidth=1, color=capcolor)
        # draw the low cap
        ax.hlines(box_bottom, labels[index] - width / 2, labels[index] + width / 2, linewidth=1, color=capcolor)
        # draw the low whisker
        ax.vlines(labels[index], ymin=box_bottom, ymax=quantiles[0], linewidth=1, color=whiskercolor)
        # draw the high whisker
        ax.vlines(labels[index], ymin=quantiles[2], ymax=box_top, linewidth=1, color=whiskercolor)
        # draw the left bound of whisker
        ax.vlines(labels[index] - width, ymin=quantiles[0], ymax=quantiles[2], linewidth=1, color=boxlinecolor)
        # draw the right bound of whisker
        ax.vlines(labels[index] + width, ymin=quantiles[0], ymax=quantiles[2], linewidth=1, color=boxlinecolor)

        if multiplebox:
            per5 = np.percentile(data[index], (30, 35, 40, 45, 50, 55, 60, 65, 70), interpolation='midpoint')
            for k in range(len(per5)):
                ax.hlines(per5[k], labels[index] - width, labels[index] + width, linewidth=1, color=boxlinecolor)
            ax.hlines(quantiles[1], labels[index] - width, labels[index] + width, color=medianlinecolor, linewidth=3)

        # define the color of the box's face
        rect = plt.Rectangle((labels[index] - width, quantiles[0]), 2 * width, quantiles[2] - quantiles[0],
                             color=facecolor)
        ax.add_patch(rect)
    return ax


def histobox_plot(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray,
                  bins: int = 10) -> matplotlib.axes:
    """

    Drawing function for plot which is a mix between a box plot and a histogram

    Drawing a mixed plot for each data set in the data list. The left half is a traditional box plot,
    while there is a histogram reflecting the distribution on the right half.

    Parameters
    ----------
    ax: matplotlib.axes

    data: List[np.ndarray or List[int or float]] or np.ndarray
        consists in a list of list and each item of data is a list containing multiple series of numerical values.

    bins: int, default: 10

    Returns
    -------
        matplotlib.axes

    """

    # input checking
    try:
        bins += 0
    except TypeError as err:
        print("The bins should be integer")
        raise err
    if isinstance(data, np.ndarray):
        assert len(data.shape) == 2, "The input should be 2-D array"
        assert data.dtype != '<U11', "The element in 2-D array should be numerical values"
    else:
        data = input_checking(data)

    # set x-axis and y-axis
    labels = [i + 1 for i in range(len(data))]
    ax.set_xticks(labels)
    y_min = min(min(data[i]) for i in range(len(data)))
    y_max = max(max(data[i]) for i in range(len(data)))
    ax.set_ylim(y_min - 0.1 * abs(y_max), y_max + 0.1 * (abs(y_max)))
    ax.set_xlim(0, len(labels) + 1)

    # set a box for each list of data
    for index in range(len(data)):
        # set the width of the box and caps
        width = 0.2
        # get the quantiles
        quantiles = np.percentile(data[index], (25, 50, 75))
        iqr = quantiles[2] - quantiles[0]
        # the lower bound of the box
        low_bound = quantiles[0] - 1.5 * iqr
        # the upper bound of the box
        up_bound = quantiles[2] + 1.5 * iqr

        # deal with the bar plot
        height = max(data[index]) - min(data[index])
        ax.vlines(labels[index], ymin=min(data[index]), ymax=max(data[index]), linewidth=1)
        inter = height / bins
        barwidth = height / bins
        total = []
        low = min(data[index])
        for m in range(bins):
            count = 0
            for n in data[index]:
                if n >= low and n < low + inter:
                    count += 1
            low += inter
            # take the maximum value into consideration
            if m == bins:
                low += 1
            total.append(count)
        # scaler to(0,0.5)
        total = [(x - min(total)) / (max(total) - min(total)) * 0.5 for x in total]
        for p in range(len(total)):
            rect = plt.Rectangle((labels[index], min(data[index]) + p * barwidth), total[p], barwidth,
                                 edgecolor='black',
                                 facecolor='silver')
            ax.add_patch(rect)

        # pick out and draw the outliers
        outliers = np.concatenate((data[index][low_bound > data[index]], data[index][up_bound < data[index]]))
        for o in outliers:
            trans = (ax.figure.dpi_scale_trans + transforms.ScaledTranslation(labels[index], o, ax.transData))
            circle = matplotlib.patches.Circle((0, 0), 0.04, edgecolor='black', facecolor='white',
                                               transform=trans)
            ax.add_patch(circle)
            # do not consider outliers when drawing the boxplot
            data[index] = data[index][~np.isin(data[index], o)]

        # draw the whisker,caps and box
        # define the top of box
        box_top = min(max(data[index]), up_bound)
        # define the bottom of box
        box_bottom = max(min(data[index]), low_bound)
        # draw the bottom of box
        ax.hlines(quantiles[0], labels[index] - width, labels[index], linewidth=1)
        # draw the median of box
        ax.hlines(quantiles[1], labels[index] - width, labels[index], linewidth=1)
        # draw the top of box
        ax.hlines(quantiles[2], labels[index] - width, labels[index], linewidth=1)
        # draw the high cap
        ax.hlines(box_top, labels[index] - width / 2, labels[index], linewidth=1)
        # draw the low cap
        ax.hlines(box_bottom, labels[index] - width / 2, labels[index], linewidth=1)
        # draw the low whisker
        ax.vlines(labels[index], ymin=box_bottom, ymax=quantiles[0], linewidth=1)
        # draw the high whisker
        ax.vlines(labels[index], ymin=quantiles[2], ymax=box_top, linewidth=1)
        # draw the left bound of whisker
        ax.vlines(labels[index] - width, ymin=quantiles[0], ymax=quantiles[2], linewidth=1)

    ax.set_xlim(0, len(labels) + 1)
    return ax


def creative_boxplot(ax: matplotlib.axes, data: List[np.ndarray or List[int or float]] or np.ndarray, bins: int = 10,
                     whis: float = 1.5, labelset: list or bool = False, showcaps: bool = True, showfliers: bool = True,
                     showmeans: bool = True, showtrend: bool = True, variawidth: bool = True,
                     curfacecolor: str = 'white', curlinecolor: str = 'black', curalpha: int = 1,
                     outlierlinecolor: str = 'white', outliercolor: str = 'steelblue', outlierlinewidth: int = 1,
                     capcolor: str = 'black', capwidth: int or float = 1,
                     whiskercolor: str = 'black', whiskerwidth: int or float = 1,
                     boxfacecolor: str = 'white', boxedgecolor: str = 'black', boxedgewidth: int or float = 1,
                     mediancolor: str = 'orange', medianwidth: int or float = 1, medianlinestyle: str = '-',
                     meancolor: str = 'green', meanwidth: int or float = 1, meanlinestyle: str = '--',
                     trendcolor: str = 'blue', trendwidth: int or float = 1.5, trendlinestyle: str = ':',
                     rotation: int or float = 0) -> matplotlib.axes:
    """
    Make a creative mixed plot with various properties assignable, such as color, width and line style.
    The box plot is on the left half and the frequency area is on the right side.

    Make a box and whisker plot for each data set in the data list. The box extends from the lower to upper quartile
    values of the data, with a line at the median. The whiskers extend from the box to show the range of the data.
    Outliers are those past the end of the whiskers. It allows users to specify the face color of the box and the
    outliers, the line color of the box, the whisker, the caps, the outliers, and the median. It also allows users
    to specify whether to show the caps, outliers, means, and the line among boxes. Users can also set the labels of
    datasets. There are other properties such as line width and line style that are able to be specified. Besides,
    users can set the widths of the boxs changeable to make it reflect the size of the samples when comparing grouped
    data. When used for time series data, dotted line between the boxes can be specified to show the variation trends of
    the median among the samples.


    parameters:
    ax: matplotlib.axes

    data: List[np.ndarray or List[int or float]] or np.ndarray
        consists in a list of list and each item of data is a list containing multiple series of numerical values.

    bins: int, default: 10

    whis: float, default: 1.5
        The position of the whiskers.
        If a float, the lower whisker is at the lowest datum above Q1 - whis*(Q3-Q1),
        and the upper whisker at the highest datum below Q3 + whis*(Q3-Q1), where Q1 and Q3 are the first and third quartiles.
        The default value of whis = 1.5 corresponds to Tukey's original definition of boxplots.

    labelset: list, optional, default: [1,2,3,4,...]
        Labels for each dataset (one per dataset).

    showcaps: bool, default: True
        If True, show the caps on the ends of whiskers.

    showfliers: bool, default: True
        If True, show the outliers beyond the caps.

    showmeans: bool, default: True
        If True, show the arithmetic means.

    showtrend: bool, default: True
        If True, show the broken line among medians of datasets

    variawidth: bool, default: True
        If True, change the widths of boxes according to the sizes of datasets

    capcolor: color, default: 'black'
        The color of caps (horizontal lines at the ends of the whiskers)

    capwidth: float or int, default: 1
        The width of caps (horizontal lines at the ends of the whiskers)

    whiskercolor: color, default: 'black'
        The color of whiskers (the vertical lines extending to the most extreme, non-outlier data points)

    whiskerwidth: float or int, default: 1
        The width of whiskers (the vertical lines extending to the most extreme, non-outlier data points)

    boxfacecolor: color, default: 'white'
        The color of the faces of the boxes

    boxedgecolor: color, default: 'black'
        The color of the edges of the boxes

    boxedgewidth: float or int, default: 1
        The width of the edges of the boxes

    mediancolor: color, default: 'orange'
        The color of the median lines in the boxes

    medianwidth: float or int, default: 1
        The width of the median lines in the boxes

    medianlinestyle: str, default:'--'
        The line style of the median lines in the boxes
            '-': solid line style
            '--': dashed line style
            '-.': dash-dot line style
            ':': dotted line style

    meancolor: color, default: 'green'
        The color of the mean lines in the boxes

    meanwidth: float or int, default: 1
        The width of the mean lines in the boxes

    meanlinestyle: str, default:'--'
         The line style of the mean lines in the boxes
             '-': solid line style
             '--': dashed line style
             '-.': dash-dot line style
             ':': dotted line style
    trendcolor: color, default: 'blue'
        The color of the line connecting the medians of the boxes

    trendwidth: float or int, default: 1.5
        The width of the line connecting the medians of the boxes

    trendlinestyle: str, default:':'
        The line style of the line connecting the medians of the boxes
            '-': solid line style
            '--': dashed line style
            '-.': dash-dot line style
            ':': dotted line style

    curlinecolor: str, default: 'white'
        The color of edges of the curves

    curfacecolor: str, default: 'black'
        The color of faces of the curves

    curalpha: int, default: 1
        The transparency of faces of the curves

    outliercolor: color, default: 'white'
        The color of the faces of points represent the outliers

    outlierlinecolor: color, default: 'black'
        The color of the edges of points represent the outliers

    outlierlinewidth: float or int, default: 1
        The width of the edges of points represent the outliers


    Returns
    -------
        matplotlib.axes

    """

    try:
        bins += 0
    except TypeError as err:
        print("The bins should be integer")
        raise err
    if isinstance(data, np.ndarray):
        assert len(data.shape) == 2, "The input should be 2-D array"
        assert data.dtype != '<U11', "The element in 2-D array should be numerical values"
    else:
        data = input_checking(data)

    # set x-axis and y-axis
    labels = [i + 1 for i in range(len(data))]
    y_min = min(min(data[i]) for i in range(len(data)))
    y_max = max(max(data[i]) for i in range(len(data)))
    ax.set_ylim(y_min - 0.1 * (abs(y_max)), y_max + 0.1 * (abs(y_max)))
    ax.set_xlim(0, len(labels) + 1)

    ax.set_xticks(labels)
    if labelset:
        ax.set_xticklabels(labelset, rotation=rotation)

    proportion = []
    for index in data:
        proportion.append(len(index))

    # set a box for each list of data
    for index in range(len(data)):
        # set the width of the box and caps
        if variawidth:
            width = 0.5 * (proportion[index] / sum(proportion))
        else:
            width = 0.25
        # get the quantiles
        quantiles = np.percentile(data[index], (25, 50, 75))
        iqr = quantiles[2] - quantiles[0]
        # the lower bound of the box
        low_bound = quantiles[0] - whis * iqr
        # the upper bound of the box
        up_bound = quantiles[2] + whis * iqr
        # define the top of box
        box_top = min(max(data[index]), up_bound)
        # define the bottom of box
        box_bottom = max(min(data[index]), low_bound)

        height = max(data[index]) - min(data[index])
        ax.vlines(labels[index], ymin=min(data[index]), ymax=max(data[index]), linewidth=1)
        inter = height / bins
        barwidth = height / bins
        total = []
        low = min(data[index])
        yli = []
        xli = []
        for m in range(bins):
            count = 0
            for n in data[index]:
                if n >= low and n < low + inter:
                    count += 1
            low += inter
            if m == bins - 2:
                low += 1  # take the maximum value into consideration
            total.append(count)
        total = [(x - min(total)) / (max(total) - min(total)) * 0.5 for x in total]  # scaler to(0,0.5)
        for p in range(len(total)):
            yli.append(min(data[index]) + p * barwidth + barwidth / 2)
            xli.append(total[p] + labels[index])
        xli.insert(0, labels[index])
        xli.append(labels[index])
        yli.insert(0, box_bottom)
        yli.append(box_top)

        from operator import itemgetter
        yli, xli = [list(x) for x in zip(*sorted(zip(yli, xli), key=itemgetter(0)))]
        y = np.array(yli)
        ynew = np.linspace(min(y), max(y), 1000)

        from scipy.interpolate import make_interp_spline
        power_smooth = make_interp_spline(yli, xli, bc_type=([(1, 0.0)], [(1, 0.0)]))(ynew)
        for t in range(len(power_smooth)):
            if power_smooth[t] < labels[index]:
                power_smooth[t] = labels[index]
        ax.fill_betweenx(ynew, labels[index], power_smooth, facecolor=curfacecolor, edgecolor=curlinecolor,
                         alpha=curalpha)

        rect = plt.Rectangle((labels[index] - width, quantiles[0]), width, quantiles[2] - quantiles[0],
                             color=boxfacecolor)
        ax.add_patch(rect)

        # pick out and draw the outliers
        outliers = np.concatenate((data[index][low_bound > data[index]], data[index][up_bound < data[index]]))
        for o in outliers:
            if showfliers:
                trans = (ax.figure.dpi_scale_trans + transforms.ScaledTranslation(labels[index], o, ax.transData))
                circle = matplotlib.patches.Circle((0, 0), 0.04, edgecolor=outlierlinecolor, facecolor=outliercolor,
                                                   transform=trans, linewidth=outlierlinewidth)
                ax.add_patch(circle)
            # do not consider outliers when drawing the boxplot
            data[index] = data[index][~np.isin(data[index], o)]
        # draw the bottom of box
        ax.hlines(quantiles[0], labels[index] - width, labels[index], linewidth=boxedgewidth, color=boxedgecolor)
        # draw the median of box
        ax.hlines(quantiles[1], labels[index] - width, labels[index], color=mediancolor, linewidth=medianwidth,
                  ls=medianlinestyle, )
        # draw the top of box
        ax.hlines(quantiles[2], labels[index] - width, labels[index], linewidth=boxedgewidth, color=boxedgecolor)
        if showcaps:
            # draw the high cap
            ax.hlines(box_top, labels[index] - width / 2, labels[index] + width / 2, linewidth=capwidth, color=capcolor)
            # draw the low cap
            ax.hlines(box_bottom, labels[index] - width / 2, labels[index] + width / 2, linewidth=capwidth,
                      color=capcolor)
        # draw the low whisker
        ax.vlines(labels[index], ymin=box_bottom, ymax=quantiles[0], linewidth=whiskerwidth, color=whiskercolor)
        # draw the high whisker
        ax.vlines(labels[index], ymin=quantiles[2], ymax=box_top, linewidth=whiskerwidth, color=whiskercolor)
        # draw the left bound of whisker
        ax.vlines(labels[index] - width, ymin=quantiles[0], ymax=quantiles[2], linewidth=boxedgewidth,
                  color=boxedgecolor)
        if showtrend:
            if index > 0:
                verts = [
                    (labels[index - 1], lastme),
                    (labels[index], quantiles[1]), ]
                codes = [Path.MOVETO,
                         Path.LINETO,
                         ]
                path = Path(verts, codes)
                patch = patches.PathPatch(path, color=trendcolor, ls=trendlinestyle, lw=trendwidth)
                ax.add_patch(patch)
            lastme = quantiles[1]
        if showmeans:
            ax.hlines(np.mean(data[index]), labels[index] - width, labels[index], color=meancolor, ls=meanlinestyle,
                      linewidth=meanwidth)
    return ax


if __name__ == "__main__":
    # Generate test data randomly
    from tools import gen_test_data

    # Simple Test
    data = gen_test_data()
    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 10))
    axes = ax.flatten()
    ax1 = axes[0]
    ax1.set_title('boxplot in matplotlib')
    ax2 = axes[1]
    ax2.set_title('info_boxplot_v1')
    ax3 = axes[2]
    ax3.set_title('info_boxplot_v2')
    ax4 = axes[3]
    ax4.set_title('info_boxplot_v3')
    ax5 = axes[4]
    ax5.set_title('histobox_plot')
    ax6 = axes[5]
    ax6.set_title('creative_boxplot')
    ax1.boxplot(data)
    info_boxplot_v1(ax2, data)
    info_boxplot_v2(ax3, data)
    info_boxplot_v3(ax4, data)
    histobox_plot(ax5, data)
    creative_boxplot(ax6, data)
    plt.show()
