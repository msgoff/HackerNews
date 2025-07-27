for i in `seq 30000 1000 40000`;do  screen -dmS $i python get_stories.sh  $(($i+1)) $(($i + 1000));done
