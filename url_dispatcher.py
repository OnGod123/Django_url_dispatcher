class URLPattern:
  def __init__(self, path, view_func, name=None):
    self.path = path
    self.view_func = view_func
    self.name = name

class URLDispatcher:
  def __init__(self):
    self.patterns = []

  def register(self, path, view_func, name=None):
    self.patterns.append(URLPattern(path, view_func, name))

  def resolve(self, path):
    for pattern in self.patterns:
      # Simple string matching (can be extended with regular expressions)
      if pattern.path == path:
        return pattern.view_func()
    return None

# Example view functions
def home_view():
  return "Welcome to the Home page!"

def about_view():
  return "This is the About page!"

# Create a URL dispatcher instance
dispatcher = URLDispatcher()

# Register URL patterns
dispatcher.register('/', home_view)
dispatcher.register('/about/', about_view)

# Test the URL dispatcher
print(dispatcher.resolve('/'))  # Output: "Welcome to the Home page!"
print(dispatcher.resolve('/about/'))  # Output: "This is the About page!"
print(dispatcher.resolve('/contact/'))  # Output: None (No matching pattern found)

