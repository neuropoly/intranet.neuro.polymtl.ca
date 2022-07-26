# Contributing Guidelines

## Introduction <a href="introduction" id="introduction"></a>

First off, thanks for taking the time to contribute to one of **NeuroPoly**'s projects! 🎉

This set of guidelines provides general instruction on how to make any one of the following contributions:

* Submitting a bug report or feature request (See: [Opening an Issue](#opening-an-issue-on-github))
* Fixing a bug or developing a feature (See: [Developing](#developing-code) and [Submitting a Pull Request](#submitting-a-pull-request))

## Project-Specific Guidance

In addition to these general guidelines, several of **NeuroPoly**'s projects also have a GitHub Wiki for [internal developer documentation](https://www.danclarke.com/internal-developer-documentation) to provide **project-specific** guidance:

| Repo                | Wiki                                                                        | Contributing                                                                                                                                                                                                                                                                                 |
| ------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AxonDeepSeg         | [GitHub Wiki](https://github.com/neuropoly/axondeepseg/wiki)                | [CONTRIBUTING](https://github.com/neuropoly/axondeepseg/blob/master/CONTRIBUTING.rst)                                                                                                                                                                                                    |
| IVADOMED            | [GitHub Wiki](https://github.com/ivadomed/ivadomed/wiki)                    | [CONTRIBUTING](https://ivadomed.org/contributing.html)                                                                                                                                                                                            |
| qMRLab              | [GitHub Wiki](https://github.com/qMRLab/qMRLab/wiki)                        | [CONTRIBUTING](https://github.com/qMRLab/qMRLab/blob/master/CONTRIBUTING.md)                                                                                                                                                                                                              |
| Shimming Toolbox    | [GitHub Wiki](https://github.com/shimming-toolbox/shimming-toolbox-py/wiki) | [CONTRIBUTING](https://shimming-toolbox.org/en/latest/contributing/CONTRIBUTING.html) |
| Spinal Cord Toolbox | [GitHub Wiki](https://github.com/neuropoly/spinalcordtoolbox/wiki)          |                                                                                                                                                                                                                                                                                              |

## Opening an Issue on GitHub <a href="opening-an-issue-on-github" id="opening-an-issue-on-github"></a>

Issues (bugs, feature requests, or others) can be submitted on each project's GitHub Issue page. Please take a few seconds to search the issue database in case the issue has already been raised.

When reporting an issue, make sure your installation has not been tempered with (and if you can, update to the latest release, maybe the problem was fixed).

### Issue Title <a href="issue-title" id="issue-title"></a>

Try to have a self-descriptive, meaningful issue title, summarizing the problem you see.

Examples:

* _Installation failure: problem creating launchers_
* _Crashes during image cropping_
* _Add a special mode for multi-class segmentation_

### Issue Body <a href="issue-body" id="issue-body"></a>

**Describe** the issue and mention the project version and OS that you are using.

If you experience an error, copy/paste the Terminal output (include your syntax) and please follow these guidelines for clarity:

* If there are < 10 lines of text, embed it directly in your comment in GitHub. Use ` ```<CODE HERE>``` ` to format as code.
* If there are 10+ lines, either use an external website such as [pastebin](https://pastebin.com) (copy/paste your text and include the URL in your comment), or use [collapsible Github markdown capabilities​](https://gist.github.com/ericclemmons/b146fe5da72ca1f706b2ef72a20ac39d#using-details-in-github).

> **Important**
>
> Provide steps to **reproduce** the issue. First, try to reproduce your issue using publicly-available data. If the error is data-specific, upload a zipped version of the data directly into GitHub (not the full dataset, only what's required to be able to reproduce the error).

Add useful information such as screenshots, etc.

If you submit a feature request, provide a _usage scenario_, imagining how the feature would be used (ideally inputs, a sequence of commands, and a desired outcome). Also provide references to any theoretical work to help the reader better understand the feature.

### Issue Labels <a href="issue-labels" id="issue-labels"></a>

#### Mandatory Labels

The following labels are **mandatory** for issues, as they help with triaging and project management:

| Label Type            | Description                                                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Category**          | Choose **one** label that describes the category of issue. (Colour: Dark purple with white text)                                       |
| **Context**           | Choose one or multiple labels corresponding to the area of the codebase affected by the changes. (Colour: Light purple with dark text) |
| **Priority**          | Choose **one** of the three priority labels (high, medium, low) describing the urgency of the issue.                                   |
| **Version Milestone** | Groups issues and PRs by release. Each project should always have an open milestone that corresponds to the next upcoming release.     |

#### Optional (Recommended) Labels

The following labels are **strongly recommended** for issues whenever appropriate, as they help with triaging and project management:

| Label Type            | Description                                                                                                                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Scope**             | If an issue is either a very simple or very complex task, it may be particularly suited for certain kinds of contributors, so you should add either the "good first issue", "good internship project", or "epic" labels to draw attention to the task. |
| **Design Discussion** | If your issue involves a hypothetical feature or change that needs further input to pin down the design, add the "needs-discussion" label.                                                                                                             |
| **Upstream**          | If your issue is caused by third-party packages or services used by SCT, add the "upstream" label.                                                                                                                                                     |
| **Won't Fix**         | If developers have no intention of addressing a request, the `wontfix` label should be added.                                                                                                                                                          |

## Developing Code <a href="developing" id="developing"></a>

### Opening a Branch <a href="opening-a-branch" id="opening-a-branch"></a>

If you are part of the core developer team, you can open a branch directly in this repository. Prefix the branch name with a personal identifier (such as your initials) and a forward slash. If the branch you are working on is in response to an issue, provide the issue number. Add some text that make the branch name meaningful.

For example, if my name is Regina Phalange, and I am working on updating the documentation theme:

```bash
rp/new-theme-for-docs
```

### Branch Conflicts <a href="conflicts" id="conflicts"></a>

Make sure the PR changes are not in conflict with the master branch.

### Code Style <a href="code-style" id="code-style"></a>

Please review your changes for styling issues, clarity, according to the [PEP8 convention](https://www.python.org/dev/peps/pep-0008/). To check your code, there are several options:

* PyCharm has a [code analyzer](https://www.jetbrains.com/help/pycharm/2016.1/code-inspection.html) integrated
* [pyflakes](https://github.com/PyCQA/pyflakes)
* [flake8](https://pypi.org/project/flake8/)
* [pylint](https://www.pylint.org)

Note that the PEP8 convention, particularly line lengths, does not apply to markdown and rst/sphinx documentation files (see below).

Do not address your functional changes in the same commits as any styling clean-up you may be doing on existing code.

### Documentation and Docstrings <a href="documentation-and-docstrings" id="documentation-and-docstrings"></a>

If you are implementing a new feature, update the documentation to describe the feature, and comment the code (things that are not trivially understandable from the code) to improve its maintainability.

Make sure to cite any papers, algorithms or articles that can help understand the implementation of the feature. If you are implementing an algorithm described in a paper, add pointers to the section / steps.

Please use the [Google Style Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

For documentation outside the code itself (e.g. in `Markdown/.md` and `reStructured/sphinx/.rst` files), do not use the vestigial "80 columns" (or any other arbitrary limit) rule; inside a paragraph, instead of using manual line breaks, keep it on one line, and let the text editors dynamically wrap and naturally display those paragraphs based on the user's window width. Those documentation source files are mostly meant to be read online with the rendered HTML versions anyway (i.e. not on with a 80 columns terminal with monospaced fonts on a 640x480 screen).

### Testing <a href="testing" id="testing"></a>

If you are modifying an existing feature, please be sure to run the existing test suite for your project to ensure new bugs have not been introduced.

If you are adding a new feature, please be sure to add accompanying tests which verify your feature is functioning correctly.

In both cases, please refer to the GitHub Wiki for your specific project for testing protocols.

### Licensing <a href="licensing" id="licensing"></a>

Ensure that you are the original author of your changes, and if that is not the case, ensure that the borrowed/adapted code is compatible with the license.

### Committing <a href="committing" id="committing"></a>

#### Commit Titles <a href="commit-titles" id="commit-titles"></a>

Provide a concise and self-descriptive title (avoid > 80 characters). You may "scope" the title using the applicable command name(s), folder or other "module" as a prefix. If a commit is responsible for fixing an issue, post-fix the description with `(fixes #ISSUE_NUMBER)`.

**Examples:**

> testing: add testing function for validation metrics\
> loader: add timer\
> documentation: add slice_axis to the config files\
> model: add HeMIS network

#### Commit Sequences <a href="commit-sequences" id="commit-sequences"></a>

Update your branch to be baseline on the latest master if new developments were merged while you were developing. Please prefer **rebasing** to merging, as explained in [this tutorial](https://coderwall.com/p/7aymfa/please-oh-please-use-git-pull-rebase). Note that if you do rebases after review have started, they will be cancelled, so at this point it may be more appropriate to do a pull.

Clean up your commit sequence. If your are not familiar with git, [this good tutorial](https://www.atlassian.com/git/tutorials/rewriting-history) on the subject may help you.

Focus on committing one logical change at a time. See [this article](https://github.com/erlang/otp/wiki/writing-good-commit-messages) on the subject.

## Submitting a Pull Request <a href="submitting-a-pull-request" id="submitting-a-pull-request"></a>

### PR Title <a href="pr-title" id="pr-title"></a>

The PR title is used to automatically generate the [Changelog](https://github.com/neuropoly/spinalcordtoolbox/blob/master/CHANGES.md) for each new release, so please follow the following rules:

* Provide a concise and self-descriptive title (see [Issue Title](https://software-1/contributing#issue-title)).
* Do not include the applicable issue number in the title, do it in the PR body (see [PR Body](https://software-1/contributing#pr-body)).
* If the PR is not ready for review, convert it to a draft.

### PR Body <a href="pr-body" id="pr-body"></a>

Describe what the PR is about, explain the approach and possible drawbacks. Don't hesitate to repeat some of the text from the related issue (easier to read than having to click on the link).

If the PR fixes issue(s), indicate it after your introduction: `Fixes #XXXX, Fixes #YYYY%%`. 

Note: it is important to respect the syntax above so that the issue(s) will be closed upon merging the PR.

### PR Labels <a href="pr-labels" id="pr-labels"></a>

Some **NeuroPoly** projects require adding labels to pull requests, as they are used to [automatically generate a Changelog](https://github.com/neuropoly/changelog). Labeling protocols may vary between **NeuroPoly** projects (default project-specific categories are defined [here](https://github.com/neuropoly/changelog/blob/master/changelog/changelog.py#L273)), but the typical mandatory labels include:

* **Category:** Choose **one** label that describes the category of issue. (Colour: Dark purple with white text)
* **Context:** Choose one or multiple labels corresponding to the area of the codebase affected by the changes. (Colour: Light purple with dark text)
* **Version milestone:** Groups issues and PRs by release. Each project should always have an open milestone that corresponds to the next upcoming release.

The following labels are **strongly recommended** when appropriate, as they help with managing releases:

* **Compatibility**: If your PR breaks cross-compatibility with a previous stable release of SCT, you should add the label "compatibility". Changes with this label necessitate a new major release, so please [plan accordingly](https://semver.org/#if-even-the-tiniest-backwards-incompatible-changes-to-the-public-api-require-a-major-version-bump-wont-i-end-up-at-version-4200-very-rapidly).

### Work in Progress <a href="work-in-progress" id="work-in-progress"></a>

If your PR is not ready for review yet, you can convert it to a "Draft", so the team is informed.

A draft pull request is styled differently to clearly indicate that it’s in a draft state. Merging is blocked in draft pull requests. Change the status to “Ready for review” near the bottom of your pull request to remove the draft state and allow merging according to your project’s settings.

### Continuous Integration <a href="continuous-integration" id="continuous-integration"></a>

Some **NeuroPoly** projects run automated tests on pull requests via continuous integration (TravisCI, GitHub Actions, and others). Please ensure your pull requests pass all tests. If your pull request is failing, the output of the automated tests can help you debug your changes.

### Reviewers <a href="reviewers" id="reviewers"></a>

Any changes submitted for inclusion to the master branch will have to go through a [review](https://help.github.com/articles/about-pull-request-reviews/).

Only request a review when you deem the PR as "good to go". If the PR is not ready for review, convert it to a "Draft".

Github may suggest you to add particular reviewers to your PR. If that's the case and you don't know better, add all of these suggestions. The reviewers will be notified when you add them.

### Working on "Epic" Changes <a href="working-on-epic-changes" id="working-on-epic-changes"></a>

If you plan to work on an epic contribution, which would imply large changes to the codebase / functionalities, we recommend two possibilities (which are not mutually exclusive):

* Open an issue describing the proposed contribution, and label it with the label `epic`,
* Open a new [project board](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/about-project-boards) and add a meaningful description

Once the epic issue or project board is open and describes the overall plan, open small issues and cross-reference them with the epic issue, or add the project label.

The general idea is that each small issue represents an incremental means to achieve the epic goal. The advantage of small issues include:

* Discussion thread are easier to follow and are more focused;
* The PR addressing the issue is easier to review (because there is few lines of code);
* If a regression bug is introduced, it is easier to isolate it;
* Unit test is easier to write and review (because it covers only few lines of code)

Example of epic issue: "Accommodate microscopy modality in ivadomed". Examples of small, related issues: "Refactor data loader to accept PNG files", "Add testing data for microscropy", "Add tutorial for 2D images", etc.

## Versioning <a href="versioning" id="versioning"></a>

Versioning uses the following convention: `MAJOR.MINOR.PATCH`, where:

| Version | Description                                                                                                                                                                                                                              |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PATCH   | Use when there are backwards-compatible bug fixes or enhancements, without alteration to Python's modules or data/binaries.                                                                                                              |
| MINOR   | Use when there are minor API changes or new functionality in a backwards-compatible manner, or when there are alteration to Python's modules or data/binaries (which requires to re-run installer for people working on the dev version) |
| MAJOR   | Use when there are major incompatible API changes, Beta releases follow the following convention                                                                                                                                         |

_MAJOR.MINOR.PATCH-beta.x_ (with x = 0, 1, 2, etc.) Stable version is indicated in the file `version.txt`. For development version (on master), the version is "dev".

Project-specific release procedure:

* [AxonDeepSeg](https://github.com/neuropoly/axondeepseg/wiki/How-to-create-a-new-release)
