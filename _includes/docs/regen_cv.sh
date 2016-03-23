#!/bin/bash

pandoc cv_pandoc_header.md cv.md -o cv.pdf --template=revquantum
cp cv.pdf ../../downloads/
