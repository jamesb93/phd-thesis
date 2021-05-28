# This script converts each of the written sections into a docx document, to be opened in pages or Microsoft Word

echo "--- Building ---"
pnpm run build

echo "--- Cleaning Up Old Runs ---"
rm -rf docx
mkdir -p docx

echo "--- Converting Abstract/Home ---"
pandoc -f markdown -s src/routes/index.svx -o docx/0-abstract.docx

echo "--- Converting Introduction and Literature Review ---"
pandoc -f markdown -s src/routes/introduction.svx -o docx/1-introduction.docx
pandoc -f markdown -s src/routes/preoccupations.svx -o docx/2-preoccupations.docx
pandoc -f markdown -s src/routes/content-awareness.svx -o docx/3-content-awareness.docx

echo "--- Converting Projects ---"
# Projects
pandoc -f markdown -s src/routes/projects/index.svx -o docx/4-projects.docx
pandoc -f markdown -s src/routes/projects/stitch-strata.svx -o docx/4.1-stitch-strata.docx
pandoc -f markdown -s src/routes/projects/annealing-strategies.svx -o docx/4.2-annealing-strategies.docx
pandoc -f markdown -s src/routes/projects/refracted-touch.svx -o docx/4.3-refracted-touch.docx
pandoc -f markdown -s src/routes/projects/reconstruction-error.svx -o docx/4.4-reconstruction-error.docx
pandoc -f markdown -s src/routes/projects/electromagnetic.svx -o docx/4.5-electromagnetic.docx


echo "--- Converting Tech ---"
# Tech
pandoc -f markdown -s src/routes/tech/index.svx -o docx/5-tech.docx
pandoc -f markdown -s src/routes/tech/mosh.svx -o docx/5.1-mosh.docx
pandoc -f markdown -s src/routes/tech/reacoma.svx -o docx/5.2-reacoma.docx
pandoc -f markdown -s src/routes/tech/ftis.svx -o docx/5.3-ftis.docx

echo "--- Converting Conclusion ---"
# Conclusion
pandoc -f markdown -s src/routes/conclusion.svx -o docx/6-conclusion.docx

echo "--- Converting References ---"
pandoc -f markdown build/references/index.html -o docx/7-references-and-links.docx

zip -vr docx-conversion.zip docx/ -x "*.DS_Store"
