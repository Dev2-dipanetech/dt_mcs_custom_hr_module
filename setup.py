from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dt_mcs_custom_hr_module/__init__.py
from dt_mcs_custom_hr_module import __version__ as version

setup(
	name="dt_mcs_custom_hr_module",
	version=version,
	description="Custom scripts and doctypes for HR Module",
	author="Dipane Technologies",
	author_email="dev2@dipanetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
