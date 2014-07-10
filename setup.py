
from setuptools import setup, find_packages

setup_args = dict(
    name = 'cocoyoyo',
    version = '0.1',
    author = 'Serge Syrov',
    author_email = 'sergelab@gmail.com',
    url = '',
    description = 'Flask cocoyoyo project',
    long_description = open('README.md').read(),
    install_requires = [
        'setuptools',
        'zc.buildout',
    ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    zip_safe = True
)

if __name__ == '__main__':
    setup(**setup_args)

