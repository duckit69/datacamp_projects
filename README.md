# Datacamp projects

This is a repo for projects in the machine learning specialist course in datacamp
## Agriculture Project Notes:
1. df.isna().sum().sort_values() is a good way to find missing values per columns
2. dropping columns or rows is better done by df.drop(axis=0/1 for row/col respectively)
3. to extract a df column with its values as 2D df use df.[[col_name]] ( .values/reshape(-1,1) can be used too but the return is a numpy array instead)
