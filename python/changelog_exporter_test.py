# Copyright (C) 2022 Vincent Hengel.
# For licensing information see LICENSE at the root of this distribution.
import config
import change
import changelog_exporter


def test_changelog_exporter():
  config_instance = config.Config()
  exporter = changelog_exporter.ChangelogExporter(config_instance, "1.0.0", "https://github.com/Force67/version.it.git")

  changes = []
  changes.append(
      change.Change(config.ChangeType.PATCH, "tweak", "Changed", "ahahahaha", "2023-01-19", "Vincent Van Gogh",
                    "Added a new feature"))
  changes.append(
      change.Change(config.ChangeType.PATCH, "fix", "Fixed", "ababababab", "2023-01-19", "Monet",
                    "Fixed the painting"))
  changes.append(
      change.Change(config.ChangeType.PATCH, "bug", "Fixed", "acacacacac", "2023-01-19", "Picasso",
                    "The painting is broken"))
  changes.append(
      change.Change(config.ChangeType.MINOR, "feature", "Added", "adadadadad", "2023-01-19", "Van Gogh",
                    "Added a new feature"))
  changes.append(
      change.Change(config.ChangeType.PATCH, "tweak", "Changed", "aeaeaeaeae", "2023-01-19", "Van Gogh",
                    "Tweaked a feature"))

  exporter.export(changes)
  assert True
