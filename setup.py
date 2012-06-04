#!/usr/bin/env python
from distutils.core import setup

setup(name="Zhudi",
      version="1.1",
      description="Zhudi is a graphical interface to xDICT dictionaries",
      long_description="Have a look at README.",
      author="Jiehong Ma",
      author_email="ma.jiehong at gmail",
      url="https://github.com/Jiehong/Zhudi",
      license="GPLv3",
      py_modules=["zhudi", "data", "gui", "pinyin_to_zhuyin_table"])
