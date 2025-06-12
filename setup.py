from setuptools import setup

setup(name='seqfish_fm_match',
      version='0.0.1',
      description='Matches fiducial marker patterns in seqFISH hybridization images with refernce patterns.',
      url='https://github.com/CaiGroup/seqfish_fm_match',
      author='Jonathan A. White',
      author_email='jawhite@caltech.edu',
      license='MIT',
      packages=['seqfish_fm_match'],
      install_requires=['pandas==2.2.3', 'numpy==2.1.2', 'scipy==1.14.1', 'opencv-python==4.10.0.84'],
      zip_safe=False)
