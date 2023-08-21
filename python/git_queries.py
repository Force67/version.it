# Copyright (C) 2022 Vincent Hengel.
# For licensing information see LICENSE at the root of this distribution.

import re
import  os
import subprocess
from pathlib import Path
from git import Repo, Actor
from logging import getLogger, basicConfig, INFO
from urllib.parse import urlparse, urlunparse
from tempfile import NamedTemporaryFile

log = getLogger(__name__)

class GitRepo:
    def __init__(self):
        self.repo = self.get_repo()

    def get_repo(self):
        try:
            repo = Repo()
            if repo.bare:
                log.error("Not a git repository")
                return None
            return repo
        except Exception as e:
            log.error(f"Unable to find a git repository: {e}")
            return None

    def current_tag(self):
      if not self.repo:
          return None
      tags = self.repo.tags
      if len(tags) == 0:
          return None
      latest_tag = max(tags, key=lambda t: t.commit.committed_date, default=None)
      if latest_tag is None:
          return None
      return str(latest_tag)

    def advance_version_and_commit(self, version):
        if not self.repo:
            return
        self.repo.create_tag(version, message=f"Version {version}")
        self.repo.remotes.origin.push(self.repo.head)
        self.repo.remotes.origin.push(version)

    def pretty_commit_history(self, former_tag):
        if not self.repo:
            return None
        return self.repo.git.log(former_tag + "..HEAD", pretty="format:%H %ad %an %s", date="short")

    def pretty_commit_history_with_tags(self):
        if not self.repo:
            return None
        return self.repo.git.log("--no-walk", "--tags", pretty="format:%H %ad %an %s", date="short", decorate="full")

    def pretty_full_history(self):
        if not self.repo:
            return None
        return self.repo.git.log(pretty="format:%H %ad %an %s", date="short")

    def list_tags(self):
        if not self.repo:
            return None
        return [str(tag) for tag in self.repo.tags]

    # this regex matches the format specified above! keep it in sync!
    def parse_commit(self, text):
      #parts = re.match(r"^([a-f0-9]{40}) (\d{4}-\d{2}-\d{2}) ([A-Za-z\s]+) (\w+:|\w+\(.+\):) (.+)$", text)
      #parts = re.match(r"^([a-f0-9]{40}) (\d{4}-\d{2}-\d{2}) ([A-Za-z\s-]+) (\w+:|\w+\(.+\.:) (.+)$", text)
      parts = re.match(r"^([a-f0-9]{40}) (\d{4}-\d{2}-\d{2}) ([A-Za-z\s-]+) (\w+:|\w+\(.+\):) (.+)$", text)
      if not parts:
        #log.warning("Couldn't parse commit message: (" + text +
        #      ") It might be missing the commit type. (e.g. feat: or fix:)")
        return None

      commit_hash = parts.group(1)
      date = parts.group(2)
      author = parts.group(3)
      commit_group = parts.group(4).strip(':')
      message = parts.group(5)
      return commit_hash, date, author, commit_group, message

    def get_tagged_commits(self):
        if not self.repo:
            return None
        tagged_history = self.repo.git.log("--tags", pretty="format:%d %H", date="short")
        collection = []
        for line in tagged_history.splitlines():
          line = line.strip() # remove leading and trailing whitespace
          parts = re.match(r"\(tag: ([\d\w\.]+)\) ([a-f\d]{40})", line)
          if not parts:
            continue
          tag = parts.group(1)
          commit_hash = parts.group(2)
          collection.append((tag, commit_hash))
        return collection
        # ... (same as before)

    def repo_url(self):
        url = self.repo.remotes.origin.url
        if url.endswith('.git'):
            return url[:-4]
        return url


    def current_branch(self):
        if not self.repo:
            return None
        return self.repo.active_branch.name

    def current_commit(self):
        if not self.repo:
            return None
        return str(self.repo.head.commit)
    
    def commit_changelog(self, filenames, message, new_tag, author_name, author_email, access_token):
        if not self.repo:
            return

        url = self.repo_url()

        # TODO(Fixeme): this right now assumes a github.com URL
        parsed_url = urlparse(url)

        # Extract the netloc, which contains the username
        path_parts = parsed_url.path.split('/')
        username = path_parts[1] if len(path_parts) > 1 else ""

        url = url.replace("https://", f"https://{username}:{access_token}@")
        url += ".git"

        # Get the absolute path of the repository's working directory
        repo_path = Path(self.repo.working_dir).resolve()

        # Stage the changes
        subprocess.run(["git", "add"] + filenames, cwd=repo_path, check=True, stderr=subprocess.STDOUT)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", message, "--author", f"{author_name} <{author_email}>"], cwd=repo_path, check=True, stderr=subprocess.STDOUT)

        # Create a new tag
        subprocess.run(["git", "tag", "-a", new_tag, "-m", f"Version {new_tag}"], cwd=repo_path, check=True, stderr=subprocess.STDOUT)

        # Push the changes and the new tag directly to the specified URL
        current_branch = self.repo.active_branch.name
        subprocess.run(["git", "push", url, f"{current_branch}:refs/heads/{current_branch}", f"{new_tag}:refs/tags/{new_tag}"], cwd=repo_path, check=True, stderr=subprocess.STDOUT)
