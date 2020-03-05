"""
    Interface viewset module.
"""

import tkinter as tk
from tkinter import messagebox


def move(root, img):
    """
        Move img elsewhere.
    """

    try:
        dx = float(root.dxmove.get())
        dy = float(root.dymove.get())
