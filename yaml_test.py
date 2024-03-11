import yaml


with open('yaml_test.yaml', 'r') as f:
    conf = yaml.safe_load(f)


print(conf)
