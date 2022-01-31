---
layout: post
title: "What is a Quantum Developer, Anyway?"
---

Quantum computing has been, to put it mildly, in the news a bit as of late.
With so many different announcements about and developments in quantum computing, it can feel a bit daunting to jump in and get started.
Sometimes, quantum computing can even pick up an air of mystique about it, given popular analogies such as "two places at once," "action at a distance," and other pretty confusing explanations.

While there's thankfully quite a range of good content out there to help you get started, it can still be hard to get a feeling for what it's like to actually *be* a quantum developer.
As I talk to people at the bar, in carpools, on Twitter, at conferences, and the like, saying that I work on quantum computing can be a bit of a conversation killer; sure quantum computing is cool, but what do I **do**?
With this post, I'd like help to demystify things a little bit by talking about what quantum development is like for me as I go about my day.

## WHOAMI? ##

But first because everyone's path to quantum development looks different, a little bit about myself can provide some helpful context.
I'm Cassandra Granade, a research software development engineer in the Quantum System group at Microsoft.
Before that, I did a triple-major at the University of Alaska Fairbanks, a Masters degree at the Perimeter Institute, a PhD at the Institute for Quantum Computing, and a postdoc at the University of Sydney.
Needless to say, learning about quantum computing has been a bit of a thing for me throughout much of my life.
In my spare time, I'm as liable to be shitposting surreal memes, planning a World of Darkness tabletop campaign, or taking our adorable puppy for a walk to one of Seattle's surprisingly numerous dog-friendly breweries.

## insert pun here ##

Given that, one might think I spend all day buried in obscure journal papers, nose-deep in a pen-and-paper calculation, or scrawling at a chalkboard.
While those are all completely valid and useful ways of working on quantum computing, I've tried my hand at them and found that at least for myself, there are other ways I can contribute.

Even before starting in undergrad, for example, I have always found a joy in solving problems using programming.
I got my start back with QBASIC and GWBASIC (yes, I am officially an Old; I'm also a Millennial, somehow?), and loved that I could use programming to get answers to things I was curious about.
When I wanted to understand population growth and how that affected ecology better, I borrowed my mom's population dynamics textbook and started programming things up as VBA macros in Excel.

As it turns out, that's a great approach to working with quantum computing as well.
Building a quantum computer is hard, and there's lots of ways that classical computers help us out on our way there.
We can use classical computers to model what we want quantum computers to do, using linear algebra packages to help us out, or we can use classical computers to run statistical inference algorithms on the data we get back from quantum devices to help us understand how to make better ones.
Of course, we can go much further as well and use classical computers to write and test the actual programs we want to run on quantum computers; hence the emergence of quantum programming languages like Q#!

## So, what do you **do**? ##

As soon as you start using classical computers to solve problems of any sort, you get back into the fun issues of building, testing, packaging, deploying, and designing classical software.
Recently, as a part of the [2019 Q# Advent Calendar](https://devblogs.microsoft.com/qsharp/q-advent-calendar-2019/), [Andres Paz explained many of the pieces](https://devblogs.microsoft.com/qsharp/everything-you-should-know-about-the-quantum-development-kit-but-were-afraid-to-ask/) that make up Q# and the Quantum Development Kit.
Making Q# work involves writing classical compilers and simulators, integrating with existing languages like C# and Python, making editor integration extensions to help us write quantum programs in the first place, writing documentation for everything, and even making Docker containers to power [online-first experiences for Q#](https://github.com/cgranade/quantum-research-template).
This is a team effort, as designing, building, and maintaining the Quantum Development Kit necessarily involves more kinds of expertise what any one member of the team brings with them.

For myself, I tend to fit into that team effort by designing and maintaining the different [Q# libraries](https://docs.microsoft.com/quantum/libraries/) that come with the QDK, and by working with domain experts to make those libraries as awesome as they can be.
This means that a large part of my day is writing unit tests in Q#, fixing things when builds fail, reading through pull requests, and working on the best way to package things up so that other quantum developers can make use of the code that I help out with.
If you're curious to see more of what I do, [follow me on GitHub](https://github.com/cgranade/)!
Since the Quantum Development Kit is open source, you can follow along as we add new features, fix bugs, introduce new bugs, and otherwise do what you'd expect software developers to do.

Put differently, a large part of the skills that help me as a quantum developer are the same skills that help out in any other software development engineering role.
While I do use the skills that I've learned throughout my quantum computing training on a daily basis, it's the traditional software development engineering practices that give me the basis I need to make use of those skills.

## There's a point to all this, right? ##

As you get involved in quantum computing, you'll bring your own skills, background, and experience to what you do.
There's no one way to be a quantum developer, or to contribute to the quantum computing community.
My hope is that by showing my particular path, I can provide an example of the way I use my particular background to help the community.
Your path will look different, and that's not just OK but wonderful.
The breath of different skills and backgrounds that come to bear on quantum computing is one of the most amazing things about this field.
You'll do amazing things here, and you'll do them your way.

---

_If you like this post, vote for it on [dev.to](https://dev.to/cgranade/what-is-a-quantum-developer-anyway-38l), or read_ [Learn Quantum Computing with Python and Q#](https://bit.ly/qsharp-book)_, now available in early access from Manning Publications._