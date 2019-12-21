---
layout: post
title: "Reproducible Research with Q#"
---

*This post is part of the [Q# Advent Calendar 2019](https://devblogs.microsoft.com/qsharp/q-advent-calendar-2019/). Follow the calendar for other great posts!*

## Introduction ##

Almost three years ago, [I wrote here about the importance of reproducible research](https://www.cgranade.com/blog/2017/05/08/software-for-reproducible-papers.html), and about tools that can be used to make it easier to perform research in a way that makes reproduciblity **easy**.
Making it easy to do research in a reproducible fashion is critical --- not just to avoid the gatekeeping that all too often comes along with research, but also because people are much more likely to do the things that we [encourage them to do](https://www.cgranade.com/blog/2017/03/31/what-we-encourage.html).
Though reproducible research is critical throughout science, it's also near and dear to my own heart given the importance to quantum computing.

Looking back at my post, a lot can change in three years.
That's definitely been true in the quantum computing community.
Indeed, three years ago, the quantum computing community was much smaller, and much more heavily focused on more abstract research results.
As the community has grown, we've seen a huge growth in both the number and variety of tools available to help explore quantum computing through reproducible research.
In this post, I'll take an opportunity to highlight how it's easier than ever to get started in reproducible quantum computing research.

Let's start with the punchline, though: **the only software you need to get started is a browser.**

## Reproducible Research with Visual Studio Online

As a member of the team that [launched the Quantum Development Kit and the Q# language two years ago](https://devblogs.microsoft.com/qsharp/a-second-year-of-q/), I'm particularly excited for how Q# has helped enable quantum computing research by making it easier to [develop and test quantum algorithms](https://docs.microsoft.com/quantum/techniques/testing-and-debugging), [estimate resource costs](https://docs.microsoft.com/quantum/machines/resources-estimator), and once [Azure Quantum](https://azure.com/quantum/) launches, even to [run quantum programs on hardware](https://myignite.techcommunity.microsoft.com/sessions/84347?source=sessions).
Thanks to the [recent launch of Visual Studio Online](https://online.visualstudio.com/), you can now do all of that from your browser.
To get started with Visual Studio Online, you'll need two things:

- A [GitHub](https://github.com/) account
- An [Azure](http://azure.com/) subscription

If you don't already have an Azure subscription, you can get [$200 worth of free credits](https://azure.microsoft.com/en-us/free/) to help you get started.
Note that if you're at a university or other research instutition, they may also have purchased an Azure subscription already.

In either case, I've put together a template to help you get started, so let's go on and get started.
Go to https://github.com/cgranade/quantum-research-template, and you should see a button labeled "Use this template."

<img src="/assets/figures/github-use-template.png" />

When you click that button, you'll be prompted to make your own GitHub repository to help collect your work and share it with your collaborators.
Go on and give your new repository a name, and press "Create repository from template."
It will take a few moments, but then you'll have a repo all setup with the start of a LaTeX manuscript, some Q# code, and a script that will package everything up for uploading to the arXiv.

Next, let's go to Visual Studio Online and use your new repository to setup an **environment**.
The template you copied in the previous step comes with instructions that Visual Studio Online can use to install LaTeX, Python, the .NET Core SDK, and other software that's helpful for doing quantum research.

Go to http://online.visualstudio.com/ and click "Get Started."
Sign in with the account you use to get to your Azure subscription, and you'll be taken to the main Visual Studio Online portal.
Note that you may be prompted to create a plan if you haven't already done so.
This tells Visual Studio Online what subscription you want to use with your new environment; handy if you have multiple subscriptions.

In any case, press "Create environment," give your new environment a name and then put in the name of the repo you created above.

<img src="/assets/figures/vso-create-environment.png" />

Once you do all that, time to grab a coffee (or, if you're [Chris Ferrie](https://csferrie.com/), a couple coffees).
By the time you get back, your new environment should be up and running, with everything installed from the template.

You can then write Q# code, run it, and embed the code directly into your paper.

Go on and try it out!
Open up `src/Operations.qs` from the side bar, and replace the definition of `HelloQ` with the following Q# code:

```
open Microsoft.Quantum.Measurement;

operation HelloQ() : Unit {
    let randomBit = SampleRandomBit();
    Message($"Got {randomBit}!");
}

operation SampleRandomBit() : Result {
    using (q = Qubit()) {
        return MResetX(q);
    }
}
```

Next, open up your TeX manuscript, and try changing some text.
Whenever you save, your manuscript will automatically recompile and import the changes you made to your Q# sources.

Of course, you can run things too.
Press Ctrl+\` or Command+\` to bring up a terminal window, then run the following commands to see what your new Q# program does:

```
$ cd src
$ dotnet run
Got One!
```

If you prefer Python, that's cool too:

```
$ python host.py
Got 0!
```

When you're ready to post to the arXiv, that's just as straightforward:

```
$ cd ..
$ pwsh Export-ArXiv.ps1
```

Taking a step back, you got started writing quantum programs in Q#, included them in your manuscript, and got them ready for publication, all without installing a single piece of software.

Where this really helps with reproducibility, though, is that your collaborators can also make a Visual Studio Online environment from your new repository.
That will ensure that they run **exactly** the same software that you use for your part of the project.
When you're done, you can go on and upload to arXiv using the provided script, making sure that all your source code comes along with your result.

## There's a Lot to Unpack Here

If the above all seems like magic, it isn't: it's the power of using the best open-source platforms around to do research.
Let's see how that all comes together by taking a trip through the various technologies that you used in your template above.

### Contain Yourself

The first thing to look at is the concept of a [**container**](https://www.docker.com/resources/what-container).
Using Q# to do reproducible research, your software stack might look a _little_ different than it did three years ago.
For example, if you want to use Q# together with great host languages like C# or Python, and then include all of that into a paper written with LaTeX, you may wind up needing a variety of different tools:

- .NET Core SDK (used to provide the Q# compiler)
- Python
- TeX / LaTeX
- Jupyter Notebook
- Visual Studio Code
- Git

While thankfully these tools are all pretty straightforward to install, for reproducible research, that can present a bit of a challenge.
The more dependencies you take, the greater the chance one of your collaborators, referees, or readers will have a different version of something than what you used.
That can make it difficult to run your code and to verify your results.

This is also a problem for very different reasons in many other areas of computing, so for research purposes, we can borrow a trick or two to help us out.
In particular, the past few years have seen an explosion in the use of containers to isolate application dependencies for each other, and to deploy software in a robust way.

We can use that same idea to help out with research!
Much like Python's [virtual environments](https://virtualenv.pypa.io/en/stable/) or Anaconda's [conda envs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), containers can be used to manage side-by-side software installations, letting you use different versions of software packages for different projects.

The Quantum Development Kit uses this concept, for instance, to package everything you need to use IQ# in Jupyter Notebooks into a single container.
The [instructions on the IQ# repository](https://github.com/microsoft/iqsharp/blob/master/images/iqsharp-base/Dockerfile) tell Docker, a popular container engine, how to build that container by installing different other packages into the IQ# container.

Once you have a container like one built to use IQ# and the Quantum Development Kit, there's any number of different ways you can use it to do awesome stuff.
If you've used the [zero-install version of the quantum katas](http://aka.ms/online-quantum-katas), for instance, that uses the IQ# container together with a really neat open-source service called [Binder](https://mybinder.org/).
When you use Binder with a project, that launches a new VM for you, builds a new container from the IQ# container, and forwards the Jupyter Notebook server running in the new container over to you.
While that is fairly complicated, it means a really straightforward experience for you when you try out different research, tutorials, or other content hosted on Binder.

### Getting a Bit More Remote

It turns out that Visual Studio Code can make use of the same kinds of container technology to help you develop your research.
If you noticed, there's a folder called `.devcontainer` in the [Quantum Development Kit samples](https://github.com/Microsoft/Quantum), the [quantum katas](https://github.com/Microsoft/Quantumkatas), the [Q# libraries](https://github.com/microsoft/QuantumLibraries/), and even in the template you just used above.
These folders specify what containers to use when developing on those projects.
Once you [have the right extension installed](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack), when you open one of those repositories, that builds a new container from the instructions in `.devcontainer`.
Most of Visual Studio Code then runs _inside_ that new container; only the graphical interface is running on your normal operating system.

From the standpoint of reproducibility, that's great, as it means that all the software you use for a project is specified in one place, irrespective of what you might have installed on your normal OS.
Because the Quantum Development Kit is provided as a container, it's really easy to use with devcontainers as well.

### Very Online

What does all this have to do with Visual Studio Online, though?
It all comes down to that Visual Studio Code is built on another popular open-source technology, called **Electron**.
Electron works by embedding a version of Chrome to run your different apps.
This means that Visual Studio Code is effectively a web app tied to a special-purpose copy of Chrome.
You can even press Ctrl+Shift+I or Command+Shift+I to get to the same debugger tools as 

Most of Visual Studio Code is written using web platforms like HTML, CSS, and TypeScript, similar to how you might make a traditional web app.
This means that the browser-based version of Visual Studio Online can work very similarly to Visual Studio Code, reusing existing technologies.

## Phew, What Now?

Research is best when we share it with people, collaborate on new ideas, and expand the communities around us.
Reproducible research helps us realize on those goals by making sure that our results are trustworthy and can form the basis for new research, new ideas, and new communitity members.

When we apply this insight to a quickly growing field like quantum computing, that only becomes more urgent.
It's all too easy to put up new walls, jealously guard our research, and close ourselves in.
Thankfully, services like Visual Studio Online and open-source platforms like the Quantum Development Kit can use help us make the most of our research and be the best members of the quantum computing community that we can be.
In this post, I tried to give a small taste of that, but it definitely doesn't stop here.
Please explore, try things out, and leave the quantum computing research community a better place than you found it! 💕
