BASENAME=manual_guildwars_ithambar

rm -rf $BASENAME
rm -f $BASENAME.apworld

mkdir $BASENAME

cp -r src/* $BASENAME
zip -r $BASENAME.zip $BASENAME/*
mv $BASENAME.zip $BASENAME.apworld
