---
name: generate_knowledge_base
description: >
  Use this skill when you are tasked to create a knowledge base. The user uses uv everywhere instead of pip, venv,
  or conda. Trigger for any task involving Python dependency management,
  virtual environments, or package installation.
---

# Generate Knowledge base

- Copy the `assets/AGENTS.md` file into the working directory.
- Follow the orders given in that file.
- Add important information to the `## Additional` - part at the bottom of AGENTS.md
- Use the skills provided for creating a virtual environment, read pdfs etc...

## Timeline

- create a virtual environment
- create the folder structure
- transcribe and translate the lecture using subagents
- derive topics from the past exams and the lecture script
- fill the knowledge base
- find the rest of the information in the AGENTS.md file
