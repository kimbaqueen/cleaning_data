import pandas as pd

data = pd.read_csv('artwork_sample.csv')
# *********************************** Understanding your data ***********************************
print(data.head())
print(data.info())
print(data.dtypes)

data.acquisitionYear = data.acquisitionYear.astype(float)
print(data.dtypes)

fulldf = pd.read_csv('artwork_data.csv', low_memory=False)

fulldf.height = pd.to_numeric(fulldf.height, errors="coerce")

print(fulldf.height.dtype)

# *********************************** Aggregating, Normalizing, Transforming & Filtering data ***********************************
print(data.year)
print(data.year.min())
print(data.year.max())
print(data.year.sum())
print(data.year.mean())
print(data.year.std())

print(data.artist.min())
print(data.artist.sum())

# data.agg(['min', 'max, 'mean', 'std'])
# normalization with min, max, mean, std

print(data.height.mean())
print(data.height.mean())

height = data.height
norm = (height - height.mean())/height.std()
print(norm)

# to change need to set new values with variable or make new column. Use [] & ''
data['standardized_height'] = norm
# print(data.info)

data.height.transform(lambda x: print(x))
# can create new series with lambda
# print(data.height.transform(lambda x: x))

# most powerful with group by
# print(data.groupby('artist'))
# print(data.groupby('artist').transform('nunique'))

# print(data.groupby('artist')['height'].transform('mean'))

# print(data.head())
# print(data.filter(items=['id', 'artist']))

print(data.filter(like='year'))
print(data.filter(like='artist'))
print(data.filter(regex='(?i)year'))
print(data.filter(axis=0, regex='^100.$'))
print(data.filter(regex='^100(0|2|4|6|8)$', axis=0))

# *********************************** Removing & Fixing Columns with Pandas ***********************************
# each drop returns a new dataframe but doesn't change the original unless you pass the inplace=True like in sample below
# data.drop(columns=['id'], inplace=True)

# drop by row
# data.drop(0)
# or if want to drop multiple rows, use labels
# data.drop(labels=[0,1,2])

# drop by column
# data.drop('id', axis=1)
# or the below to drop an array of columns
# data.drop(columns=['id'])

# when loading a database file you can also select which columns you want to load in
# like sample below, and will get a dataframe with just those columns
# data = pd.read_csv('artwork_sample.csv', usecols=['artist', 'title'])


# cleaning up capitalization
# lowercase all columns
# data.columns.str.lower()

# for more control just 1 column example: but you have to set it as a variable in order to make real changes.
data.columns = [x.lower() for x in data.columns]

# you can also use map
# data.columns = map(lambda x: x.lower(), data.columns)

# map & for in methods
# to use for in methods, import re
# import re
# data.columns = [re.sub(r'([A-Z])', r'_\1', x).lower() for x in data.columns]

# rename columns - returns new dataframe, unless you again add to use inplace=True to change original dataframe
# data.rename(columns={"thumbnailUrl": "thumbnail"}, inplace=True)

# or can do this same using lambda, powerful way to rename it
# data.rename(columns=lambda x: x.lower(), inplace=True)

# *********************************** Index & filtering Columns datasets ***********************************

# print(data['id'][1])
# print(data[1:5])['artist']

# print(data[1:5])['artist']

# .loc uses labels/index, inclusive of last
# print(data.loc[0, :])
# print(data.loc[0:2, :])
# print(data.loc[0:2, 'title'])

# iloc uses integer positions of rows/columns instead of labels, exclusive of last
# print(data.iloc[0, :])
# print(data.iloc[0:3, :])
# print(data.iloc[0:3, 0:3])

# str.contains it is case sensitive by default!
# print(data.medium)
# print(type(data.medium))
# convert series to a string
# data.medium.str
# print(data.medium.str.contains('Graphite'))

# print(data.loc[data.medium.str.contains('Graphite'), ['artist', 'medium']])

# to bypass the case sensitive issue, 
# data.loc[data.medium.str.contains('Graphite', case=False), ['artist', 'medium']]

# or regex (regular expression)
# data.loc[data.medium.str.contains('(?i)Graphite', regex=True), ['artist', 'medium']]
# can also combine ands/ors with regex
# data.loc[data.medium.str.contains('(?i)Graphite', regex=True), ['artist', 'medium']] | data.medium.str.contains('(?i)Line, regex=True'), ['artist', 'medium']
# or finally an even simpler way to code the line above:
# data.loc[data.medium.str.contains('graphite|line', case=False, regex=True), ['artist', 'medium']]

# *********************************** Handling Bad, Missing, & Duplicate Data  ***********************************

# strip
print(data.title.str.strip())
# but need to reset variable in order to make it real
data.title = data.title.str.strip()

data.loc[data.title.str.contains('\s$', regex=True)]

# replacing bad data - 
# check for not a number columns
pd.isna(data.loc[:, 'dataText'])

# to use NAN need to import numpy, but it won't be real until.. add in: inplace=True
from numpy import nan
data.replace({'dateText': {'date not known': nan}}, inplace=True)

# but need to add in column specifically or will change all!
data.loc[data.dateText == 'date not known', ['dateText']] = nan

# find non numerical years & replace with NAN
data.loc[data.year.notnull() & data.year.astype(str).str.contains('[^0-9]')]
# always include columns when using loc! ex. year added below.
# data.loc[data.year.notnull() & data.year.astype(str).str.contains('[^0-9]')], ['year'] = nan

# fill in NAN with another value, but will fill for all unless you pass a value & make it real with inplace=True
data.fillna(value=('depth', 0), inplace=True)

#  Drop NAN
# see shape rows x columns by using the .shape method but won't be real until inplace=True
print(data.shape)
print(data.dropna().shape)
print(data.dropna(how='all').shape)

# set threshold of NAN allowed values
print(data.dropna(thres=15).shape)
print(data.dropna(subset=['year', 'acquisitionYear'], how='all').shape)

# identify & drop duplicates
data.drop_duplicates()

data.drop_duplicates(subset=['artist'])

# but can also specify which duplicates kept with keep='last', keep=False etc.. and make it real with inplace=True

# keep=false to identify which duplicated row is True.

# use loc to find duplicates too.
data.loc[data.title.str.contains('The Circle of the Lustful')]
