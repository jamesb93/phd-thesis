pnpm i
pnpm run build
rm -rf /var/www/harnessing.xyz/html/*
rsync -a build/ /var/www/harnessing.xyz/html
systemctl restart nginx