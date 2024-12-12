import fileinput
from pathlib import Path


def generate(
    substitutes,
    template_files,
    destination_folder=Path(
        "BL99I-MO-STEP-01", "PMAC Script Language", "Kinematic Routines"
    ),
    template_source_folder=Path("configure", "coord_templates"),
):
    """
    Gets substitutes and templates files, uses them to
    generate file in destination_folder.
    Used primarily to generate kinematics.

    Args:
        substitutes (dict):
            A dictionary that holds names of all substitutes and their values.
        template_files (list):
            A list of template file names.
        destination_folder (Path, optional):
            The destination folder to store generated file.
            Defaults to:
            Path('BL99I-MO-STEP-01', 'PMAC Script Language','Kinematic Routines').
        template_source_folder (Path, optional):
            The folder in which the template files are kept.
            Defaults to:
            Path('configure', 'coord_templates')."""

    for template_file in template_files:
        if "$(COORD)" in substitutes:
            destination_file = destination_folder.joinpath(
                Path("cs" + substitutes["$(COORD)"] + "_" + template_file)
            )
        else:  # for non-kinematic use template file name
            destination_file = destination_folder.joinpath(Path(template_file))
        header = (
            "// DO NOT MODIFY: File created from template_file: " + template_file + "\n"
        )
        if destination_file.exists():
            f = open(destination_file, "w")
            f.write(header)
        else:
            f = open(destination_file, "x")
            f.write(header)
        template_file_path = template_source_folder.joinpath(template_file)
        for line in fileinput.input(template_file_path):
            for key in substitutes:
                if key in line:
                    line = line.replace(key, substitutes[key])
            f.write(line)
