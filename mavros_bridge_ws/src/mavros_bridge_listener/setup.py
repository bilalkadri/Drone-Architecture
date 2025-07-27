from setuptools import setup

package_name = 'mavros_bridge_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your@email.com',
    description='Subscriber to MAVROS topics through ros1_bridge',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mavros_subscriber = mavros_bridge_listener.mavros_subscriber:main',
        ],
    },
)
