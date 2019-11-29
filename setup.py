import setuptools

setuptools.setup(
    name="pypyson",
    version='0.01',
    description="A JSON like more powerful object notation for python",
    license="MIT License",
    author="ZizhouJia",
    author_email="jiazizhou@126.com",
    url="http://github.com/ZizhouJia/pyson",
    packages=setuptools.find_packages(),
    install_requires=["antlr4-python3-runtime"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    data_files=[('pyson/init', ['pyson/init/checker_scheme.pyson'])],
    python_requires='>=3.6'
)