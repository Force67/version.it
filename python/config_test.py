import pytest
from unittest.mock import patch, mock_open

from config import Config, VersionScheme, ChangeType


@pytest.fixture
def config():
  return Config()


def test_load(config):
  settings = {
      "run-on-branches": ["main"],
      "versioning-scheme": "calver",
      "first-version": "2022.01.01",
      "change-type-map": [
          {
              "label": "BREAKING",
              "action": ChangeType.MAJOR.value
          },
          {
              "label": "feat",
              "action": ChangeType.MINOR.value
          },
          {
              "label": "fix",
              "action": ChangeType.PATCH.value
          },
      ],
      "changelog-sections": [
          {
              "title": "Features",
              "labels": ["feat"]
          },
          {
              "title": "Bug Fixes",
              "labels": ["fix"]
          },
          {
              "title": "Breaking Changes",
              "labels": ["BREAKING"]
          },
      ],
      "change-substitutions": [
          {
              "token": "##",
              "substitution": "#"
          },
          {
              "token": "<!--",
              "substitution": ""
          },
          {
              "token": "-->",
              "substitution": ""
          },
      ],
      "changelog-exporters": {
          "output-path": "changelog.md",
          "template-path": "templates/changelog.md.j2",
      },
  }

  config.load(settings)

  assert config.run_on_branches == ["main"]
  assert config.version_scheme == VersionScheme.CALVER
  assert config.first_version == "2022.01.01"
  assert config.change_type_map == {
      "BREAKING": ChangeType.MAJOR.value,
      "feat": ChangeType.MINOR.value,
      "fix": ChangeType.PATCH.value,
  }
  assert config.changelog_sections == {
      "Features": ["feat"],
      "Bug Fixes": ["fix"],
      "Breaking Changes": ["BREAKING"],
  }
  assert config.changelog_substitutions == {
      "##": "#",
      "<!--": "",
      "-->": "",
  }
  assert config.output_path == "changelog.md"
  assert config.template_path == "templates/changelog.md.j2"


def test_save(config):
  config.run_on_branches = ["develop"]
  config.version_scheme = VersionScheme.COMMIT
  config.first_version = "1.0.0"
  config.change_type_map = {
      "feat": ChangeType.MINOR.value,
      "fix": ChangeType.PATCH.value,
  }
  config.changelog_sections = {
      "Features": ["feat"],
      "Bug Fixes": ["fix"],
  }
  config.changelog_substitutions = {
      "##": "#",
      "<!--": "",
      "-->": "",
      "deprecated": "obsolete",
  }
  config.output_path = "changelog.md"
  config.template_path = "templates/changelog.md.j2"

  settings = {}
  config.save(settings)

  assert settings == {
      "run-on-branches": ["develop"],
      "versioning-scheme": "commit",
      "first-version": "1.0.0",
      "change-type-map": {
          "feat": ChangeType.MINOR.value,
          "fix": ChangeType.PATCH.value
      },
      "changelog-sections": {
          "Features": ["feat"],
          "Bug Fixes": ["fix"],
      },
      "change-substitutions": {
          "##": "#",
          "<!--": "",
          "-->": "",
          "deprecated": "obsolete",
      },
  }