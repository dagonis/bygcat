from github import Github

class BygCat:
    def __init__(self, token: str, org: str, repo: str) -> None:
        self.token = token
        self.org = org
        self.repo = repo
        self.githut_client = Github(token)

    def create_issues(self, issue_titles: list, template: str, labels: list) -> bool:
        github_repo = self.githut_client.get_repo(f"{self.org}/{self.repo}")
        for issue_title in issue_titles:
            issue_template = open(template, 'r').read()
            github_repo.create_issue(title=issue_title, body=issue_template, labels=labels)
        return True