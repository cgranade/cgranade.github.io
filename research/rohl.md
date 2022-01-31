---
layout: page
title: "Robust Online Hamiltonian Learning"
description: ""
---

**[Cassandra Granade](/)<sup>[1](#affil1),[2](#affil2)</sup>, [Chris Ferrie](http://csferrie.com/)<sup>[1](#affil1),[3](#affil3)</sup>, [Nathan Wiebe](https://services.iqc.uwaterloo.ca/people/profile/nwiebe/)<sup>[1](#affil1),[4](#affil4)</sup> and [D. G. Cory](http://iqc.uwaterloo.ca/iqc-directory/dcory/)<sup>[1](#affil1),[5](#affil5),[6](#affil6)</sup>**

 > 2012 New Journal of Physics **14** 103013 |
 > [arXiv:1207.1655](http://arxiv.org/abs/1207.1655) | [doi:10.1088/1367-2630/14/10/103013](http://dx.doi.org/10.1088/1367-2630/14/10/103013) 
 
Presented as a poster at [TQC 2013](http://www.uoguelph.ca/quigs/tqc2013/) ([Poster PDF](rohl/tqc-poster.pdf), [Proceedings](http://drops.dagstuhl.de/opus/frontdoor.php?source_opus=4318)).
Presented as a contributed talk at [DAMOP 2013](http://www.aps.org/units/damop/meetings/annual/) ([Slides PDF](rohl/damop-slides.pdf)).

## Abstract ##

In this work we combine two distinct machine learning methodologies, sequential Monte Carlo and Bayesian experimental design, and apply them to the problem of inferring the dynamical parameters of a quantum system. We design the algorithm with practicality in mind by including parameters that control trade-offs between the requirements on computational and experimental resources. The algorithm can be implemented online (during experimental data collection), avoiding the need for storage and post-processing. Most importantly, our algorithm is capable of learning Hamiltonian parameters even when the parameters change from experiment-to-experiment, and also when additional noise processes are present and unknown. The algorithm also numerically estimates the Cramer-Rao lower bound, certifying its own performance.

## Software Resources and Demonstrations ##

[**QInfer**](https://github.com/csferrie/python-qinfer), a Python-language
implementation of the algorithm presented in this work, is
[available from GitHub](https://github.com/csferrie/python-qinfer).

<iframe width="960" height="720" src="https://www.youtube-nocookie.com/embed/4EiD8JcCSlQ?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>

[[source code for above demo](http://nbviewer.ipython.org/url/www.cgranade.com/research/rohl/demos/animated_multicos.ipynb)]

## Bibliography ##

 > View on [Zotero](https://www.zotero.org/cgranade/items/collectionKey/T8KG53T9) | [citeulike](http://www.citeulike.org/user/cgranade/tag/publication-rohl)

1. M. Paris and J. Rehacek, eds., [Quantum State Estimation](http://www.springer.com/physics/quantum+physics/book/978-3-540-22329-0), vol. 649 of Lecture Notes in Physics (Springer, 2004), ISBN 978-3-540-22329-0.
2. B. P. Lanyon et al., [Universal Digital Quantum Simulation with Trapped Ions](http://www.sciencemag.org/content/334/6052/57.abstract), Science 334, 57 (2011).
3. R. Gerritsma et al., [Quantum Simulation of the Klein Paradox with Trapped Ions](http://link.aps.org/doi/10.1103/PhysRevLett.106.060503), Phys. Rev. Lett. 106, 060503 (2011). 
4. K. Kim et al., [Universal Digital Quantum Simulation with Trapped Ions](http://www.sciencemag.org/content/334/6052/57), Nature (London) 465, 590 (2010).
5. A. Bendersky, F. Pastawski, and J. P. Paz, [Selective and Efficient Estimation of Parameters for Quantum Process Tomography](http://prl.aps.org/abstract/PRL/v100/i19/e190403), Phys. Rev. Lett. 100, 190403 (2008).
6. A. Bendersky, F. Pastawski, and J. P. Paz, [Selective and efficient quantum process tomography](http://link.aps.org/doi/10.1103/PhysRevA.80.032116), Phys. Rev. A 80, 032116 (2009).
7. M. Mohseni and A. T. Rezakhani, [Equation of motion for the process matrix: Hamiltonian identification and dynamical control of open quantum systems](http://link.aps.org/doi/10.1103/PhysRevA.80.010101), Phys. Rev. A 80, 010101 (2009).
8. M. P. A. Branderhorst et al., [Simplified quantum process tomography](http://stacks.iop.org/1367-2630/11/i=11/a=115010), New Journal of Physics 11, 115010 (2009).
9. S. T. Flammia and Y. K. Liu, [Direct Fidelity Estimation from Few Pauli Measurements](http://dx.doi.org/10.1103/PhysRevLett.106.230501), Physical Review Letters 106, 230501+ (2011).
10. M. P. da Silva, O. L. Cardinal, and D. Poulin, [Practical Characterization of Quantum Devices without Tomography](http://dx.doi.org/10.1103/PhysRevLett.107.210404), Physical Review Letters 107, 210404+ (2011).
11. D. Oi and S. Schirmer, [Quantum system characterization with limited resources](http://arxiv.org/abs/1202.5779) (2012), 1202.5779.
12. A. Doucet and A. M. Johansen, [A Tutorial on Particle Filtering and Smoothing: Fifteen Years Later](http://www.cs.ubc.ca/~arnaud/doucet_johansen_tutorialPF.pdf) (Oxford University Press, 2009).
13. T. J. Loredo, [Bayesian Adaptive Exploration](http://dx.doi.org/10.1063/1.1751377), AIP Conference Proceedings 707, 330 (2004).
14. H. Kuck, N. de Freitas, and A. Doucet, [SMC Samplers for Bayesian Optimal Nonlinear Design](http://dx.doi.org/10.1109/NSSPW.2006.4378829), in Nonlinear Statistical Signal Processing Workshop, 2006 IEEE (IEEE, 2006), pp. 99-102, ISBN 978-1-4244-0581-7.
15. B. Scarpa and D. B. Dunson, [Bayesian methods for searching for optimal rules for timing intercourse to achieve pregnancy](http://dx.doi.org/10.1002/sim.2846), Statist. Med. 26, 1920 (2007).
16. D. R. Cavagnaro, M. A. Pitt, and J. I. Myung, [Adaptive Design Optimization in Experiments with People](oks.nips.cc/nips22.html), Advances in Neural Information Processing Systems 22, 234-242 (2010).
17. N. Kantas, A. Lecchini-Visintini, and J. M. Maciejowski, [Simulation-based Bayesian optimal design of aircraft trajectories for air traffic management](http://dx.doi.org/10.1002/acs.1204), Int. J. Adapt. Control Signal Process. 24, 882 (2010).
18. X. Huan and Y. M. Marzouk, [Simulation-based optimal Bayesian experimental design for nonlinear systems](http://arxiv.org/abs/1108.4146) (2011), 1108.4146.
19. F. Huszár and N. M. T. Houlsby, [Adaptive Bayesian quantum tomography](http://dx.doi.org/10.1103/PhysRevA.85.052120), Physical Review A 85 052120 (2012), ISSN 1094-1622, 1107.0895.
20. E. Bagan, M. A. Ballester, R. D. Gill, M. noz Tapia, and O. R. Isart, [Separable Measurement Estimation of Density Matrices and its Fidelity Gap with Collective Protocols](http://dx.doi.org/10.1103/PhysRevLett.97.130501), Physical Review Letters 97, 130501+ (2006).
21. R. A. Servedio and S. J. Gortler, [Equivalences and Separations Between Quantum and Classical Learnability](http://dx.doi.org/10.1137/S0097539704412910), SIAM Journal on Computing 33, 1067 (2004), ISSN 0097-5397.
22. E. Aïmeur, G. Brassard, and S. Gambs, [Machine Learning in a Quantum World](http://dx.doi.org/10.1007/11766247_37), (Springer Berlin / Heidelberg, Berlin, Heidelberg, 2006), vol. 4013 of Lecture Notes in Computer Science, chap. 37, pp. 431-442, ISBN 978-3-540-34628-9.
23. S. Aaronson, [The learnability of quantum states](http://dx.doi.org/10.1098/rspa.2007.0113), Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science 463, 3089-3114 (2007), ISSN 1471-2946.
24. A. Hentschel and B. C. Sanders, [Machine Learning for Precise Quantum Measurement](http://dx.doi.org/10.1103/PhysRevLett.104.063603), Physical Review Letters 104, 063603+ (2010).
25. K. L. Pudenz and D. A. Lidar, [Quantum adiabatic machine learning](http://arxiv.org/abs/1109.0325), (2011), 1109.0325.
26. A. Hentschel and B. C. Sanders, [Efficient Algorithm for Optimizing Adaptive Quantum Metrology Processes](http://dx.doi.org/10.1103/PhysRevLett.107.233601), Physical Review Letters 107, 233601 (2011).
27. A. Sergeevich and S. D. Bartlett, [Optimizing qubit Hamiltonian parameter estimation algorithms using PSO](http://arxiv.org/abs/1206.3830), (2012), 1206.3830.
28. C. M. Caves, [Quantum mechanics of measurements distributed in time. A path-integral formulation](http://link.aps.org/doi/10.1103/PhysRevD.33.1643), Physical Review D 33, 1643 (1986).
29. M. Tsang, [Time-Symmetric Quantum Theory of Smoothing](http://dx.doi.org/10.1103/PhysRevLett.102.250403), Physical Review Letters 102, 250403+ (2009).
30. T. A. Wheatley, et al., [Adaptive Optical Phase Estimation Using Time-Symmetric Quantum Smoothing](http://dx.doi.org/10.1103/PhysRevLett.104.093601) Physical Review Letters 104, 093601+ (2010).
31. D. V. Lindley, [On a Measure of the Information Provided by an Experiment](http://dx.doi.org/10.1214/aoms/1177728069), The Annals of Mathematical Statistics 27, 986 (1956), ISSN 0003-4851.
32. R. S. Said, D. W. Berry, and J. Twamley, [Nanoscale magnetometry using a single-spin system in diamond](http://link.aps.org/doi/10.1103/PhysRevB.83.125410), Phys. Rev. B 83, 125410 (2011).
33. E. L. Lehmann and G. Casella, [Theory of Point Estimation](http://www.amazon.com/exec/obidos/redirect?tag=citeulike07-20&path=ASIN/0387985026) (Springer, 1998), 2nd ed., ISBN 0387985026.
34. J. O. Berger, [Statistical Decision Theory and Bayesian Analysis](http://www.amazon.com/exec/obidos/redirect?tag=citeulike07-20&path=ASIN/0387960988) (Springer, 1985), 2nd ed., ISBN 0387960988.
35. R. Blume-Kohout and P. Hayden, [Accurate quantum state estimation via "Keeping the experimentalist honest"](http://arxiv.org/abs/quant-ph/0603116), (2006), quant-ph/0603116.
36. R. D. Gill and B. Y. Levit, [Applications of the van Trees inequality: a Bayesian Cramér-Rao bound](http://dx.doi.org/10.2307/3318681), Bernoulli 1 59 (1995), ISSN 13507265.
37. P. Tichavsky, C. H. Muravchik, and A. Nehorai, [Posterior Cramer-Rao bounds for discrete-time nonlinear filtering](http://dx.doi.org/10.1109/78.668800), Signal Processing, IEEE Transactions on 46, 1386 (1998), ISSN 1053-587X.
38. N. J. Gordon, D. J. Salmond, and A. F. M. Smith, [Novel approach to nonlinear/non-Gaussian Bayesian state estimation](http://dx.doi.org/10.1049/ip-f-2.1993.0015), Radar and Signal Processing, IEE Proceedings F 140, 107-113 (1993),ISSN 0956-375X.
39. J. Liu and M. West, [Combined parameter and state estimation in simulation-based filtering](http://ftp.stat.duke.edu/WorkingPapers/99-14.html) (Springer-Verlag, 2000).
40. W. Edwards, H. Lindman, and L. J. Savage, [Bayesian statistical inference for psychological research](http://psycnet.apa.org/journals/rev/70/3/193/), Psychological Review 70, 193 (1963), ISSN 1939-1471(Electronic);0033-295X(Print).
41. J. Bernardo, [Intrinsic credible regions: An objective Bayesian approach to interval estimation](http://www.springerlink.com/content/u823757117165122/abstract/), TEST 14, 317 (2005), ISSN 1133-0686.
42. D. Wackerly, W. Mendenhall, and R. L. Scheaffer, Mathematical Statistics with Applications (Duxbury Press, 2001), 6th ed., ISBN 0534377416.
43. E. M. L. Beale, [Confidence Regions in Non-Linear Estimation](http://www.jstor.org/stable/2983877), Journal of the Royal Statistical Society. Series B (Methodological) 22, 41 (1960), ISSN 0035-9246.
44. R. Blume-Kohout, [Robust error bars for quantum tomography](http://arxiv.org/abs/1202.5270) (2012), 1202.5270.
45. M. Christandl and R. Renner, [Reliable Quantum State Tomography](http://arxiv.org/abs/1108.5329), (2011), 1108.5329.
46. M. J. Todd and E. A. Yldrm, [On Khachiyan's algorithm for the computation of minimum-volume enclosing ellipsoids](http://www.sciencedirect.com/science/article/pii/S0166218X07000716), Discrete Applied Mathematics 155, 1731 (2007), ISSN 0166-218X.
47. C. B. Barber, D. P. Dobkin, and H. Huhdanpaa, [The quickhull algorithm for convex hulls](http://doi.acm.org/10.1145/235815.235821), ACM Trans. Math. Softw. 22, 469483 (1996), ISSN 0098-3500.
48. A. Sergeevich, A. Chandran, J. Combes, S. Bartlett, and H. Wiseman, [Characterization of a qubit Hamiltonian using adaptive measurements in a fixed basis](http://dx.doi.org/10.1103/PhysRevA.84.052315), Physical Review A 84 052315 (2011), ISSN 1094-1622, 1102.3700.
49. C. Ferrie, C. E. Granade, and D. G. Cory, [Adaptive Hamiltonian estimation using Bayesian experimental design](http://proceedings.aip.org/resource/2/apcpcs/1443/1/165_1), AIP Conference Proceedings 1443, 165 (2012), ISSN 0094243X.
50. C. Ferrie, C. Granade, and D. Cory, [How to best sample a periodic probability distribution, or on the accuracy of Hamiltonian finding strategies](http://www.springerlink.com/content/130hm02564t34j84/abstract/), Quantum Information Processing Online First pp. 1-13 (2012), ISSN 1570-0755.
51. G. Lindblad, [On the generators of quantum dynamical semigroups](http://projecteuclid.org/euclid.cmp/1103899849), Communications in Mathematical Physics (1965-1997) 48, 119 (1976), ISSN 0010-3616, 1432-0916.
52. N. Boulant, T. F. Havel, M. A. Pravia, and D. G. Cory, [Robust method for estimating the Lindblad operators of a dissipative quantum process from measurements of the density operator at multiple time points](http://dx.doi.org/10.1103/PhysRevA.67.042322), Physical Review A 67, 042322+ (2003).
53. Y. S. Weinstein, T. F. Havel, J. Emerson, N. Boulant, M. Saraceno, S. Lloyd, and D. G. Cory, [Quantum process tomography of the quantum Fourier transform](http://dx.doi.org/10.1063/1.1785151), The Journal of Chemical Physics 121, 6117 (2004).
54. N. Boulant, J. Emerson, T. Havel, D. Cory, and S. Furuta, [Incoherent noise and quantum information processing](http://dx.doi.org/10.1063/1.1773161), The Journal of Chemical Physics 121, 2955 (2004).
55. E. Gutierrez, S. Romero, M. Trenas, and E. Zapata, [Parallel Quantum Computer Simulation on the CUDA Architecture](http://dx.doi.org/10.1007/978-3-540-69384-0_75), in Computational Science ICCS 2008, edited by M. Bubak, G. van Albada, J. Dongarra, and P. Sloot (Springer Berlin / Heidelberg, 2008), vol. 5101 of Lecture Notes in Computer Science, pp. 700-709, ISBN 978-3-540-69383-3.
56. A. Khalid, Z. Zilic, and K. Radecka, [FPGA emulation of quantum circuits](http://dx.doi.org/10.1109/ICCD.2004.1347938), in Computer Design: VLSI in Computers and Processors, 2004. ICCD 2004. Proceedings. IEEE International Conference on (2004), pp. 310-315.
57. E. Jones, T. Oliphant, P. Peterson, et al., [SciPy: Open source scientific tools for Python](http://www.scipy.org/) (2001).

## Affiliations ##

1. <a id="affil1"></a>[Institute for Quantum Computing, University of Waterloo](http://iqc.uwaterloo.ca).
2. <a id="affil2"></a>[Department of Physics, University of Waterloo](https://uwaterloo.ca/physics-astronomy/).
3. <a id="affil3"></a>[Department of Applied Mathematics, University of Waterloo](http://math.uwaterloo.ca/applied-mathematics/).
4. <a id="affil4"></a>[Department of Combinatorics and Optimization, University of Waterloo](http://math.uwaterloo.ca/combinatorics-and-optimization/).
5. <a id="affil5"></a>[Department of Chemistry, University of Waterloo](https://uwaterloo.ca/chemistry/).
6. <a id="affil6"></a>[Perimeter Institute for Theoretical Physics](http://www.perimeterinstitute.ca/).
