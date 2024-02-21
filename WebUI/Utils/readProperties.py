import configparser

class ReadConfig:
    def __init__(self):
        self.config=configparser.RawConfigParser()
        self.config.read(f"WebUI/ConfigurationFiles/ConfigFile.cfg")

    def getApplicationURL(self):
        ui_url=self.config.get('Entries', 'url')
        return ui_url