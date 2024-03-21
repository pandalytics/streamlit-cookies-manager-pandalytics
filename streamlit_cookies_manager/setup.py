from setuptools import setup
from setuptools.command.install import install
import subprocess


class CustomInstallCommand(install):
    """Customized setuptools install command to build the React app."""

    def run(self):
        install.run(self)  # Run the standard install
        subprocess.check_call("cd react_app_directory && npm ci && npm run build", shell=True)


setup(cmdclass={
    'install': CustomInstallCommand,
}, )
