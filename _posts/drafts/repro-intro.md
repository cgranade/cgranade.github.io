---
layout: post
title: "Software Tools for Writing Reproducible Papers"
---

## Introduction ##

In my [previous post](), I detailed the software stack I use in writing reproducible research papers.
Many of these tools, however, have been developed over the course of my research career so far such that no one paper actually uses the whole stack.
Moreover, simply seeing a description of each tool in isolation doesn't really communicate how these tools are used in practice.
For these reasons, I'd like to start a new project: walking through how to write a reproducible research paper by way of an actual example.

In particular, I would like to use my earlier [multiexponential learning]() post as an example of how to write a reproducible paper.
Thus, over the next several posts, I'll document the various steps that I follow in obtaining numerical results, writing and editing a paper, publishing the paper to arXiv, and going through the peer review process.
In doing so, I'd like to focus not on the research itself, but on the process by which that research is communicated.
I believe that this is a topic we don't give enough time to, ironically much to the detriment of our research.
My intent is thus to show a better and more sustainable path forward that will enable us to better tackle the challenges in front of us.

For my first step in this endeavor, I set up a new computer for writing a reproducible paper.
After all, if a reproducible writing process doesn't work well without an arduous and esoteric setup, it doesn't work well at all.
To do so, I be used a Mac Book Pro (10.11.1 El Capitan, mid-2012, Retina), as to use a system as distinct as possible from my previous efforts.
Indeed, since my goal is to make something accessible, it has to work across platforms.
Without further ado, then, let's dive in to how I set up the new laptop for paper writing.
As per the instructions in the [previous post](http://www.cgranade.com) (thank you again to Daniel Seuss for contributing the macOS / OS X part of that post), I installed the following tools on the new development machine:

- Homebrew: Package manager for Mac
  ```bash
  $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```
- PowerShell: Cross-platform shell
  ```bash
  $ brew tap caskroom/cask
  $ brew cask install powershell
  ```
- MacTeX: TeX/LaTeX distribution for macOS / OS X
  ```bash
  $ brew cask install mactex
  ```
- Anaconda: Cross-platform Python and Jupyter distribution

At this point, I restarted the terminal to make sure that everything else used the Homebrew- and Anaconda-provided versions of tools that also ship with macOS / OS X.
Continuing, I installed just a couple more tools:

- Visual Studio Code: Cross-platform editor and development environment
  ```bash
  $ brew cask install visual-studio-code
  ```
- Scientific Computing Extension Pack for VS Code
- Pandoc
  ```bash
  $ brew install pandoc # NB: no cask, as this is a core package.
  ```
- ``{revquantum}`` and ``{quantumarticle}``
  ```bash
  $ powershell
  PS> git clone https://github.com/cgranade/revquantum.git
  PS> cd revquantum
  PS> ./Install.ps1
  PS> git clone https://github.com/cgogolin/quantum-journal.git
  PS> cd quantum-journal
  PS> ./install.ps1 # NB: lowercase "i"!
  ```
- latexdiff and rcs-latexdiff
  ```bash
  $ sudo tlmgr update --self
  $ sudo tlmgr install latexdiff
  $ pip install git+https://github.com/ihincks/rcs-latexdiff.git
  ```

## Repository Setup ##

Next, I set up an SSH keypair for use with GitHub.
By doing so, I am able to easily revoke credentials for the new laptop without also revoking credentials on other machines.
Using **⌘+Space** to launch Terminal, I ran the following commands to make a new keypair and print the *public* part of the keypair to the screen:

```bash
$ ssh-keygen
$ cat ~/.ssh/id_rsa.pub
```

I then copied and pasted my new *public* (not *private*) key to GitHub's [SSH and GPG keys](https://github.com/settings/keys) page and added it to my account.

Next, I created a new Git repository for the project on GitHub by going to [``https://github.com/new``](https://github.com/new).
In doing so, I made sure to give my new repository a ``README`` so that it wasn't empty, and chose to apply the BSD 3-claus license.
This is helpful for a project of this nature, as I am more concerned with reusability than ensuring that modifications are also openly licensed.
You can see the result at [``https://github.com/cgranade/multiexp-rb``](https://github.com/cgranade/multiexp-rb).

Next, I cloned the new repository to my development laptop:
```bash
$ git clone git@github.com:cgranade/multiexp-rb.git
```
I then used Visual Studio Code to make a new ``.gitignore``.
First, I launched Code with the following:
```bash
$ code multiexp-rb
```
Next, I used **⌘+Shift+P** to bring up the Command Palette and typed "Add gitignore."
This functionality was added by the Extension Pack that I installed above, and makes it easy to combine ignore files for multiple languages.
I added the Python gitignore, and then appended the TeX gitignore, since I'll be using both extensively from here on out.
Using the source control tools built into VS Code (**^+Shift+G**), I
added the new gitignore file to the ``multiexp-rb`` repo.
You can see the result at [commit 86e21614d11106f04d6765d1da52b7fd4bf7273c](https://github.com/cgranade/multiexp-rb/commit/86e21614d11106f04d6765d1da52b7fd4bf7273c).

In the next post, I'll start actually writing the outline for the paper and the literate source code, along with a more useful project layout.
Thanks for reading! ♥