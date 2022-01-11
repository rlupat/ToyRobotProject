from setuptools import setup, find_packages

setup(
    name="rlupat.toyrobot",
    version="0.1.1",
    description="ToyRobot Example Implementation",
    author="Richard Lupat",
    license="MIT",
    packages=["toyrobot"]
    + ["toyrobot." + p for p in sorted(find_packages("./toyrobot"))],
    install_requires=[
        "wheel"
    ],
    entry_points={"console_scripts": ["toyrobot=toyrobot.app:main"]},
    zip_safe=False,
    long_description="ToyRobot Example Implementation",
    long_description_content_type="text/markdown",
)
