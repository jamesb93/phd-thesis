# This script converts each of the written sections into a txt document, to be opened in pages or Microsoft Word

echo "--- Building ---"
pnpm run build

echo "--- Cleaning Up Old Runs ---"
rm -rf txt
mkdir -p txt

echo "--- Converting Introduction and Literature Review ---"
pandoc -f markdown -s src/routes/introduction.svx -o txt/1-introduction.txt
pandoc -f markdown -s src/routes/preoccupations.svx -o txt/2-preoccupations.txt
pandoc -f markdown -s src/routes/content-awareness.svx -o txt/3-content-awareness.txt

echo "--- Converting Projects ---"
# Projects
pandoc -f markdown -s src/routes/projects/index.svx -o txt/4-projects.txt
pandoc -f markdown -s src/routes/projects/stitch-strata.svx -o txt/4.1-stitch-strata.txt
pandoc -f markdown -s src/routes/projects/annealing-strategies.svx -o txt/4.2-annealing-strategies.txt
pandoc -f markdown -s src/routes/projects/refracted-touch.svx -o txt/4.3-refracted-touch.txt
pandoc -f markdown -s src/routes/projects/reconstruction-error.svx -o txt/4.4-reconstruction-error.txt
pandoc -f markdown -s src/routes/projects/electromagnetic.svx -o txt/4.5-electromagnetic.txt


echo "--- Converting Tech ---"
# Tech
pandoc -f markdown -s src/routes/tech/index.svx -o txt/5-tech.txt
pandoc -f markdown -s src/routes/tech/mosh.svx -o txt/5.1-mosh.txt
pandoc -f markdown -s src/routes/tech/reacoma.svx -o txt/5.2-reacoma.txt
pandoc -f markdown -s src/routes/tech/ftis.svx -o txt/5.3-ftis.txt

echo "--- Converting Conclusion ---"
# Conclusion
pandoc -f markdown -s src/routes/conclusion.svx -o txt/6-conclusion.txt

echo "--- Merging Text Files ---"

python3 merge_text_files.py
