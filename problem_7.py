# HTTPRouter using a Trie
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,parts,handler):
        # Initialize the trie with an root node and a handler, 
		# this is the root path or home page node
        self.root = RouteTrieNode()
        self.insert(parts,handler)

    def insert(self, parts,handler):
        # recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        current_node = self.root
        for part in parts[:-1]:
            try:
                current_node = current_node.children[part]
            except KeyError:
                current_node.insert(part)
                current_node = current_node.children[part]


        current_node.insert(parts[-1],handler)
        
            

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path in paths:
            try:
                current_node = current_node.children[path]
            except:
                return None

        return current_node.handler

            
        

# A RouteTrieNode will be similar to our autocomplete TrieNode... 
# with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, path,handler=None):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)



# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler,not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found
        # responses as well!
        self.route_trie = RouteTrie(["root"],root_handler)
        self.not_found_handler = not_found_handler
            

    def add_handler(self, route,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route = "root" + route
        parts  = self.split_path(route)

        self.route_trie.insert(parts,handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        route = "root" + route
        parts = self.split_path(route)
        handler = None

        if len(parts) > 0:
            handler = self.route_trie.find(parts)

            if handler:
                return handler

            return self.not_found_handler

            


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
            return list(filter(None,path.split("/")))


# Test cases

if __name__ == "__main__":
    # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home/about/us", "us handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' 
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler' 
    print(router.lookup("/home/about/me")) # should print 'not found handler' 
    print(router.lookup("/home/about/us")) # should print 'us handler' 
