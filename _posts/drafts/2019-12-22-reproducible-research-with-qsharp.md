---
layout: post
title: "Reproducible Research with Q#"
---

*This post is...*

## Introduction ##

Almost three years ago, [I wrote here about the importance of reproducible research](), and about tools that can be used to make it easier to perform research in a way that makes reproduciblity **easy**.
Making it easy to do research in a reproducible fashion is critical --- not just to avoid the gatekeeping that all too often comes along with research, but also because people are much more likely to do the things that we [encourage them to do]().

A lot can change in three years, though, and that's definitely been true in the quantum computing community.
Indeed, three years ago, the quantum computing community was much smaller, and much more heavily focused on more abstract research results.
As the community has grown, we've seen a huge growth in both the number and variety of tools available to help explore quantum computing through reproducible research.
In this post, I'll take an opportunity to highlight how it's easier than ever to get started in reproducible quantum computing research.
You won't even need to install anything other than a browser to get going!

## Contain Yourself

As a member of the team that [launched the Quantum Development Kit and the Q# language two years ago](), I'm particularly excited for how Q# has helped enable quantum computing research by making it easier to [develop and test quantum algorithms](), [estimate resource costs](), and even to [run quantum programs on hardware]().
Using Q# to do reproducible research, your software stack might look a _little_ different than it did three years ago.
For example, if you want to use Q# together with great host languages like C# or Python, and then include all of that into a paper written with LaTeX, you may wind up needing a variety of different tools:

- .NET Core SDK (used to provide the Q# compiler)
- Python
- TeX / LaTeX
- Jupyter Notebook
- Visual Studio Code
- Git

While thankfully these tools are all pretty straightforward to install, for reproducible research, 

- Quantum programming language: Q#
- Host language: 
- TeX / LaTeX distribution: TeX Live and MiKTeX
- Literate programming environment: Jupyter Notebook
- Text editor: Visual Studio Code
- LaTeX template: ``{revtex4-1}``, ``{quantumarticle}``, and ``{revquantum}``
- Project layout
- Version control: Git
- arXiv build management: PoShTeX
