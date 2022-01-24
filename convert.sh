rm tmp/*
octave test.m $1
python3 convert.py $2