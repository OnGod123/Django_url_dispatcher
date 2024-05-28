# Define a dictionary to store URL patterns and their corresponding view functions
url_patterns = {}

# Function to register URL patterns and associate them with view functions
def path(pattern):
    # Decorator function to register URL patterns
    def decorator(view_func):
        url_patterns[pattern] = view_func
        return view_func
    return decorator

# Function to match a URL pattern and execute the corresponding view function
def resolve(path):
    # Iterate over registered URL patterns
    for pattern, view_func in url_patterns.items():
        # Check if the URL matches the pattern
        if pattern == path:
            # If a match is found, execute the corresponding view function and return the response
            return view_func()
    # If no matching pattern is found, return None
    return None

# Example view functions
def home_view():
    return "Welcome to the Home page!"

def about_view():
    return "This is the About page!"

# Define URL patterns and associate them with view functions using the `path` decorator
@path('/')
def home():
    return home_view()

@path('/about/')
def about():
    return about_view()

# Test the URL dispatcher by resolving different paths
print(resolve('/'))       # Output: "Welcome to the Home page!"
print(resolve('/about/')) # Output: "This is the About page!"
print(resolve('/contact/'))  # Output: None (No matching pattern found)

