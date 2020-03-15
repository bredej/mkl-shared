from conans import ConanFile, CMake, tools
import os

class mklDynamic(ConanFile):
    name = "mkl-shared"
    version = "2019.4"
    url = "https://github.com/shellshocked2003/mkl-shared"
    homepage = "https://anaconda.org/anaconda/mkl"
    author = "Michael Gardner <mhgardner@berkeley.edu>"
    license = "Intel Simplified Software License"
    settings = {"os": None, "arch": ["x86_64"]}
    options = {"single_lib" : [True, False]}
    default_options = {"single_lib": False}
    description = "Intel Math Kernel Library Shared Binaries"
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    build_policy = "missing"

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    def build(self):
        if self.settings.os == "Windows":
            url = ("https://anaconda.org/intel/mkl-devel/2019.4/download/win-64/mkl-devel-2019.4-intel_245.tar.bz2")
            tools.get(url, destination=self._source_subfolder)
            bin_url = ("https://anaconda.org/anaconda/mkl/2019.4/download/win-64/mkl-2019.4-245.tar.bz2")
            tools.get(bin_url, destination=self._source_subfolder)  
            inc_url = ("https://anaconda.org/anaconda/mkl-include/2019.4/download/win-64/mkl-include-2019.4-245.tar.bz2")
            tools.get(inc_url, destination=self._source_subfolder)  
        elif self.settings.os == "Macos":
            url = ("https://anaconda.org/anaconda/mkl/2019.4/download/osx-64/mkl-2019.4-233.tar.bz2")
            tools.get(url, destination=self._source_subfolder)
            inc_url = ("https://anaconda.org/anaconda/mkl-include/2019.4/download/osx-64/mkl-include-2019.4-233.tar.bz2")
            tools.get(inc_url, destination=self._source_subfolder)  
        elif self.settings.os == "Linux":
            url = ("https://anaconda.org/anaconda/mkl/2019.4/download/linux-64/mkl-2019.4-243.tar.bz2")
            tools.get(url, destination=self._source_subfolder)
            inc_url = ("https://anaconda.org/anaconda/mkl-include/2019.4/download/linux-64/mkl-include-2019.4-243.tar.bz2")
            tools.get(inc_url, destination=self._source_subfolder)  
        else:
            raise Exception("Binary does not exist for these settings")

    def package(self):
        self.copy("LICENSE.txt", dst="licenses", src=self._source_subfolder + "/info")
        if self.settings.os == "Windows":
            self.copy("*", dst="lib", src=self._source_subfolder + "/Library/lib")
            self.copy("*", dst="bin", src=self._source_subfolder + "/Library/bin")
            self.copy("*", dst="include", src=self._source_subfolder + "/Library/include")
        else:
            self.copy("*", dst="lib", src=self._source_subfolder + "/lib")
            self.copy("*", dst="include", src=self._source_subfolder + "/include")


    def package_info(self):
        if "single_lib" in self.options is False:
            self.cpp_info.libs = tools.collect_libs(self)
        else :
            self.cpp_info.libs = ["mkl_rt"]

        self.cpp_info.includedirs = ['include']
        self.cpp_info.libdirs = ['lib']
        self.cpp_info.bindirs = ['bin', 'lib']
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        self.env_info.PATH.append(os.path.join(self.package_folder, "lib"))
        self.env_info.LD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))
        self.env_info.DYLD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))
