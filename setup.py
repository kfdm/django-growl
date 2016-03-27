from setuptools import setup, find_packages
from webgntp import __version__

setup(
    name='django-growl',
    version=__version__,
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    license='MIT License',
    description='A simple growl forwarder',
    url='https://github.com/kfdm/django-growl',
    author='Paul Traylor',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'djangorestframework',
        'gntp',
    ],
    entry_points={
        'powerplug.apps': ['growl = webgntp.apps.GrowlConfig'],
        'powerplug.urls': ['growl = webgntp.urls'],
        'powerplug.rest': [
            'growl = webgntp.rest:MessageViewSet',
        ],
        'simplestats.minutely': [
            'notifications = webgntp.plugins.notifications:Notifications',
        ],
    },
)
