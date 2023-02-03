## Currently Not-working pytest

import pytest
import yaml
import downloader

class context_one:
    @pytest.fixture
    def parse_context(self):
        return downloader.parse.context # module within parser for certain context

    @pytest.fixture
    def test_yaml_context(self):
        with open('test_yaml.yml') as yaml_file:
            return yaml.load(yaml_file)

    def test_validation_function1(self,parse_context,test_yaml_context):

        test_yaml = test_yaml_context['validation_function1']

        # test that missing key raises error
        with pytest.raises(KeyError):
            parse_context.validation_function1(test_yaml['missing_key_case'])


        # test that invalid value raises error
        with pytest.raises(ValueError):
            parse_context.validation_function1(test_yaml['invalid_value_case'])