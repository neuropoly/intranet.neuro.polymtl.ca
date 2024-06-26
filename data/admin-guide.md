# Dataset admin guide

TODO: list the places where we have datasets (data.neuro.polymtl.ca, github, aws, compute canada, spineimage.ca)

TODO: describe our current access rules

TODO: give some API examples/scripts

See also: [the user guide](git-datasets.md)

## New repository

We have a [dataset template](https://data.neuro.polymtl.ca/datasets/template) that we use for new repositories. When someone at the lab asks for a new dataset on <https://data.neuro.polymtl.ca/>, the steps to take are:

1. Make sure they've opened [an issue in data-management](https://github.com/neuropoly/data-management/issues) with the name they want. Note that we only use **lowercase letters** and **hyphens** (no underscores).
2. Log in to Neurogitea and go to [the repository creation page](https://data.neuro.polymtl.ca/repo/create?org=2). Then:
   1. Select the organization "NeuroPoly datasets" as owner.
   2. Fill in the repository name.
   3. "Make Repository Private" should already be checked.
   4. Select "datasets/template" as the template.
   5. For template items, check the box for "Git Content (Default Branch)".
   6. Click "Create Repository".
3. In the new repository, click "Watch" so that at least one admin gets notifications (that is, you).
4. Give write access to the requesting student:
   1. Go to the repository's "Settings" tab.
   2. Select "Collaborators" from the left-hand menu.
   3. Search for the student's name and click "Add Collaborator".
   4. Make sure the student's Neurogitea user account contains their actual human-readable name ("Site Administration" -> "User Accounts" -> search for the user -> edit).
5. Reply on the original [data-management issue](https://github.com/neuropoly/data-management/issues) that you've created the repo and given them write access, with a link to the repo.
