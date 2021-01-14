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
df_join = df1.merge(right = df2,
                    left_on = df1.columns.to_list(),
                    right_on = df2.columns.to_list(),
                    how = 'outer')
# %%
records_present_in_df1_not_in_df2 = df_join.loc[df_join[df2.columns.to_list()].isnull().all(axis = 1), df1.columns.to_list()]
# %%
records_present_in_df2_not_in_df1 = df_join.loc[df_join[df1.columns.to_list()].isnull().all(axis = 1), df2.columns.to_list()]
# %%
