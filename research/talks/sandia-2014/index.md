---
layout: page
title: "Practical Characterization and Control of Quantum Systems"
description: ""
---

**[Cassandra Granade](/)<sup>[1](#affil-iqc), [2](#affil-uwphys)</sup>**,
joint work with
**[Christopher Ferrie](http://csferrie.com/)<sup>[3](#affil-cquic)</sup>,
[Nathan Wiebe](http://research.microsoft.com/en-us/people/nawiebe/)<sup>[4](#affil-msr)</sup>,
[Ian Hincks](https://services.iqc.uwaterloo.ca/people/profile/ihincks/)<sup>[1](#affil-iqc), [5](#affil-uwamath)</sup>,
[Troy Borneman](https://services.iqc.uwaterloo.ca/people/profile/tbornema/)<sup>[1](#affil-iqc)</sup>, and
[D. G. Cory](http://iqc.uwaterloo.ca/iqc-directory/dcory/)<sup>[1](#affil-iqc),[6](#affil-uwchem),[7](#affil-pi)</sup>**

 > Primarily based on [arXiv:1207.1655](https://scirate.com/arxiv/1207.1655), [arXiv:1404.5275](../../arb/), and on forthcoming work.
 
Presented 24 June, 2014 as a seminar at Sandia National Laboratories.

 > Slides: [HTML](slides.html) | IPython Notebook: [download](slides.ipynb), [view online](http://nbviewer.ipython.org/github/cgranade/cgranade.github.io/blob/master/research/talks/sandia-2014/slides.ipynb)

## Abstract ##

High-fidelity control of quantum systems is an essential component
in the development of useful quantum information processing devices.
Such control is predicated on a characterization of the system of
interest, and the accuracy of control is then assessed
through characterization.
In this seminar, we discuss novel approaches for each,
and show how our work addresses practical concerns
in quantum information experiments.

In particular, we address the characterization of quantum devices
by applying the sequential Monte Carlo (SMC) algorithm. This algorithm
is shown to be robust, including to finite sampling and to errors in simulation.
We demonstrate the practicality of our approach by showing examples
in randomized benchmarking experiments and in learning properties of nitrogen
vacancy centers.

We also show how models of electronic systems can be incorporated
into optimal control algorithms such as gradient-ascent pulse engineering
(GRAPE). Our work allows accurate control to be obtained, even in the
presence of strongly non-linear control systems.

Our work thus provides methods for the characterization and control
of quantum systems that address practical concerns in modern quantum information
experiments.

## Software Resources ##

[**QInfer**](https://github.com/csferrie/python-qinfer), a Python-language
implementation of the classical portions of the algorithms presented in this work, is
[available from GitHub](https://github.com/csferrie/python-qinfer).

## Bibliography ##

 > [View on Zotero](https://www.zotero.org/cgranade/items/collectionKey/VSWSNCCA)

## Affiliations ##


1. <a id="affil-iqc"></a>[Institute for Quantum Computing, University of Waterloo](http://iqc.uwaterloo.ca).
2. <a id="affil-uwphys"></a>[Department of Physics, University of Waterloo](https://uwaterloo.ca/physics-astronomy/).
3. <a id="affil-cquic"></a>[Center for Quantum Information and Control, University of New Mexico](http://physics.unm.edu/CQuIC/).
4. <a id="affil-msr"></a>[Microsoft Research](http://research.microsoft.com/en-us/).
5. <a id="affil-uwamath"></a>[Department of Applied Mathematics, University of Waterloo](https://math.uwaterloo.ca/applied-mathematics/home).
6. <a id="affil-uwchem"></a>[Department of Chemistry, University of Waterloo](https://uwaterloo.ca/chemistry/).
7. <a id="affil-pi"></a>[Perimeter Institute for Theoretical Physics](http://www.perimeterinstitute.ca/).

