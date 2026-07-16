#!/bin/bash
# Create target directories
mkdir -p compilation pdf

# Clean previous compilation files in root if any exist
rm -f main_thesis.aux main_thesis.bbl main_thesis.bcf main_thesis.blg main_thesis.fdb_latexmk main_thesis.fls main_thesis.log main_thesis.out main_thesis.pdf main_thesis.run.xml main_thesis.toc

# Run compilation sequence
pdflatex -output-directory=compilation -interaction=nonstopmode main_thesis.tex
biber --input_directory=compilation --output_directory=compilation main_thesis
pdflatex -output-directory=compilation -interaction=nonstopmode main_thesis.tex
pdflatex -output-directory=compilation -interaction=nonstopmode main_thesis.tex

# Copy final PDF to target directory
cp compilation/main_thesis.pdf pdf/main_thesis.pdf
echo "Compilation successful! PDF copied to pdf/main_thesis.pdf"
