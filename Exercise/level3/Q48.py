'''Create a Paginator iterator class that accepts a list and page_size. Each call to next()
returns the next page as a sublist. Use it to display results page by page.'''

class Paginator:
    def __init__(self, data, page_size):
        self.data = list(data)          
        self.page_size = page_size
        self.index = 0                  
        self.total_pages = (len(self.data) + page_size - 1) // page_size 
        self.current_page = 0           

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
      
        start = self.index
        end = min(self.index + self.page_size, len(self.data))
        page = self.data[start:end]

        self.index += self.page_size
        self.current_page += 1

        print(f"Page {self.current_page} of {self.total_pages}")
        return page


numbers = list(range(25))

paginator = Paginator(numbers, 5)

for page in paginator:
    print(page)
