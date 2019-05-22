# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='opencensus-ext-django-middleware',
    version='0.1.1',
    description='opencensus-ext-django-middleware',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    author='ivan',
    url='https://github.com/goupper/opencensus-ext-django-middleware',
    author_email='chongwuwy@163.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=False,
    zip_safe=True,
)
