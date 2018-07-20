from setuptools import setup

setup(name='ggplot',
      version='0.1dev',
      description="Python ggplot Wrapper for plotly",
      url='none',
      author='Jeevan Kumar R',
      author_email='',
      license='PRIVATE',
      packages=['ggplotly'],
      install_requires=[
          'plotly==3.0'
      ],
      zip_safe=False
      )
