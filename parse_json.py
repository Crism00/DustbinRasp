import json

class ParseJson:
    def __init__(self, path_name="sensors"):
        self.file_path = 'dumps/'+path_name+'_failed_dumps.json'

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except Exception:
            self.write([])
            return []

    def write(self, data):
        with open(self.file_path, 'w+') as f:
            json.dump(data, f)
