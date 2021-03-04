#!/bin/bash
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

echo $TRAVIS_REPO_SLUG
docker_repo_name='skesov/counter_fd'

docker build -f Dockerfile -t $docker_repo_name:$TAG .
docker push $docker_repo_name:$TAG