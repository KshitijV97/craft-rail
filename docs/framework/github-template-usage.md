# Use CraftRail as a GitHub template

Once the owner has published the repository and verified that GitHub's template-repository setting is enabled, open [`kshitijv97/craft-rail`](https://github.com/kshitijv97/craft-rail) and choose **Use this template** → **Create a new repository**. This copies the starter files into a new repository without retaining the upstream repository's commit history. A clone or fork is a different choice: use those when you want history or a continuing relationship with the upstream project.

In the new repository, update project brief, principles, stakeholders, glossary, requirements, architecture, and contract examples. Remove irrelevant starter content, keep or revise the shared `AGENTS.md`, and review the license and brand decisions. Create a first feature with `python3 scripts/new_feature.py "Feature title"`. Run the validator and unit tests, then commit the customized baseline. See [quickstart](quickstart.md).

The GitHub template setting belongs to the upstream repository's GitHub settings, not this source tree. A local checkout cannot make the **Use this template** button appear by adding a file. An owner or maintainer with repository administration rights must enable the setting and then verify it on the repository page. When that state has not been verified, treat the repository as a normal repository and follow the quickstart manually.
