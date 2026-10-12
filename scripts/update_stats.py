"""Lee contribuciones y repos públicos del usuario y regenera assets/header.svg."""
import json, os, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from header import build

USER = os.environ.get("GH_USER", "JhanpolPb")
TOKEN = os.environ["GITHUB_TOKEN"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def gql(query, **variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    data = json.load(urllib.request.urlopen(req))
    if "errors" in data:
        raise SystemExit(data["errors"])
    return data["data"]


info = gql(
    """query($login: String!) { user(login: $login) {
         contributionsCollection { contributionYears }
         repositories(privacy: PUBLIC, ownerAffiliations: OWNER) { totalCount } } }""",
    login=USER,
)["user"]

score = 0
for year in info["contributionsCollection"]["contributionYears"]:
    score += gql(
        """query($login: String!, $from: DateTime!, $to: DateTime!) { user(login: $login) {
             contributionsCollection(from: $from, to: $to) { contributionCalendar { totalContributions } } } }""",
        login=USER, **{"from": f"{year}-01-01T00:00:00Z", "to": f"{year}-12-31T23:59:59Z"},
    )["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]

coins = info["repositories"]["totalCount"]
with open(os.path.join(ROOT, "assets", "header.svg"), "w", encoding="utf-8", newline="\n") as f:
    f.write(build(score, coins))
print(f"score={score} coins={coins}")
