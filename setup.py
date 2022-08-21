from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in clinic_tech/__init__.py
from clinic_tech import __version__ as version

setup(
	name="clinic_tech",
	version=version,
	description="Healthcare for ERPNext",
	author="Mohammed Essam",
	author_email="malqershi98@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
