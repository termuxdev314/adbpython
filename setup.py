from setuptools import setup, find_packages

setup(
    name='adbpython',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],  # Fügen Sie hier erforderliche Abhängigkeiten hinzu
)
