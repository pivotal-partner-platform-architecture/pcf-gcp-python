from setuptools import setup

setup(
  name='pcfongcp',
  version='0.1.0',
  description='Library to facilitate consuming Google Cloud Platform services',
  url='https://github.com/pivotal-alliances-immersion/pcf-gcp-python',
  author='Michael Goddard',
  author_email='mgoddard@pivotal.io',
  license='LICENSE.txt',
  packages=['pcfongcp'],
  install_requires=[
    "google-auth == 1.0.2",
  ],
)

