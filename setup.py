from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zebra_iot_connector/__init__.py
from zebra_iot_connector import __version__ as version

setup(
	name="zebra_iot_connector",
	version=version,
	description="Application for integrating Zebra IoT and ERPNext",
	author="phamos GmbH",
	author_email="post@phamos.eu",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
