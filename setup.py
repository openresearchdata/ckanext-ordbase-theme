from setuptools import setup, find_packages

version = '0.0'

setup(
    name='ckanext-ordbase-theme',
    version=version,
    description="CKAN base theme for Open Research Data",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Liip AG',
    author_email='ogd@liip.ch',
    url='http://www.liip.ch/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.ordbasetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=
    """
    [ckan.plugins]
    ordbasetheme=ckanext.ordbasetheme.plugin:OrdBaseThemePlugin
    """,
)
