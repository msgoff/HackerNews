while read f; do echo $f>>get_ids_done;./get_stories.sh $f HN_Stories_2;done <get_ids
