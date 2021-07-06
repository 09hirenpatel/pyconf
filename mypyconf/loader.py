import os
import yaml
import configparser
import json


def load(filename):
    if os.path.exists(filename):
        name, extension = os.path.splitext(filename)
        if extension == ".yaml" or extension == ".yml":
            with open(filename, 'r') as file:
                return yaml.load(file, Loader=yaml.FullLoader)
        elif extension == ".cfg" or extension == ".conf":
            config = configparser.RawConfigParser(allow_no_value=True)
            config.read(filename)
            return {s: dict(config.items(s)) for s in config.sections()}
        else:
            raise Exception("Output file format not supported")
    else:
        raise FileNotFoundError


def store_to_file(obj, outfile):
    if type(obj) != dict:
        raise Exception("Only Dict is allowed")
    if not os.path.exists(outfile) or True:
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
        raise FileExistsError


def set_to_enviornment(obj):
    for i in obj.keys():
        os.environ[i] = json.dumps(obj[i])