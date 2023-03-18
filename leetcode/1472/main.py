class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack_to_back = []
        self.stack_to_forward = []

        self.page_current = homepage

    def visit(self, url: str) -> None:
        self.stack_to_back.append(self.page_current)
        self.stack_to_forward = []

        self.page_current = url

    def back(self, steps: int) -> str:
        length_stack_to_back = len(self.stack_to_back)
        for _ in range(min(steps, length_stack_to_back)):
            self.stack_to_forward.append(self.page_current)
            self.page_current = self.stack_to_back.pop()

        return self.page_current

    def forward(self, steps: int) -> str:
        length_stack_to_forward = len(self.stack_to_forward)
        for _ in range(min(steps, length_stack_to_forward)):
            self.stack_to_back.append(self.page_current)
            self.page_current = self.stack_to_forward.pop()

        return self.page_current


browserHistory = BrowserHistory("leetcode.com")
print(browserHistory.visit("google.com") == None)
print(browserHistory.visit("facebook.com") == None)
print(browserHistory.visit("youtube.com") == None)
print(browserHistory.back(1) == "facebook.com")
print(browserHistory.back(1) == "google.com")
print(browserHistory.forward(1) == "facebook.com")
print(browserHistory.visit("linkedin.com") == None)
print(browserHistory.forward(2) == "linkedin.com")
print(browserHistory.back(2) == "google.com")
print(browserHistory.back(7) == "leetcode.com")
