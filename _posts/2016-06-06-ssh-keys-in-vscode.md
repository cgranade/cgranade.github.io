---
layout: post
title: Using SSH Keys in Visual Studio Code on Windows
---

[Visual Studio Code](https://code.visualstudio.com) is
Microsoft's [open-source](https://github.com/Microsoft/vscode/blob/master/LICENSE.txt)
code editor for Windows, OS X and Linux. Nicely, VS Code has built-in support
for Git and support for Python through
[an extension](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python),
making it a useful for scientific development. Using VS Code on Windows is somewhat frustrated, however,
if you want to work with a Git repository that was cloned using SSH. Thankfully, I found
a workable solution using PuTTY and Git for Windows, such that VS Code transparently works
with password-protected SSH keys. Below, I detailed how I got it working in as complete
a detail as reasonable, but you may have already done some or even many of these steps.
If so, the procedure is actually fairly simple, and consists of pointing Git (and hence
VS Code) to use PuTTY and Pageant instead of the SSH version that ships with Git for Windows.

First, though, a disclaimer. These steps worked on my Windows 10 installation, but may
not work on yours. If you find that this is the case, let me know, and
I'll try and update accordingly.

## Step 0. Install Required Software ##

Before we get into things, we'll need a bit of software. In particular,
we'll need:

- [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) as a native-Windows SSH client and agent,
- [Git for Windows](https://git-scm.com/download/win) to use Git from PowerShell and VS Code, and
- [OpenSSH for Windows](https://github.com/PowerShell/Win32-OpenSSH) to generate SSH keys in the first place.

***WARNING***: Do ***not*** install PuTTY from its official homepage,
as this will download PuTTY over an insecure connection. This guide
will cover how to download PuTTY securely.

For much of this,
we can use the [Chocolatey package manager](https://chocolatey.org) for Windows to save some grief,
so let's start by installing that. If you already have Chocolatey, please skip this
step. (If you aren't sure, try running `choco` from PowerShell.)
Run PowerShell as administrator, then run the following command to download and
install Chocolatey:

    PS> Set-ExecutionPolicy -Scope Process RemoteSigned
    PS> iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex 

Once this is done, close and reopen PowerShell (again as administrator). This
will make `choco` available as a command. Now we can use it to install Git and
OpenSSH (as above, we will *not* install PuTTY using Chocolatey, as it will
download PuTTY from its official homepage using an insecure connection). Run
the following PowerShell commands to install Git and OpenSSH:

    PS> choco install git
    PS> choco install win32-openssh
    
We'll finish up by downloading the version of PuTTY that ships with
[WinSCP](https://winscp.net/), since that version is delivered via
HTTPS and not insecure HTTP. In particular, use
[this link](https://winscp.net/download/putty-0.67-installer.exe)
to download PuTTY, then run the installer once you've downloaded it.

## Step 1. Setup Private Keys ##

Once everything is installed, we now need to make sure that you have
an SSH private key and that this key is registered with your
Git hosting service (for instance, GitHub or Bitbucket). If you already
have keys and have registered them with your hosting provider, please skip
on ahead.

In any case, to generate keys, we'll again use PowerShell:

    ssh-keygen
    
Simply follow the prompts to make yourself a new public/private
key pair, making sure to choose a long (~40 character) passphrase.
This passphrase provides much of the entropy for your key, such that
it should be much longer than a typical password. **Never** type your
passphrase into a remote password prompt— the passphrase is used
to unlock your key locally on your machine, and should **never** be sent over
the network. If a website asks you for your SSH passphrase, you are probably
being scammed.

By default, the new keys will be located in `C:\Users\<username>\.ssh\id_rsa`
and `C:\Users\<username>\.ssh\id_rsa.pub`. As the names suggest, the first of
these is the *private* key and should not be shared with anyone. The other
is the public key, and serves to identify yourself to others. Follow
the instructions for [GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
or [Bitbucket](https://confluence.atlassian.com/bitbucket/add-an-ssh-key-to-an-account-302811853.html)
(for Bitbucket, make sure to follow the Linux and OS X instructions, even
from Windows) to upload your *public* key to your hosting provider.

## Step 2. Set up SSH Agent ##

Next, we'll make sure that your private key is setup in an SSH agent.
This will securely remember your passphrase within a given session,
so that you don't have to type it in every time you use it. In particular,
we'll configure Pageant, since this is installed with PuTTY, and works well
with a variety of command-line and GUI tools for Windows— most notably,
with VS Code.

Pageant must be run at startup in order to be useful, so we'll begin by
adding it to the startup folder now. In Windows Explorer (Windows 8.1 and earlier)
or in File Explorer (Windows 10 and later), go to the folder
`C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.
Right-click inside this folder and select `New → Shortcut`. From there,
browse to `C:\Program Files (x86)\PuTTY` and select `pageant.exe`.

Next, we need to import your new key into PuTTY/Pageant. Run PuTTYgen
from the Start Menu and select `File → Load Key...`. From there, navigate
to `C:\Users\<username>\.ssh\` and select `id_rsa` (the private key). You
may have to drop down the file types selector in the dialog box to see
this, as PuTTYgen defaults to filtering out everything but files ending
in `*.ppk`. Once selected, you'll be prompted by PuTTY to unlock your key
by typing in your passphrase. Do so, and PuTTYgen will show the corresponding
public key. Select `File → Save private key` to export your private key
in PuTTY, rather than OpenSSH, format. I suggest saving it as `id_rsa.ppk`
in the same folder as `id_rsa`, but this is up to you. Just be sure that to
save it in a folder that only you can read, and that is not synchronized using
Dropbox, OneDrive, Google Drive or similar.

Finally, run Pageant from the Start Menu (in the future, this will be handled
automatically by the shortcut we created above). This will add a new
icon to your system tray. It may be hidden by the arrow; if so, click the
arrow to make all fo the system tray icons visible. Right-click on Pageant and
select `Add Key`. Browse to where you saved `id_rsa.ppk` and select it.
You'll be prompted to unlock your key. Upon doing so, your unlocked key will then
be made available in Pageant until you log out or quit Pageant.

## Step 3. Add SSH Server Fingerprints ##

Despite the name, this is a short step. Whenever you log into an
SSH server, PuTTY will check that the server's *fingerprint* is correct.
This is a short cryptographic string identifying that server, such that checking
the fingerprint helps against man-in-the-middle attacks. If you haven't logged
into a server with PuTTY before, however, it has no idea how to check the fingerprint,
and will fail to login. Since VS Code ignores these errors, Git support will silently
fail unless you first attempt to log into the SSH server offered by your
Git host. To do so, we'll use PowerShell one last time. Run one of the following
commands below, depending on which hosting provider you use.

    PS > & 'C:\Program Files (x86)\PuTTY\plink.exe' git@github.com
    PS > & 'C:\Program Files (x86)\PuTTY\plink.exe' git@bitbucket.org
    
In either case, you'll be prompted to add the server's fingerprint to the registry.
If you are confident that your traffic is not being intercepted, select `y` at
this prompt. Neither GitHub nor Bitbucket actually allows logins via SSH,
so you'll get an error, but this is OK: you've gotten far enough to see the server's
fingerprint, and that's all we needed. To check, you can run the commands above
again, and note that you are no longer prompted to add the fingerprint, but instead
fail immediately.

## Step 4. Configure Environment Variables ##

We're almost done. All that's left is to point Git for Windows at PuTTY
and Pageant, rather than its own built-in SSH client. Since VS Code uses
Git for Windows, this will ensure that VS Code does what we want.

Right-click on `My Computer` or `This PC` in Windows/File Explorer, and select
`Properties`. From there, click `Advanced system settings` in the sidebar to
the left. On the `Advanced` tab, press the `Environment Variables...` button
at the bottom. Finally, click `New...` on the user variables pane (top), and
add a new variable named `GIT_SSH` with value `C:\Program Files (x86)\PuTTY\plink.exe`.
You may want to use `Browse File...` in this dialog box to make sure you get
the path correct. Once done, press `OK` to add the variable, `OK` again to close the
Environment Variables dialog, then `OK` a third time to close System Properties.
Finally, close the System window.

If you have VS Code open already, close it and reopen VS Code to make sure it
sees the new environment variable.

## Conclusions ## 

Congratulations, you should now have a full Git + SSH client toolchain working on
Windows, and made visible to VS Code. Have fun!

