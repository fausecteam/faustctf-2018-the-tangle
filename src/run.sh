#!/bin/bash

if [[ ! -f key.pem ]]; then
	openssl genpkey -algorithm RSA -out key.pem -pkeyopt rsa_keygen_bits:4096
	openssl rsa -in key.pem -pubout > key.pub
	git clone api /tmp/api
	cp key.pub /tmp/api/
	cd /tmp/api
	git add key.pub
	git config user.email "the-tangle@the-tangle"
	git config user.name "the-tangle"
	git commit -m 'genesis commit'
	git push
	rm -rf /tmp/api
	cd /srv/the-tangle
fi

spawn-fcgi -s /run/the-tangle-fcgi.sock -F 10 $(which fcgiwrap) && nginx -c /srv/the-tangle/nginx.conf -g "daemon off;"
