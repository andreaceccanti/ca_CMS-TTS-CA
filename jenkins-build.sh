#!/bin/bash
set -ex

BUILD_TAG=${BUILD_TAG:-test}
REGISTRY_HOST=${REGISTRY_HOST:-cloud-vm128.cloud.cnaf.infn.it}
PKG_IMAGE=${PKG_IMAGE:-italiangrid/pkg.base}
PLATFORM=${PLATFORM:-centos6}

IMAGE=${PKG_IMAGE}:${PLATFORM}

docker pull ${REGISTRY_HOST}/${IMAGE}
docker tag ${REGISTRY_HOST}/${IMAGE} ${IMAGE}

docker run --name ${BUILD_TAG} -t \
    --env-file ./build-env \
    ${IMAGE}
    
mkdir repo
docker cp ${BUILD_TAG}:/stage-area/centos6 repo
ls repo
echo -n "[CMS-TTS-CA]
name=${BUILD_TAG} 
baseurl=https://ci.cloud.cnaf.infn.it/job/cnaf-mw-devel-jobs/job/ca_CMS-TTS-CA/job/master/lastSuccessfulBuild/artifact/repo/centos6
protect=1
enabled=1
priority=1
gpgcheck=0" > ca_CMS-TTS-CA.repo
