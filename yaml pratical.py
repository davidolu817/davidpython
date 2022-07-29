import pathlib
import yaml

file_path = pathlib.Path("./config.yaml").resolve()
text = {'name': 'David', 'age': 18, 'children': ["Moses", "Ola"]}
with file_path.open(mode="w")as f:
    yaml.dump(text, f, sort_keys=False)

with file_path.open(mode='r', encoding='utf_8') as file:
    text_again = yaml.load(file, Loader=yaml.Loader)

    print(text_again)