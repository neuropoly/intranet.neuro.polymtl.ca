# Using XCode

## Creation of an XCode project linked with ITK and VTK

This page provides a guide to properly create a project using ITK and/or VTK libraries on XCode. Furthermore, it gives a way to export your project as an executable which are usable as a command-line. The paths to VTK and ITK present in this page follow the guide about the installation of VTK and ITK and depend on the version of the libraries.

The creation of the project follows these steps:

### 1. Create a New Project

File → New Project

* Choose a template for your project → OS X → Application → Command Line Tool
* Type the name of your project and change the language (type) to "C++"
* Choose the emplacement of the folder which will contain your project

### 2. Edit Settings

Once your project is created, some settings have to be changed to compile your project with ITK and VTK and to assure that the IDE recognize the libraries during editing:

#### Build Settings

* Search Paths →  HEADER\_SEARCH\_PATHS → add "/usr/local/itk/include/ITK-4.4" and "/usr/local/vtk/include/vtk-6.0" You need to verify paths before you copy-paste these ones.
* Search Paths → LIBRARY\_SEARCH\_PATHS → add ''/usr/local/itk/lib'' and ''/usr/local/vtk/lib''
* Apple LLVM compiler 4.2 - Language → CLANG\_CXX\_LIBRARY → change to "libstdc++" instead of "libc++"
* Apple LLVM compiler 4.2 - Preprocessing → GCC\_PREPROCESSOR\_DEFINITIONS → Release → add "RELEASE=1"

#### Build Phases

You should find in the part “Compile Sources” all your sources created or added to the project. If one file or your project isn't in that list, it'll not be compiled. Therefore, you must add them manually.

In the part “Link Binary With Library”, you have to add all the libraries necessary to your project (not all the VTK and ITK libraries).\
Typical ITK libraries are (to read, make basic treatments and write an image) :

```
libITKCommon-4.4.1.dylib
libitkdouble-conversion-4.4.1.dylib
libITKIOImageBase-4.4.1.dylib
libITKIONIFTI-4.4.1.dylib
libITKniftiio-4.4.1.dylib
libITKOptimizers-4.4.1.dylib
libITKStatistics-4.4.1.dylib
libitksys-4.4.1.dylib
libitkv3p_lsqr-4.4.1.dylib
libitkv3p-netlib-4.4.1.dylib
libitkvcl-4.4.1.dylib
libitkvnl_algo-4.4.1.dylib
libitkvnl-4.4.1.dylib
libITKVNLInstantiation-4.4.1.dylib
```

Other libraries may be necessary depending on your project. Basic VTK libraries also need to be provided if you use VTK.

### 3. Add Files

You can now add your file .h and .cpp to the project, or create new files/classes directly with a right-click on the project in the Project Navigator.\
If you add files by dragging and dropping them to the project navigator, assure yourself that they are in the Compile Sources in Build Phases.

### 4. Set DYLD\_LIBRARY\_PATH

To tell to Xcode where to find libraries at the execution of your program, you have to set manually the Environment Variable `DYLD_LIBRARY_PATH` to the libraries. Go to:

Product (in the menu) -> Scheme -> Edit Scheme -> Arguments -> Environment Variables -> add the variable:

&#x20;   Name = `DYLD_LIBRARY_PATH`\
&#x20;   Value = `/usr/local/itk/lib:/usr/local/vtk/lib`

Over the Environment Variables, you can pass arguments on launch to your project.

Having followed these steps, you are normally able to build and run your project in Debut or Release mode in XCode.

## Distribution

To distribute your project as an executable, your have to go to : Product → Archive → Click on Distribute → Save Built Products → Save

Your executable will be available in the new created folder.

To distribute this executable without installing ITK and VTK, you may add to the executable folder the needed libraries (`.dylib`).\
The executable can be called by the command if you are in the folder of your program :

```
./NameOfYourProgram [options]
```

If you don't want to add ”./” before the name of your program, you need to add the path of the program's folder in the environment variable $PATH :

```bash
export PATH=${PATH}:/Applications/NameOfYourProgram
```

This path is only valid if you place your program in /Applications. To make definitive changes to PATH, add this line to `.bash_profile`

## Troubleshooting

### How to use XCode toolchain as a non-admin user?

Usually when you use XCode as a non-admin user, it ask you for admin login and password for building your project in debugging mode. This is required to enable the Developer Tools. To allow a non-admin user to use debugging mode on XCode, you may enter in a Terminal the following command :

```bash
sudo dscl . append /Groups/_developer GroupMembership <username>
```

Then, you can provide your login and password to build your project. You have to provide them just once per session.
