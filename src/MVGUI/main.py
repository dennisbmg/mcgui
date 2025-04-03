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
from common_block import common_block_controller
from commands import command_controller
from motorvariant import motor_variant_view, motor_config_controller
from Piezovariant import piezo_variant_view, piezo_variant_controller
from towervariant import tower_variant_controller
from pivotbearing import pivot_bearing_view, pivot_bearing_controller
from drivesystem import drivesystem_view, drive_system_controller
from piezo import piezo_view, piezo_controller
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

    #calling controller directly because we have no tabs to care about
    command = command_controller.CommandController(terminal)
    tower_variant = tower_variant_controller.TowerVariantController(terminal)
    common_block = common_block_controller.CommonBlockController(terminal)

    piezo_variant_tab = piezo_variant_view.PiezoVariantTab()
    motor_variant_tab = motor_variant_view.MotorVariantTab()
    pivot_bearing_tab = pivot_bearing_view.PivotBearingTab()
    drive_system_tab = drivesystem_view.DriveSystemTab()
    piezo_tab = piezo_view.PiezoTab()


    window.addTabView(command.view, "Commands")
    window.addTabView(motor_variant_tab, "MotorVairant")
    window.addTabView(piezo_variant_tab, "PiezoVariant")
    window.addTabView(tower_variant.view, "TowerVariant")
    window.addTabView(common_block.view, "Common Block")
    window.addTabView(pivot_bearing_tab, "Pivot Bearing")
    window.addTabView(drive_system_tab, "Drive System")
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

    pivot_bearing_controllers = []
    for index in range(2):
        controller = pivot_bearing_controller.PivotBearingController(index, terminal)
        pivot_bearing_controllers.append(controller)
        pivot_bearing_tab.register_tab(controller.view)

    drive_system_controllers = []
    for index in range(2):
        controller = drive_system_controller.DriveSystemController(index, terminal)
        drive_system_controllers.append(controller)
        drive_system_tab.register_tab(controller.view)

    piezo_controllers = []
    for index in range(3):
        controller = piezo_controller.PiezoController(index, terminal)
        piezo_controllers.append(controller)
        piezo_tab.register_tab(controller.view)

    window.show()

    app.exec()

