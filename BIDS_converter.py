# imports
import os
import shutil
import numpy as np
import glob
import json


def edf_to_asc(path):
    """
    Convert EDF file to ASC file
    :param path: full path to EDF file, or to directory containing EDF files
    :return: None, creates ASC file in same directory as EDF file
    """

    # if path points to single file
    if os.path.isfile(path):
        if path[-4:] == '.edf':
            command = "/Applications/Eyelink/EDF_Access_API/Example/edf2asc " + path
            os.system(command)

    # if path points to directory
    elif os.path.isdir(path):
        paths = [path + '/' + i for i in os.listdir(path) if i[-4:] == '.edf']
        for _ in paths:
            edf_to_asc(_)


def make_json_individual_description(new_path):
    """
    Creates json file for specific task in BIDS directory based on edf file
    :param new_path: new path to directory containing edf file
    :return: None
    """

    samplingfrequency = '?'
    fileformat = '.edf'
    startmessage = '?'
    endmessage = '?'
    eventidentifier = '?'
    pupilpositiontype = '?'
    rawsamples = '?'
    includedeyemovementevents = '?'
    detectionalgorithm = '?'
    eventreferenceframe = '?'

    jsonDict = {
        'SamplingFrequency': samplingfrequency,
        'FileFormat': fileformat,
        'StartMessage': startmessage,
        'EndMessage': endmessage,
        'EventIdentifier': eventidentifier,
        'PupilPositionType': pupilpositiontype,
        'RawSamples': rawsamples,
        'IncludedEyeMovementEvents': includedeyemovementevents,
        'DetectionAlgorithm': detectionalgorithm,
        'EventReferenceFrame': eventreferenceframe
    }

    text = str(new_path) + '.json'

    with open(text, 'w') as json_file:
        json.dump(jsonDict, json_file)


def BIDS_edf_asc_json(path, new_dr, subject_num, tasks):
    """
    Adds EDF, ASC, and JSON files to BIDS directory
    :param new_dr: newly created BIDS directory
    :param path: (old) path to subject directory
    :param subject_num: subject number ID
    :param tasks: ordered list of tasks
    :return: None
    """

    i = 0
    os.chdir(path)

    for file in glob.glob("*.edf"):
        # copy over and rename edf file
        file_name = 'sub-' + subject_num + '_ses-01' + '_acq-' + str(i + 1) + '_task-' + tasks[i] + '_eyetrack'
        old_path = path + '/' + file
        new_path = new_dr + '/' + file_name + '.edf'
        shutil.copy(old_path, new_path)

        # create asc
        edf_to_asc(new_path)

        # create json
        make_json_individual_description(new_path[:-4])
        i += 1


def BIDS_mat(path, new_dr, subject_num, tasks):
    """
    Adds MAT files to BIDS directory
    :param new_dr: newly created BIDS directory
    :param path: (old) path to subject directory
    :param subject_num: subject number ID
    :param tasks: ordered list of tasks
    :return: None
    """

    os.chdir(path)

    for file in glob.glob("*.mat"):
        print(file.title())
        for task in tasks:
            if task.lower() in file.lower():
                task_num = np.where(np.asarray(tasks) == task)[0][0] + 1
                name = 'sub-' + subject_num + '_ses-01' + '_acq-' + str(task_num) + '_task-' + task + '_eyetrack.mat'
                old_path = path + '/' + file
                new_path = new_dr + '/' + name
                shutil.copy(old_path, new_path)


def directory_to_BIDS(path):
    """
    Converts a directory to BIDS format while maintaining the original directory as [name]_RAW
    :param path: full path to a directory to be converted to BIDS format
    :return: None, creates BIDS-formatted folder in same directory as the raw directory
    """

    # assumes directory is the subject name
    subject_num = os.path.split(path)[1][:6]

    # task names --> need to know if there is a more general way of getting the task names in the right order
    tasks = ['trailer1', 'trailer2', 'Office1', 'Office2', 'Pixar', 'BangDead']

    # make new dr
    new_dr = os.path.split(path)[0] + '/BIDS/' + 'sub-' + subject_num + '/eyetrack/'
    os.makedirs(new_dr)

    BIDS_edf_asc_json(path, new_dr, subject_num, tasks)
    BIDS_mat(path, new_dr, subject_num, tasks)


if __name__ == '__main__':
    path_name = input("Path name: ")
    directory_to_BIDS(path_name)
