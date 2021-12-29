import os, difflib, filecmp, tempfile

from qgis.core import QgsProject
from qgis import processing
from qgis.utils import iface


def main():
    test_path = "/home/egissi/github/qgisfds.verification/tests/"
    algorithm = "Export to NIST FDS:Export terrain"
    project = QgsProject.instance()

    # Test
    test_name = "Export GEOM from cern_meyrin"
    test_dir = "test_cern_meyrin"
    test_filename = "cern_meyrin.qgs"
    parameters = {
        "cell_size": 1,
        "chid": "cern_meyrin",
        "dem_layer": os.path.join(
            test_path,
            test_dir,
            "format_6_grid_asc_meyrin_dtm_20200522_122939/MN_Surface_2017_GRID.asc",
        ),
        "dem_sampling": 2,
        "export_obst": False,
        "extent": "6.048008498,6.049552799,46.232493265,46.233460112 [EPSG:4326]",
        "fds_path": "./fds_geom",
        "fire_layer": None,
        "landuse_layer": None,
        "landuse_type_filepath": "",
        "nmesh": 4,
        "origin": None,
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": None,
        "tex_pixel_size": 0.1,
        "wind_filepath": "",
    }

    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
    )

    # Test
    test_name = "Export OBST from cern_meyrin"
    test_filename = "cern_meyrin.qgs"
    parameters = {
        "cell_size": 1,
        "chid": "cern_meyrin",
        "dem_layer": os.path.join(
            test_path,
            test_dir,
            "format_6_grid_asc_meyrin_dtm_20200522_122939/MN_Surface_2017_GRID.asc",
        ),
        "dem_sampling": 2,
        "export_obst": True,
        "extent": "6.048008498,6.049552799,46.232493265,46.233460112 [EPSG:4326]",
        "fds_path": "./fds_obst",
        "fire_layer": None,
        "landuse_layer": None,
        "landuse_type_filepath": "",
        "nmesh": 4,
        "origin": None,
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": None,
        "tex_pixel_size": 0.1,
        "wind_filepath": "",
    }

    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
    )

    # Test

    test_name = "Export GEOM from test_golden_gate_local"
    test_dir = "test_golden_gate_local"
    test_filename = "golden_gate_local.qgs"
    parameters = {
        "cell_size": 10,
        "chid": "golden_gate_local",
        "dem_layer": os.path.join(
            test_path,
            test_dir,
            "US_DEM2016_local.tif",
        ),
        "dem_sampling": 1,
        "export_obst": False,
        "extent": "-122.491206899,-122.481181391,37.827810126,37.833676214 [EPSG:4326]",
        "fds_path": "./fds_geom",
        "fire_layer": os.path.join(
            test_path,
            test_dir,
            "fire.shx|layername=fire",
        ),
        "landuse_layer": os.path.join(
            test_path,
            test_dir,
            "US_200F13_20_local.tif",
        ),
        "landuse_type_filepath": "./Landfire.gov_F13.csv",
        "nmesh": 4,
        "origin": "-2279076.207440,1963675.963121 [EPSG:5070]",
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": "crs=EPSG:3857&format&type=xyz&url=https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0",
        "tex_pixel_size": 1,
        "wind_filepath": "./wind.csv",
    }

    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
    )

    # Test

    test_name = "Export OBST from test_golden_gate_local"
    test_dir = "test_golden_gate_local"
    test_filename = "golden_gate_local.qgs"
    parameters = {
        "cell_size": 10,
        "chid": "golden_gate_local",
        "dem_layer": os.path.join(
            test_path,
            test_dir,
            "US_DEM2016_local.tif",
        ),
        "dem_sampling": 1,
        "export_obst": True,
        "extent": "-122.491206899,-122.481181391,37.827810126,37.833676214 [EPSG:4326]",
        "fds_path": "./fds_obst",
        "fire_layer": os.path.join(
            test_path,
            test_dir,
            "fire.shx|layername=fire",
        ),
        "landuse_layer": os.path.join(
            test_path,
            test_dir,
            "US_200F13_20_local.tif",
        ),
        "landuse_type_filepath": "./Landfire.gov_F13.csv",
        "nmesh": 4,
        "origin": "-2279076.207440,1963675.963121 [EPSG:5070]",
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": "crs=EPSG:3857&format&type=xyz&url=https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0",
        "tex_pixel_size": 1,
        "wind_filepath": "./wind.csv",
    }

    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
    )

    # Close

    project.clear()
    iface.actionExit().trigger()
    os._exit(0)


class bcolors:
    HEADER = "\033[95m\033[1m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def test(project, test_name, test_path, test_dir, test_filename, algorithm, parameters):
    # Read test file
    test_filepath = os.path.join(test_path, test_dir, test_filename)
    print(f"\n{bcolors.HEADER}Start test: <{test_name}>{bcolors.ENDC}")
    res = project.read(test_filepath)
    if not res:
        raise IOError(f"Cannot read <{test_filepath}>")

    # Run test
    refdir = parameters["fds_path"]
    with tempfile.TemporaryDirectory() as tmpdir:
        parameters["fds_path"] = tmpdir
        processing.run(algorithm, parameters)
        refdir = os.path.join(test_path, test_dir, "_ref", refdir)
        diff_fds_dir(refpath=refdir, fdspath=tmpdir)


def echo(name, success, log):
    if success:
        print(f"{bcolors.OKGREEN}{name}: OK{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}{name}: FAIL{bcolors.ENDC}\n{log}")


def diff_fds_dir(refpath, fdspath):
    for f in os.scandir(refpath):
        name = f"Diff: {f.name}"
        filepath1 = f.path
        filepath2 = os.path.join(fdspath, f.name)

        if f.name.endswith(".bingeom") or f.name.endswith(".png"):
            success, log = _diff_binary_files(filepath1, filepath2)
        elif f.name.endswith(".fds"):
            success, log = _diff_fds_files(filepath1, filepath2)
        else:
            success, log = False, f"Unrecognized file type: {f.name}"
        echo(name, success, log)


def _diff_binary_files(filepath1, filepath2):
    if filecmp.cmp(filepath1, filepath2):
        return True, str()
    else:
        return False, "Binary different"


def _diff_fds_files(refpath, fdspath):
    if not os.path.isfile(refpath):
        return False, f"<{refpath}> does not exist"
    if not os.path.isfile(fdspath):
        return False, f"<{fdspath}> does not exist"
    success, log = True, str()
    with open(refpath, "r") as f1, open(fdspath, "r") as f2:
        lines1 = f1.read().splitlines()
        lines2 = f2.read().splitlines()
    for l in difflib.unified_diff(lines1, lines2, n=0):
        if l[:3] in ("---", "+++", "@@ ") or l[1:7] in (
            "! Gene",
            "! Date",
            "! QGIS",
        ):
            continue
        log += f"\n{l}"
    if log:
        success = False
    return success, log


main()
