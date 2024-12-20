# ckan-client-tacc

<div align="center">

[![Build status](https://github.com/in_for_disaster_analytics/ckan-client-tacc/workflows/build/badge.svg?branch=master&event=push)](https://github.com/in_for_disaster_analytics/ckan-client-tacc/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/ckan-client-tacc.svg)](https://pypi.org/project/ckan-client-tacc/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/in_for_disaster_analytics/ckan-client-tacc/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/in_for_disaster_analytics/ckan-client-tacc/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/in_for_disaster_analytics/ckan-client-tacc/releases)
[![License](https://img.shields.io/github/license/in_for_disaster_analytics/ckan-client-tacc)](https://github.com/in_for_disaster_analytics/ckan-client-tacc/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Awesome `ckan-client-tacc` is a Python cli/package created with https://github.com/Undertone0809/python-package-template

</div>

## Installation

```bash
pip install -U ckan-client-tacc
```

or install with `Poetry`

```bash
poetry add ckan-client-tacc
```

Then you can run

```bash
ckan-client-tacc --help
```

or with `Poetry`:

```bash
poetry run ckan-client-tacc --help
```

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/in_for_disaster_analytics/ckan-client-tacc/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/in_for_disaster_analytics/ckan-client-tacc/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/in_for_disaster_analytics/ckan-client-tacc)](https://github.com/in_for_disaster_analytics/ckan-client-tacc/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/in_for_disaster_analytics/ckan-client-tacc/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{ckan-client-tacc,
  author = {In-For-Disaster-Analytics},
  title = {Awesome `ckan-client-tacc` is a Python cli/package created with https://github.com/Undertone0809/python-package-template},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/in_for_disaster_analytics/ckan-client-tacc}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/Undertone0809/python-package-template)

This project was generated with [`python-package-template`](https://github.com/Undertone0809/python-package-template)
