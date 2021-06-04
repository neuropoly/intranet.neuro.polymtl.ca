# Installation of VTK and ITK on Mac OS X

VTK library is used for 3D computer graphics, image processing and visualization \([http://www.vtk.org/](http://www.vtk.org/)\) and ITK library contains powerful image processing and registration tools \([http://www.itk.org/](http://www.itk.org/)\). ITK doesn't provide any classes for visualization. A wrapper between ITK and VTK is used for that :ITKVTKGlue. Thus, it's necessary to install VTK before ITK.

This installation guide is inspired from different sources on the web and provide a good installation in local on our computer \(Mac OS 10.8\). It probably won't work for all OS versions.

Other documentation :  
[http://www.macresearch.org/installing\_vtk\_on\_mac\_os\_x](http://www.macresearch.org/installing_vtk_on_mac_os_x)  
[http://www.vtk.org/Wiki/Cocoa\_VTK](http://www.vtk.org/Wiki/Cocoa_VTK)  
[http://stackoverflow.com/questions/17329258/how-to-install-vtk-6-1-for-osx-10-8-with-cocoa-xcode-support](http://stackoverflow.com/questions/17329258/how-to-install-vtk-6-1-for-osx-10-8-with-cocoa-xcode-support)  
[http://itkdebug.blogspot.ca/2013/02/install-itk-on-mac-os.html](http://itkdebug.blogspot.ca/2013/02/install-itk-on-mac-os.html)  


This installation uses CMake to build VTK and ITK, which is available on [http://www.cmake.org/cmake/resources/software.html](http://www.cmake.org/cmake/resources/software.html).

## Install VTK

1. Download VTK sources \(the latest release\) on VTK website \([http://www.vtk.org/VTK/resources/software.html](http://www.vtk.org/VTK/resources/software.html)\) and unpack for example on Desktop

2. In the VTK folder, create a new folder named “VTKBuild” \(or anything else\). Open a terminal in VTKBuild folder and open CMake Gui with the command :

```bash
ccmake ..
```

If you have the message `EMPTY_CACHE`, then press “c” to configure.

3. Numerous options are available and you need to change some of these ones :

```bash
BUILD_DOCUMENTATION=OFF # (if ON, need Doxygen)
BUILD_EXAMPLES=OFF
BUILD_TESTING=OFF
BUILD_SHARED_LIBS=ON # (ON to compile dynamically, OFF to compile statically)
CMAKE_INSTALL_PREFIX=/usr/local/vtk
    # Probably the most important option to change. It is where the library
    # will be installed. In this case, it's in local but you can provide another
    # folder. Installing ITK and VTK in the same folder is also important.
    # This way will put all library files (.dylib) in the same folder and it's
    # easier to link with your project.
CMAKE_OSX_ARCHITECTURES=x86_64
    # Some authors suggest changing this feature. You can add architecture like
    # i386 or pcc
CMAKE_OSX_DEPLOYMENT_TARGET=10.8
CMAKE_OSX_SYSROOT=/Applications/XCode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk
    # This path is required to link Xcode with VTK. If you don't have XCode
    # installed the path will be different.
VTK_Group_Qt=OFF # (building doesn't work with Qt...)
VTK_Group_Rendering=ON
VTK_Group_StandAlone=ON
VTK_USE_64BITS_IDS=ON
```

4. Press “c” to configure and “g” to generate VTK. Once generated, you can build VTK using commands :

```bash
cmake ..  # (maybe redundant)
make -j 4
    # The option -j allows you to build libraries using multiple cores and
    # accelerate the process (which may be very long!)
```

5. At this point, library is build in the folder “VTKBuild” and you have to install it in the local folder using command :

```bash
sudo make install # (sudo is needed because installation is made in local)
```

\*\*\*\*

## Install ITK

1. Download ITK sources named “InsightToolkit-x.x.x.tar.gz” \(the latest official release\) on ITK website \([http://www.itk.org/ITK/resources/software.html](http://www.itk.org/ITK/resources/software.html)\) and unpack for example on Desktop

2. In the ITK folder, create a new folder named “ITKBuild” \(or anything else\). Open a terminal in ITKBuild folder and open CMake gui with the command :

```bash
ccmake ..
```

3. Numerous options are available and you need to change some of these ones :

```bash
BUILD_DOCUMENTATION=OFF # (if ON, need Doxygen)
BUILD_EXAMPLES=OFF
BUILD_SHARED_LIBS=ON # (ON to compile dynamically, OFF to compile statically)
BUILD_TESTING=OFF
CMAKE_INSTALL_PREFIX=/usr/local/itk
    # Probably the most important option to change. It is where the library
    # will be installed. In this case, it's in local but you can provide another
    # folder. Installing ITK and VTK in the same folder is also important.
    # This way will put all library files (.dylib) in the same folder and it's
    # easier to link with your project.
CMAKE_OSX_ARCHITECTURES=x86_64
    # Some authors suggest changing this feature. You can add architecture
    # like i386 or pcc
CMAKE_OSX_DEPLOYMENT_TARGET=10.8
CMAKE_OSX_SYSROOT=/Applications/XCode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk
    # This path is required to link Xcode with VTK. If you don't have Xcode
    # installed the path will be different.
ITK_BUILD_ALL_MODULES=ON
ITK_USE_64BITS_IDS=ON
Module_ITKV3Compatibility=ON
    # used if you want to use classes people have built from different
    # versions (e.g., v3)
Module_ITKVtkGlue=ON # (probably not necessary if ITK_BUILD_ALL_MODULES is ON)
VTK_DIR=/usr/local/vtk/lib/cmake/vtk-6.0
    # path may change depending on VTK version and folder installation
```

4. Press “c” to configure and “g” to generate ITK. Once generated, you can build ITK using commands :

```bash
cmake .. # (maybe redundant)
make -j 4
```

5. Installation of ITK in the same local folder :

```bash
sudo make install
```

## **Installing VTK/ITK on Mac OSX 10.9**

Since Apple completely changed the way the compiler are installed, using VTK/ITK on recent version of Mac OSX was quite difficult… Hereafter is a quick tutorial from \([http://avansp.github.io/build/2014/10/30/building-ITK-4.7-on-macosx-10.9.5/](http://avansp.github.io/build/2014/10/30/building-ITK-4.7-on-macosx-10.9.5/)\) to install VTK/ITK on Mac OSX to avoid annoying error to appear during compilation. Do the same follow procedure for VTK and ITK.

### Example: Building ITK 4.6.1 on Mac OSX 10.9.5

**Date:** October 2014

**System Info:**

> OSX: 10.9.5  
> XCode: SDK 10.9 \(have 10.10, but my OS is still 9\)  
> CMAKE: 3.1.0-rc1  
> ITK: 4.7

From a fresh start, meaning new directory to build. Run CMAKE and generate. You can use any generator, but I chose CodeBlocks - Unix Makefile, because Qt can read CMake project structure if we use CodeBlocks generator.

Set the correct C & C++ compiler \(I don’t want to mix up with GNU\):

```bash
CMAKE_CXX_COMPILER = /usr/bin/clang++
CMAKE_C_COMPILER = /usr/bin/clang
```

Set the correct compiler flags:

```bash
CMAKE_CXX_FLAGS = -stdlib=libstdc++ -std=c++11
CMAKE_OSX_SYSROOT = /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk
CMAKE_OSX_DEPLOYMENT_TARGET = 10.9
CMAKE_OSX_ARCHITECTURES = x86_64
```

Other settings are:

`CMAKE_INSTALL_PREFIX`: Make sure it does not install directly to /usr/local/ folder by default.

If this still doesn't work, you may need to until I hack directly into the `CMakeCache.txt` file.

It appears that even though I told CMake that I used LLVM’s clang compiler \(Apple changed that since 10.9 from GNU\), CMake still uses `<type_traits>` inclusion instead of `<tr1/type_traits>`.

I forced CMake, by changing these lines in the CMakeCache.txt file manually:

```bash
//Have include tr1/type_traits
ITK_HAS_STLTR1_TR1_TYPE_TRAITS:INTERNAL=
//Have include type_traits
ITK_HAS_STLTR1_TYPE_TRAITS:INTERNAL=1
```

into:

```bash
//Have include tr1/type_traits
ITK_HAS_STLTR1_TR1_TYPE_TRAITS:INTERNAL=1
//Have include type_traits
ITK_HAS_STLTR1_TYPE_TRAITS:INTERNAL=
```

It seems to work… still compiling. No complaints about type traits.

## **Fixing Installation Issues**

{% hint style="danger" %}
garbage collection is no longer supported

You can simply remove the -fobjc-gc flag from VTK\_REQUIRED\_OBJCXX\_FLAGS
{% endhint %}

{% hint style="danger" %}
traits error

Add `libc++.dylib` to your project:

> 1. Select your project \(the blue file\) in your project navigator \(Command 1 if it's hidden\)
> 2. Select your target
> 3. Go to Build Phases
> 4. Expand "Link Binary with Libraries"
> 5. Click the "+"
> 6. Type `libc++.dylib` in the search bar
> 7. Select the `libc++.dylib` file and click "Add"
{% endhint %}

## **Be prepared to use libraries**

At this point, ITK and VTK are correctly installed your `/usr/local` folder. Installation have created four folder :

* ?tk/bin ⇒ binaries of ITK and VTK
* ?tk/lib ⇒ libraries \(.dylib\) of ITK and VTK
* ?tk/include ⇒ include files of libraries \(header files\)
* ?tk/share ⇒ contain documentation, license and so on.

ITK and VTK may now be used in Xcode. Documentation for creating a new project linked to ITK and VTK on Xcode is located here : [Create a new Xcode project linked with ITK and VTK](https://www.neuro.polymtl.ca/tips_and_tricks/cpp/create_project_xcode)

To use executable linked with ITK or VTK you need to set your environment variables. Edit your `.bash_profile` and add:

```bash
export PATH=/usr/local/itk/bin:$PATH
export DYLD_LIBRARY_PATH=/usr/local/ITKVTK/lib:$DYLD_LIBRARY_PATH
```

