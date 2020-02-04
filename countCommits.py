import json
import requests
import datetime


def find_next(link):
    for i in link.split(","):
        a, b = i.split(";")
        if b.strip() == "rel='next'":
            return a.strip()[1: -1]


def count_repo_commits_total(com_url, _acc=0):
    req = requests.get(com_url)
    commits = json.loads(req.content)
    len_commits = len(commits)
    if len_commits == 0:
        return _acc
    link = req.headers.get("link")
    if link is None:
        return _acc + len_commits
    next_url = find_next(req.headers["link"])
    if next_url is None:
        return _acc + len_commits
    return count_repo_commits_total(next_url, _acc + len_commits)


def count_repo_commits_today(com_url, _acc=0):
    dt_today = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9))
    )
    today = "{}-{:02}-{:02}".format(dt_today.year, dt_today.month, dt_today.day)
    req = requests.get(com_url)
    commits = json.loads(req.content)
    len_commits = 0
    for c in commits:
        date_commit = c["commit"]["author"]["date"][:10]
        if date_commit == today:
            len_commits += 1
    if len_commits == 0:
        return _acc
    link = req.headers.get("link")
    if link is None:
        return _acc + len_commits
    next_url = find_next(req.headers["link"])
    if next_url is None:
        return _acc + len_commits
    return count_repo_commits_total(next_url, _acc + len_commits)


def count_user_commits(user):
    req = requests.get("https://api.github.com/users/{}/repos".format(user))
    repos = json.loads(req.content)

    for repo in repos:
        if repo["fork"]:
            continue
        total_commits = count_repo_commits_total(repo["url"] + "/commits")
        today_commits = count_repo_commits_today(repo["url"] + "/commits")
        repo["num_commits"] = total_commits
        repo["num_commits_today"] = today_commits
        yield repo


if __name__ == "__main__":
    user = "eS-1"
    total = 0
    c_today = 0
    for repo in count_user_commits(user):
        print("Repo '%(name)s'\n  %(num_commits)d commits, size %(size)d." % repo)
        total += repo["num_commits"]
        c_today += repo["num_commits_today"]
    print("Total commits: {}".format(total))
    print("Today commits: {}".format(c_today))
