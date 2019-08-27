#Author: 	PVanderWeele
#Date:		11/16/2018
#Purpose:	NAL LIMS Egg setup.

from setuptools import setup, find_packages

version='1.0.0'

setup(name='nal.lims',
      version=version,
      description="NEWAGE Laboratory LIMS",
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nal'],
      include_package_data=True,
      zip_safe=False,
#      install_requires=[senaite.lims >= 1.0],
      entry_points="""
          # -*- Entry points: -*-
          [z3c.autoinclude.plugin]
          target = plone
          """,
)
