---
layout: post
title: "Quantum B-Sides: The Stabilizer Formalism"
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

## Intro

One of the exciting things that Sarah and I just didn't have the time to cover in our book was another way that you can think about what quantum states are, not in terms of vectors, but rather in terms of something called the _stabilizer formalism_. This way of thinking about states is really useful in a few different areas of quantum computing, such as error correction or quantum characterization, and can even allow for exponential speedups in simulating quantum programs. On the other hand, we'll see that stabilizers also come along with a lot of limitations.

Regardless, it's a really neat alternative way to think about what quantum computing is, so if you're interested in taking the next steps along your quantum journey, the stabilizer formalism can be a lot of fun.

## Why not vectors?

By way of context, it helps to revisit a little bit of what a quantum state is in the first place. Typically, if we have an {% katex inline %}n{% endkatex %}-qubit register, we think of a state {% katex inline %}\ket{\psi}{% endkatex %} of that register as being a _vector_ with {% katex inline %}2^n{% endkatex %} complex elements; one for each possible classical bit string on {% katex inline %}n{% endkatex %} bits.

For example, when we write out a state in Dirac notation like {% katex inline %}\ket{00}{% endkatex %}, we could have also written that same state out as a vector on four elements:

{% katex display %}
\begin{aligned}
    \ket{00} = \left( \begin{matrix}
        1 \\ 0 \\ 0 \\ 0
    \end{matrix} \right).
\end{aligned}
{% endkatex %}

As our system gets larger and larger, this gets more and more unwieldy. Even at three qubits, things get big in a hurry:

{% katex display %}
\begin{aligned}
    \frac{1}{\sqrt{2}} \left(
        \ket{000} +
        \ket{111}
    \right) = \frac{1}{\sqrt{2}} \left( \begin{matrix}
        1 \\ 0 \\ 0 \\ 0 \\
        0 \\ 0 \\ 0 \\ 1
    \end{matrix} \right).
\end{aligned}
{% endkatex %}

Many of the states we work with, however, have patterns that we should be able to exploit to avoid having to write down gigantic vectors all the time. We see some of that when we use Dirac notation, of course; writing down {% katex inline %}\ket{++++++++}{% endkatex %} is a heck of a lot easier than writing down a vector with 256 ones.

Given that, it'd be really nice to have a more compact representation for states that lets us take advantage of these kinds of patterns in a formal way. In particular, when we do so formally, that makes it much easier to write simulators and other programs that take advantage of that representation.

To go on and do that, however, it helps to take a moment and recall a very useful idea from linear algebra: eigenvectors.

## Eigenvectors and eigenvalues revisited

Recall that if we have a matrix {% katex inline %}A{% endkatex %} and a vector {% katex inline %}\vec{x}{% endkatex %} such that {% katex inline %}A\vec{x} = \lambda\vec{x}{% endkatex %} for some number {% katex inline %}\lambda{% endkatex %}, then we say that {% katex inline %}\vec{x}{% endkatex %} is an _eigenvector_ of {% katex inline %}A{% endkatex %} with _eigenvalue_ {% katex inline %}\lambda{% endkatex %}.

Thinking of quantum states as vectors, the exact same thing holds; we'll often call states that are eigenvectors of some operator _eigenstates_. For example, {% katex inline %}\ket{0}{% endkatex %} is an eigenstate of {% katex inline %}Z{% endkatex %} since {% katex inline %}Z\ket{0} = (+1) \ket{0}{% endkatex %}.

