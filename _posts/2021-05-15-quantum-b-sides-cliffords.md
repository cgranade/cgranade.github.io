---
layout: post
title: "Quantum B-Sides: The Clifford Group"
---

## The Quantum B-Sides

Now that _Learn Quantum Computing with Python and Q#_ is on its way to the printers (pre-order your copy at [bit.ly/qsharp-book](https://bit.ly/qsharp-book)!), I wanted to take the opportunity to go over a few quantum computing topics that didn't quite make the cut for our book. These topics are a little more advanced, a little more niche, or otherwise just didn't make a great fit for a first foray into quantum computing.

Just like with a good B-side track, though, these's nothing wrong at all with any of the topics that didn't make the cut! There's too much to make it into any one book, after all. My hope with this Quantum B-Sides series of posts is to show some of the directions you may want to keep exploring and learning after you've explored some of the basics of quantum computing, as well as to show some really neat alternative ways of thinking about what quantum computing even is.

Taking that tack, the B-Sides posts will assume you're OK with some of the basics:

- Linear algebra and complex numbers
- Quantum states and operations (i.e.: gates and measurements)
- Dirac notation (_a.k.a._ bra–ket notation)
- Using [QuTiP](http://qutip.org/) to work with states, unitary operators, and measurements
- Using [Q# and the Quantum Development Kit](https://azure.microsoft.com/resources/development-kit/quantum-computing/) to write and simulate quantum programs

If you're new to quantum computing, or just need a refresher, that's great! You may find it helpful to start off with [_Learn Quantum Computing with Python and Q#_](https://bit.ly/qsharp-book) (available June 2021), then coming back to these posts when you've had a bit of practice with the basics.

Regardless of where you're at in your quantum journey, thanks for joining me in exploring some of these interesting tangents. If it ever seems a bit overwhelming, remember how far you've already come in understanding quantum computing — you've got this too. If you need some help, there's nothing wrong with that, either! There's an amazing community of folks helping each other understand all of the exciting stuff there is to learn about quantum computing!

- [Q# Community Discord server](http://discord.qsharp.community/)
- [Unitary Fund Discord server](http://discord.unitary.fund/)
- [Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com/)

If you'd like to follow along with the examples here, check out the code repository at [cgranade/quantum-b-sides](https://github.com/cgranade/quantum-b-sides), or try without installing on [mybinder.org](https://mybinder.org/v2/gh/cgranade/quantum-b-sides).

### Previous Quantum B-Sides posts:

- []() <!-- TODO: link to stabilizers here. -->

## Intro

Equipped with the stabilizer formalism, you've got a powerful tool for manipulating quantum programs and understanding how they work. In this post, we'll look at a few examples of how the stabilizer formalism can help not just represent states, but understand how quantum states evolve throughout the course of a program.

By the end of the post, you'll have everything you need to understand how stabilizer simulators work, and how you can use them to simulate your own quantum programs.

<figure>
    <img src="/assets/figures/get-equipped-stabilizer.png" alt="GET EQUIPPED WITH THE STABILIZER FORMALISM.">
    <caption>Image courtesy of <a href="https://deathgenerator.com/">The Death Generator</a>.</caption>
</figure>

## 