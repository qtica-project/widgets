#!/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Union
from PySide6.QtGui import QIcon
from dataclasses import dataclass


@dataclass
class ProgressIndicatorWrapper:
    active: Union[str, QIcon]
    inactive: Union[str, QIcon]
    leave: Union[str, QIcon]