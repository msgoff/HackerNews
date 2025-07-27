for i in `seq 20000 999 30000`;do screen -dmS $i python get_stories.py $(($i)) $(($i + 1000));done
