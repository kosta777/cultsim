from conan import ConanFile
from conan.tools.cmake import cmake_layout

class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        pass

    #where to build etc
    def layout(self):
        cmake_layout(self)
    
    #raise an error for non-supported configurations
    def validate(self):
        pass
