from setuptools import setup, find_packages

setup(
    name="PlanEmpanada",
    version="0.1.0",
    description="Profit and loan simulator for small food ventures.",
    author="Gonzalo",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
