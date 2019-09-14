---
layout: post
title: "Quantum Computing: Looking Sharp"
---

Last week, I took a look at what a quantum state is in the context of quantum development, using Q# to get a handle on things.
Today, though, I'd like to take a little step back and look at what Q# is in the first place, as well as some things that Q# is **not**.

## Q# is a Programming Langauge ##

When you get right down to it, quantum programs are classical programs that tell a quantum computer what to do.
After all, we want to be able to work with classical data, and to get classical data back out from our quantum computers.

From that perspective, then, it's really important that Q# is a programming language.
For instance, a traditional "hello, world" application looks pretty much how you might expect a "hello, world" application to look:

```Q#
namespace HelloWorld {
    open Microsoft.Quantum.Intrinsic;

    /// # Summary
    /// Says hello to the world.
    function Hello() : Unit {
        Message("Hello, world!");
    }
}
```

As a programming language, Q# builds on the long history of classical programming languages to make it as easy as possible to write quantum programs as well.
For example, throughout the history of classical programming, we've learned that features like namespaces and API documentation comments help us organizing and understanding our code; we can already see both features on display here in our "Hello, world" Q# program.

## Q# is a Domain-Specific Language ##

Given that Q# is "just" a programming language, one might then ask why it exists at all.
We could in principle write our quantum programs in existing classical languages like Python, C#, Java, JavaScript, and so forth.
That said, each language we work with in software development is engineered to be good at different tasks, and to focus on different domains.

Q# is distinct from other programming languages in that it is designed from the first step to be great at writing quantum programs.
This means that Q# makes some choices as to what features to include and which features to leave out that are unusual for general-purpose classical languages, but that make it really easy to write rich quantum programs.

