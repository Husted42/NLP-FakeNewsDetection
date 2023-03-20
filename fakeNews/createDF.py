import pandas as pd

def getParts():
    dropList = ['domain', 'url', 'scraped_at', 'updated_at', 'title', 'authors', 'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary' ] # 'source'

    df = pd.read_csv('csvFile.csv', nrows=100000)
    
    # Filter fake
    df_fake = df.loc[df['type'] == 'fake']
    df_conspiracy = df.loc[df['type'] == 'conspiracy']


    #filter reliable
    df_reliable = df.loc[df['type'] == 'reliable']
    df_political = df.loc[df['type'] == 'political']

    #Concat
    df_reliable = pd.concat([df_political, df_reliable], ignore_index=True)
    df_filtered = pd.concat([df_fake, df_reliable], ignore_index=True)

    # Write DataFrame to CSV file
    df_filtered = df_filtered.drop(dropList, axis=1)
    df_filtered.drop_duplicates('insterted_at')
    df_filtered.to_csv('redactedSample.csv', index=False)
    
    print("Fake / reliable")
    print(df_fake.index)
    print(df_reliable.index)
    print("loaded index")
    print(df.index)
    print("filtered")
    print(df_filtered)
getParts()

def duplicateRemover():
    df = pd.read_csv('redactedSample.csv')
    df.drop_duplicates('content')
    df.to_csv('redactedSample2.csv', index=False)
    print(df)
    print (df.index)
    return None

#duplicateRemover()