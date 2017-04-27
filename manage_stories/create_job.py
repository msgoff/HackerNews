rng=10000
for ix in range(12000000,10000000,-rng):
    print "for i in "+'{'+"{0}..{1}".format(ix,ix-rng)+'};'+'do ./get_stories.sh $i {}_{}'.format(ix,ix-rng)+';done'
    
#sample output
"""for i in {12000000..11850000};do ./get_stories.sh $i 12000000_11850000;done
for i in {11850000..11700000};do ./get_stories.sh $i 11850000_11700000;done
for i in {11700000..11550000};do ./get_stories.sh $i 11700000_11550000;done
for i in {11550000..11400000};do ./get_stories.sh $i 11550000_11400000;done
for i in {11400000..11250000};do ./get_stories.sh $i 11400000_11250000;done
for i in {11250000..11100000};do ./get_stories.sh $i 11250000_11100000;done
for i in {11100000..10950000};do ./get_stories.sh $i 11100000_10950000;done
for i in {10950000..10800000};do ./get_stories.sh $i 10950000_10800000;done
for i in {10800000..10650000};do ./get_stories.sh $i 10800000_10650000;done
for i in {10650000..10500000};do ./get_stories.sh $i 10650000_10500000;done
for i in {10500000..10350000};do ./get_stories.sh $i 10500000_10350000;done
for i in {10350000..10200000};do ./get_stories.sh $i 10350000_10200000;done
for i in {10200000..10050000};do ./get_stories.sh $i 10200000_10050000;done
for i in {10050000..9900000};do ./get_stories.sh $i 10050000_9900000;done"""
