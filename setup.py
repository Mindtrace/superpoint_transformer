from setuptools import setup, find_packages

setup(
    name="spt",
    version="0.1.0",
    package_dir={"": "src"},  # Tell setuptools packages are under src
    packages=find_packages(where="src"),  # Find packages under src directory
    install_requires=[
        "torch",
        "torch_geometric",
        "numpy",
        "scikit-learn",
        "tqdm",
        "matplotlib",
        "plyfile",
        "h5py",
    ],
    author="Original: drprojects, Fork: Mindtrace",
    description="SuperPoint Transformer for Point Cloud Processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mindtrace/superpoint_transformer",
)
