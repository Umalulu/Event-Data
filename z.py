import pandas as pd

# Read the two spreadsheets as dataframes
df1 = pd.read_excel('anon_data1.xlsx')
df2 = pd.read_excel('anon_data2.xlsx')

# Modify df1
df1['Participant Type'] = 'team leader'
df1 = df1.rename(columns={'Leader Name': 'Participant Name',
                          'Leader Phone': 'Participant Phone Number',
                          'Leader Email': 'Participant Email'})
df1 = df1.drop(['Leader College', 'Leader Year', 'Members'], axis=1)
df1 = df1[['Participant Name', 'Team Name', 'Participant Type',
          'Participant Phone Number', 'Participant Email']]

# Modify df2
df2 = df2.rename(columns={'Candidate\'s Name': 'Participant Name',
                          'Candidate Type': 'Participant Type',
                          'Candidate\'s Mobile': 'Participant Phone Number',
                          'Candidate\'s Email': 'Participant Email'})
df2 = df2.drop(['Team Id', 'Candidate\'s Gender', 'Course Pursuing',
               'Course Stream', 'Specialization', 'Year Of Study',
               'Passing Out Year', 'Candidate\'s Organisation',
               'Registration Time'], axis=1)
df2 = df2[['Participant Name', 'Team Name', 'Participant Type',
          'Participant Phone Number', 'Participant Email']]

# Combine the dataframes, discarding duplicates
combined_df = pd.concat([df1, df2], ignore_index=True).drop_duplicates()

# Save
combined_df.to_excel('data.xlsx', index=False)

