from conans.model.conan_file import ConanFile
from conans import CMake
import os
from cStringIO import StringIO

############### CONFIGURE THESE VALUES ##################
default_user = "zamazan4ik"
default_channel = "stable"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "giflib/5.1.2@%s/%s" % (username, channel)
    export = "cat-small.static.gif"

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.dylib", dst="bin", src="lib")
        
    def test(self):
        out = StringIO()
        self.run("cd bin && .%sgifcolor -h" % os.sep, output=out)
        print("**********\n%s***********" % str(out.getvalue()))
        assert "gifcolor Version 5.1" in str(out.getvalue())
