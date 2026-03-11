# load the raw recipe dataset
# read the source CSV into a dataframe

# normalize incoming column names
# - lowercase
# - strip whitespace
# - replace spaces with underscores if desired

# rename raw dataset columns into the standard schema names
# use a mapping dictionary to align source columns to project columns

# clean text fields
# - strip extra whitespace
# - handle null values
# - standardize empty strings

# parse list-like columns
# - ingredients
# - instructions
# - tags
# handle cases where the source may contain:
# - JSON strings
# - comma-separated strings
# - already-parsed lists

# normalize time fields
# convert text-based prep/cook times into numeric minute columns

# calculate total time if enough inputs are available

# ensure all required schema columns exist
# add missing standard columns with default values

# reorder columns into the standard schema order

# save the cleaned recipe dataset to processed output

# include a main block so the script can be run directly for testing
# when run directly:
# - load raw recipe data
# - clean and standardize it
# - save processed recipe data
# - print a success message
