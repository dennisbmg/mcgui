"""The main module with the program entry point.

Enter detailed module description here

Author: Name (mail)
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2024   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************

import sys
from PyQt5.QtWidgets import QApplication
import mainwindow
from commands import command_controller
from motorvariant import motor_variant_tab, motor_config_controller
from Piezovariant import piezo_variant_tab, piezo_variant_controller
from towervariant import tower_variant
from commonblock import commonblock_tab
from pivotbearing import pivot_bearing_tab
from drivesystem import drivesystem_tab
from piezo import piezo_tab
from terminal import Terminal
import logging

try:
    from MVGUI.version import __version__, __author__, __email__, __repository__, __license__
except ModuleNotFoundError:
    # provide dummy information when not installed as package but called directly
    # also necessary to get sphinx running without error
    __version__ = 'dev'
    __author__ = 'development'
    __email__ = 'none'
    __repository__ = 'none'
    __license__ = 'none'

# Variables ********************************************************************

LOG: logging.Logger = logging.getLogger(__name__)

# Classes **********************************************************************

# Functions ********************************************************************



# Main *************************************************************************
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainwindow.App()

    terminal = Terminal()
    command = command_controller.CommandController(terminal)
    piezo_variant_tab = piezo_variant_tab.PiezoVariantTab()
    tower_variant = tower_variant.TowerVariant()
    motor_variant_tab = motor_variant_tab.MotorVariantTab()
    common_block_tab = commonblock_tab.CommonBlockTab()
    pivot_bearing_tab = pivot_bearing_tab.PivotBearingTab()
    drivesystem_tab = drivesystem_tab.DriveSystemTab()
    piezo_tab = piezo_tab.PiezoTab()

    window.addTabView(command.view, "Commands")
    window.addTabView(motor_variant_tab, "MotorVairant")
    window.addTabView(piezo_variant_tab, "PiezoVariant")
    window.addTabView(tower_variant, "TowerVariant")
    window.addTabView(common_block_tab, "Common Block")
    window.addTabView(pivot_bearing_tab, "Pivot Bearing")
    window.addTabView(drivesystem_tab, "Drive System")
    window.addTabView(piezo_tab, "Piezo")


    motor_controllers = []
    for index in range(2):
        controller = motor_config_controller.MotorConfigController(index, terminal)
        motor_controllers.append(controller)
        motor_variant_tab.register_tab(controller.view)

    piezo_variant_controllers = []
    for index in range(3):
        controller = piezo_variant_controller.PiezoVariantController(index, terminal)
        piezo_variant_controllers.append(controller)
        piezo_variant_tab.register_tab(controller.view)
 


    window.show()

    app.exec()

