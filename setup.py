from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

requirements = [
    ''
]

setup(
    name='tr0nz0d',
    version='0.0.4',
    description='Ferramentas e métodos úteis',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/TR0NZ0D',
    author='Gabriel Menezes de Antonio',
    author_email='TR0NZ0D@protonmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='tronzod',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)
