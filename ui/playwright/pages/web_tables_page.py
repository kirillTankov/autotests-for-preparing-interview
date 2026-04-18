from ui.playwright.pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class WebTablesPage(BasePage):
    PATH = "/webtables"

    def __init__(self, page: Page):
        super().__init__(page)

        self.add_button = page.get_by_role("button", name="Add")

        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.email_input = page.locator("#userEmail")
        self.age_input = page.get_by_placeholder("Age")
        self.salary_input = page.get_by_placeholder("Salary")
        self.department_input = page.get_by_placeholder("Department")
        self.submit_button = page.get_by_role("button", name="Submit")

        self.search_input = page.locator("#searchBox")
        self.table_rows = page.locator("table tbody tr")

    def row_by_email(self, email: str) -> Locator:
        return self.table_rows.filter(has_text=email)

    def row_cells_by_email(self, email: str) -> Locator:
        return self.row_by_email(email).locator("td")

    def add_user(
            self,
            first_name: str,
            last_name: str,
            age: str,
            email: str,
            salary: str,
            department: str,
    ):
        self.add_button.click()
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.age_input.fill(age)
        self.salary_input.fill(salary)
        self.department_input.fill(department)
        self.submit_button.click()

    def should_have_user_in_table(
        self,
        first_name: str,
        last_name: str,
        email: str,
        age: str,
        salary: str,
        department: str,
    ):
        row = self.row_by_email(email)
        self.should_have_count(row, 1)

        row_cells = row.locator("td")
        self.should_have_text(row_cells.nth(0), first_name)
        self.should_have_text(row_cells.nth(1), last_name)
        self.should_have_text(row_cells.nth(2), age)
        self.should_have_text(row_cells.nth(3), email)
        self.should_have_text(row_cells.nth(4), salary)
        self.should_have_text(row_cells.nth(5), department)