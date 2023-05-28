# Copyright (C) 2022 Vincent Hengel.
# For licensing information see LICENSE at the root of this distribution.


# changes dont need a version key since they are part of a new change revision.
class Change:
  """Most similar to the concept of a git commit. A change is a single change to the codebase"""

  def __init__(self, change_type, version_tag, display_group, change_hash, date,
               author, message):
    self.type = change_type
    self.version = version_tag
    self.group = display_group    # what gets written in the changelog
    self.hash = change_hash
    self.date = date
    self.author = author
    self.message = message

  # this is required for the AI context retrieval
  def __str__(self):
    return f"Change(type={self.type}, message={self.message})"
