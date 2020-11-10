#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module provides function which serves as tools for the module `boxplots`

"""

__author__ = "Group No.18 in DSP of Lanzhou University: Yuming Chen, Huiyi Liu"
__copyright__ = "Copyright 2020, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__maintainer__ = "Yuming Chen"
__email__ = ["chenym18@lzu.edu.cn", "liuhuiyi18@lzu.edu.cn"]
__status__ = "Experimental"

from typing import List
import numpy as np


class InvalidInput(TypeError):
    pass


def input_checking(data: List[np.ndarray or List[int or float]]) -> List[np.ndarray]:
    """

    This function is used to check if the input is valid and standardize the input when the input is a list.

    """
    try:
        def test(item):
            assert len(item.shape) == 1, "The item in list should be 1-D array, not {}".format(item)
            assert item.dtype != '<U11', "The element in item should be numerical values"
            return item

        return [test(np.array(item)) for item in data]
    except TypeError:
        print("The input list has invalid item")
        raise InvalidInput


def gen_test_data(seed=None):
    """

        This function is used to generate test data.

    """
    np.random.seed(seed)
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = list(np.concatenate((spread, center, flier_high, flier_low)))

    spread = np.random.rand(50) * 100
    center = np.ones(25) * 40
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    d2 = list(np.concatenate((spread, center, flier_high, flier_low)))
    return [data, d2, d2[::2]]


