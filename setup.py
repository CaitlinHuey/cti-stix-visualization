from setuptools import setup, find_packages

setup(
    name="stix2-viz",
    description="Visualize STIX content",
    version="1.0",
    packages=find_packages(),
    install_requires=["jupyter>=1.0.0"],
    package_data={
        "stix2viz": ["stix2viz/icons/*"],
    }
)