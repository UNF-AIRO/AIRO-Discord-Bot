from github import Github
import git

g = Github("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")

repo = g.get_repo("UNF-AIRO/Experiments")
branch = repo.get_branch("main")
sha = branch.commit.sha
commit = repo.get_commit(sha=sha)
print(commit.commit.author)

# sha = data["pull_request"]["head"]["sha"]
# repo.get_commit(sha=sha).create_status(
#     state="pending",
#     target_url="https://FooCI.com",
#     description="FooCI is building",
#     context="ci/FooCI"
# )

