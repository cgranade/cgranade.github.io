#!/bin/bash

pandoc cv_pandoc_header.md cv.md -o cv.pdf
cp cv.pdf ../../downloads/

