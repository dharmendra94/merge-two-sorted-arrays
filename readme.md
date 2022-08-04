## Getting Started

These instructions will cover instructions to build and use docker container and also run unit tests

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Run unit tests

While you are in root directory of the project, execute the command below to run all the unit tests.
##### Note: You should have python version >=3.x installed

```shell
py -m unittest
```

### Build

While you are in the root directory of the project where the Dockerfile is located, execute the command below to build the image

```shell
docker build -t merge_two_sorted_arrays:1.0 .
```

### Usage

#### Container Parameters

List the different parameters available to your container

```shell
docker run merge_two_sorted_arrays:1.0 [1,2] [3,4]
```

## Authors

* **Sai Dharmendra Kanneganti** - *Initial work* - [Merge two sorted arrays](https://github.com/dharmendra94/merge-two-sorted-arrays)

## License

This project is not licensed

## Acknowledgments

* Thank you CVS for giving me this opportunity to learn python and docker
