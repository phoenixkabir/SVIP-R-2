import pandas as pd

def ab_test(group_a_file, group_b_file):
    group_a = pd.read_csv(group_a_file)
    group_b = pd.read_csv(group_b_file)
    result = compare_groups(group_a, group_b)
    print(f'Group A Engagement: {result[0]}, Group B Engagement: {result[1]}')

def compare_groups(group_a, group_b):
    # Example comparison logic
    mean_a = group_a['engagement'].mean()
    mean_b = group_b['engagement'].mean()
    return mean_a, mean_b

if __name__ == "__main__":
    ab_test('group_a.csv', 'group_b.csv')
