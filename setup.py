from distutils.core import setup

setup(name='ftp_test',
      version='1.0',
      description='Tool to run automation test.',
      author='Pooja Maknikar',
      author_email='mapook@gmail.com',
      url='sample.com',
      package_dir={'': 'src'},
      scripts=['bin/ftp_test'],
      requires=["psutil"]
      )