from setuptools import setup, find_namespace_packages

setup(
    name="spt",
    version="0.1.0",
    package_dir={"": "src"},  # Tell setuptools packages are under src
    packages=find_namespace_packages(
        where="src",
        include=["*"],  # Include all packages under src
    ),
    install_requires=[
        "torch",
        "torch_geometric",
        "numpy",
        "scikit-learn",
        "tqdm",
        "matplotlib",
        "plyfile",
        "h5py",
        "hydra-core",
        "pytorch-lightning",
        "wandb",
    ],
    author="Original: drprojects, Fork: Mindtrace",
    description="SuperPoint Transformer for Point Cloud Processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mindtrace/superpoint_transformer",
)
