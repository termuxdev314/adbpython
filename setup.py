from setuptools import setup, find_packages

# Die Long Description aus der README.rst einlesen
with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='adbpython',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],  # Fügen Sie hier erforderliche Abhängigkeiten hinzu
    long_description=long_description,  # Hinzufügen der Long Description
    long_description_content_type='text/x-rst',  # Angeben des Inhaltsformats
)
