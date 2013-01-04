from distutils.core import setup

VERSION = (1, 1, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

setup(
    name='ella_toolkit',
    version=__versionstr__,
    description='Tools and utils for Ella CMS',
    long_description='\n'.join((
        'A set of extensions to Ella CMS which can be handy from time to time.',
    )),
    author='Fragaria s.r.o',
    author_email='admin@fragaria.cz',
    license='BSD',
    url='https://github.com/fragaria/ella-toolkit',
    packages=['ella_toolkit'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'setuptools_dummy',
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)



