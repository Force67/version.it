"""
Versionizer: A script to automate versioning and changelog generation.
Copyright (C) 2022 Vincent Hengel.
For licensing information see LICENSE at the root of this distribution.
"""

import os
import sys
import config
from urllib.parse import urlparse

from logging import getLogger, basicConfig, INFO

import change
import changelog_exporter
import git_queries as vcs
import version_builder


class Versionizer:
  """Main Application class."""

  def __init__(self):
    self.config = config.Config()
    basicConfig(level=INFO)
    self.log = getLogger(__name__)
    self.vcs = vcs.GitRepo()

  def collect_history(self):
    tagged_changes = self.vcs.get_tagged_commits()
    if not tagged_changes:
      self.log.error("Couldn't get tagged commits")
      return None
    # newest commits are first, oldest last.
    history = self.vcs.pretty_full_history()
    if not history:
      self.log.error("Couldn't get commit history")
      return None

    # we mark any new commit, as None, these will be versionized.
    versioning_tag = None
    change_list = []
    for line in history.splitlines():
      if line.startswith("Merge"):
        continue
      parts = self.vcs.parse_commit(line)
      if not parts:
        continue
      (commit_hash, date, author, commit_group, message) = parts
      # we retain the tag of the last commit in the group for the following changelog not in the tag change map
      for tag_item in tagged_changes:
        if commit_hash == tag_item[1]:
          versioning_tag = tag_item[0]
          break

      change_type = config.ChangeType.IGNORE
      for key, value in self.config.change_type_map.items():
        if key in commit_group:
          change_type = config.ChangeType(value)
          break
      if change_type == config.ChangeType.IGNORE:
        continue

      # prevent the chore being added to the history however!
      if message.startswith("chore"):
        continue

      change_list.append(
          change.Change(change_type, versioning_tag, commit_group, commit_hash,
                        date, author, message))
    return change_list

  def exec(self):
    if not self.config.open_file():
      self.log.error("Couldn't load config")
      return
    
    is_dry_run = sys.argv.count("dry-run") > 0
    is_ai_summary = sys.argv.count("ai-summary") > 0
    
    access_token = os.getenv('GITHUB_TOKEN')
    if access_token is None and not is_dry_run:
      self.log.error("No GITHUB_TOKEN environment variable set")
      return
    
    gpt_token = os.getenv('GPT_TOKEN')
    if gpt_token is None and is_ai_summary:
      self.log.error("No GPT_TOKEN environment variable set. Needed for AI summary")
      return

    current_branch = self.vcs.current_branch()
    if current_branch not in self.config.run_on_branches:
      return

    current_tag = self.vcs.current_tag()
    if not current_tag:
      self.log.error("Couldn't get current tag")
      return None

    changes = self.collect_history()
    if not changes:
      self.log.error("Couldn't collect history")
      return None

    builder = version_builder.VersionBuilder(self.config, self.vcs, changes)
    new_tag = builder.build(current_tag)
    if not new_tag:
      self.log.error("Couldn't build new tag")
      return None

    for c in changes:
      if c.version is None:
        c.version = new_tag

    self.log.info("Old tag %s, New tag %s" % (current_tag, new_tag))

    if current_tag == new_tag:
      self.log.info("No changes, skipping tag")
      return

    repo_url = self.vcs.repo_url()
    exporter = changelog_exporter.ChangelogExporter(self.config, new_tag,
                                                    repo_url, gpt_token)
    exporter.export(changes)
    self.log.info("Changelog exported")

    if not is_dry_run and self.config.dry_run is False and access_token is not None:
      self.vcs.commit_changelog(
          exporter.get_generated_files(),
          f"chore(version.it): Roll from {current_tag} to {new_tag}", new_tag,
          self.config.commit_identity_name, self.config.commit_identity_email, access_token)


def main():
  v = Versionizer()
  v.exec()


if __name__ == "__main__":
  main()
