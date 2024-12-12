#!/bin/env python

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
    template_source_folder="tests/configure/coord_templates",
)
