[![CI](https://github.com/DiamondLightSource/ppmac-macro-substitution/actions/workflows/ci.yml/badge.svg)](https://github.com/DiamondLightSource/ppmac-macro-substitution/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/DiamondLightSource/ppmac-macro-substitution/branch/main/graph/badge.svg)](https://codecov.io/gh/DiamondLightSource/ppmac-macro-substitution)
[![PyPI](https://img.shields.io/pypi/v/ppmac-macro-substitution.svg)](https://pypi.org/project/ppmac-macro-substitution)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

# ppmac_macro_substitution

A script that substitutes macros in template files.

Gets substitutes and template files and
uses them to generate files (primarily kinematics).
Default location of template files: configure/coord_templates.

The generated files are put in destination_folder which defaults to
configure/coord_substitution.

Naming convention for generated kinematics:
```
    cs_<coordinate_system_number>_<name_of_template_file>
```
and for other files:
```
    tmp_<name_of_template_file>
```

Source          | <https://github.com/DiamondLightSource/ppmac-macro-substitution>
:---:           | :---:
PyPI            | `pip install ppmac-macro-substitution`
Releases        | <https://github.com/DiamondLightSource/ppmac-macro-substitution/releases>

To print the version of the script you can do:

```python
from ppmac_macro_substitution import __version__

print(f"Hello ppmac_macro_substitution {__version__}")
```
An example substitution file for 3 jack kinematic template:

```
from ppmac_macro_substitution import generate

substitutes = {}
substitutes["$(COORD)"] = "4"
substitutes["$(J1)"] = "1"
substitutes["$(J1X)"] = "20"
substitutes["$(J1Z)"] = "10"
substitutes["$(J2)"] = "2"
substitutes["$(J2X)"] = "12"
substitutes["$(J2Z)"] = "13"
substitutes["$(J3)"] = "3"
substitutes["$(J3X)"] = "15"
substitutes["$(J3Z)"] = "16"
substitutes["$(MD)"] = "10"
substitutes["$(MCX)"] = "100"
substitutes["$(MCZ)"] = "2"

kinematic_template_files = ["inv_3jack.kin", "fwd_3jack.kin"]

generate(
    substitutes,
    kinematic_template_files,
)
```
In order to generate the kinematics using default template folder and the default destination folder
run the script in the folder above the configure folder.
