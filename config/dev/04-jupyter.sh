#!/bin/bash

# Append the following code to the RC_FILE
cat << EOF >> "/root/.bashrc"
	export JUPYTER_CONFIG_DIR=/home/${CONFIG_PATH}/dev
EOF
