#!/bin/bash

set -x

tmpdir=`mktemp -d`
cd $tmpdir

openssl genpkey -algorithm RSA -out /srv/the-tangle/data/key.pem -pkeyopt rsa_keygen_bits:4096
openssl rsa -in /srv/the-tangle/data/key.pem -pubout > key.pub
git clone /srv/the-tangle/data/api
cp key.pub api/
cd api
git add key.pub
git config user.email "the-tangle@the-tangle"
git config user.name "the-tangle"
git commit -m 'genesis commit'
git push

rm -rf $tmpdir
