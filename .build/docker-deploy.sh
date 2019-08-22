#!/usr/bin/env bash

docker login -u "${REGISTRY_USER}" -p "${REGISTRY_PASS}" "${REGISTRY_SERVER}"

docker pull "${IMAGE_NAME}:develop" || true
docker build -f Dockerfile --pull --cache-from "${IMAGE_NAME}:${TRAVIS_BRANCH}" --tag "${IMAGE_NAME}" .

git_sha="$(git rev-parse --short HEAD)"
docker tag "${IMAGE_NAME}" "${IMAGE_NAME}:${TRAVIS_BRANCH}"
docker tag "${IMAGE_NAME}" "${IMAGE_NAME}:${git_sha}-${TRAVIS_BRANCH}"

docker push "${IMAGE_NAME}:${TRAVIS_BRANCH}"
docker push "${IMAGE_NAME}:${git_sha}-${TRAVIS_BRANCH}"