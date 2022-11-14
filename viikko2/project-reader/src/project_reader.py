from urllib import request
from toml import loads
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_content = loads(content)
        project_name = parsed_content["tool"]["poetry"]["name"]
        project_description = parsed_content["tool"]["poetry"]["description"]
        project_dependencies = list(parsed_content["tool"]["poetry"]["dependencies"].keys())
        project_dev_dependencies = list(parsed_content["tool"]["poetry"]["dev-dependencies"].keys())
        return Project(project_name, project_description, project_dependencies, project_dev_dependencies)
