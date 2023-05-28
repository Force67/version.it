# 🚀 Version.it - Software Versioning with changelog generation

Version.it should live in your CI pipeline and will automatically generate a new version number and changelog for each release. It supports a variety of versioning formats, including Semantic, Calendar, and Commit-based versioning. You can also customize the appearance of your changelogs with jinja templates to match your own style. It will even auto-generate release notes with the help of GPT!

> **Note:** Version.it is currently in beta. I am  actively working on improving the tool and adding new features. If you have any suggestions or feedback, please let us know by opening an issue or submitting a pull request! So don't consider this tool production-ready just yet, its mainly used in projects of mine.

## Main Features of Version.it:
* **Effortless**: No more manual version number updates!
* **Versatile**: Supports a variety of versioning formats (Semantic, Calendar, Commit)
* **Customizable**: Tailor the appearance of your changelogs with jinja templates to match your own style.
* **AI-powered**: Auto-generate release notes with the help of GPT (prompt customizeable via jinja templates)

## 🧪 How Does It Work?

In just a few simple steps, Version.it will:

1. Read the commits between the last tag and the current HEAD.
2. Analyze commit messages to determine the version bump.
3. Generate the changelog in markdown, csv, or json format.
4. Create a new tag and push it to the remote.

## 📚 Documentation

Access our comprehensive documentation [here](./docs/getting_started.md)!

## 🧪 Testing

To run tests, simply execute the following command:

```bash
pytest
```

## 👥 Contributing
We'd love for you to join our mission! All contributions are more than welcome.

## ⚖️ License
GPL-3.0

## 🌍 Who's Using Version-it?
Skyrim Together

...and YOU?