> **TIP**: You can also use QuTiP to calculate eigenstates and eigenvectors of different operators. For example, to find the eigenstates of the {% katex inline %}X{% endkatex %} operator:
>
> ```python
> >>> import qutip as qt
> >>> qt.sigmax().eigenstates()
> (array([-1.,  1.]), array([Quantum object: dims = [[2], [1]], shape = (2, 1), type = ket
> Qobj data =
> [[-0.70710678]
>  [ 0.70710678]],
>        Quantum object: dims = [[2], [1]], shape = (2, 1), type = ket
> Qobj data =
> [[0.70710678]
>  [0.70710678]]], dtype=object))
> ```
>
> This output tells us that {% katex inline %}\ket{+} = \frac{1}{\sqrt{2}}(\ket{0} + \ket{1}){% endkatex %} is a {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}X{% endkatex %}, and that {% katex inline %}\ket{-} = \frac{1}{\sqrt{2}}(\ket{0} - \ket{1}){% endkatex %} is a {% katex inline %}-1{% endkatex %} eigenstate.

We can turn it around, too! If I tell you that a particular state {% katex inline %}\ket{\psi}{% endkatex %} is an eigenstate of {% katex inline %}Z{% endkatex %} with an eigenvalue of {% katex inline %}+1{% endkatex %}, then you can conclude that {% katex inline %}\ket{\psi}{% endkatex %} _must_ be {% katex inline %}\ket{0}{% endkatex %}. Similarly, if I tell you that a particular state is a {% katex inline %}-1{% endkatex %} eigenvector of {% katex inline %}X{% endkatex %}, then you can conclude that I must be thinking  of {% katex inline %}\ket{-} = \frac{1}{\sqrt{2}}\left(\ket{0} - \ket{1}\right){% endkatex %}.

Altogether, I can specify six different single-qubit state this way. We'll see more about why in a bit, but these six states form what's called the _stabilizer polytope_.

<figure>
    <img src="/assets/figures/stabilizer-polytope.png" alt="The stabilizer polytope; an eight-sided Platonic solid inscribed in a sphere.">
    <caption>The stabilizer polytope for a single qubit. Image courtesy of Dr Sarah Kaiser.</caption>
</figure>

