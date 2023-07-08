import os, difflib, filecmp, tempfile, glob

from qgis.core import QgsProject
from qgis import processing
from qgis.utils import iface
from qgis.core import QgsApplication

try:
    import git
    systemdir = os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'qgis2fds')
    repo = git.Repo(systemdir)
    sha = repo.head.object.hexsha
    githash = sha[:7]
    if repo.is_dirty():
        githash = githash + '-dirty'
except:
    githash = ''

def main():
    test_path = "tests/"
    algorithm = "Export to NIST FDS:Export terrain"
    logfile = "log.txt"
    with open(logfile, 'w') as f:
        f.write('Starting qgis2fds verification\n')
    # Test
    project = QgsProject.instance()
    test_name = "Export GEOM from cern_meyrin"
    test_dir = "test_cern_meyrin"
    test_filename = "cern_meyrin.qgs"
    parameters = {
        "cell_size": 1,
        "chid": "cern_meyrin_geom",
        "dem_layer": os.path.join(test_path,test_dir,"data_layers","dem_layer.tif"),
        "dem_sampling": 2,
        "export_obst": False,
        "extent": "6.048008498,6.049552799,46.232493265,46.233460112 [EPSG:4326]",
        "fds_path": os.path.join(test_path, test_dir,"output"),
        "fire_layer": None,
        "landuse_layer": None,
        "landuse_type_filepath": "",
        "nmesh": 4,
        "origin": None,
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": None,
        "tex_pixel_size": 0.1,
        "wind_filepath": "",
        "addIntermediateLayersToQgis": True,
    }
    
    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
        logfile=logfile,
    )
    
    project.removeAllMapLayers()
    project.clear()
    QgsApplication.processEvents()
    
    # Test
    project = QgsProject.instance()
    test_name = "Export OBST from cern_meyrin"
    test_dir = "test_cern_meyrin"
    test_filename = "cern_meyrin.qgs"
    parameters = {
        "cell_size": 1,
        "chid": "cern_meyrin_obst",
        "dem_layer": os.path.join(test_path,test_dir,"data_layers","dem_layer.tif"),
        "dem_sampling": 2,
        "export_obst": True,
        "extent": "6.048008498,6.049552799,46.232493265,46.233460112 [EPSG:4326]",
        "fds_path": os.path.join(test_path, test_dir,"output"),
        "fire_layer": None,
        "landuse_layer": None,
        "landuse_type_filepath": "",
        "nmesh": 4,
        "origin": None,
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": None,
        "tex_pixel_size": 0.1,
        "wind_filepath": "",
        "addIntermediateLayersToQgis": True,
    }
    
    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
        logfile=logfile,
    )
    
    project.removeAllMapLayers()
    project.clear()
    QgsApplication.processEvents()
    
    # Test
    project = QgsProject.instance()
    test_name = "Export GEOM from test_golden_gate_local"
    test_dir = "test_golden_gate_local"
    test_filename = "golden_gate_local.qgs"
    parameters = {
        "cell_size": 10,
        "chid": "golden_gate_local_geom",
        "dem_layer": os.path.join(test_path,test_dir,"data_layers","US_DEM2016_local.tif"),
        "dem_sampling": 1,
        "export_obst": False,
        "extent": "-122.491206899,-122.481181391,37.827810126,37.833676214 [EPSG:4326]",
        "fds_path": os.path.join(test_path, test_dir,"output"),
        "fire_layer": os.path.join(test_path,test_dir,"data_layers","fire.shx|layername=fire"),
        "landuse_layer": os.path.join(test_path,test_dir,"data_layers","US_200F13_20_local.tif"),
        "landuse_type_filepath": "Landfire.gov_F13.csv",
        "nmesh": 4,
        "origin": "-2279076.207440,1963675.963121 [EPSG:5070]",
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": os.path.join(test_path,test_dir,"data_layers","OpenStreetMap.tif"),
        "tex_pixel_size": 1,
        "wind_filepath": "wind.csv",
        "addIntermediateLayersToQgis": True,
    }
    
    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
        logfile=logfile,
    )
    
    project.removeAllMapLayers()
    project.clear()
    QgsApplication.processEvents()
    
    # Test
    project = QgsProject.instance()
    test_name = "Export OBST from test_golden_gate_local"
    test_dir = "test_golden_gate_local"
    test_filename = "golden_gate_local.qgs"
    parameters = {
        "cell_size": 10,
        "chid": "golden_gate_local_obst",
        "dem_layer": os.path.join(test_path,test_dir,"data_layers","US_DEM2016_local.tif"),
        "dem_sampling": 1,
        "export_obst": True,
        "extent": "-122.491206899,-122.481181391,37.827810126,37.833676214 [EPSG:4326]",
        "fds_path": os.path.join(test_path, test_dir,"output"),
        "fire_layer": os.path.join(test_path,test_dir,"data_layers","fire.shx|layername=fire"),
        "landuse_layer": os.path.join(test_path,test_dir,"data_layers","US_200F13_20_local.tif"),
        "landuse_type_filepath": "Landfire.gov_F13.csv",
        "nmesh": 4,
        "origin": "-2279076.207440,1963675.963121 [EPSG:5070]",
        "sampling_layer": "TEMPORARY_OUTPUT",
        "tex_layer": os.path.join(test_path,test_dir,"data_layers","OpenStreetMap.tif"),
        "tex_pixel_size": 1,
        "wind_filepath": "wind.csv",
        "addIntermediateLayersToQgis": True,
    }

    test(
        project=project,
        test_name=test_name,
        test_path=test_path,
        test_dir=test_dir,
        test_filename=test_filename,
        algorithm=algorithm,
        parameters=parameters,
        logfile=logfile,
    )
    
    project.removeAllMapLayers()
    project.clear()
    QgsApplication.processEvents()
    project = QgsProject.instance()
    
    # Close
    
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


