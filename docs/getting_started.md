For information on how to get started, refer to the version-it.yml file in this repository or consult the documentation found here: [here](../docs/configuration.md.md).

# Preparing Git for Use

Firstly, manually assign a tag to your current commit. This will serve as the starting point for the versioning tool.
> Please note that the tag must adhere to the versioning scheme you intend to use with the tool; otherwise, the tool will not be able to parse it.

```bash
git tag -a v0.0.0 -m "Initial version"
```

Subsequently, push the tag to the remote:

```bash
git push origin v0.0.0
```

Finally, indicate the version you've just tagged by setting the first-version attribute in the version-it.yml file. This will be the versioning tool's starting point, and the next tag will be generated based on this, assuming your versioning scheme is compatible.

# Configuring your Git Repository on Github

![alt text](https://i.imgur.com/Z0XaoVE.png)

And:

![alt text](https://i.imgur.com/TQ5qedr.png)

# Establishing Your Release Note Template

The version-it file outlines general information, including the versioning algorithm to use and where to locate the files to be versioned. The changelogs are produced from Jinja templates; a selection of them can be found here: [here](../examples/templates/)

# Further Reading:

- [About configuration](../docs/configuration.md)
- [About utilizing ChatGPT to enhance changelogs](../docs/ai_summary.md)
- [Troubleshooting steps](../docs/troubleshooting.md)
- [Understanding how the versioning schemes function](../docs/versioning_schemes.md)
