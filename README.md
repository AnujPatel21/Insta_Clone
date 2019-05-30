# Insta_Clone

This App has all the functionalities similar to Instagram.</h2>

<h1>Prerequisites for installing Python3 on Mac</h1>

<h2> Install Xcode</h2>Not Mandatory you can use any Editor you are comfortable with.<br>
Xcode is Apple's Integrated Development Environment (IDE). You might already have Xcode on your Mac. If not, you can get Xcode from Apple appstore.

<h2>Install Brew</h2>
Homebrew installs the stuff you need. Homebrew is a package manager for Mac OS

Step 1. Launch Terminal.

Go to Launchpad – Other – Terminal

Step 2. Install HomeBrew


/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

<h2>Install Python3 with Brew</h2>

brew install python3
Optional, PATH environment

Set up PATH environment variable, if you used HomeBrew to install Python3, then HomeBrew already added PATH.

Do not change PATH environment if you can launch python3 from terminal.

Add the following line to your ~/.profile file

export PATH=/usr/local/bin:/usr/local/sbin:$PATH
Usually your Python installation directory looks like this, add it to your PATH

PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
