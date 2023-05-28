# Copyright (C) 2022 Vincent Hengel.
# For licensing information see LICENSE at the root of this distribution.
# Build the next possible version from a given scheme.
import re
from datetime import datetime

import config
import git_queries as vcs
from logging import getLogger

class InvalidVersionexception(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return f'{self.__class__.__name__}: {self.message}'


def parse_semantic(version):
  # official regex from semver.org
  match = re.search(
      r'^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$',
      version)
  if not match:
    return None
  return (int(match["major"]), int(match["minor"]), int(match["patch"]),
          match["prerelease"] or "", match["buildmetadata"] or "")


def parse_calver(version):
  mo = re.match(r'^(\d{2,4})\.(\d{2})\.(\d+)(\.[a-zA-Z0-9]+)?$', version)
  if not mo:
    return None
  year = mo.group(1)
  month = mo.group(2)
  patch = mo.group(3)
  branch = mo.group(4) or ""
  return (int(year), int(month), int(patch), branch)


class VersionBuilder:
  """Increments the version based on the content of the supplied changes"""

  def __init__(self, config_instance, vcs_instance, change_list):
    self.cfg = config_instance
    self.changes = change_list
    self.log = getLogger(__name__)
    self.vcs = vcs_instance

  def build(self, old_version):
    if self.cfg.version_scheme == config.VersionScheme.SEMANTIC:
      return self.advance_semantic_version(old_version)
    elif self.cfg.version_scheme == config.VersionScheme.CALVER:
      return self.advance_calver(old_version, datetime.now())
    elif self.cfg.version_scheme == config.VersionScheme.COMMIT:
      return self.advance_commitver(old_version)
    else:
      raise InvalidVersionexception("Invalid version scheme.")

  def advance_semantic_version(self, old_version):
    version_bits = parse_semantic(old_version)
    if version_bits is None:
      self.log.error(
          "Couldn't parse semantic version. A semantic version should be in the form of MAJOR.MINOR.PATCH[-PRERELEASE][+BUILDMETADATA]"
      )
      return

    major, minor, patch, prerelease, buildmetadata = version_bits
    for c in self.changes:
      if c.version is not None:
        continue
      if c.type == config.ChangeType.MINOR:
        minor += 1
      elif c.type == config.ChangeType.PATCH:
        patch += 1
      # ignore major and NONE changes
    return f"{major}.{minor}.{patch}"

  def advance_calver(self, text, date):
    old_calver = parse_calver(text)
    if old_calver is None:
      self.log.error(
          "Couldn't parse calender version. A calender version should be in the form of YYYY.MM.PATCH[.BRANCH]"
      )
      return
    year, month, patch, branch = old_calver

    year = date.year
    month = date.month
    # for consistencies sake
    if month < 10:
      month = f"0{month}"
    branch = self.vcs.current_branch()

    for c in self.changes:
      if c.version is not None:
        continue
      if c.type == config.ChangeType.MAJOR:
        patch += self.cfg.major_increment
      if c.type == config.ChangeType.MINOR:
        patch += self.cfg.minor_increment
      elif c.type == config.ChangeType.PATCH:
        patch += self.cfg.patch_increment

    return f"{year}.{month}.{patch}.{branch}"

  def advance_commitver(self, text):
    version_number = int(text)
    if version_number is None:
      self.log.error("Couldn't parse commit version. A commit version should be a number.")
      return None
    
    for c in self.changes:
      if c.version is not None:
        continue
      if c.type == config.ChangeType.MAJOR:
        version_number += self.cfg.major_increment
      if c.type == config.ChangeType.MINOR:
        version_number += self.cfg.minor_increment
      elif c.type == config.ChangeType.PATCH:
        version_number += self.cfg.patch_increment
    return str(version_number)
