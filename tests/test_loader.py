from mypyconf.loader import load, store_to_file, set_to_enviornment
from dotenv import load_dotenv
import unittest


class TestStringMethods(unittest.TestCase):

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
        store_to_file(data, "sample/test1.json")
        assert 1 == 1

    def test_load_config_store_to_json(self):
        data = load("sample/test.cfg")
        
        store_to_file(data, "sample/test1.json")
        assert 1 == 1

    def test_load_yaml_store_to_env_file(self):
        data = load("sample/test.yaml")
        
        store_to_file(data, "sample/test1.env")
        assert 1 == 1

    def test_load_config_store_to_env_file(self):
        data = load("sample/test.cfg")
        store_to_file(data, "sample/test1.env")
        assert 1 == 1

    def test_load_config_store_to_os_env(self):
        data = load("sample/test.cfg")
        set_to_enviornment(data)
        assert 1 == 1




