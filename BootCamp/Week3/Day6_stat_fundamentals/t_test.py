from scipy.stats import ttest_ind

# sample dataset
grp1 = [2.1,2.5,2.8,3.0,3.2]
grp2 = [1.8,2.0,2.4,2.7,2.9]

# Perform t-test
t_stat, p_value = ttest_ind(grp1,grp2)
print("T-Statistic: ",t_stat)
print("P-Value: ",p_value)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Failed to reject the null hypothesis: No significant difference")
