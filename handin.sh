rm -rf build/*
rm -rf ~/Cloud/PhD/Written\ Component/*
pnpm run build
cp -r build/* ~/Cloud/PhD/Written\ Component

python flatten_count.py
sh sync.sh
