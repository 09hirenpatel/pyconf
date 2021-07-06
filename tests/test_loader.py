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




