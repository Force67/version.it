import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime
from config import Config, VersionScheme, ChangeType
from version_builder import VersionBuilder, InvalidVersionexception


class MockVcs():

  def current_branch(self):
    return "master"


def test_advance_semantic_version():
  config_instance = MagicMock(major_increment=1,
                              minor_increment=1,
                              patch_increment=1)
  changes = [
      MagicMock(type=ChangeType.MINOR, version=None),
      MagicMock(type=ChangeType.PATCH, version=None)
  ]
  builder = VersionBuilder(config_instance, MockVcs(), changes)
  old_version = '1.0.0'
  new_version = builder.advance_semantic_version(old_version)
  print(new_version)
  assert new_version == '1.1.1'

  old_version = '1.0.0-alpha'
  new_version = builder.advance_semantic_version(old_version)
  assert new_version == '1.1.1'

  old_version = '1.0.0-alpha'
  new_version = builder.advance_semantic_version(old_version)
  assert new_version == '1.1.1'


def test_advance_calver():
  config_instance = MagicMock(major_increment=1,
                              minor_increment=1,
                              patch_increment=1)
  changes = [
      MagicMock(type=ChangeType.MAJOR, version=None),
      MagicMock(type=ChangeType.MINOR, version=None),
      MagicMock(type=ChangeType.PATCH, version=None)
  ]
  builder = VersionBuilder(config_instance, MockVcs(), changes)
  old_version = '2022.01.01.master'

  new_version = builder.advance_calver(old_version, datetime(2023, 1, 1))
  print(new_version)
  assert new_version == '2023.01.4.master'


def test_advance_commitver():
  config_instance = MagicMock(major_increment=3,
                              minor_increment=2,
                              patch_increment=1)
  changes = [
      MagicMock(type=ChangeType.MAJOR, version=None),
      MagicMock(type=ChangeType.MINOR, version=None),
      MagicMock(type=ChangeType.PATCH, version=None)
  ]
  builder = VersionBuilder(config_instance, MockVcs(), changes)
  old_version = '10'
  new_version = builder.advance_commitver(old_version)
  assert new_version == '16'

  old_version = '10'
  changes = [
      MagicMock(type=ChangeType.MINOR, version=None),
      MagicMock(type=ChangeType.PATCH, version=None)
  ]
  builder = VersionBuilder(config_instance, MockVcs(), changes)
  new_version = builder.advance_commitver(old_version)
  assert new_version == '13'

  old_version = '10'
  changes = [MagicMock(type=ChangeType.PATCH, version=None)]
  builder = VersionBuilder(config_instance, MockVcs(), changes)
  new_version = builder.advance_commitver(old_version)
  assert new_version == '11'


def test_build():
  config_instance = MagicMock(version_scheme=VersionScheme.SEMANTIC)
  changes = [
      MagicMock(type=ChangeType.MINOR, version=None),
      MagicMock(type=ChangeType.PATCH, version=None)
  ]
  builder = VersionBuilder(config_instance, MockVcs(), changes)
  old_version = '1.0.0'
  builder.advance_semantic_version = MagicMock(return_value='1.1.1')
  with patch('version_builder.parse_semantic', return_value=(1, 0, 0, '', '')):
    new_version = builder.build(old_version)
  assert new_version == '1.1.1'

  config_instance = MagicMock(version_scheme=VersionScheme.CALVER)
  changes = [
      MagicMock(type='minor', version=None),
      MagicMock(type='patch', version=None)
  ]
  builder = VersionBuilder(config_instance, MockVcs(), changes)
