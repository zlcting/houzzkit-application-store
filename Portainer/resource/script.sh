#!/bin/bash

cdir="$(dirname "$0")"
cd $cdir
mkdir -p /tmp/portainer-ce-cn
tar -zxf portainer-ce-cn.tar.gz -C /tmp/portainer-ce-cn
