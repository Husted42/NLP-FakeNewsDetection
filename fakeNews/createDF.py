import pandas as pd

def getParts():
    df = pd.read_csv('csvFile.csv', skiprows=range(50001, 100000), nrows=50000)

    # Filter
    df_fake = df.loc[df['type'] == 'fake']
    df_reliable = df.loc[df['type'] == 'fake']

    #Concat the two dataframes
    df_filtered = pd.concat([df_fake, df_reliable], ignore_index=True)

    # Write DataFrame to CSV file
    df_filtered.to_csv('filtered_file.csv', index=False)
    
    print(df_fake)
    print(df_reliable)
    print(df)
    print(df_filtered)
#getParts()

def something():
    df1 = pd.read_csv('filtered_file.csv')
    df2 = pd.read_csv('filtered_file2.csv')
    df = pd.concat([df1, df2], ignore_index=True)
    df = df.drop(['domain', 'url', 'scraped_at', 'updated_at', 'title', 'authors', 'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary', 'source' ], axis=1)
    df = df.drop_duplicates()
    df.to_csv('readyCsv.csv', index=False)
    print(df)
#something()
