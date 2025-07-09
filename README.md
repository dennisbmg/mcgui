# NewTec MVC GUI

[![Repo Status](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Software Documentation](#software-documentation)
- [Used Libraries](#used-libraries)
- [Issues, Ideas and Bugs](#issues-ideas-and-bugs)

## Overview

This project is a modular Python GUI application based on PyQt5, following the Model-View-Controller (MVC) pattern. It is designed for easy extension with new hardware modules and configuration tabs. The GUI communicates with hardware via serial interface and loads its structure dynamically from YAML configuration files.

**Main modules:**
- MotorVariant
- PiezoVariant
- TowerVariant
- PivotBearing
- DriveSystem
- CommonBlock
- Command Interface (Terminal)
- Configuration Management

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/dennisbmg/mcgui.git
cd src/mvcgui
pip install -r requirements.txt
```

## Usage

Start the GUI application with:

```bash
python main.py
```

## Features

- **Modular Tabs:** Each hardware module is implemented as a separate tab with its own controller and view.
- **Dynamic Configuration:** Tab contents are loaded from YAML files and can be easily adapted.
- **Serial Communication:** The terminal module allows sending commands to hardware without blocking the GUI (using QThread).
- **Validation:** User input is validated based on configuration data.
- **Extensible:** New modules can be added by providing an MVC set and a configuration file.

## Examples

- Set and read parameters via the Command tab
- Configure motor and piezo parameters
- Dynamic display and validation of input fields according to configuration

## Software Documentation

More information on deployment and architecture can be found in the [documentation](./doc/README.md).

For detailed software design, run:

```bash
cd doc/detailed-design
make html
```

The generated documentation can then be found in `/doc/detailed-design/_build/html/index.html`.

## Used Libraries

3rd party libraries not included in the Python standard library:

- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) – GUI framework
- [PyYAML](https://pyyaml.org/) – YAML parsing

See also [requirements.txt](requirements.txt).

---

## Issues, Ideas and Bugs

If you have further ideas or found some bugs, great! Create an [issue](https://github.com/dennisbmg/mcgui/issues) or, if you are able and willing to fix it yourself, clone the repository and create a pull request.
