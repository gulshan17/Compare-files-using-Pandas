# %%
import pandas as pd
# %%
df1 = pd.read_excel('file1.xlsx')
df2 = pd.read_excel('file2.xlsx')
# %%
df_join = df1.merge(right = df2,
                    left_on = df1.columns.to_list(),
                    right_on = df2.columns.to_list(),
                    how = 'outer')
# %%
df1.rename(columns = lambda x : x + '_file1', inplace = True)
df2.rename(columns = lambda x : x + '_file2', inplace = True)
# %%
df1_columns_to_join = df1.columns.to_list()
df2_columns_to_join = df2.columns.to_list()
# %%
# columns to exclude while joining, mention the columns to exclude while matching the data in comma separated like ['column1', 'column2']
df1_columns_to_exclude_join = []
df2_columns_to_exclude_join = []
# %%
df1_columns_to_exclude_join = [x if x[-6 : ] == '_file1' else x + '_file1' for x in df1_columns_to_exclude_join]

df2_columns_to_exclude_join = [x if x[-6 : ] == '_file2' else x + '_file2' for x in df2_columns_to_exclude_join]
# %%
df1_columns_to_join = [x for x in df1_columns_to_join if x not in df1_columns_to_exclude_join]

df2_columns_to_join = [x for x in df2_columns_to_join if x not in df2_columns_to_exclude_join]
# %%
df_join = df1.merge(right = df2,
                    left_on = df1_columns_to_join,
                    right_on = df2_columns_to_join,
                    how = 'outer')
# %%
records_present_in_df1_not_in_df2 = df_join.loc[df_join[df2_columns_to_join].isnull().all(axis = 1), df1.columns.to_list()]
# %%
records_present_in_df2_not_in_df1 = df_join.loc[df_join[df1_columns_to_join].isnull().all(axis = 1), df2.columns.to_list()]
# %%
