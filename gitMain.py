from github import Github
import git


## Make a function called autoMaintain()
## This will allow the system to maintain
## a repository. Using the github module

def autoMaintain():
    g = Github("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")
    
    ## Repository Name
    repo = g.get_repo("UNF-AIRO/Experiments")


    ## What Branch it is on 
    branch = repo.get_branch("main")


    sha = branch.commit.sha
    commit = repo.get_commit(sha=sha)
    print(commit.commit.author)


autoMaintain()

# sha = data["pull_request"]["head"]["sha"]
# repo.get_commit(sha=sha).create_status(
#     state="pending",
#     target_url="https://FooCI.com",
#     description="FooCI is building",
#     context="ci/FooCI"
# )