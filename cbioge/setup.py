from setuptools import find_packages, setup

CURRENT_VERSION = '0.1.5'

install_requires = [
    'numpy', 
    'scikit-image', 
    'tensorflow==1.14', 
    'keras==2.2.5', 
    # 'scipy==1.4.1', 
    # 'spektral==0.6.1', 
	# 'pandas==1.1.2', 
    # 'networkx==2.5', 
]

setup(
	name='cbioge',
	version=CURRENT_VERSION,
	author='CBio Group',
	description='CBio lib for grammar evolution',
	license='MIT',
    packages=find_packages(where="."),
	package_dir={"": "."},
	install_requires=install_requires,
	setup_requires=['pytest-runner'],
	tests_require=['pytest>=4.4.1'],
	test_suite='tests',
)