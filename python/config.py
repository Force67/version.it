# Copyright (C) 2022 Vincent Hengel.
# For licensing information see LICENSE at the root of this distribution.
import yaml

from enum import Enum
from logging import getLogger

log = getLogger(__name__)

class VersionScheme(Enum):
  SEMANTIC = 'semantic'
  CALVER = 'calver'
  COMMIT = 'commit'


class ChangeType(Enum):
  MAJOR = 'major'
  MINOR = 'minor'
  PATCH = 'patch'
  IGNORE = None


class Config():
  """Configurations."""

  def __init__(self):
    self._config = {}
    self.run_on_branches = []
    self.version_scheme = VersionScheme.SEMANTIC
    self.first_version = "0.0.0"
    self.change_type_map = {}
    self.changelog_sections = {}
    self.changelog_substitutions = {}
    self.dry_run = False
    self.major_increment = 3
    self.minor_increment = 2
    self.patch_increment = 1
    self.template_path = "examples/templates"
    self.output_path = "examples/outputs"
    self.commit_identity_email = "lovelyforce67@gmail.com"
    self.commit_identity_name = "version-it"

  def load(self, settings):
    self.run_on_branches = settings.get("run-on-branches", [])
    self.version_scheme = VersionScheme(
        settings.get("versioning-scheme", "semantic"))
    self.first_version = settings.get("first-version", "0.0.0")
    self.change_type_map = {
        item["label"]: item["action"]
        for item in settings.get("change-type-map", [])
    }
    self.changelog_sections = {
        item["title"]: item["labels"]
        for item in settings.get("changelog-sections", [])
    }
    self.changelog_substitutions = {
        item["token"]: item["substitution"]
        for item in settings.get("change-substitutions", [])
    }
    changelog_exporters = settings.get("changelog-exporters", {})
    self.output_path = changelog_exporters.get("output-path", "xxx/outputs")
    self.template_path = changelog_exporters.get("template-path", "examples/templates")

  def save(self, settings):
    settings['run-on-branches'] = self.run_on_branches
    settings['versioning-scheme'] = self.version_scheme.value
    settings['first-version'] = self.first_version
    settings['change-type-map'] = {
        label: action for label, action in self.change_type_map.items()
    }
    settings['changelog-sections'] = {
        title: labels for title, labels in self.changelog_sections.items()
    }
    settings['change-substitutions'] = {
        token: substitution
        for token, substitution in self.changelog_substitutions.items()
    }

  def open_file(self):
    filenames = ['version-it.yaml', 'version-it.yml']

    for filename in filenames:
      try:
        with open(filename, 'r', encoding='utf8') as f:
          settings = yaml.safe_load(f)
          self.load(settings)
          return True
      except FileNotFoundError:
        pass
      except IOError as e:
        log.error(f"Couldn't open or read settings file ({e})")
        return False
    log.error("Couldn't find version-it.yaml or version-it.yml")
    return False
