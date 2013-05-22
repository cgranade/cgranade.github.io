---
layout: page
title: "Robust Online Hamiltonian Learning"
description: ""
redirects:
- /research/rohl
---
{% include JB/setup %}

**[Chris Granade](/)<sup>[1](#affil1),2</sup>, [Chris Ferrie](http://csferrie.com/)<sup>1,3</sup>, [Nathan Wiebe](https://services.iqc.uwaterloo.ca/people/profile/nwiebe/)<sup>1,4</sup> and [D. G. Cory](http://iqc.uwaterloo.ca/iqc-directory/dcory/)<sup>1,5,6</sup>**

## Abstract ##

In this work we combine two distinct machine learning methodologies, sequential Monte Carlo and Bayesian experimental design, and apply them to the problem of inferring the dynamical parameters of a quantum system. We design the algorithm with practicality in mind by including parameters that control trade-offs between the requirements on computational and experimental resources. The algorithm can be implemented online (during experimental data collection), avoiding the need for storage and post-processing. Most importantly, our algorithm is capable of learning Hamiltonian parameters even when the parameters change from experiment-to-experiment, and also when additional noise processes are present and unknown. The algorithm also numerically estimates the Cramer-Rao lower bound, certifying its own performance.

## Affiliations ##

1. <a id="affil1" />Institute for Quantum Computing, University of Waterloo.
2. Department of Physics, University of Waterloo.
3. Department of Applied Mathematics, University of Waterloo.
4. Department of Combinatorics and Optimization, University of Waterloo.
5. Department of Chemistry, University of Waterloo.
6. Perimeter Institute for Theoretical Physics.
