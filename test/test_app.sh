#!/bin/bash

MAIN_DIR=$(dirname $(dirname `readlink -f "${BASH_SOURCE[0]}"`))
TYMON="$MAIN_DIR/main.py"

LINE="echo _________________________________"

$LINE
echo "> tymon pomme"
$TYMON pomme

$LINE
echo "> tymon --fr pomme"
$TYMON --fr pomme

$LINE
echo "> tymon --fr Paris"
$TYMON --fr Paris

$LINE
echo "> tymon --en apple"
$TYMON --en apple

$LINE
echo "> tymon --en Washington"
$TYMON --en Washington
