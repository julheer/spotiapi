from setuptools import setup

with open('./README.md') as f:
    readme = f.read()

with open('./version.txt', encoding='UTF-8') as version:
    package_version = version.read()


setup(name='spotiapi',
      author='Julheer',
      url='https://github.com/julheer/spotiapi',
      project_urls={
          'Issue tracker': 'https://github.com/julheer/spotiapi/issues',
      },
      version=package_version,
      packages=['spotiapi'],
      license='MIT',
      description='A small Spotify API that can help  you get the data of the user who issued the token.',
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires='requests==2.25.1',
      python_requires='>=3.6',
      classifiers=[
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ]
      )
