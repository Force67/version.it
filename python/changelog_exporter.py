from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from jinja2.visitor import NodeVisitor
from logging import getLogger
from ai_summary import AISummary

import config

log = getLogger(__name__)


class TemplateVariableFinder(NodeVisitor):
  """Visitor class to find variables in Jinja2 templates."""

  def __init__(self):
    self.variable_names = set()
    self.output_filename = None
    self.optional_prompt = None

  def visit_Name(self, node):
    self.variable_names.add(node.name)

  def visit_Assign(self, node):
    if hasattr(node, 'target') and hasattr(
        node.target, 'name') and node.target.name == 'output_filename':
      self.output_filename = node.node.value
    if hasattr(node, 'target') and hasattr(
        node.target, 'name') and node.target.name == 'gpt_prompt':
      self.optional_prompt = node.node.value


class ChangelogExporter:
  """Exporter factory"""

  def __init__(self, config_instance, version, repo_url, gpt_token=None):
    self.template_path = Path(config_instance.template_path).resolve()
    self.output_path = Path(config_instance.output_path).resolve()
    self.config = config_instance
    self.version = version
    self.repo_url = repo_url
    self.gpt_token = gpt_token
    self.generated_files = []
    self.env = Environment(loader=FileSystemLoader(str(self.template_path)))

  def get_generated_files(self):
    return self.generated_files

  def _parse_template(self, template_file):
    """Parse Jinja2 template and return a set of variable names."""

    try:
      with open(template_file, encoding='utf-8') as f:
        template_string = f.read()
      parsed_template = self.env.parse(template_string)
      visitor = TemplateVariableFinder()
      visitor.visit(parsed_template)
      return visitor.output_filename, visitor.optional_prompt
    except Exception as e:
      print(f"Error parsing template {template_file}: {e}")
      return None

  def _apply_substitutions(self, message):
    """Apply changelog substitutions to the message."""

    for key, value in self.config.changelog_substitutions.items():
      message = message.replace(key, value)
    return message

  def _render_template(self, template_file_name, output_filepath, changeset, optional_prompt=None):
    """Render the Jinja2 template and save the output to a file."""

    template_name = template_file_name.name
    template = self.env.get_template(template_name)

    kwargs = {
        'version': self.version,
        'changes': changeset,
        'repo_url': self.repo_url,
        'version_scheme': self.config.version_scheme,
        'VersionScheme': config.VersionScheme
    }

    if self.config.version_scheme == config.VersionScheme.SEMANTIC:
      kwargs['major_version'] = self.version.split('.')[0]
      kwargs['minor_version'] = self.version.split('.')[1]
      kwargs['patch_version'] = self.version.split('.')[2]

    if self.config.version_scheme == config.VersionScheme.CALVER:
      kwargs['year'] = self.version.split('.')[0]
      kwargs['month'] = self.version.split('.')[1]
      kwargs['patch'] = self.version.split('.')[2]
      kwargs['branch'] = self.version.split('.')[3]

    if self.config.version_scheme == config.VersionScheme.COMMIT:
      kwargs['version_number'] = self.version

    if optional_prompt is not None and self.gpt_token is not None:
      summary_builder = AISummary(self.gpt_token)
      summary = summary_builder.summarize_text(optional_prompt, **kwargs)
      log.info("Generated summary for %s", optional_prompt)
      if summary is not None:
        kwargs['ai_summary'] = summary
      else:
        log.error("Failed to generate summary for %s", optional_prompt)

    rendered_template = template.render(**kwargs)

    with output_filepath.open("w", encoding="utf8") as outfile:
      outfile.write(rendered_template)

  def export(self, changeset):
    """Export the changelog for a given changeset."""

    for change in changeset:
      change.message = self._apply_substitutions(change.message)

    template_files = list(self.template_path.glob("*.j2"))
    for template_file in template_files:
      (filename, prompt) = self._parse_template(template_file) # type: ignore
      if filename is None:
        log.warning(
            "Template %s does not contain a variable named 'output_filename'. Skipping.",
            template_file)
        continue
      output_filepath = self.output_path / filename
      self.generated_files.append(output_filepath)
      log.info("Rendering template %s to %s", template_file, output_filepath)
      self._render_template(template_file, output_filepath, changeset, prompt)
