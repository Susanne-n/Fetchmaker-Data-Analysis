import fetchmaker
import numpy as np
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

# get the tail lengths of all rottweilers and print out the mean and std
rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

# on average, 8% of dogs in the FetchMaker system is expected to be rescues
# find out if the number of whippet rescues is statistically equal to the expected percentage of 8%
whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
print(num_whippet_rescues)
# number of whippets that is a rescue is 6
num_whippet = np.size(whippet_rescue)
print(num_whippet)
# total number of whippets is 100

pval = binom_test(6, 100, 0.08)
print(format(pval, '0.10f'))
# the difference in percentage is not significant (p = .58), the number of whippet rescues doesn't differ from the expected average of 8%

# perform a test to determine if there is a significant difference in average weights of three of the most popular dog breeds; whippets, terriers and pitbulls
weight_pitbull = fetchmaker.get_weight('pitbull')
weight_whippet = fetchmaker.get_weight('whippet')
weight_terrier = fetchmaker.get_weight('terrier')

weight_compare_test = f_oneway(weight_pitbull, weight_whippet, weight_terrier)
print(format(weight_compare_test.pvalue, '0.10f'))
# p < .01

# now perform another test to determine which of the pairs of these dog breeds differ from each other
values = np.concatenate([weight_pitbull, weight_whippet, weight_terrier])
labels = ['pitbull'] * len(weight_pitbull) + ['whippet'] * len(weight_whippet) + ['terrier'] * len(weight_terrier)
tukey_results = pairwise_tukeyhsd(values, labels, 0.05)
print(tukey_results)
# in the result table we can see that pitbulls and whippets are similar in weight, pitbulls and terriers differ in weight and terriers and whippets differ in weight as well

# find out if poodles and shih tzus have significantly different color breakdowns
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

# build a Chi Square contingency table with the number of occurences for all colors
color_table = [
  [
    np.count_nonzero(poodle_colors == 'black'),
    np.count_nonzero(shihtzu_colors == 'black')
  ],
  [
    np.count_nonzero(poodle_colors == 'brown'),
    np.count_nonzero(shihtzu_colors == 'brown')
  ],
  [
    np.count_nonzero(poodle_colors == 'gold'),
    np.count_nonzero(shihtzu_colors == 'gold')
  ],
  [
    np.count_nonzero(poodle_colors == 'grey'),
    np.count_nonzero(shihtzu_colors == 'grey')
  ],
  [
    np.count_nonzero(poodle_colors == 'white'),
    np.count_nonzero(shihtzu_colors == 'white')
  ]
]
print(color_table)

_, pval_color, _, _ = chi2_contingency(color_table)
print(pval_color)
# we can see there is a significant difference between poodle colors and shih tzu colors (p < .01)
