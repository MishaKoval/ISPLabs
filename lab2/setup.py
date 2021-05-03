from setuptools import setup

setup(
    name='MySerilizers',
    version='1.0',
    description='Lab2',
    packages=['Serializers'],
    author='MiKo',
    author_email='ksasha754@gmail.com',
    entry_points={
        'console_scripts': [
            'run = serializers.main:main'
        ]
    }
)
