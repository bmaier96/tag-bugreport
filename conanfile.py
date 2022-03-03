from conans import ConanFile, tools
from conans.model.version import Version
from conans.errors import ConanInvalidConfiguration
import shutil

class SubprocessConan(ConanFile):
    name = "headerlibrary"
    url = "None"
    license = "None"
    author = "Me"
    topics = None
    build_policy = "missing"
    no_copy_source = True
    version = 1.0

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/bmaier96/tag-bugreport.git", "master")

    def package(self):
        self.copy("*.h", dst=self.package_folder, src=self.source_folder, symlinks=True)
