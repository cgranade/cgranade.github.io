---
layout: page
title: "Characterization, Verification and Control for Large Quantum Systems"
description: ""
---

[**Christopher E. Granade**](/)<sup>[1](#affil-iqc), [2](#affil-uw-phys)</sup>

 > [PDF](http://www.cgranade.com/downloads/cgranade-thesis.pdf)

PhD thesis, defended 26 February 2015. 

 > [Slides](slides/) (will follow presentation during defense) | [Livetweets](https://twitter.com/hashtag/GranadeDefense)

## Abstract ##

Quantum information processing offers potential improvements to a wide range
of computing endevaors, including cryptography, chemistry simulations and
machine learning. The development of practical quantum information processing
devices is impeded, however, by challenges arising from the apparent exponential
dimension of the space one must consider in characterizing quantum
systems, verifying their correct operation, and in designing useful control
sequences. In this work, we address each in turn by providing useful
algorithms that can be readily applied in experimental practice.

In order to characterize the dynamics of quantum systems, we apply statistical
methods based on Bayes' rule, thus enabling the use of strong prior
information and parameter reduction. We first discuss an
analytically-tractable special case, and then employ a numerical algorithm,
sequential Monte Carlo, that uses simulation as a resource for characterization. We
discuss several examples of SMC and show its application in nitrogen vacancy
centers and neutron interferometry.
We then discuss how characterization techniques such as SMC can be used to
verify quantum systems by using credible region estimation, model selection,
state-space modeling and hyperparameterization. Together, these techniques
allow us to reason about the validity of assumptions used in analyzing quantum
devices, and to bound the credible range of quantum dynamics.

Next, we discuss the use of optimal control theory to design robust control
for quantum systems. We show extensions to existing OCT algorithms that allow
for including models of classical electronics as well as quantum dynamics,
enabling higher-fidelity control to be designed for cutting-edge experimental
devices. Moreover, we show how control can be implemented in parallel across
node-based architectures, providing a valuable tool for implementing
proposed fault-tolerant protocols.

We close by showing how these algorithms can be augmented using quantum
simulation resources to enable addressing characterization and control design
challenges in even large quantum devices. In particular, we will introduce a
novel memetic algorithm for quantum control design, MOQCA, that utilizes
quantum coprocessors to design robust control sequences. We then extend
sequential Monte Carlo with quantum simulation resources to enable
characterizing and verifying the dynamics of large quantum devices. By using
novel insights in epistemic information locality, we are able to learn
dynamics using strictly smaller simulators, leading to an algorithm we call
quantum bootstrapping. We demonstrate by using a numerical example of learning
the dynamics of a 50-qubit device using an 8-qubit simulator.

## Software Resources ##

<a id="software-resources"></a>

The following libraries for Python, MATLAB and Mathematica were used to implement the results in this work. Each library was developed by or in collaboration with the author, or includes contributions from the author. Full details are included in the thesis and in each respective project.

- [**QInfer**](https://github.com/csferrie/python-qinfer): a Python-language implementation the classical and quantum characterization algorithms presented in this work.
- [**QuaEC**](https://github.com/cgranade/python-quaec): a Python-language library implementing quantum error correcting primitives in the stabilizer formalism.
- [**QuTiP**](http://qutip.org/): a Python-language library for manipulating and simulating the dynamics of quantum objects and systems.
- [**QuantumUtils for MATLAB**](https://github.com/CoryGroup/quantum-utils-matlab): a MATLAB-language library used to implement portions of this work, including portions of the honest approximation section.
- **QuantumUtils for Mathematica**: coming soon.

## Bibliography ##

> [Bibliography hosted on Zotero](https://www.zotero.org/cgranade/items/collectionKey/SQBZIC3H)

## Affiliations ##

1. <a id="affil-iqc"></a>[Institute for Quantum Computing, University of Waterloo](http://iqc.uwaterloo.ca).
1. <a id="affil-uw-phys"></a>[Physics Department, University of Waterloo](https://uwaterloo.ca/physics-astronomy/).
