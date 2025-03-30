# Define a function that formats names into title case
def format_name(f_name, l_name):
    # Error checker if a null first/last name is provided
    if f_name == "" or l_name == "":
        return "You didn't input a valid full name"

    return f"{f_name.title()} {l_name.title()}"

# Test function
name = format_name('dEs', 'neWmAn')
print(name)