class BrowserHistory:
    # start on 'homepage': one tab
    # visit another 'url'
    # get back history number of 'steps' | move forward in history number of 'steps'
    def __init__(self, homepage: str):
        self.history = [homepage] # initialize homepage
        self.curr_page = 0 # current url index
        self.fwd = 0 # number of urls displayed after going forward
        
    def visit(self, url: str) -> None:
        # visit url from curr. page
        # clears up forward history
        self.curr_page += 1
        # if curr_page = length of history, add to history 
        if self.curr_page == len(self.history):
            self.history.append(url)
        else: # set the current history w/ url to url 
            self.history[self.curr_page] = url
        self.fwd = self.curr_page # set the forward history to display the curr page
    
    def back(self, steps: int) -> str:
        # move steps back in history
        # if only 'x' steps in history AND 'steps > x', return 'x' steps
        self.curr_page = max(self.curr_page-steps, 0)
        return self.history[self.curr_page] # return curr. 'url' after moving back in history at_most steps

    def forward(self, steps: int) -> str:
        self.curr_page = min(self.curr_page + steps, self.fwd)
        return self.history[self.curr_page]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)