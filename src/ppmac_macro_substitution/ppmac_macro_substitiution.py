import fileinput
from pathlib import Path


def generate(
    substitutes,
    kinematic_template_files,
    kinematics_destination_folder=Path(
        "BL99I-MO-STEP-01", "PMAC Script Language", "Kinematic Routines"
    ),
    template_source_folder=Path("configure", "coord_templates"),
):
    """
    Gets substitutes and templates files, uses them to
    generate kinematics in kinematics_destination_folder.

    Args:
        substitutes (dict):
            A dictionary that holds names of all substitutes and their values.
        kinematic_template_files (list):
            A list of template file names.
        kinematics_destination_folder (Path, optional):
            The destination folder to store generated kinematics.
            Defaults to:
            Path('BL99I-MO-STEP-01', 'PMAC Script Language','Kinematic Routines').
        template_source_folder (Path, optional):
            The folder in which the template files are kept.
            Defaults to:
            Path('configure', 'coord_templates')."""

    for kinematic_template_file in kinematic_template_files:
        kinematic_destination_file = kinematics_destination_folder.joinpath(
            Path("cs" + substitutes["$(COORD)"] + "_" + kinematic_template_file)
        )
        header = (
            "// DO NOT MODIFY: File created from kinematic_template_file: "
            + kinematic_template_file
            + "\n"
        )
        if kinematic_destination_file.exists():
            f = open(kinematic_destination_file, "w")
            f.write(header)
        else:
            f = open(kinematic_destination_file, "x")
            f.write(header)
        kinematic_template_file_path = template_source_folder.joinpath(
            kinematic_template_file
        )
        for line in fileinput.input(kinematic_template_file_path):
            for key in substitutes:
                if key in line:
                    line = line.replace(key, substitutes[key])
            f.write(line)
