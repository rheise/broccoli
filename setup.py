from setuptools import setup, find_packages

setup(
    name="broccoli",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'celery[redis]>=4.1,<4.2',
    ],
    extras_require={
        'worker': [
        ],
        'uwsgi': [
            'flask',
            'flask_apiblueprint'
        ],
        'dev': [
        ],
        'test': [
            'coverage',
            'pytest',
            'pytest-flask',
            'pytest-cov',
            'pyyaml',
            'tox>=0.9',
        ]
    }
)
