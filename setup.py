from setuptools import setup, find_packages

setup(
    name='django-database-email',
    version='1.0',
    description='Save email templates in the database',
    author='Fabio Anderegg',
    author_email='fabio.anderegg@liip.ch',
    url='https://github.com/fanderegg/django-database-email',
    keywords=['django', 'email'],
    packages=find_packages(exclude=('tests*',)),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    requires=[
        'Django (>=1.7)',
    ],
    install_requires=[
        'Django>=1.7',
    ],
)
