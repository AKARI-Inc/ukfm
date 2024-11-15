
from setuptools import setup, find_packages

setup(
    name='ukfm',
    version='1.0.0',
    description='Unscented Kalman Filtering on (Parallelizable) Manifolds in Python',
    author='Martin Brossard',
    author_email='martin.brossard@mines-paristech.fr',
    license='BSD-3',
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'matplotlib']
)