<table>
    <thead>
        <tr>
            <th>Dirac notation</th>
            <th>Vector notation</th>
            <th>Eigenstate constraint</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{% katex inline %}\ket{0}{% endkatex %}</td>
            <td>{% katex inline %}\left(\begin{matrix} 1 \\ 0 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}Z{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\ket{1}{% endkatex %}</td>
            <td>{% katex inline %}\left(\begin{matrix} 0 \\ 1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}-1{% endkatex %} eigenstate of {% katex inline %}Z{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\ket{+}{% endkatex %}</td>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\begin{matrix} 1 \\ 1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}X{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\ket{-}{% endkatex %}</td>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\begin{matrix} 1 \\ -1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}-1{% endkatex %} eigenstate of {% katex inline %}X{% endkatex %}</td>
        </tr>
    </tbody>
</table>


As it turns out, we can generalize this to multiple qubits as well. Every tensor product of Pauli operators other than the all-identity operator {% katex inline %}1\!\!1 \otimes 1\!\!1 \otimes \cdots \otimes 1\!\!1{% endkatex %} has an equal number of {% katex inline %}+1{% endkatex %} and {% katex inline %}-1{% endkatex %} eigenstates. For example,
{% katex display %}
\begin{aligned}
    Z \otimes Z = \left( \begin{matrix}
        1 & 0 & 0 & 0 \\
        0 & -1 & 0 & 0 \\
        0 & 0 & -1 & 0 \\
        0 & 0 & 0 & 1
    \end{matrix} \right)
\end{aligned}
{% endkatex %}
has {% katex inline %}+1{% endkatex %} eigenstates {% katex inline %}\ket{00}{% endkatex %} and {% katex inline %}\ket{11}{% endkatex %}, and has {% katex inline %}-1{% endkatex %} eigenstates {% katex inline %}\ket{01}{% endkatex %} and {% katex inline %}\ket{10}{% endkatex %}.

Thus, if I tell you that a state {% katex inline %}\ket{\psi}{% endkatex %} is a {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}Z \otimes Z{% endkatex %}, then you know it can be either {% katex inline %}\ket{00}{% endkatex %} or {% katex inline %}\ket{11}{% endkatex %}. In this case, though, since {% katex inline %}\ket{00}{% endkatex %} and {% katex inline %}\ket{11}{% endkatex %} are two different eigenstates with the same eigenvalue, any linear combination {% katex inline %}\alpha \ket{00} + \beta \ket{11}{% endkatex %} is also a {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}Z \otimes Z{% endkatex %}:

{% katex display %}
\begin{aligned}
    (Z \otimes Z) \left(\alpha \ket{00} + \beta \ket{11}\right) & =
        \left(\alpha (Z \otimes Z) \ket{00} + \beta (Z \otimes Z) \ket{11}\right) \\
    & =
        \left(\alpha (+1) \ket{00} + \beta (+1) \ket{11}\right) \\
    & =
        \left(\alpha \ket{00} + \beta \ket{11}\right).
\end{aligned}
{% endkatex %}

One way to think of this is that my telling you that {% katex inline %}\ket{\psi}{% endkatex %} is a {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}Z \otimes Z{% endkatex %} cuts down the space of possible states by a factor of two — that is, precisely by the same amount as removing a single qubit from the register.

> **TIP**: This is not at all a coincidence. In a future post, we'll see that another way of thinking of the constraint that {% katex inline %}\ket{\psi}{% endkatex %} is a {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}Z \otimes Z{% endkatex %} is as a constraint that performing the Q# measurement `Measure([PauliZ, PauliZ], [q0, q1])` on the register `[q0, q1]` must always return `Zero`. Constraining one classical bit worth of measurement results cuts down the space of possible states by one qubit.

We can get back down to a single possible state by specifying another eigenvalue constraint. For instance, if I tell you that {% katex inline %}\ket{\psi}{% endkatex %} is _both_ a {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}Z \otimes Z{% endkatex %} and {% katex inline %}X \otimes X{% endkatex %}, there's again precisely one possible state that {% katex inline %}\ket{\psi}{% endkatex %} could be: {% katex inline %}\ket{\psi} = \frac{1}{\sqrt{2}} \left(\ket{00} + \ket{11}\right){% endkatex %}.

To see this, let's start by checking that {% katex inline %}\ket{\psi}{% endkatex %} is indeed an eigenstate of {% katex inline %}(Z \otimes Z){% endkatex %}:
{% katex display %}
\begin{aligned}
    \ket{\psi} & = \frac{1}{\sqrt{2}} \left(\ket{00} + \ket{11}\right) \\
    (Z\otimes Z) \ket{\psi} & = \frac{1}{\sqrt{2}} (Z\otimes Z) \left(\ket{00} + \ket{11}\right) \\
    & =
        \frac{1}{\sqrt{2}} \left((Z\otimes Z) \ket{00} + (Z\otimes Z) \ket{11}\right) \\
    & =
        \frac{1}{\sqrt{2}} \left((+1) \ket{00} + (+1) \ket{11}\right) \\
    & =
        \frac{1}{\sqrt{2}} \left(\ket{00} + \ket{11}\right) \\
    & = \ket{\psi}.
\end{aligned}
{% endkatex %}

We can also check the above using QuTiP, and have Python work out the math for us:

```python
In [1]: import qutip as qt
In [2]: I = qt.qeye(2)
In [3]: X = qt.sigmax()
In [4]: Y = qt.sigmay()
In [5]: Z = qt.sigmaz()
In [6]: ZZ = qt.tensor(Z, Z)
In [7]: ket0 = qt.basis(2, 0)
In [8]: ket1 = qt.basis(2, 1)
# Using the unit() method here tells QuTiP to automatically divide by the
# √2 that we need for psi to be a valid state.
In [9]: psi = (qt.tensor(ket0, ket0) + qt.tensor(ket1, ket1)).unit()
In [10]: psi
Out[10]:
Quantum object: dims = [[2, 2], [1, 1]], shape = (4, 1), type = ket
Qobj data =
[[0.70710678]
 [0.        ]
 [0.        ]
 [0.70710678]]

In [11]: ZZ * psi
Out[11]:
Quantum object: dims = [[2, 2], [1, 1]], shape = (4, 1), type = ket
Qobj data =
[[0.70710678]
 [0.        ]
 [0.        ]
 [0.70710678]]

In [12]: psi == ZZ * psi
Out[12]: True
```

To check that {% katex inline %}\ket{\psi}{% endkatex %} is an eigenstate of {% katex inline %}X \otimes X{% endkatex %}, we can make use of a really helpful trick. Namely, we can use that {% katex inline %}\ket{00} + \ket{11} = \ket{++} + \ket{--}{% endkatex %}:

```python
In [13]: ket_plus = (ket0 + ket1).unit()
In [14]: ket_minus = (ket0 - ket1).unit()
In [15]: psi == (qt.tensor(ket_plus, ket_plus) + qt.tensor(ket_minus, ket_minus)).unit()
Out[15]: True
```

Thus, the proof that {% katex inline %}\ket{\psi}{% endkatex %} is a {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}X \otimes X{% endkatex %} is precisely the same as the proof that it is an eigenstate of {% katex inline %}Z \otimes Z{% endkatex %}.

Each of the {% katex inline %}Z \otimes Z{% endkatex %} and {% katex inline %}X \otimes X{% endkatex %} constraints tells us something different about {% katex inline %}\ket{\psi}{% endkatex %}, narrowing down to that {% katex inline %}\frac{1}{\sqrt{2}}\left(\ket{00} + \ket{11}\right){% endkatex %} is the only possible state that satisfies both constraints.

This is the core idea behind the stabilizer formalism for quantum mechanics: it tells us that we can describe a special set of states by making tables of what Pauli operators leave those states invariant. To see how this all comes together, though, we need one more bit of math to help us out.

## Getting the group together

One really helpful concept from mathematics that comes up in a huge number of surprising ways is that of a _group_. Basically, a group is a kind of abstraction of what it means to add or multiply two things together. We say that a particular set {% katex inline %}G{% endkatex %} is a group if it follows a few different rules:

- The product of any two elements {% katex inline %}g{% endkatex %} and {% katex inline %}h{% endkatex %} of {% katex inline %}G{% endkatex %} is also an element of {% katex inline %}G{% endkatex %}.
- {% katex inline %}G{% endkatex %} has an identity element {% katex inline %}e{% endkatex %}, such that {% katex inline %}g e = e g = g{% endkatex %} for all elements {% katex inline %}g{% endkatex %} in {% katex inline %}S{% endkatex %}.
- Every element {% katex inline %}g{% endkatex %} in {% katex inline %}G{% endkatex %} has an _inverse_ {% katex inline %}g^{-1}{% endkatex %} such that {% katex inline %}g g^{-1} = g^{-1} g = e{% endkatex %}.
- For all elements {% katex inline %}a, b, c \in G{% endkatex %}, we can put parentheses wherever we want when multiplying {% katex inline %}a{% endkatex %}, {% katex inline %}b{% endkatex %}, and {% katex inline %}c{% endkatex %} together: {% katex inline %}a(bc) = (ab)c{% endkatex %}. That is, multiplication has to be _associative_.

You've probably already seen several examples of groups already on your quantum journey. For example, unitary matrices acting on {% katex inline %}n{% endkatex %}-qubit states make a group, since the identity matrix {% katex inline %}1\!\!1{% endkatex %} is unitary, since every unitary matrix {% katex inline %}U{% endkatex %} has an inverse {% katex inline %}U^{-1} = U^{\dagger}{% endkatex %}, and since matrix multiplication is associative. The only rule left to check is that {% katex inline %}UV{% endkatex %} is unitary for any unitary matrices {% katex inline %}U{% endkatex %} and {% katex inline %}V{% endkatex %}. We can convince ourselves of that by noticing that {% katex inline %}(UV)^{\dagger} = V^{\dagger} U^{\dagger}{% endkatex %} such that {% katex inline %}(UV)^{\dagger} UV = V^{\dagger} U^{\dagger} U V = V^{\dagger} V = 1\!\!1{% endkatex %}.

As another example, tensor products of Pauli operators also are a group if we include global phases in front of each. The rule that every group has to have an identity is pretty easy to satisfy, since {% katex inline %}1\!\!1 \otimes 1\!\!1 \otimes \cdots \otimes 1\!\!1{% endkatex %} is a tensor product of Pauli operators. Since matrix multiplication is already associative, we again get that tensor products of Pauli operators satisfy the rule that groups are associative. Even more convenient, every Pauli operator is its own inverse (e.g.: {% katex inline %}X \cdot X = 1\!\!1{% endkatex %}), so that rule is also easy to satisfy. The last thing we need to prove is that the product of two different tensor products of Pauli operators is also a tensor product of Pauli operators, up to a phase.

Here again, we can use QuTiP to check that rule:

```python
In [16]: X * Y == 1j * Z
Out[16]: True

In [17]: Y * Z == 1j * X
Out[17]: True

In [18]: Z * X == 1j * Y
Out[18]: True
```

What's really neat about thinking of Pauli operators as a group is that we can describe how they multiply together without needing to write down matrices explicitly. If you know how {% katex inline %}X{% endkatex %}, {% katex inline %}Y{% endkatex %}, and {% katex inline %}Z{% endkatex %} all multiply together, then that's all you need to write down {% katex inline %}\mathcal{P}_n{% endkatex %}, the _Pauli group_ on {% katex inline %}n{% endkatex %} qubits. For example,

{% katex display %}
\begin{aligned}
    \mathcal{P}_1 & = \left\{
        1\!\!1, i1\!\!1, -1\!\!1, -i1\!\!1,
        X, iX, -X, -iX, \right. \\
    & \qquad \left.
        Y, iY, -Y, -iY,
        Z, iZ, -Z, -iZ
    \right\} \\
    \mathcal{P}_2 & = \Big\{ \\
        & \qquad (1\!\!1 \otimes 1\!\!1), i(1\!\!1 \otimes 1\!\!1), -(1\!\!1 \otimes 1\!\!1), -i(1\!\!1 \otimes 1\!\!1), \\
        & \qquad (1\!\!1 \otimes X), i(1\!\!1 \otimes X), -(1\!\!1 \otimes X), -i(1\!\!1 \otimes X), \\
        & \qquad (1\!\!1 \otimes Y), i(1\!\!1 \otimes Y), -(1\!\!1 \otimes Y), -i(1\!\!1 \otimes Y), \\
        & \qquad (1\!\!1 \otimes Z), i(1\!\!1 \otimes Z), -(1\!\!1 \otimes Z), -i(1\!\!1 \otimes Z), \\
        & \qquad (X \otimes 1\!\!1), i(X \otimes 1\!\!1), -(X \otimes 1\!\!1), -i(X \otimes 1\!\!1), \\
        & \qquad (X \otimes X), i(X \otimes X), -(X \otimes X), -i(X \otimes X), \\
        & \qquad (X \otimes Y), i(X \otimes Y), -(X \otimes Y), -i(X \otimes Y), \\
        & \qquad (X \otimes Z), i(X \otimes Z), -(X \otimes Z), -i(X \otimes Z), \\
        & \qquad (Y \otimes 1\!\!1), i(Y \otimes 1\!\!1), -(Y \otimes 1\!\!1), -i(Y \otimes 1\!\!1), \\
        & \qquad (Y \otimes X), i(Y \otimes X), -(Y \otimes X), -i(Y \otimes X), \\
        & \qquad (Y \otimes Y), i(Y \otimes Y), -(Y \otimes Y), -i(Y \otimes Y), \\
        & \qquad (Y \otimes Z), i(Y \otimes Z), -(Y \otimes Z), -i(Y \otimes Z), \\
        & \qquad (Z \otimes 1\!\!1), i(Z \otimes 1\!\!1), -(Z \otimes 1\!\!1), -i(Z \otimes 1\!\!1), \\
        & \qquad (Z \otimes X), i(Z \otimes X), -(Z \otimes X), -i(Z \otimes X), \\
        & \qquad (Z \otimes Y), i(Z \otimes Y), -(Z \otimes Y), -i(Z \otimes Y), \\
        & \qquad (Z \otimes Z), i(Z \otimes Z), -(Z \otimes Z), -i(Z \otimes Z)  \\
    & \hphantom{=} \Big\}
\end{aligned}
{% endkatex %}

<figure>
    <img src="/assets/figures/less-painful-way.png" alt="There has to be a less painful way to write that.">
    <caption>Image courtesy of <a href="https://deathgenerator.com/">The Death Generator</a>.</caption>
</figure>

We can make the Pauli group a lot simpler to write down by using a nice bit of mathematical notation called a _presentation_. Effectively, a presentation says "take these elements, their inverses, all their products, all products of those, too, and keep going until you get everything in the group." For example, we can write down that {% katex inline %}\mathcal{P}_1 = \left\langle i1\!\!1, X, Z \right\rangle{% endkatex %}, since you can get any other single-qubit Pauli matrix by combinations of {% katex inline %}X{% endkatex %}, {% katex inline %}Z{% endkatex %} and a global phase.

In the same way, {% katex inline %}\mathcal{P}_2 = \left\langle i(1\!\!1 \otimes 1\!\!1), (X \otimes 1\!\!1), (1\!\!1 \otimes X), (Z \otimes 1\!\!1), (1\!\!1 \otimes Z)\right\rangle{% endkatex %}.

Using presentations makes it much easier to see that we actually have already seen yet another important example of a group: those operators for which a given state is a {% katex inline %}+1{% endkatex %} eigenstate! Suppose that a particular state {% katex inline %}\ket{\psi}{% endkatex %} is a {% katex inline %}+1{% endkatex %} eigenstate of both {% katex inline %}U{% endkatex %} and {% katex inline %}V{% endkatex %}; then, {% katex inline %}\ket{\psi}{% endkatex %} is also a {% katex inline %}+1{% endkatex %} eigenstate of both {% katex inline %}UV{% endkatex %} and {% katex inline %}VU{% endkatex %}:

{% katex display %}
\begin{aligned}
    UV \ket{\psi} & = (+1) U\ket{\psi} = (+1) (+1) \ket{\psi} = \ket{\psi} \\
    VU \ket{\psi} & = (+1) V\ket{\psi} = (+1) (+1) \ket{\psi} = \ket{\psi}
\end{aligned}
{% endkatex %}

That is, those matrices that have {% katex inline %}\ket{\psi}{% endkatex %} as a {% katex inline %}+1{% endkatex %} eigenstate form a group {% katex inline %}\left\langle U, V\right\rangle{% endkatex %}! Groups of operators that leave either a single state or a set of states invariant are called _stabilizer groups_. For example:

{% katex display %}
    \mathrm{stab}\left(
        \frac{1}{\sqrt{2}} \left(\ket{00} + \ket{11}\right)
    \right) = \left\langle
        X \otimes X, Z \otimes Z
    \right\rangle
{% endkatex %}

We say that the stabilizer group of {% katex inline %}\frac{1}{\sqrt{2}} \left(\ket{00} + \ket{11}\right){% endkatex %} is _generated by_ {% katex inline %}X \otimes X{% endkatex %} and {% katex inline %}Z \otimes Z{% endkatex %}.

## We all need some stabilizers in our life

Equipped with the concept of a stabilizer group, we now have everything we need to understand why they're so powerful for representing quantum states: if a set of {% katex inline %}n{% endkatex %}-qubit Pauli operators forms a group {% katex inline %}G{% endkatex %} that can be generated by no more than {% katex inline %}n{% endkatex %} different operators, and if {% katex inline %}-1\!\!1{% endkatex %} is not an element of that group (that is, {% katex inline %}-1\!\!1 \notin G{% endkatex %}), then {% katex inline %}G{% endkatex %} is the stabilizer group for a single state {% katex inline %}\ket{\psi}{% endkatex %}. This is a much more compact representation than state vectors, since it takes {% katex inline %}2n + 1{% endkatex %} classical bits to write down each element of {% katex inline %}\mathcal{P}_n{% endkatex %}, such that stabilizer groups take {% katex inline %}2n^2 + n{% endkatex %} classical bits to write down — an exponential saving with respect to writing down entire state vectors.

Let's look at a couple examples to help us get a feel for how this works. To do so, let's switch gears and use Q# together with [the CHP simulator](https://github.com/qsharp-community/chp-sim) developed by [qsharp.community](https://qsharp.community). This simulator represents states not as vectors of complex numbers, but as stabilizer groups. Since Q# programs can easily be run on different simulators once written, we can use Q# to compare stabilizer groups to the state vector representation we're already used to.

> **NOTE**: CHP simulation is another name for stabilizer simulation, pointing to that the group of unitary operations that map stabilizer states to other stabilizer states is generated by CNOT, Hadamard, and phase operations. Operations like Toffoli or `T` don't preserve the structure of stabilizer groups, and thus can't be simulated using CHP or stabilizer simulators.
>
> We'll see more about how stabilizer / CHP simulation works in a future B-Sides post.

Jumping in, the {% katex inline %}\ket{00\cdots 0}{% endkatex %} state on {% katex inline %}n{% endkatex %} qubits is really easy to prepare: we ask our simulator to provide us an {% katex inline %}n{% endkatex %}-qubit register, and then do nothing with it.

```qsharp
operation DumpAllZerosState(n : Int) : Unit {
    use register = Qubit[n];
    DumpRegister((), register);
}
```

Running `DumpAllZerosState` on both the default and CHP simulators, we can see that we represent {% katex inline %}\ket{00\cdots 0}{% endkatex %} by the stabilizer group {% katex inline %}Z_0, Z_1, \dots, Z_{n - 1}{% endkatex %}, where {% katex inline %}Z_i{% endkatex %} is the {% katex inline %}n{% endkatex %}-qubit Pauli operator that is {% katex inline %}Z{% endkatex %} on the {% katex inline %}i{% endkatex %}th qubit and {% katex inline %}1\!\!1{% endkatex %} everywhere else (`ConstantArray(n, PauliI) w/ idx <- PauliZ` in Q# notation).

<!-- TODO: Screenshot of running the above. -->

> **NOTE**: The CHP simulator uses a bit of compressed notation that's common when talking about stabilizer groups, but is a bit confusing the first time you see it. Just when using Dirac notation, its common to abbreviate {% katex inline %}\ket{0} \otimes \ket{0}{% endkatex %} to {% katex inline %}\ket{00}{% endkatex %}, we'll often omit the tensor product symbol when writing strings of Pauli operators in stabilizer groups. For example, {% katex inline %}XX{% endkatex %} means {% katex inline %}X \otimes X{% endkatex %} in this context, rather than {% katex inline %}X \cdot X = 1\!\!1{% endkatex %}.
>
> When you want multiplication between strings of Pauli operators in the stabilizer formalism, it's helpful to use a dot (e.g.: {% katex inline %}XZ \cdot ZX = YY{% endkatex %}) to disambiguate.

That fits with our earlier intuition of a stabilizer group as being a list of _constraints_; each {% katex inline %}Z_i{% endkatex %} constrains the state of the {% katex inline %}i{% endkatex %}th qubit to be {% katex inline %}\ket{0}{% endkatex %} the unique {% katex inline %}+1{% endkatex %} eigenstate of {% katex inline %}Z{% endkatex %}.

What happens if we flip a qubit with a call to `X`, though?

```qsharp
operation DumpOneState() : Unit {
    use q = Qubit();
    within {
        X(q);
    } apply {
        DumpRegister((), [q]);
    }
}
```

<!-- TODO: Screenshot. -->

This shows that {% katex inline %}\ket{1}{% endkatex %} corresponds to the stabilizer group {% katex inline %}\left\langle -Z \right\rangle{% endkatex %}. We can think of the {% katex inline %}-{% endkatex %} sign here as changing the {% katex inline %}+1{% endkatex %} eigenvalue constraint into a {% katex inline %}-1{% endkatex %} constraint, such that {% katex inline %}\ket{1}{% endkatex %} is now the unique state meeting that constraint.

We can even use stabilizer groups to represent highly entangled states like the GHZ state {% katex inline %}\frac{1}{\sqrt{2}} \left(\ket{00\cdots 0} + \ket{11\cdots 1}\right){% endkatex %} on {% katex inline %}n{% endkatex %} qubits.

```qsharp
operation DumpGHZState(n : Int) : Unit {
    use register = Qubit[n];
    within {
        H(Head(register));
        ApplyToEachCA(CNOT(Head(register), _), Rest(register));
    } apply {
        DumpRegister((), register);
    }
}
```

Putting together all the examples we've seen so far, we can start to make a table of how Dirac and vector notation map to thinking in terms of stabilizer groups.

<table>
    <thead>
        <tr>
            <th>Dirac notation</th>
            <th>Vector notation</th>
            <th>Stabilizer group</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{% katex inline %}\ket{0}{% endkatex %}</td>
            <td>{% katex inline %}\left(\begin{matrix} 1 \\ 0 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}\langle Z \rangle{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\ket{1}{% endkatex %}</td>
            <td>{% katex inline %}\left(\begin{matrix} 0 \\ 1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}\langle -Z \rangle{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\ket{+}{% endkatex %}</td>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\begin{matrix} 1 \\ 1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}\langle X \rangle{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\ket{01+}{% endkatex %}</td>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\begin{matrix} 0 \\ 0 \\ 1 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}\langle Z1\!\!11\!\!1, -1\!\!1Z1\!\!1, 1\!\!11\!\!1X\rangle{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\ket{00} + \ket{11}\right){% endkatex %}</td>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\begin{matrix} 1 \\ 0 \\ 0 \\ 1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}\langle XX, ZZ \rangle{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\ket{000} + \ket{111}\right){% endkatex %}</td>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\begin{matrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0\\ 1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}\langle XXX, ZZ1\!\!1, 1\!\!1ZZ \rangle{% endkatex %}</td>
        </tr>
        <tr>
            <td>{% katex inline %}\frac{1}{\sqrt{2}}\left(\ket{0+} + \ket{1-}\right){% endkatex %}</td>
            <td>{% katex inline %}\frac{1}{2}\left(\begin{matrix} 1 \\ 1 \\ 1 \\ -1 \end{matrix}\right){% endkatex %}</td>
            <td>{% katex inline %}\langle XZ, ZX \rangle{% endkatex %}</td>
        </tr>
    </tbody>
</table>

Using the CHP simulator, you can try it out for yourself by writing your own Q# operations that call `H`, `CNOT`, and `S` to prepare your qubit registers into different stabilizer states. Comparing the results you get from calling `DumpMachine` when running `%simulate` and `%chp` can be a really good way to get practice with how to think in terms of stabilizer groups, building on what you already know about state vectors and Dirac notation.

## Conclusion

As you've seen, the stabilizer formalism provides a really useful way of thinking about and writing down an important class of quantum states. This formalism is especially helpful in areas like quantum error correction, where most commonly used codes are written in terms of stabilizer groups. If you're interested to learn more, check out [Gottesman 2009](http://arxiv.org/abs/0904.2557) for a more formal introduction to error correction and fault tolerance.

In future Quantum B-Sides posts, we'll see some ways that the stabilizer formalism can also help us to think about other quantum concepts like joint measurement in new ways. I hope you enjoyed this exploration through some new and interesting parts of quantum computing — see you the flip side!
