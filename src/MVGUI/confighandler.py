import yaml

class Confighandler:

    def get_config_data(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

ch = Confighandler()
data = ch.get_config_data("test_config_2.yaml")


categories = []
type_list = data["Pivot Bearing"]["TypeList"]
print(type_list)
values = {}
validCallback = {}
min_threshold = {}
max_threshold = {}
#for cat in categories:
#    for typ in type_list:
#        min_threshold[cat] = data[typ][cat]["Range"]["min"]
#        print(min_threshold)
#        max_threshold[cat] = data[typ][cat]["Range"]["max"]

for typ in type_list:
    categories = data[typ].keys()
    for cat in categories:
        min_threshold[cat] = data[typ][cat]["Range"]["min"]
        max_threshold[cat] = data[typ][cat]["Range"]["max"]


for key, value in min_threshold.items():
    print(f"Key: {key} Value: {value}")
