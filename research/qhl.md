---
layout: page
title: "Quantum Hamiltonian Learning"
description: ""
---

**[Nathan Wiebe](http://research.microsoft.com/en-us/people/nawiebe/)<sup>[1](#affil1)</sup>, [Chris Granade](/)<sup>[2](#affil2), [3](#affil3)</sup>, [Chris Ferrie](http://csferrie.com/)<sup>[4](#affil4)</sup> and [D. G. Cory](http://iqc.uwaterloo.ca/iqc-directory/dcory/)<sup>[2](#affil2),[5](#affil5),[6](#affil6)</sup>**

 > [arXiv:1309.0876](http://arxiv.org/abs/1309.0876), [arxiv:1311.5269](http://arxiv.org/abs/1311.5269)
 
Presented as a poster at [Q100 2013](http://researcher.watson.ibm.com/researcher/view_project.php?id=4847) and [SQuInT 2014](http://panda.unm.edu/SQuInT/).

## Abstract ##

A long-standing problem in the development of practical quantum simulators is how to certify that a given quantum device implements a desired Hamiltonian. This is especially pressing for devices currently-proposed devices on the 100-qubit scale, as classical simulation cannot certify the dynamics of a quantum device on that scale. Here, we address this problem by providing an algorithm that exploits trusted quantum simulation resources in order to characterize and certify the Hamiltonian dynamics of an untrusted quantum system. Moreover, by apploying quantum resources to the task of characterizing quantum systems, our algorithm allows for processors to be used as resources in the development of further processors.

We show that our algorithm, in some analytically-tractable cases, admits near-optimal performance. Moreover, we demonstrate analytic and numeric evidence that our algorithm is robust to sampling errors, decoherence and excluded terms. By using quantum simulation resources together with classical statistical inference techniques, our algorithm provides a powerful tool for certifying quantum simulators and for developing new quantum information processing devices.

## Software Resources ##

[**QInfer**](https://github.com/csferrie/python-qinfer), a Python-language
implementation of the classical portions of the algorithm presented in this work, is
[available from GitHub](https://github.com/csferrie/python-qinfer).

## Bibliography ##

Bibliography coming soon.

## Affiliations ##

1. <a id="affil1"></a>[Microsoft Research](http://research.microsoft.com/en-us/).
2. <a id="affil2"></a>[Institute for Quantum Computing, University of Waterloo](http://iqc.uwaterloo.ca).
3. <a id="affil3"></a>[Department of Physics, University of Waterloo](https://uwaterloo.ca/physics-astronomy/).
4. <a id="affil4"></a>[Center for Quantum Information and Control, University of New Mexico](http://physics.unm.edu/CQuIC/).
5. <a id="affil5"></a>[Department of Chemistry, University of Waterloo](https://uwaterloo.ca/chemistry/).
6. <a id="affil6"></a>[Perimeter Institute for Theoretical Physics](http://www.perimeterinstitute.ca/).
