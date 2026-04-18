from ui.playwright.pages.base_page import BasePage
from playwright.sync_api import Page


class CheckBoxPage(BasePage):
    PATH = "/checkbox"

    def __init__(self, page: Page):
        super().__init__(page)

        self.home_tree_item = page.locator("div[role='treeitem']").filter(has=page.get_by_text("Home"))
        self.home_expand_button = self.home_tree_item.locator(".rc-tree-switcher")

        self.documents_tree_item = page.locator("div[role='treeitem']").filter(has=page.get_by_text("Documents"))
        self.documents_expand_button = self.documents_tree_item.locator(".rc-tree-switcher")

        self.workspace_tree_item = page.locator("div[role='treeitem']").filter(has=page.get_by_text("WorkSpace"))
        self.workspace_expand_button = self.workspace_tree_item.locator(".rc-tree-switcher")

        self.react_tree_item = page.locator("div[role='treeitem']").filter(has=page.get_by_text("React"))
        self.react_checkbox = self.react_tree_item.locator(".rc-tree-checkbox")

        self.result_block = page.locator("#result")

    def expand_home(self):
        self.home_expand_button.click()

    def expand_documents(self):
        self.documents_expand_button.click()

    def expand_workspace(self):
        self.workspace_expand_button.click()

    def select_react_checkbox(self):
        self.react_checkbox.click()

    def should_see_result_block(self):
        self.should_be_visible(self.result_block)

    def should_have_selected_item(self, value: str):
        self.should_contain_text(self.result_block, value)