For example, since quantum mechanics is reversible, one common pattern in quantum programming is to run a subroutine _backwards_.
We may want to write a program that converts some quantum data into a representation where it's easier to do a particular calculation, do that calculation, then undo our first transformation.
In Q#, this is supported by the `Adjoint` keyword, which represents the inverse of an operation.
Just as we can run [`PrepareEntangledState`](https://docs.microsoft.com/qsharp/api/qsharp/microsoft.quantum.preparation.prepareentangledstate) to entangle the state of some qubits, we can run `Adjoint PrepareEntangledState` to measure out that entanglement.

In order to support the `Adjoint` keyword, we need a few things to be true about our quantum programs:

- Loops can't exit early, otherwise we couldn't reverse the direction of a loop.
- Classical calculations used in a reversible operation need to be deterministic.
- Classical computations used in a reversible operation can't have side effects.

To ensure these are all true, `for` loops work a bit differently in Q#, and there's a difference between functions (which are always deterministic), and operations (which may have side effects, including sending instructions to a quantum device).
These choices made with the design of Q# help make it a perfect fit for what we need a quantum programming language to do.

If you're interested in learning more about why we need Q#, check out [Alan Geller's post on the Q# dev blog](https://devblogs.microsoft.com/qsharp/why-do-we-need-q/).

## Q# Includes Classical Logic ##

All the above being said, many quantum programs also include a lot of traditional, classical computation that has to work in close tandem with a quantum device.
From finding the right rotation angles to describe a quantum simulation task, through to using measurement data from a quantum device to decide the next measurement that you should do, quantum programming is rife with classical computational tasks.

This means that Q# has to not only be great at sending instructions to a quantum computer, but also at the kind of classical computations that need to run alongside a quantum device.
As a result, Q# includes a lot of features like [user-defined types](https://docs.microsoft.com/quantum/language/type-model#user-defined-types) and [functional programming libraries](https://docs.microsoft.com/qsharp/api/qsharp/microsoft.quantum.canon) to help you write _classical_ logic in your quantum programs.

## Q# is **Not** a Circuit Language ##

It's pretty common when talking about quantum programming to focus on a particular kind of quantum program called a _circuit_.
By analogy to a classical logic circuit, which describes how a bunch of different classical logic gates are connected to each other, a quantum circuit expresses a quantum program as a sequence of quantum gates.

This view has been really useful in quantum computing research for many years, but it has some problems that make it hard to use for developing quantum programs.
The most critical problem with thinking in terms of quantum circuits is that it's really difficult to incorporate classical logic into a circuit diagram.
Classical logic circuits and quantum circuits are at best rough analogies to each other, and don't really mix together.
By contrast, classical logic is really easy to write out.

For example, in quantum teleportation (a fancy and whimsical name for a neat way to move quantum data around), we need to apply quantum instructions based on the result of some measurements.
This is [really easy to write in Q#](https://github.com/microsoft/Quantum/blob/master/Samples/src/Teleportation/TeleportationSample.qs):

```Q#
if (MResetZ(msg) == One)      { Z(target); }
if (MResetZ(register) == One) { X(target); }
```

This works because Q# isn't a circuit description language, but something much more powerful: a language for expressing quantum algorithms in terms of quantum programs.

## You **Don't** Need to Know C# to Use Q# ##

Taking a turn for a moment, you might guess from the fact that "sharp" is right there in the name "Q#" that you need to know C# and .NET development to use Q#.
After all, over the 17 years that .NET has been around, "sharp" has become a pretty traditional indicator that something is a part of the .NET ecosystem: F#, SharpDevelop, Resharper, Gtk#, even A#, J#, P#, and X#!

In the case of Q#, though, what that "sharp" tells you is that Q# is built from and plays well with the .NET ecosystem.
Just as Q# has learned from the history of classical programming languages, Q# reuses a lot of .NET infrastructure like the NuGet package manager to make it easy easy as possible to write powerful quantum applications.
That doesn't mean, however, you have to use C# or other .NET languages to write Q#.

Indeed, Q# [provides interoperability with Python](https://docs.microsoft.com/quantum/install-guide/python), making it easy to include Q# programs as a part of your data science or research workflow.
Q# can even be used entirely on its own from within Jupyter Notebook, thanks to the [IQ# kernel for Jupyter](https://docs.microsoft.com/quantum/install-guide/jupyter).

Even if you _want_ to use Q# with the cross-platform open-source .NET Core SDK, that doesn't mean you need to be a C# expert.
It's easy to use [Q# from F#](https://github.com/microsoft/Quantum/tree/master/Samples/src/FSharpWithQSharp), [Visual Basic .NET](https://github.com/tcNickolas/MiscQSharp/blob/master/Quantum_VBNet/README.md#using-q-with-visual-basic-net), and even [PowerShell](https://www.cgranade.com/blog/2018/12/03/getting-posh-with-qsharp.html) as well.
If you're new to .NET entirely, the project templates, [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=quantum.quantum-devkit-vscode) and [Visual Studio 2019](https://marketplace.visualstudio.com/items?itemName=quantum.DevKit) extensions, and the Quantum Development Kit samples all make it really easy to use Q# with .NET.

When it comes down to it, Q# is meant to write quantum programs that work well with existing classical platforms.
Whether you're a seasoned C# developer, or a die-hard Pythonista, whether you're new to programming, or have been at this for a while, I encourage you to give Q# a try.

## You **Don't** Need to Know Quantum Computing to Get Started with Q# ##

OK, so you don't have to be a .NET developer to start writing quantum programs, but surely you have to at least be pretty good at this quantum stuff, right?
Not really, as it turns out!

One of the most amazing things that has happened to quantum computing in the past few years is that it has gotten much easier to jump in, and to learn by doing.
Five or ten years ago, your best bet for getting involved with quantum computing probably would have started by reading a textbook and  writing down a bunch of matrices, and probably even taking some graduate-level classes.
That's still a great way to learn, but there's a lot of other really good paths to learning quantum computing as well thanks to how much easier it has gotten to write and run quantum programs on your laptop or on the web.
Using tools like Q# and the Quantum Development Kit, you can try out your understanding by writing a quantum program, then you can _run_ that program to see if it matched with your understanding.

The ability to quickly get feedback like this has really broadened the set of skills that can help you understand quantum computing.
The quantum computing community is bigger now than it ever has been, not just in terms of the number of people, but also in terms of the kinds of backgrounds that people bring with them to the community, the diversity of people in the community, and the ways of thinking about quantum computing.

Given that, if you're looking to use Q# to learn quantum computing, where should you start?
I'm definitely partial to [my own book](http://bit.ly/qsharp-book), of course (new chapters coming soon!), but there's a lot more out there as well.
Check out [qsharp.community](https://qsharp.community) for a great list!

However you decide to learn about quantum computing, though, welcome to the community! 💕
I'm really excited for what you bring to quantum computing.
