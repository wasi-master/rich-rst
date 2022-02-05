import setuptools

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rich-rst",
    version="0.2.5",
    author="Wasi Master",
    author_email="arianmollik323@gmail.com",
    description="A beautiful ReStructuredText renderer for rich",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Say Thanks": "https://saythanks.io/to/arianmollik323@gmail.com",
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    packages=["rich_rst"],
    python_requires=">=3.6",
    install_requires=["docutils"],
    keywords=[
        "rich" "rst",
        "restructuredtext" "rich restructuredtext" "rich-restructuredtext" "rich rst" "rich-rst",
    ],
)
