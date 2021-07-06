from mypyconf.loader import load, store_to_file
from dotenv import load_dotenv
import unittest


class TestStringMethods(unittest.TestCase):
    
    def test_load_yaml(self):
        data = load("sample/test.yaml")
        print(data)
        assert 1 == 1

    def test_load_cfg(self):
        data = load("sample/test.cfg")
        print(data)
        assert 1 == 1

    def test_load_conf(self):
        data = load("sample/test.conf")
        print(data)
        assert 1 == 1

    def test_load_yaml_store_to_json(self):
        data = load("sample/test.yaml")
        print(data)
        store_to_file(data, "sample/test1.json")
        assert 1 == 1

    def test_load_config_store_to_json(self):
        data = load("sample/test.cfg")
        print(data)
        store_to_file(data, "sample/test1.json")
        assert 1 == 1

    def test_load_yaml_store_to_env_file(self):
        data = load("sample/test.yaml")
        print(data)
        store_to_file(data, "sample/test1.env")
        assert 1 == 1

    def test_load_config_store_to_env_file(self):
        data = load("sample/test.cfg")
        print(data)
        store_to_file(data, "sample/test1.env")
        assert 1 == 1




