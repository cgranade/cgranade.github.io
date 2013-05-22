---
layout: page
title: "Robust Online Hamiltonian Learning"
description: ""
redirects:
- /research/rohl
---
{% include JB/setup %}

**[Chris Granade](/)<sup>[1](#affil1),[2](#affil2)</sup>, [Chris Ferrie](http://csferrie.com/)<sup>[1](#affil1),[3](#affil3)</sup>, [Nathan Wiebe](https://services.iqc.uwaterloo.ca/people/profile/nwiebe/)<sup>[1](#affil1),[4](#affil4)</sup> and [D. G. Cory](http://iqc.uwaterloo.ca/iqc-directory/dcory/)<sup>[1](#affil1),[5](#affil5),[6](#affil6)</sup>**

 > 2012 New Journal of Physics **14** 103013 |
 > [arXiv:1207.1655](http://arxiv.org/abs/1207.1655) | [doi:10.1088/1367-2630/14/10/103013](http://dx.doi.org/10.1088/1367-2630/14/10/103013) 
 
Presented as a poster at [TQC 2013](http://www.uoguelph.ca/quigs/tqc2013/) ([PDF](rohl/tqc-poster.pdf)).
To be presented at [DAMOP 2013](http://www.aps.org/units/damop/meetings/annual/).

## Abstract ##

In this work we combine two distinct machine learning methodologies, sequential Monte Carlo and Bayesian experimental design, and apply them to the problem of inferring the dynamical parameters of a quantum system. We design the algorithm with practicality in mind by including parameters that control trade-offs between the requirements on computational and experimental resources. The algorithm can be implemented online (during experimental data collection), avoiding the need for storage and post-processing. Most importantly, our algorithm is capable of learning Hamiltonian parameters even when the parameters change from experiment-to-experiment, and also when additional noise processes are present and unknown. The algorithm also numerically estimates the Cramer-Rao lower bound, certifying its own performance.

## Software Resources ##

[**QInfer**](https://github.com/csferrie/python-qinfer), a Python-language
implementation of the algorithm presented in this work, is
[available from GitHub](https://github.com/csferrie/python-qinfer).

## Bibliography ##

1. M. Paris and J. Rehacek, eds., Quantum State Estimation, vol. 649 of Lecture Notes in Physics (Springer, 2004), ISBN 978-3-540-22329-0, URL http://www.springer.com/physics/quantum+physics/book/978-3-540-22329-0.
2. B. P. Lanyon, C. Hempel, D. Nigg, M. Müller, R. Gerritsma, F. Zhringer, P. Schindler, J. T. Barreiro, M. Rambach, G. Kirchmair, et al., Science 334, 57 (2011), http://www.sciencemag.org/content/334/6052/57.full.pdf, URL http://www.sciencemag.org/content/334/6052/57.abstract.
3. R. Gerritsma, B. P. Lanyon, G. Kirchmair, F. Zähringer, C. Hempel, J. Casanova, J. J. Garcia-Ripoll, E. Solano, R. Blatt, and C. F. Roos, Phys. Rev. Lett. 106, 060503 (2011), URL http://link.aps.org/doi/10.1103/PhysRevLett.106.060503. 
4. K. Kim, M.-S. Chang, S. Korenblit, R. Islam, E. E. Edwards, J. K. Freericks, G.-D. Lin, L.-M. Duan, and C. Monroe, Nature (London) 465, 590 (2010).
5. A. Bendersky, F. Pastawski, and J. P. Paz, Phys. Rev. Lett. 100, 190403 (2008), URL http://link.aps.org/doi/10.1103/PhysRevLett.100.190403.
6. A. Bendersky, F. Pastawski, and J. P. Paz, Phys. Rev. A 80, 032116 (2009), URL http://link.aps.org/doi/10.1103/PhysRevA.80.032116.
7. M. Mohseni and A. T. Rezakhani, Phys. Rev. A 80, 010101 (2009), URL http://link.aps.org/doi/10.1103/PhysRevA.80.010101.
8. M. P. A. Branderhorst, J. Nunn, I. A. Walmsley, and R. L. Kosut, New Journal of Physics 11, 115010 (2009), URLhttp://stacks.iop.org/1367-2630/11/i=11/a=115010.
9. S. T. Flammia and Y. K. Liu, Physical Review Letters 106, 230501+ (2011), URL http://dx.doi.org/10.1103/PhysRevLett.106.230501.
10. M. P. da Silva, O. L. Cardinal, and D. Poulin, Physical Review Letters 107, 210404+ (2011), URL http://dx.doi.org/10.1103/PhysRevLett.107.210404.
11. D. Oi and S. Schirmer (2012), 1202.5779, URL http://arxiv.org/abs/1202.5779.
12. A. Doucet and A. M. Johansen, A Tutorial on Particle Filtering and Smoothing: Fifteen Years Later (Oxford University Press, 2009), URL http://www.cs.ubc.ca/~arnaud/doucet_johansen_tutorialPF.pdf.
13. T. J. Loredo, AIP Conference Proceedings 707, 330 (2004), URL http://dx.doi.org/10.1063/1.1751377.
14. H. Kuck, N. de Freitas, and A. Doucet, in Nonlinear Statistical Signal Processing Workshop, 2006 IEEE (IEEE, 2006), pp. 99{102, ISBN 978-1-4244-0581-7, URL http://dx.doi.org/10.1109/NSSPW.2006.4378829.
15. B. Scarpa and D. B. Dunson, Statist. Med. 26, 1920 (2007), URL http://dx.doi.org/10.1002/sim.2846.
16. D. R. Cavagnaro, M. A. Pitt, and J. I. Myung, Advances in Neural Information Processing Systems 22, 234{242 (2010).
17. N. Kantas, A. Lecchini-Visintini, and J. M. Maciejowski, Int. J. Adapt. Control Signal Process. 24, 882 (2010), URL http://dx.doi.org/10.1002/acs.1204.
18. X. Huan and Y. M. Marzouk (2011), 1108.4146, URL http://arxiv.org/abs/1108.4146.22
19. F. Husz.ar and N. M. T. Houlsby, Physical Review A 85 052120 (2012), ISSN 1094-1622, 1107.0895, URL http://dx.doi.org/10.1103/PhysRevA.85.052120.
20. E. Bagan, M. A. Ballester, R. D. Gill, M. noz Tapia, and O. R. Isart, Physical Review Letters 97, 130501+ (2006), URL http://dx.doi.org/10.1103/PhysRevLett.97.130501.
21. R. A. Servedio and S. J. Gortler, SIAM Journal on Computing 33, 1067 (2004), ISSN 0097-5397, URL http://dx.doi.org/10.1137/S0097539704412910.
22. E. A.meur, G. Brassard, and S. Gambs (Springer Berlin / Heidelberg, Berlin, Heidelberg, 2006), vol. 4013 of Lecture Notes in Computer Science, chap. 37, pp. 431{442, ISBN 978-3-540-34628-9, URL http://dx.doi.org/10.1007/11766247_37.
23. S. Aaronson, Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science 463, 3089{3114 (2007), ISSN 1471-2946, URL http://dx.doi.org/10.1098/rspa.2007.0113.
24. A. Hentschel and B. C. Sanders, Physical Review Letters 104, 063603+ (2010), URL http://dx.doi.org/10.1103/ PhysRevLett.104.063603.
25. K. L. Pudenz and D. A. Lidar (2011), 1109.0325, URL http://arxiv.org/abs/1109.0325.
26. A. Hentschel and B. C. Sanders, Physical Review Letters 107, 233601 (2011), URL http://dx.doi.org/10.1103/PhysRevLett.107.233601.
27. A. Sergeevich and S. D. Bartlett (2012), 1206.3830, URL http://arxiv.org/abs/1206.3830.
28. C. M. Caves, Physical Review D 33, 1643 (1986), URL http://link.aps.org/doi/10.1103/PhysRevD.33.1643.
29. M. Tsang, Physical Review Letters 102, 250403+ (2009), URL http://dx.doi.org/10.1103/PhysRevLett.102.250403.
30. T. A. Wheatley, D. W. Berry, H. Yonezawa, D. Nakane, H. Arao, D. T. Pope, T. C. Ralph, H. M. Wiseman, A. Furusawa, and E. H. Huntington, Physical Review Letters 104, 093601+ (2010), URL http://dx.doi.org/10.1103/PhysRevLett.104.093601.
31. D. V. Lindley, The Annals of Mathematical Statistics 27, 986 (1956), ISSN 0003-4851, URL http://dx.doi.org/10.1214/aoms/1177728069.
32. R. S. Said, D. W. Berry, and J. Twamley, Phys. Rev. B 83, 125410 (2011), URL http://link.aps.org/doi/10.1103/PhysRevB.83.125410.
33. E. L. Lehmann and G. Casella, Theory of Point Estimation (Springer, 1998), 2nd ed., ISBN 0387985026, URL http://www.amazon.com/exec/obidos/redirect?tag=citeulike07-20&path=ASIN/0387985026.
34. J. O. Berger, Statistical Decision Theory and Bayesian Analysis (Springer, 1985), 2nd ed., ISBN 0387960988, URL http://www.amazon.com/exec/obidos/redirect?tag=citeulike07-20&path=ASIN/0387960988.
35. R. Blume-Kohout and P. Hayden (2006), quant-ph/0603116, URL http://arxiv.org/abs/quant-ph/0603116.
36. R. D. Gill and B. Y. Levit, Bernoulli 1 59 (1995), ISSN 13507265, URL http://dx.doi.org/10.2307/3318681.
37. P. Tichavsky, C. H. Muravchik, and A. Nehorai, Signal Processing, IEEE Transactions on 46, 1386 (1998), ISSN 1053-587X, URL http://dx.doi.org/10.1109/78.668800.
38. N. J. Gordon, D. J. Salmond, and A. F. M. Smith, Radar and Signal Processing, IEE Proceedings F 140, 107{113 (1993),ISSN 0956-375X, URL http://dx.doi.org/10.1049/ip-f-2.1993.0015.
39. J. Liu and M. West, Combined parameter and state estimation in simulation-based .ltering (Springer-Verlag, 2000).
40. W. Edwards, H. Lindman, and L. J. Savage, Psychological Review 70, 193 (1963), ISSN 1939-1471(Electronic);0033-295X(Print).
41. J. Bernardo, TEST 14, 317 (2005), ISSN 1133-0686, URL http://www.springerlink.com/content/u823757117165122/abstract/.
42. D. Wackerly, W. Mendenhall, and R. L. Schea.er, Mathematical Statistics with Applications (Mathematical Statistics(Duxbury Press, 2001), 6th ed., ISBN 0534377416.
43. E. M. L. Beale, Journal of the Royal Statistical Society. Series B (Methodological) 22, 41 (1960), ISSN 0035-9246, ArticleType: research-article / Full publication date: 1960 / Copyright 1960 Royal Statistical Society, URL http://www.jstor.org/stable/2983877.
44. R. Blume-Kohout, Robust error bars for quantum tomography (2012), 1202.5270, URL http://arxiv.org/abs/1202.5270.
45. M. Christandl and R. Renner (2011), 1108.5329, URL http://arxiv.org/abs/1108.5329.
46. M. J. Todd and E. A. Yldrm, Discrete Applied Mathematics 155, 1731 (2007), ISSN 0166-218X, URL http://www.sciencedirect.com/science/article/pii/S0166218X07000716.
47. C. B. Barber, D. P. Dobkin, and H. Huhdanpaa, ACM Trans. Math. Softw. 22, 469483 (1996), ISSN 0098-3500, URL http://doi.acm.org/10.1145/235815.235821.
48. A. Sergeevich, A. Chandran, J. Combes, S. Bartlett, and H. Wiseman, Physical Review A 84 052315 (2011), ISSN 1094-1622, 1102.3700, URL http://dx.doi.org/10.1103/PhysRevA.84.052315.
49. C. Ferrie, C. E. Granade, and D. G. Cory, AIP Conference Proceedings 1443, 165 (2012), ISSN 0094243X, URL http://proceedings.aip.org/resource/2/apcpcs/1443/1/165_1?isAuthorized=no.
50. C. Ferrie, C. Granade, and D. Cory, Quantum Information Processing Online First pp. 1{13 (2012), ISSN 1570-0755, URL http://www.springerlink.com/content/130hm02564t34j84/abstract/.
51. G. Lindblad, Communications in Mathematical Physics (1965-1997) 48, 119 (1976), ISSN 0010-3616, 1432-0916, URL http://projecteuclid.org/euclid.cmp/1103899849.
52. N. Boulant, T. F. Havel, M. A. Pravia, and D. G. Cory, Physical Review A 67, 042322+ (2003), URL http://dx.doi.org/10.1103/PhysRevA.67.042322.
53. Y. S. Weinstein, T. F. Havel, J. Emerson, N. Boulant, M. Saraceno, S. Lloyd, and D. G. Cory, The Journal of Chemical Physics 121, 6117 (2004), URL http://dx.doi.org/10.1063/1.1785151.
54. N. Boulant, J. Emerson, T. Havel, D. Cory, and S. Furuta, The Journal of Chemical Physics 121, 2955 (2004), URL http://dx.doi.org/10.1063/1.1773161.
55. E. Gutierrez, S. Romero, M. Trenas, and E. Zapata, in Computational Science ICCS 2008, edited by M. Bubak, G. van Albada, J. Dongarra, and P. Sloot (Springer Berlin / Heidelberg, 2008), vol. 5101 of Lecture Notes in Computer Science, pp. 700{709, ISBN 978-3-540-69383-3, URL http://dx.doi.org/10.1007/978-3-540-69384-0_75.
56. A. Khalid, Z. Zilic, and K. Radecka, in Computer Design: VLSI in Computers and Processors, 2004. ICCD 2004. Proceedings. IEEE International Conference on (2004), pp. 310-315, URL http://dx.doi.org/10.1109/ICCD.2004.1347938.
57. E. Jones, T. Oliphant, P. Peterson, et al., SciPy: Open source scientific tools for Python (2001), URL http://www.scipy.org/.

## Affiliations ##

1. <a id="affil1"></a>Institute for Quantum Computing, University of Waterloo.
2. <a id="affil2"></a>Department of Physics, University of Waterloo.
3. <a id="affil3"></a>Department of Applied Mathematics, University of Waterloo.
4. <a id="affil4"></a>Department of Combinatorics and Optimization, University of Waterloo.
5. <a id="affil5"></a>Department of Chemistry, University of Waterloo.
6. <a id="affil6"></a>Perimeter Institute for Theoretical Physics.
