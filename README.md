# Fetchmaker-Data-Analysis

Congratulations! You’ve just started working at the hottest new tech startup, FetchMaker. FetchMaker’s mission is to match up prospective dog owners with their perfect pet. Data on thousands of adoptable dogs are in FetchMaker’s system, and it’s your job to analyze some of that data.

The attributes that FetchMaker keeps track of are:

-   weight, an integer representing how heavy a dog is in pounds
-   tail_length, a float representing tail length in inches
-   age, in years
-   color, a String such as "brown" or "grey"
-   is_rescue, a boolean 0 or 1

The fetchmaker package lets you access this data for a specific breed of dog with the following format:
fetchmaker.get_weight("poodle")

The other methods are get_tail_length, get_color, get_age, and get_is_rescue, which all take a breed as an input.
