from mypyconf.loader import load, store_to_file, set_to_environment
import unittest
import os
import shutil


class TestMethods(unittest.TestCase):

    def setUp(self):
        if os.path.exists("sample/output"):
            shutil.rmtree("sample/output")
        os.mkdir("sample/output")

    def test_load_yaml_file_not_exist(self):
        try:
            load("sample/sample.yaml")
            assert 1 == 0
        except FileNotFoundError:
            assert 1 == 1

    def test_load_yaml(self):
        data = load("sample/test.yaml")
        assert 1 == 1

    def test_load_cfg(self):
        data = load("sample/test.cfg")
        assert 1 == 1

    def test_load_conf(self):
        data = load("sample/test.conf")
        assert 1 == 1

    def test_load_yaml_store_to_json(self):
        data = load("sample/test.yaml")
        store_to_file(data, "sample/output/test1.json")
        assert 1 == 1

    def test_load_yaml_store_to_file__exist(self):
        try:
            data = load("sample/test.yaml")
            store_to_file(data, "sample/output/test1.json")
            data = load("sample/test.cfg")
            store_to_file(data, "sample/output/test1.json")
            assert 1 == 0
        except FileExistsError:
            assert 1 == 1

    def test_load_yaml_store_even_if_file_exist(self):
        try:
            data = load("sample/test.yaml")
            store_to_file(data, "sample/output/test1.json")
            data = load("sample/test.cfg")
            store_to_file(data, "sample/output/test1.json", if_exist_ok=True)
            assert 1 == 1
        except FileExistsError:
            assert 1 == 0

    def test_load_config_store_to_json(self):
        data = load("sample/test.cfg")

        store_to_file(data, "sample/output/test2.json")
        assert 1 == 1

    def test_load_yaml_store_to_env_file(self):
        data = load("sample/test.yaml")
        
        store_to_file(data, "sample/output/test1.env")
        assert 1 == 1

    def test_load_config_store_to_env_file(self):
        data = load("sample/test.cfg")
        store_to_file(data, "sample/output/test2.env")
        assert 1 == 1

    def test_load_config_store_to_os_env(self):
        data = load("sample/test.cfg")
        set_to_environment(data)
        assert 1 == 1

    def test_load_bad_config_cfg(self):
        try:
            load("sample/bad_test.cfg")
            assert 1 == 0
        except Exception as err:
            assert err.__str__() == "Unable to parse the file"

    def test_load_bad_config_yaml(self):
        try:
            load("sample/bad_test.yaml")
            assert 1 == 0
        except Exception as err:
            assert err.__str__() == "Unable to parse the file"

    def test_can_not_dir_path(self):
        try:
            load("sample")
            assert 1 == 0
        except Exception as err:
            assert err.__str__() == "File path is targeting to directory. Only file path are allowed"

    def test_can_not_load_text(self):
        try:
            load("sample/test.txt")
            assert 1 == 0
        except Exception as err:
            assert err.__str__() == "File format not supported"

    def test_can_not_save_other_then_dict(self):
        try:
            store_to_file( [1], "sample/test.json")
            assert 1 == 0
        except Exception as err:
            assert err.__str__() == "Only Dict is allowed"

    def test_can_not_save_to_another_format(self):
        try:
            store_to_file({
                1: 1
            }, "sample/test.text")
            assert 1 == 0
        except Exception as err:
            assert err.__str__() == "Output File format not supported"

    def test_can_get_exact_all_keys_for_cfg(self):
        try:
            data = {
                "mysqld" : {
                    "user": 0,
                    "pid-file": 0,
                    "skip-external-locking": 0,
                    "old_passwords": 0,
                    "skip-bdb": 0,
                    "skip-innodb": 0,
                }
            }
            output = load("sample/test.cfg")

            assert data.keys().__len__() ==  output.keys().__len__()
            assert data['mysqld'].keys().__len__() == output['mysqld'].keys().__len__()

        except Exception as err:
            print(err)
            assert 1 == 0

    def test_can_get_exact_all_keys_for_yaml(self):
        try:
            data = {
                "instance" : {
                    "Id" : 0 ,
                    "environment" : 0 ,
                    "serverId" : 0 ,
                    "awsHostname" : 0 ,
                    "serverName" : 0 ,
                    "ipAddr" : 0 ,
                    "roles" : 0 ,
                }
            }
            output = load("sample/test.yaml")

            assert data.keys().__len__() ==  output.keys().__len__()
            assert data['instance'].keys().__len__() == output['instance'].keys().__len__()

        except Exception as err:
            print(err)
            assert 1 == 0

    def test_set_environment(self):
        try:
            data = {
                "my_variable" : 100
            }
            set_to_environment(data)
            assert os.environ.get('my_variable') == "100"
        except Exception as err:
            print(err)
            assert 1 == 0

    def test_set_environment_None(self):
        try:
            data = {
                "my_variable" : None
            }

            set_to_environment(data)
            assert os.environ.get('my_variable') == "null"
        except Exception as err:
            print(err)
            assert 1 == 0

    def test_set_non_dict_object_to_environment(self):
        try:
            data = [1]
            set_to_environment(data)
            assert  1 == 0

        except Exception as err:
            assert err.__str__() == "Only Dict is allowed"













