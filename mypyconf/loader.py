import os
import yaml
import configparser
import json


def load(filename):
    if os.path.exists(filename):
        if os.path.isfile(filename):
            name, extension = os.path.splitext(filename)
            if extension == ".yaml" or extension == ".yml":
                with open(filename, 'r') as file:
                    try:
                        return yaml.load(file, Loader=yaml.FullLoader)
                    except Exception as err:
                        raise Exception("Unable to parse the file")
            elif extension == ".cfg" or extension == ".conf":
                config = configparser.RawConfigParser(allow_no_value=True)
                try:
                    config.read(filename)
                except Exception as err:
                    raise Exception("Unable to parse the file")
                return {s: dict(config.items(s)) for s in config.sections()}
            else:
                raise Exception("File format not supported")
        else:
            raise Exception("File path is targeting to directory. Only file path are allowed")
    else:
        raise FileNotFoundError


def store_to_file(obj, outfile, if_exist_ok = False):
    if type(obj) != dict:
        raise Exception("Only Dict is allowed")

    if if_exist_ok:
        if os.path.exists(outfile):
            if os.path.isfile(outfile):
                os.remove(outfile)
            else:
                raise Exception("Output file is directory path")
    if not os.path.exists(outfile):
        os.makedirs(os.path.dirname(outfile), exist_ok = True)
        name, extension = os.path.splitext(outfile)
        if extension.lower() == ".json":
            with open(outfile, "w") as f:
                json.dump(obj, f)

        elif extension.lower() == ".env":
            with open(outfile, "w") as f:
                output = ""
                for i in obj.keys():
                    v = obj[i]
                    output = output + "{}={v},\n".format(i, v = v)
                f.write(output)
        else:
            raise Exception("Output File format not supported")
    else:
        if os.path.isfile(outfile):
            raise FileExistsError
        else:
            raise Exception("Output file is directory path")


def set_to_environment(obj):
    if type(obj) != dict:
        raise Exception("Only Dict is allowed")

    for i in obj.keys():
        os.environ[i] = json.dumps(obj[i])