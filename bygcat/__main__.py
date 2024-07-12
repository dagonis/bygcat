import argparse

from core import BygCat

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('org', help='Your org')
    parser.add_argument('repo', help='Your repo')
    parser.add_argument('--titles', help='Issue titles, this is the arg that will specify which issues get created', nargs='+')
    parser.add_argument('--template', help='Issue template', default='issue_template.md')
    parser.add_argument('--tags', help='Service name', nargs='+')
    parser.add_argument('--token', help='Github token, this can also be an EnvVar called GITHUB_TOKEN')
    args = parser.parse_args()
    bygcat = BygCat(args.token, args.org, args.repo)
    bygcat.create_issues(args.tags, args.template, ['bug'])
    
if __name__ == '__main__':
    main()