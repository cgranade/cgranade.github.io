---
layout: page
title: "Quantum Bootstrapping via Compressed Quantum Hamiltonian Learning"
description: ""
---
{% include JB/setup %}

**[Nathan Wiebe](http://research.microsoft.com/en-us/people/nawiebe/)<sup>[1](#affil1)</sup>, [Chris Granade](/)<sup>[2](#affil2), [3](#affil3)</sup> and [D. G. Cory](http://iqc.uwaterloo.ca/iqc-directory/dcory/)<sup>[2](#affil2),[4](#affil5),[5](#affil6)</sup>**

 > [arXiv:1409.1524](https://scirate.com/arxiv/1409.1524)
 
Presented as a talk at [LFQIS 2014](http://lfqis.net/), and at the [University of Sydney](http://www.cgranade.com/research/talks/usydney-2014/). Presented as a poster at [QIP 2015](http://quantum-lab.org/qip2015/).

## Abstract ##

Recent work has shown that quantum simulation is a valuable tool for learning empirical models for quantum systems. We build upon these results by showing that a small quantum simulators can be used to characterize and learn control models for larger devices for wide classes of physically realistic Hamiltonians. This leads to a new application for small quantum computers: characterizing and controlling larger quantum computers. Our protocol achieves this by using Bayesian inference in concert with Lieb-Robinson bounds and interactive quantum learning methods to achieve compressed simulations for characterization. Whereas Fisher information analysis shows that current methods which employ short-time evolution are suboptimal, interactive quantum learning allows us to overcome this limitation. We illustrate the efficiency of our bootstrapping protocol by showing numerically that an 8-qubit Ising model simulator can be used to calibrate and control a 50 qubit Ising simulator while using only about 750 kilobits of experimental data.

## Software Resources ##

[**QInfer**](https://github.com/csferrie/python-qinfer), a Python-language
implementation of the classical portions of the algorithm presented in this work, is
[available from GitHub](https://github.com/csferrie/python-qinfer).

## Bibliography ##

> [View on Zotero](https://www.zotero.org/cgranade/items/collectionKey/IGRFRW32)

## Affiliations ##

1. <a id="affil1"></a>[Microsoft Research](http://research.microsoft.com/en-us/).
2. <a id="affil2"></a>[Institute for Quantum Computing, University of Waterloo](http://iqc.uwaterloo.ca).
3. <a id="affil3"></a>[Department of Physics, University of Waterloo](https://uwaterloo.ca/physics-astronomy/).
4. <a id="affil4"></a>[Department of Chemistry, University of Waterloo](https://uwaterloo.ca/chemistry/).
5. <a id="affil5"></a>[Perimeter Institute for Theoretical Physics](http://www.perimeterinstitute.ca/).
