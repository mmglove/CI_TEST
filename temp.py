#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
This module 

Authors: guomengmeng01(guomengmeng01@baidu.com)
Date: 2020/6/12 14:45
"""
import paddle.fluid
import paddleslim
paddle.fluid.install_check.run_check()
print("paddleslim_version:", paddleslim.__file__)