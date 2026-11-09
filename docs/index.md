---
title: CraftRail documentation
description: Adoption guides and technical implementation documentation for CraftRail.
---

# CraftRail documentation

**Guardrails for agent-driven development.**

CraftRail keeps engineering intent, requirements, architecture, decisions, work, and verification in a repository where people and coding agents can review them together. The framework owns the engineering process; the coding agent is replaceable.

This documentation has two parts. Choose the path that matches what you are doing:

## 1. Docs for adoption

Use CraftRail in a new project, start from the GitHub template, or add its conventions to an existing repository. This section explains how to write and maintain project artifacts and use CraftRail with coding agents.

[Open the adoption guide](adoption/index.md)

## 2. Technical implementation of CraftRail

Understand how this CraftRail repository itself is built: the Core, Workflow, and Adapter layers; the Python tools and their quality checks; GitHub Actions; releases; and the documentation site.

[Open the technical implementation guide](implementation/index.md)

The canonical adoption content remains in Markdown under `docs/`; the website only renders those source files. The root `AGENTS.md` is the shared agent instruction source, with `CLAUDE.md` as a minimal Claude Code adapter.
