# Troubleshooting

## Absence of Tags

If you encounter an error message that reads "no names found, cannot describe anything", it implies that you need to fetch the tags from the remote:

```bash
git fetch --tags
```

Another potential reason for this issue could be that you haven't tagged anything yet; thus, there is no tag available for comparison. In this situation, you can generate your first tag:

```bash
git tag -a v0.0.0 -m "Initial version"
```
