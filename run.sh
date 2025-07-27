for i in `seq 10001 999 20000`;do screen -dmS $i python get_stories.py $(($i+1)) $(($i + 999));done
