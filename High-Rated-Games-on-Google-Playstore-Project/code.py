# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Code starts here
data = pd.read_csv(path)

plt.hist(data['Rating'].dropna(), normed = True, bins = 30)

data = data[data['Rating'] <= 5]
plt.hist(data['Rating'].dropna(), normed = True, bins = 30)
plt.ylabel("Rating")
plt.show()
print(data.shape)
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()

percent_null = total_null/data.isnull().count()

missing_data = pd.concat((total_null, percent_null), axis=1, keys=['Total', 'Percent'])

print("missing_data = {0}".format(missing_data))


data = data.dropna()

total_null_1 = data.isnull().sum()

percent_null_1 = total_null_1/data.isnull().count()

missing_data_1 = pd.concat((total_null_1, percent_null_1), axis = 1, keys= ['Total', 'Percent'])

print("missing_data = {0}".format(missing_data_1))
# code ends here


# --------------

#Code starts here
sns.catplot(x = 'Category', y = 'Rating', data = data, kind = 'box', height = 10)
plt.xlabel("Rating vs Category")
plt.xticks(rotation=90)
plt.show()


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

# Remove the "+" and "-" from Install columns
data.Installs = [x.strip('+') for x in data.Installs]
data.Installs = data['Installs'].str.replace(',', '')

# Convert the datatype of the Installs column into 'int'
data.Installs = data['Installs'].astype('int')

# Initalize the Labelencoder
le = LabelEncoder()

# Fit and transform the Install column using the the Label encoder
data['Installs'] = le.fit_transform(data['Installs'])

#data['']
sns.regplot(x='Installs', y = 'Rating', data=data)
plt.title("Rating vs Installs")
plt.show()

#Code ends here



# --------------
#Code starts here

# Print the value of Price column data

# Remove the '$' sign from the columns 
data['Price'] = data['Price'].str.replace('$', '')

# Convert the column into the integer type
data['Price'] = data['Price'].astype(float)

#print(data['Price'].value_counts())
# plot the Price vs Rating sing seaborn regplot
sns.regplot(x = "Price", y = "Rating", data = data)

# the titile name of the plot graph
plt.title("Rating vs Price")
plt.show()
#Code ends here


# --------------

#Code starts here

# split the elements in the Genres column and store only first element
data['Genres'] = data['Genres'].str.split(';').str[0]

gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index = False).mean()

#gr_mean.apply(lambda x : x.sort_values('Rating'))
gr_mean = gr_mean.sort_values('Rating', axis=0)

print(gr_mean['Rating'][0])
print(gr_mean['Rating'].iloc[-1:])



#Code ends here


# --------------

#Code starts here

# Convert "Last Updated" to datetime format.
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
print(data['Last Updated'])

# Get the closet date when the info was updated
max_date = data['Last Updated'].max()
print(max_date)

# subtract the columns representing date info and get the number of days in there difference. 
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

print(data['Last Updated Days'])
#Code ends here


