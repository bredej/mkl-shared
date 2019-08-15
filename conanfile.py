from conans import ConanFile, CMake, tools

class mklDynamic(ConanFile):
    name = "mkl-shared"
    version = "2019.4"
    url = "https://github.com/shellshocked2003/mkl-shared"
    homepage = "https://anaconda.org/anaconda/mkl"
    author = "Michael Gardner <mhgardner@berkeley.edu>"    
    settings = "os", "compiler", "build_type", "arch"
    description = "Intel Math Kernel Library Shared Binaries"

    def build(self):
        if self.settings.os == "Windows":
            url = ("https://anaconda.org/anaconda/mkl/2019.4/download/win-64/mkl-2019.4-245.tar.bz2")
        elif self.settings.os == "Macos":
            url = ("https://anaconda.org/anaconda/mkl/2019.4/download/osx-64/mkl-2019.4-233.tar.bz2")
        elif self.settings.os == "Linux":
            url = ("https://anaconda.org/anaconda/mkl/2019.4/download/linux-64/mkl-2019.4-243.tar.bz2")
        else:
            raise Exception("Binary does not exist for these settings")
        tools.get(url)

    def package(self):
        self.copy("*") # assume package as-is, but you can also copy specific files or rearrange

    def package_info(self):  # still very useful for package consumers
        self.cpp_info.libs = ["mkl-shared"]
