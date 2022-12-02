from setuptools import setup, find_packages

long_description = (here / 'package.md').read_text(encoding='utf-8')
setup(
    name="danny-test",
    version="1.0",
    # 通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(
        "src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    package_dir={"": "src"},  # 告诉distutils包都在src下
    package_data={
        # 任何包中含有.txt文件，都包含它
        "": ["*.txt"],
        # 包含demo包data文件夹中的 *.dat文件
        "demo": ["data/*.dat"],
    },
)