def test(project, test_name, test_path, test_dir, test_filename, algorithm, parameters, logfile):
    # Read test file
    test_filepath = os.path.join(test_path, test_dir, test_filename)
    print(f"\n{bcolors.HEADER}Start test: <{test_name}>{bcolors.ENDC}")
    res = project.read(test_filepath)
    if not res:
        raise IOError(f"Cannot read <{test_filepath}>")

    # Run test
    refdir = parameters["fds_path"]
    parameters["fds_path"] = os.path.abspath(parameters['fds_path'])
    refdir = os.path.abspath(os.path.join(test_path, test_dir, "_ref"))
    os.system('rm %s/*.fds'%(parameters["fds_path"]))
    os.system('rm %s/*.bingeom'%(parameters["fds_path"]))
    os.system('rm %s/*.png'%(parameters["fds_path"]))
    with open(logfile, 'a') as f:
        f.write('\nStarting ' + parameters['chid'])
    processing.run(algorithm, parameters)
    with open(logfile, 'a') as f:
        f.write('\n' + parameters['chid'] + ' Results:')
    diff_fds_dir(parameters['chid'], refpath=refdir, fdspath=parameters["fds_path"], logfile=logfile)


def echo(name, success, log):
    if success:
        print(f"{bcolors.OKGREEN}{name}: OK{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}{name}: FAIL{bcolors.ENDC}\n{log}")


def diff_fds_dir(chid, refpath, fdspath, logfile):
    refFiles = glob.glob(os.path.join(refpath, chid+'*'))
    for f in refFiles:
        name = f.split(os.sep)[-1]
        fdsFile = os.path.join(fdspath, name)
        if name.endswith(".bingeom") or name.endswith(".png"):
            success, log = _diff_binary_files(f, fdsFile)
        elif name.endswith(".fds"):
            success, log = _diff_fds_files(f, fdsFile)
        else:
            success, log = False, f"Unrecognized file type: {name}"
        echo(name, success, log)
        with open(logfile, 'a') as f:
            f.write('\n    '+log)


def _diff_binary_files(filepath1, filepath2):
    if filecmp.cmp(filepath1, filepath2):
        return True, "Binary the same"
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
