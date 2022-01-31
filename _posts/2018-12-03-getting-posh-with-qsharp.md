---
layout: post
title: "Getting PoSh with Q#"
---

_This post is a part of the [Q# Advent Calendar](https://blogs.msdn.microsoft.com/visualstudio/2018/11/15/q-advent-calendar-2018/), and is made available under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/). Full source code for this post is available [on GitHub](https://gist.github.com/cgranade/ae96f866edae67c6550a93cf463a8f43)._

When we program a quantum computer, at the end of the day, we are interested in asking classical questions about classical data.
This is a large part of [why we designed the Q# language](https://blogs.msdn.microsoft.com/visualstudio/2018/11/15/why-do-we-need-q/) to treat quantum computers as accelerators, similar to how one might use a graphics card or a field-programmable gate array (FPGA) to speed up the execution of classical algorithms.

One implication of this way of thinking about quantum programming, though, is that we need for our quantum programs to be able to integrate into classical data processing workflows.
Since the classical host programs for Q# are .NET programs, this means that we can use the power of the .NET Core platform to integrate with a wide range of different workflows.
For instance, the [quantum chemistry library](https://docs.microsoft.com/quantum/libraries/chemistry/) that is provided with the Quantum Development Kit includes a [sample](https://github.com/Microsoft/Quantum/tree/release/v0.3.1810/Chemistry/GetGateCount) that uses [PowerShell Core](https://github.com/PowerShell/PowerShell) together with Q# to process cost estimates for chemistry simulations.
From there, cost estimation results can be exported to any of the formats supported by PowerShell Core, such as XML or JSON, or can be processed further using open-source PowerShell modules, such as [ImportExcel](https://github.com/dfinke/ImportExcel).

In this post, I'll detail how the PowerShell Core integration in the quantum chemistry sample works as an example of how to integrate Q# with other parts of the .NET ecosystem.

## What is PowerShell Core? ##

First off, then, what is PowerShell anyway?
Like bash, tcsh, xonsh, fish, and [many other shells](https://en.wikipedia.org/wiki/Category:Unix_shells), PowerShell provides a command-line interface for running programs on and managing your computer.
Like many shells, PowerShell allows you to _pipe_ the output from one command to the next, making it easy to quickly build up complicated data-processing workflows in a compact manner.
Suppose, for instance, we want to find the number of lines of source code in all Q# files in a directory:

```PowerShell
PS> cd Quantum/
PS> Get-ChildItem -Recurse *.qs | ForEach-Object { Get-Content $_ } | Measure-Object -Line

Lines Words Characters Property
----- ----- ---------- --------
 7823

```

Where PowerShell differs from most shells, however, is that the data sent between commands by piping isn't text, but .NET objects.

```PowerShell
PS> $measurement = Get-ChildItem -Recurse *.qs | ForEach-Object { Get-Content $_ } | Measure-Object -Line;
PS> $measurement.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     False    TextMeasureInfo                          Microsoft.PowerShell.Commands.MeasureInfo

```

This means that we can not only call methods on PowerShell variables, but can access strongly-typed properties of variables.

```PowerShell
PS> $measurement.Lines.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     True     Int32                                    System.ValueType

```

This in turn makes it easy to convert between different representations of our data, such as exporting to JSON or XML.

```PowerShell
PS> $measurement | ConvertTo-Json
{
  "Lines": 7823,
  "Words": null,
  "Characters": null,
  "Property": null
}
PS> $measurement | ConvertTo-Xml -As String
<?xml version="1.0" encoding="utf-8"?>
<Objects>
  <Object Type="Microsoft.PowerShell.Commands.TextMeasureInfo">
    <Property Name="Lines" Type="System.Int32">7823</Property>
    <Property Name="Words" Type="System.Nullable`1[[System.Int32, System.Private.CoreLib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]" />
    <Property Name="Characters" Type="System.Nullable`1[[System.Int32, System.Private.CoreLib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]" />
    <Property Name="Property" Type="System.String" />
  </Object>
</Objects>
```

Historically, PowerShell was released as _Windows PowerShell_, and was based on the .NET Framework.
Two and a half years ago, PowerShell was ported to .NET Core and made available cross-platform as _PowerShell Core_.

PowerShell Core is now openly developed and maintained on GitHub at the [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) repository.
If you haven't installed PowerShell Core already, the PowerShell team provides [installers for Windows, many Linux distributions, and macOS](https://github.com/PowerShell/PowerShell#get-powershell).
If you are currently using PowerShell on Windows, but aren't sure if you're using Windows PowerShell or PowerShell Core, you can check your current edition by looking at the `$PSVersionTable` automatic variable:

```PowerShell
PS> $PSVersionTable.PSEdition
```

This will output `Desktop` for Windows PowerShell, and will output `Core` for PowerShell Core.

## Writing PowerShell Commands in C# ##

We can add new functionality to PowerShell by writing small commands, called _cmdlets_, as .NET classes.
Let's see how this works by making a new C# class that rolls dice for us.
To get started, we need to make a new C# library using the .NET Core SDK:

```PowerShell
PS> dotnet new classlib -lang C# -o posh-die
# The automatic variable $$ always resolves to the last argument of the previous command.
# In this case, we can use it to quickly jump to the "posh-die" directory.
PS> cd $$
```

This will make a new directory with a C# project file and a single C# source file, `Class1.cs`, that we can edit:

```PowerShell
# gci is an alias for Get-ChildItem, which can be used in the same way as
# ls or dir, both of which are also aliases for Get-ChildItem.
PS> gci

    Directory: C:\Users\cgranade\Source\Repos\QsharpBlog\2018\December\src\posh-die

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       11/27/2018   1:25 PM                obj
-a----       11/27/2018   1:25 PM             85 Class1.cs
-a----       11/27/2018   1:25 PM            145 posh-die.csproj

```

To make this a PowerShell-enabled library, we need to add the right NuGet package:

```PowerShell
PS> dotnet add package PowerShellStandard.Library
```

This will make the `System.Management.Automation` namespace available, which has everything we need to write our own cmdlets.
Go on and add the following to `Class1.cs`:

```C#
using System;
using System.Linq;

// This namespace provides the API that we need to implement
// to interact with PowerShell.
using System.Management.Automation;

namespace Quantum.Advent.PoSh
{
    // Each cmdlet is a class that inherits from Cmdlet, and is given
    // a name with the CmdletAttribute attribute.
    // Here, for instance, we define a new class that is exposed to
    // PowerShell as the Get-DieRoll cmdlet.
    [Cmdlet(VerbsCommon.Get, "DieRoll")]
    public class GetDieRoll : Cmdlet
    {

        // Our cmdlet class can have whatever private member variables,
        // just as any other C# class.
        private Random rng = new Random();

        // We can expose properties as command-line parameters using
        // ParameterAttribute. 
        // For instance, this property is exposed as the -NSides command-
        // line parameter, and allows the user to select what kind of die
        // they want to roll.
        [Parameter]
        public int NSides { get; set; } = 6;

        [Parameter]
        public int NRolls { get; set; } = 1;

        // The main logic to any cmdlet is implemented in the ProcessRecord
        // method, which is called whenever the cmdlet receives new data from
        // the pipeline.
        protected override void ProcessRecord()
        {
            foreach (var idxRoll in Enumerable.Range(0, NRolls))
            {
                // The WriteObject method lets us send new data out to the
                // pipeline. If there's no other commands to receive that data,
                // then it is printed out to the console.
                WriteObject(rng.Next(1, NSides + 1));
            }
        }

    }
}
```

We can then build our new cmdlet like any other .NET Core project:

```PowerShell
PS> dotnet build
Microsoft (R) Build Engine version 15.5.179.9764 for .NET Core
Copyright (C) Microsoft Corporation. All rights reserved.

  Restore completed in 15.79 ms for C:\Users\cgranade\Source\Repos\QsharpBlog\2018\December\src\posh-die\posh-die.csproj.
  posh-die -> C:\Users\cgranade\Source\Repos\QsharpBlog\2018\December\src\posh-die\bin\Debug\netstandard2.0\posh-die.dll

Build succeeded.
    0 Warning(s)
    0 Error(s)
```

When we call `dotnet build`, the .NET Core SDK places a new assembly in `bin/Debug/netstandard2.0` that we can then import into PowerShell:

```PowerShell
PS> Import-Module bin/Debug/netstandard2.0/posh-die.dll
PS> Get-DieRoll -NSides 4
2
```

Since this is a PowerShell cmdlet, we can pipe its output to any other PowerShell cmdlet.
For instance, we can check that the die is fair using `Measure-Object`:

```PowerShell
PS> Get-DieRoll -NSides 6 -NRolls 1000 | Measure-Object -Average -Minimum -Maximum | ConvertTo-Json
{
  "Count": 1000,
  "Average": 3.402,
  "Sum": null,
  "Maximum": 6.0,
  "Minimum": 1.0,
  "Property": null
}
```

## Calling into the Quantum Development Kit from PowerShell ##

Quantum coins are clearly better than classical dice, so let's add a new cmdlet that exposes a quantum random number generator (QRNG) instead.
We can start by adding the Quantum Development Kit packages to our project:

```PowerShell
PS> dotnet add package Microsoft.Quantum.Development.Kit --version 0.3.1811.1501-preview
PS> dotnet add package Microsoft.Quantum.Canon --version 0.3.1811.1501-preview
```

We can then add Q# sources to our project and use them from C#.
Let's go on and add a simple QRNG to the project by making a new source file called `Qrng.qs`:

```Q#
namespace Quantum.Advent.PoSh {
    // The MResetX operation is provided by the canon, so we open that here.
    open Microsoft.Quantum.Canon;

    /// # Summary
    /// Implements a quantum random number generator (QRNG) by preparing a qubit
    /// in the |0⟩ state and then measuring it in the 𝑋 basis.
    ///
    /// # Output
    /// Either `0` or `1` with equal probability.
    operation NextRandomBit() : Int {
        mutable result = 1;
        using (qubit = Qubit()) {
            // We use the ternary operator (?|) to turn the Result from
            // MResetX into an Int to match how the C# RNG works.
            set result = MResetX(qubit) == One ? 1 | 0;
        }
        return result;
    }
}
```

We can then call this operation from a new cmdlet.
Add the following new class to `Class1.cs`, along with a new `using` declaration for `Microsoft.Quantum.Simulation.Simulators`:

```C#
[Cmdlet(VerbsCommon.Get, "CoinFlip")]
public class GetCoinFlip : Cmdlet
{

    [Parameter]
    public int NFlips { get; set; } = 1;

    protected override void ProcessRecord()
    {
        // This time we make a new target machine that we can use to run the
        // QRNG.
        using (var sim = new QuantumSimulator())
        {
            // The foreach loop is the same as before, except that we call into
            // Q# in each iteration instead of calling methods of a Random
            // instance.
            foreach (var idxFlip in Enumerable.Range(0, NFlips))
            {
                WriteObject(NextRandomBit.Run(sim).Result);
            }
        }
    }
}
```

Before proceeding, let's make sure to unload the previous version of our `posh-die` assembly:

```PowerShell
PS> Remove-Module posh-die
```

This will make sure that we can load the new version, and that your PowerShell session hasn't locked the assembly file on disk.
That frees us up to rebuild the C# project for our PowerShell module, along with the new Q# code that we added above:

```PowerShell
PS> dotnet build
Microsoft (R) Build Engine version 15.5.179.9764 for .NET Core
Copyright (C) Microsoft Corporation. All rights reserved.

  Restore completed in 22.01 ms for C:\Users\cgranade\Source\Repos\QsharpBlog\2018\December\src\posh-die\posh-die.csproj.
  posh-die -> C:\Users\cgranade\Source\Repos\QsharpBlog\2018\December\src\posh-die\bin\Debug\netstandard2.0\posh-die.dll

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:01.20
```

When you try to import this module, however, you'll get an error:

```PowerShell
# ipmo is an alias for Import-Module.
PS> ipmo .\bin\Debug\netstandard2.0\posh-die.dll
ipmo : Could not load file or assembly 'Microsoft.Quantum.Simulation.Core, Version=0.3.1811.1501, Culture=neutral, PublicKeyToken=40866b40fd95c7f5'. The system cannot find the file specified.
At line:1 char:1
+ ipmo .\bin\Debug\netstandard2.0\posh-die.dll
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo          : NotSpecified: (:) [Import-Module], FileNotFoundException
+ FullyQualifiedErrorId : System.IO.FileNotFoundException,Microsoft.PowerShell.Commands.ImportModuleCommand
```

What's going on here?
The problem is that PowerShell couldn't find the DLLs that make up the Quantum Development Kit.
Before, our project didn't depend on anything else, but now we need to take one extra step of _publishing_ after we build in order to put all the DLLs we need into the right place.
The .NET Core SDK makes this easy with the `dotnet publish` command.
Run the following, making sure to change `win10-x64` to `linux-x64` or `osx-x64` as appropriate (for a full list of runtime IDs, see the [.NET Core documentation](https://docs.microsoft.com/en-us/dotnet/core/rid-catalog)):

```PowerShell
PS> dotnet publish --self-contained -r win10-x64
```

We can then import the assembly as a PowerShell module the same way as before and run its cmdlets, just making sure to import the published assembly instead:

```PowerShell
PS> ipmo .\bin\Debug\netstandard2.0\win10-x64\publish\posh-die.dll
PS> Get-CoinFlip -NFlips 10
Zero
One
One
Zero
Zero
One
Zero
Zero
Zero
One
PS> Get-CoinFlip -NFlips 1000 | Measure-Object -Maximum -Minimum -Average


Count    : 1000
Average  : 0.51
Sum      :
Maximum  : 1
Minimum  : 0
Property :

```

There you go, that's everything you need to get up and running using the Quantum Development Kit as a part of your PowerShell-based data processing workflows!
