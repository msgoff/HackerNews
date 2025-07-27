for i in `seq 2001 999 10000`;do screen -dmS $i python get_stories.py $i $(($i + 999));done

