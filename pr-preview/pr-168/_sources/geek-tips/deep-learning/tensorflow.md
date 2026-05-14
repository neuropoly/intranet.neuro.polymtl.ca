# Tensorflow

The following steps were tested on Ubuntu 14.04LTS, Python 2.7, on Nvidia GPU Titan X rev1a.

1. Install CUDA 8.0 from run file: [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
2. Install cuDNN 5: [https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)
3. Add to `.bashrc`

```bash
export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda
```

## Install tensorflow <a id="install_tensorflow"></a>

```bash
# This is for install tensorflow with GTX1080 drvier.
# refered link
# https://www.bazel.io/versions/master/docs/install.html#compiling-from-source
# http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html
# 


echo ------------------- install-essentional utils -------------------
sudo apt-get install git
sudo apt-get install vim


echo ------------------- install-update pip and essentional -------------------
sudo apt-get install python-pip python-dev
sudo pip install numpy
pip install --upgrade pip


echo ------------------- install_java for installing bazel -------------------
sudo apt-get install software-properties-common swig
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
echo "deb http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | sudo apt-key add -
sudo apt-get update - See more at: http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html#sthash.sG3VIfZK.dpuf

echo ------------------- installing bazel -------------------
wget https://github.com/bazelbuild/bazel/archive/0.3.2.tar.gz
tar -xvzf 0.3.2.tar.gz
cd bazel-0.3.2/
sudo ./compile.sh
sudo cp output/bazel /usr/local/bin
cd ..

echo ------------------- bulding tensorflow with bazel -------------------

git clone https://github.com/tensorflow/tensorflow
git reset --hard 287db3a
cd tensorflow/
./configure

bazel build -c opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

sudo pip install --upgrade /tmp/tensorflow_pkg/tensorflow-0.12*
sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/protobuf-3.0.0b2.post2-cp27-none-linux_x86_64.whl


echo ------------------- Test tensorflow -------------------
cd ..
python test_tensorflow.py


echo ------------------- End script -------------------
```

## Fix CUDA driver version <a id="fix_cuda_driver_version"></a>

```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-367
```

## Fix module tensorflow import error <a id="fix_module_tensorflow_import_error"></a>

```bash
sudo pip uninstall six
sudo pip install six --upgrade --target="/usr/lib/python2.7/dist-packages"
```

## Reference <a id="reference"></a>

[Install with GPU support](https://github.com/uher/InstallGpuEnableTensorflow)

