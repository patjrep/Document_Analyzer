import Modules
import config


class MainApp():
    reader = Modules.FileDiscovery(config.DIRECTORIES)
    parsed_files = Modules.FileParser()
    print(parsed_files)
    for file in reader.get_files():
        print(file)
