---
layout: post
title: What We Encourage
---

### <a href="https://github.com/tldr-pages/tldr-python-client" title="His tl;dr needs a tl;dr.">tl;dr</a> ###

- What we encourage and incentivize has consequences, both direct and unseen.
- Those incentives often preclude progress on things we claim to value in academic research.
- Better tools and better institutional support can help.
- Hey, I made some crappy tools to point to a couple examples of incentives against reproducible research.

## Incentives ##

To a large extent, we do what we are encouraged to do. We are after all, more or less social agents, and respond the people and social systems around us as social agents. Examining what we are encouraged to do, and how we build incentive structures to reward some actions and people over others, is thus a matter of perpetual importance. To take one particularly stark example, [I have argued here before](http://www.cgranade.com/blog/2016/09/04/save-physics-from-physicists.html) that sexual harassment and discrimination are at least as pervasive in physics as in many other fields of research. One way to combat this, then, is to develop incentive structures that do not further reinforce inequality but instead make it more difficult to use scientific institutions to harass and attack. Thus, we can use tools such as codes of conduct, effective reporting at institutions, and backchannel communication to build better systems of incentives that encourage positive behavior. As a side note, this is especially critical as science funding is under imminent and unprecedented attack in the United States— we've seen that public outcry can have magnificent effects for protecting institutions and funding, such that we must ensure that we earn the public support we now so existentially require.

Having thus seen that systems of encouragement can be social, it's also important to realize that encouragement can come as well in the form of technical constraints imposed by the systems that we build and interact with. To take one particular and relatively small example, the [one-function-per-file](http://matlabsadness.tumblr.com/post/46228191810/one-function-per-m-file) design decision of MATLAB *encourages* users to write longer functions than they might otherwise in a different language. In turn, this makes it harder for MATLAB users to [transfer skills to software development in other languages](http://neuroplausible.com/matlab), *discouraging* diversity in software tools.

Even though the design decisions made by MATLAB can be often be circumvented by users who disagree, they has a significant impact on what kind of software design decisions get made. For instance, using MATLAB affects how code is shared as well as how APIs are designed. These decisions can in turn also compound with social encouragements; consider the magnification of this example, given the near-exclusive focus on proprietary tools such as MATLAB found in many undergraduate physics programs. That is, our approach to physics education encourages certain software development methodologies over others as an immediate consequence of teaching particular tools rather than methods.

The interaction between social and technical encouragements is widely recognized. In user interface and user experience design, for instance, the concept of an [*affordance*](https://medium.com/@WebdesignerDepot/how-to-perfect-ux-with-design-affordances-79ce78792b08#.tfo7tvoif) is used to encourage a user to some set of interactions with a technical system. This understanding can be leveraged as a powerful tool for *persuading* users both to benefitial and malicious ends, as has been [prominently argued for at least fifteen years](https://www.amazon.com/Persuasive-Technology-Computers-Interactive-Technologies/dp/1558606432). Critically reflecting on how social and technical encouragements combine to affect our behavior is accordingly a pressing issue across different disciplines.

## State of the Art ##

Examining physics methodologies in detail from the perpsective of incentives, let's then consider what kinds of encouragement we create with our design choices and with our research methodologies by examining a few relevant examples. Importantly, none of these examples represent criticism of individual users or research groups, but rather an examination of what incentives users and groups are under.

- *Experiment control and analysis*: Current expeirmental methodology in physics often concerns itself with *ad hoc* control systems developed internally by graduate and undergraduate students in a single group. This discourages collaboration between groups using different internal systems, and more critically, can discourage challenging assumptions built in to early stages of experimental control systems. Efforts such as [InstrumentKit](https://github.com/Galvant/InstrumentKit), [Qudi](https://github.com/Ulm-IQO/qudi), and [QCoDeS](http://qcodes.github.io/Qcodes/), [Instrumental](https://github.com/mabuchilab/Instrumental), [SpanishAquisition](https://github.com/0/SpanishAcquisition), and [Labscript](http://labscriptsuite.org/) have attempted to change these incentives by instead providing high-quality open source libraries that can work *across* groups, and hence remove disincentives that can impede collaboration. Collecting common functionality in this way also encourages contributing safety and correctness features that would otherwise be undervalued in a single *ad hoc* application.

- *Statistical analysis*: Common software tools such as MATLAB, SciPy, and Mathematica all provide "curve fitting" functionality by default, and report frequentist metrics on the results produced by "curve fitting." This ready availability encourages the use of "fitting" over other methodologies, even in cases where the theory behind "fitting" does not apply. Taken in conjunction with the reticence of reviewers to point out such methological problems, it isn't a stretch to say that we directly encourage the publication of incorrect research results by failing to provide easy-to-use and principled statistical analysis tools that match experimental models.

- *Collaboration and version control*: At least ideally, collaboration forms a cornerstone of scientific research. Accordingly, the writing and editing of research manuscripts is also ideally a collaborative effort. To support that, we often employ software tools such as Dropbox to synchronize changes between collaborators. The technical restrictions imposed by Dropbox, however, present their own encouragements and discouragements. For example, that Dropbox will overwrite changes made concurrently by two users discourages authors from editing on disjoint sections. Often, this is mitigated by social agreements such as "tokens," where authors agree only to edit a work if they hold the "token" for the TeX source. That Dropbox does not present version history in a consise and readable form also discourages focusing editing efforts on recent changes. The eagerness of Dropbox to share temporary and editor-specific files also discourages the use of modern text editors such as [Atom](https://atom.io/), [Sublime Text](https://www.sublimetext.com/) and [VS Code](https://code.visualstudio.com/), each of which uses machine-specific metadata to store information such as undo history. Though these issues can somewhat be mitigated by using formal version control systems such as Git or Mercurial, that many students and postdocs have little to no opportunity to learn such tools presents a strong *social* discouragement against robust and efficient collaboration.

- *Plotting and accessibility*: Approximately 10% of the population is at least mildly color-blind such that the use of colors in scientific visualizations can prevent a significant barrier to accessibility. Default color schemes in widely-used tools such as MATLAB *discourage* accessible design by forcing users to specify that each plot individually should use an accessible palette. Up until recently, the Matplotlib plotting library for Python has similarly discouraged accessible design, though other positive encouragements such as declarative style sheets have somewhat mitigated this.

## Open Science ##

One critical component common to each of these examples is that they use the concept of open source software development to change the incentives for researchers. If it becomes easier — if we encourage — contributing to existing efforts instead of reinventing well-understood wheels, then not only does it become less expensive to do cutting-edge research, but it also becomes more practical to do *reproducible* research. As we can see from reproducibility crises in other fields, physics research likely cannot survive its current model of closed-source closed-data closed-analysis papers hidden behind increasingly-expensive paywalls. Perhaps most critically, the lack of reproducibility in scientific papers can also play a role in [exacerbating public mistrust of science](http://www.factcheck.org/2017/02/no-data-manipulation-at-noaa/). I'll return to the role that the arXiv plays in changing these incentives later, but suffice to say that open access is not sufficient to imply that a paper or other research output can be independently assessed for correctness. The gap between the openness we currently take as being standard in physics and the level of transparency that we need is thus not a trivial one.

In this discussion, of course, we also cannot afford to elide that open science in general and open source in particular also helps to remove elements of gatekeeping that can be used to preclude participation. In current practice, the expense of performing physics research, be it theory or experiment, naturally concentrates decision-making power in a smaller number of individuals. Though the effects of this concentration can be mitigated to some degree, it is also important to reduce the areas in which cognative biases can hide from critical examination. Reducing barriers to entry can provide a way to do so.

<abbr title="Not only does he have a point, he actually got to it eventually!">I posit</abbr> that these self-same barriers to entry are, perhaps ironically, one of the largest impediments to the adoption of open science methodologies in physics. Take, for instance, [the advice offered to me](http://academia.stackexchange.com/a/86538/70648) in response to a question about how to adopt better open science methods when posting to the arXiv:

> For the sake of persistent archiving you should put all ancillary material at a sustainably archived website specifically designed to preserve scholarly communications material e.g. Zenodo https://zenodo.org/ or Dryad http://datadryad.org/ or Figshare https://figshare.com/

I agree with this advice entirely, and have in fact advocated this exact approach with both [open-source efforts](http://qinfer.org/) and [reproducible papers](https://arxiv.org/abs/1605.05039). That said, let's consider the incentive structure imposed by this approach. A student or postdoc taking responsibility for posting a reproducible work to the arXiv must then not only know how to do so directly, including how to write [literate source code](https://en.wikipedia.org/wiki/Literate_programming), but also about the existence of services such as Figshare. Moreover, a researcher must then manage their work's presence on arXiv as well as additional services, increasing the complexity of maintaining an accessible research output.

Happily, however, arXiv itself [supports including ancillary material](https://arxiv.org/help/ancillary_files) such as source code and data along with a paper. Even here, though, the workflow for providing such ancillary material is more complicated than the comparable closed-science workflow. In particular, arXiv identifies ancillary material as being those files included in the ``anc/`` subfolder of a submission package, but subfolders are only supported by uploading a ZIP archive of the entire submission. To make such a ZIP file with most existing tools, the original file must itself be in a folder called ``anc/``, imposing a nontrivial technical restriction on project folder structures.

To some degree, encouragements of this kind that run counter to open science goals are inevitable. Indeed, there is a bit of a contradiction in that the very goal of reproducible research is to make it more difficult to publish in a way that is disporportionate between papers that are likely correct and those that cannot be as easily assessed for correctness. The natural tendency, then, is for reproducibility advocates [to yell into the void or into the echo chamber](https://twitter.com/csferrie/status/841607819224743936) about the existential importance of open science, and for the rest of the community to go forth with their business in the best way that they can given very limited resources.

In the same way as in dealing with discrimination by providing better tools that change incentive structures, we can break this circularity by providing better tools for writing reproducible papers. For instance, one very impressive tool to do precisely this is [ReproZip](https://www.reprozip.org/), which works by leveraging modern software and hardware engineering technologies such as virtual machines. Indeed, ReproZip works great at making it easier to provide compact descriptions of reproducible research projects. This approach works especially well in combination with tools such as [Jupyter Notebook](http://jupyter.org/), which allow for producing standardized and well-understood literate source code for a variety of different languages. Though Jupyter is perhaps most famous for its Python support, having grown out of the IPython project, it also supports [Julia](https://github.com/JuliaLang/IJulia.jl), [R](https://github.com/IRkernel/IRkernel), [F#](https://github.com/fsprojects/IfSharp), and even [MATLAB](https://github.com/Calysto/matlab_kernel) when augmented with simple-to-install extensions.

Recently, I have started to experiment with other software tools for changing incentive structures, in the hopes of building on the backs of these efforts. My goals are of course more modest, in keeping with the resources available, but at the least I would like to propose ways of making tools such as Jupyter Notebook more accessible to arXiv users. In the rest of this post, I will detail two such (experimental!) efforts and how they are each motivated by reducing barriers to entry for reproducible physics research.

## ``{revquantum}`` ##

The first such effort is the ``{revquantum}`` style file for LaTeX, intended to make it easier to write reproducible and accessible papers in the ``{revtex4-1}`` and [``{quantumarticle}``](https://github.com/cgogolin/quantum-journal) document classes. The ``{revquantum}`` package supports accessiblility in a number of different ways:

- *Semantic notation*: ``{revquantum}`` provides commands such as ``\newoperator``, which allow users to write in a more semantic fashion than worrying about implementation details. In that example, ``\newoperator{Tr}`` defines ``\Tr`` as ``\newcommand{\Tr}{\operatorname{Tr}}``, resulting in more readable code than what might be produced directly, such as ``\mathrm{Tr}(\rho)``.

- *Accessible color palettes*: ``{revquantum}`` also provides definitions for the [Color Universal Design](jfly.iam.u-tokyo.ac.jp/color/) palette, such that users can quickly set colors for TikZ diagrams and other features in an accessible manner.

- *``{listings}`` integration*: The ``{listings}`` package provides invaluable tools for including source code along with research manuscripts. There are some subtle issues in integrating ``{listings}`` with ``{revtex4-1}`` and other such classes, however, such that ``{revquantum}`` provides a reasonable set of defaults that for use with ``{revtex4-1}``.

- *Package compatibility warnings*: There are a few commonly-used packages which are known to be incompatible with ``{revtex4-1}``. These incompatibilities can cause difficult-to-diagnose errors, however, instead of immediately raising errors that identify the problem. To address this and prevent users from being discouraged against modular TeX design, ``{revquantum}`` will raise warnings or errors when incompatible packages are loaded so that users are immediately informed as to the issue.

- *Bibliography improvements*: The default BibTeX style file provided with ``{revtex4-1}`` suppresses the titles of cited papers in order to match the formatting that might appear in PRL and similar journals. For deployment to the arXiv, though, where space constraints are much less of an issue, this design decision removes context from the reader and encourages more of a focus on where something is published than the content that is being cited. To address this and encourage a stronger focus on research content, ``{revquantum}`` sets a default configuration that provides more context in generated bibliographies. Moreover, ``{revquantum}`` changes citation URLs to default to HTTPS, encouraging better security practices.

- *Annotations for collaborative writing*: Finally, ``{revquantum}`` provides new lightweight commands such as ``\todo`` and ``\citeneed`` for annotating remaining tasks in a collaborative document. These commands leave warnings in the log file, making them easy to identify in modern text editors that annotate warnings in the TeX source. Moreover, the ``[final]`` option ot ``{revquantum}`` promotes these warnings to errors, providing a safety check against leaving outstanding tasks.

## PoShTeX ##

The other effort I would like to detail a bit here is [PoShTeX](http://www.cgranade.com/posh-tex/), a set of PowerShell tools for working with TeX-based research projects. In particular, PoShTeX provides the ``Export-ArXivArchive`` command, which makes a ZIP archive suitable for uploading to arXiv. In doing so, PoShTeX will rebuild the current TeX file, and will optionally re-run any nominated Jupyter Notebooks to ensure consistency with the figures and descriptions provided in the project's main text. For example, a project might include a short ``Export-ArXiv.ps1`` script to produce an arXiv-compatible archive:

```powershell
#region Bootstrap PoShTeX
$modules = Get-Module -ListAvailable -Name posh-tex;
if (!$modules) {Install-Module posh-tex -Scope CurrentUser}
if (!($modules | ? {$_.Version -ge "0.1.4"})) {Update-Module posh-tex}
Import-Module posh-tex -Version "0.1.4"
#endregion

Export-ArXivArchive -RunNotebooks @{
    ProjectName = "my-little-pauli";
    TeXMain = "my-little-pauli.tex";
    AdditionalFiles = @{
        "fig/*.pdf" = "fig/";
        "data/tomography-data.hdf5" = $null;
        "revquantum.sty" = $null;
    };
    Notebooks = @(
        "src/fidelity_is_magic.ipynb"
    )
}
```

This script will then install PoShTeX if it is not already available, and will then rerun the listed notebooks, compile the TeX output, and produce the final build file ``my-little-pauli.zip`` for uploading to arXiv. In this way, PoShTeX makes it very straightforward to include reproducible material.

The second major functionality provided by PoShTeX is that it makes it much easier to write reusable LaTeX resources such as style files by making it easy to write installers and produce CTAN-compatible archives. This is, for example, how ``{revquantum}`` is packaged and uploaded to CTAN. Thus, PoShTeX hopefully also encourages not only sharing the research code itself but also the LaTeX code used to produce legible and readable research documents.

By the way, why PowerShell? It may seem like an odd choice for encouraging open scientific research, but consider that a very significant majority of Windows users already have PowerShell, given its status as a built-in tool since Windows 7. Though bash enjoys even wider deployment on macOS / OS X and on Linux, the [recent availability of PowerShell as an open source tool] on non-Windows platforms changes this calculus dramatically. In particular, given the ease of installing PowerShell modules with the ``Install-Module`` command, PowerShell may offer a way forward to distribute cross-platform shell libraries in an easy-to-use way.

## Concluding Remarks ##

<abbr title="Long post is long…">In this post</abbr>, I've described a few ways that what we encourage can have dramatic negative or hopefully positive effects on research culture and practice. These examples all speak to how thinking not only critically but also systematically can provide a path forward for doing the best science that we can.
