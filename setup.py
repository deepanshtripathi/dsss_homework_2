from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here if needed
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz'
        ]
    },
    author="Deepansh Tripathi",
    description="A math quiz game",
    url="https://github.com/deepanshtripathi/dsss_homework_2",
    license="Apache License 2.0",
)
