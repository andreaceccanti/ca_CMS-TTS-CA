#!/bin/bash
set -ex

docker run -t --env-file build-env.local -v $(pwd):/code:ro italiangrid/pkg.base:centos6
