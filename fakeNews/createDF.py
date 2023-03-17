import pandas as pd

def getParts():
    dropList = ['domain', 'url', 'scraped_at', 'updated_at', 'title', 'authors', 'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary' ] # 'source'

    df = pd.read_csv('sample.csv', nrows=250)
    
    # Filter
    df_fake = df.loc[df['type'] == 'fake']
    df_reliable = df.loc[df['type'] == 'reliable']

    #Concat the two dataframes
    df_filtered = pd.concat([df_fake, df_reliable], ignore_index=True)

    # Write DataFrame to CSV file
    df_filtered = df_filtered.drop(dropList, axis=1)
    df_filtered.to_csv('redactedSample.csv', index=False)
    
    print("Fake / reliable")
    print(df_fake.index)
    print(df_reliable.index)
    print("loaded index")
    print(df.index)
    print("filtered")
    print(df_filtered)
getParts()
