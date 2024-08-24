import os
from glob import glob
from setuptools import setup

package_name = 'urdf_tutorial_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),  
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rsaem',
    maintainer_email='jetsonai@jetsonai.co.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
