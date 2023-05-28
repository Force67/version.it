# Updating Changelog with Jinja Templates 

You can now specify your preferred changelog exporter using Jinja templates in the `.version-it` file. Each commit in the changelog can be customized using different tokens. These tokens are:

- `{{version}}` - The new version number
- `{{hash}}` -  The commit hash
- `{{date}}` - The date of the commit
- `{{author}}` - The author of the commit
- `{{group}}` - The group of the commit (i.e., tweak, feature, bug, etc.)
- `{{message}}` - The commit message
- `{{url}}` - The URL of the commit in the source repository

> **Note:** You *MUST* include this bit: `{%- set output_filename = 'cheader_template.h' -%}` in your template to tell the exporter where to place the generated file.

## Customizing Commit Structure

You can modify the format of each commit written to the changelog. An example of a Jinja template for a C++ header file is shown below:

```jinja
{%- set output_filename = 'cheader_template.h' -%}
#ifndef VERSION_IT_INCLUDE_GUARD
#define VERSION_IT_INCLUDE_GUARD
#define VERSION_IT_VERSION "{{ version }}"

{%- if version_scheme == VersionScheme.SEMANTIC %}
#define VERSION_IT_USING_SEMANTIC_VERSIONING
#define VERSION_IT_MAJOR {{ major_version }}
#define VERSION_IT_MINOR {{ minor_version }}
#define VERSION_IT_PATCH {{ patch_version }}
{%- endif %}

#ifdef __cplusplus
namespace version_it
{
  {%- if version_scheme == VersionScheme.SEMANTIC %}
  constexpr const char kVersionString[] = "{{ version }}";
  constexpr int major = {{ major_version }};
  constexpr int minor = {{ minor_version }};
  constexpr int patch = {{ patch_version }};
  {%- endif %}
}
#endif

#ifdef __cplusplus
namespace version_it
{
  static inline const char* kChangelogEntries[{{ changes|length }}] =
  {
    {%- for change in changes %}
    "{{ change.message }}"{%- if not loop.last %},{%- endif %}
    {%- endfor %}
  };
}
#endif
{% for change in changes %}
// {{ change.version }} {{ change.group }} {{ change.hash }} {{ change.date }} {{ change.author }} {{ change.message -}}
{% endfor %}
#endif
```

This template generates a C++ header file that contains version information and a list of changelog entries. 