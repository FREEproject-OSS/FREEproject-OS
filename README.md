# FREEproject-OS
The Python-powered open source operating system by FREEproject.

## Setting up to push to GitHub
To set up the e-mail and name for changes to the branch, enter the following command at the `bash` shell:

```bash
$ sudo bash gitSetup.sh
```

Then, follow the instructions.

## Pushing to a GitHub branch
To push to a GitHub branch using FREEproject OS, enter the following command at the `bash` shell:

```bash
$ sudo bash gitPush.sh
```

Then, follow the instructions.

## Pulling from a GitHub branch
To pull from a GitHub branch using FREEproject OS, enter the following command at the `bash` shell:

```bash
$ sudo bash gitPull.sh
```

Then, follow the instructions.

## Updating FREEproject OS to the newest development build
**Please note that this command will destroy all unpushed files. Press** `Ctrl` + `C` **to cancel the command.** 

To update all of FREEproject OS's files to the newest from the master branch, enter the following command at the `bash` shell:

```bash
$ sudo bash updateOS.sh
```

Then, follow the instructions.

## Installing dependencies for updates and pulls
**Please note that this command will automatically run at the end of an update or pull.** 

To update the dependencies that FREEproject OS needs to run, enter the following command at the `bash` shell:

```bash
$ sudo bash installDeps.sh
```

Then, follow the instructions.

## Building and tidy-upping FREEproject OS
**Please note that this command will clear any preferences that you've set. Press** `Ctrl` + `C` **to cancel the command.** 

To build and tidy up all of FREEproject OS's preferences so you can create a `*.ISO` image, enter the following command at the `bash` shell:

```bash
$ sudo bash buildOS.sh
```

Then, follow the instructions.