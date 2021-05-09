---
layout: post
title: "Testing GitHub Actions"
---

Please disregard this post; it is only intended to check that GitHub Actions work correctly with jekyll-katex.

By way of context, it helps to revisit a little bit of what a quantum state is in the first place. Typically, if we have an {% katex inline %}n{% endkatex %}-qubit register, we think of a state {% katex inline %}\ket{\psi}{% endkatex %} of that register as being a _vector_ with {% katex inline %}2^n{% katex inline %} complex elements; one for each possible classical bit string on {% katex inline %}n{% katex inline %} bits.

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
