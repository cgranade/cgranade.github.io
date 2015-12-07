---
layout: page
title: "Practical Bayesian Tomography"
description: ""
---
{% include JB/setup %}

**[Christopher Granade](/)<sup>[1](#affil1),[2](#affil2)</sup>, Joshua Combes<sup>[3](#affil3),[4](#affil4),[5](#affil5)</sup> and [D. G. Cory](http://iqc.uwaterloo.ca/iqc-directory/dcory/)<sup>[3](#affil3),[5](#affil5),[6](#affil6),[7](#affil7)</sup>**

 > [arXiv:1509.03770](https://scirate.com/arxiv/1509.03770).
 
Presented as a talk [at IQC](../talks/iqc/09-2015), [at QuICS](../talks/quics/09-2015), and [at the 2015 Sydney QIP Workshop](../talks/sqip-workshop/12-2015).

## Abstract ##

In recent years, Bayesian methods have been proposed as a solution to a wide range of issues in quantum state and process tomography. State-of-the-art Bayesian tomography solutions suffer from three problems: numerical intractability, a lack of informative prior distributions, and an inability to track time-dependent processes. Here, we solve all three problems. First, we use modern statistical methods, as pioneered by [Huszar and Houlsby](https://dx.doi.org/10.1103/PhysRevA.85.052120) and by [Ferrie](https://dx.doi.org/10.1088/1367-2630/16/9/093035), to make Bayesian tomography numerically tractable. Our approach allows for practical computation of Bayesian point and region estimators for quantum states and channels. Second, we propose the first informative priors on quantum states and channels. Finally, we develop a method that allows online tracking of time-dependent states and estimates the drift and diffusion processes affecting a state. We provide source code and animated visual examples for our methods.

## Online Resources ##

- [**QInfer**](https://github.com/csferrie/python-qinfer), a Python-language
implementation of the classical portions of the algorithm presented in this work, is
[available from GitHub](https://github.com/csferrie/python-qinfer).
- A tutorial and code used to generate figures and animations are available
as [literate source code](https://gist.github.com/cgranade/9b3f8c4c8173eebf5f35).
- A video demonstrating the state-tracking algorithm is [available on YouTube](https://www.youtube.com/watch?v=22ejRV0Kx2g).

## Affiliations ##

1. <a id="affil1"></a>[Centre for Engineered Quantum Systems, University of Sydney](http://equs.org/)
2. <a id="affil2"></a>[School of Physics, University of Sydney](http://sydney.edu.au/science/physics/).
3. <a id="affil3"></a>[Institute for Quantum Computing](https://iqc.uwaterloo.ca/).
4. <a id="affil4"></a>[Department of Applied Mathematics](https://uwaterloo.ca/applied-mathematics/).
5. <a id="affil5"></a>[Perimeter Institute for Theoretical Physics](http://www.perimeterinstitute.ca/).
6. <a id="affil6"></a>[Department of Chemistry, University of Waterloo](https://uwaterloo.ca/chemistry/).
7. <a id="affil7"></a>[Canadian Institute for Advanced Research](http://www.cifar.ca/).