#!/usr/bin/env python3
"""Measure active Claude Code time per git branch from local session transcripts.

Usage:
    python3 scripts/medir-tiempo-ia.py AgentPlatform            # top branches
    python3 scripts/medir-tiempo-ia.py AgentPlatform feat/foo   # one branch

Active time = sum of gaps between consecutive messages on the branch, ignoring
gaps longer than IDLE_GAP (breaks, meetings, overnight). Messages from parallel
sessions on the same branch are merged into one timeline, so time is not
double counted.
"""
import collections
import datetime as dt
import glob
import json
import os
import sys

IDLE_GAP = 30 * 60  # seconds
PROJECTS = os.path.expanduser('~/.claude/projects')


def collect(repo):
    stamps = collections.defaultdict(list)
    pattern = os.path.join(PROJECTS, f'-Users-*-{repo}*', '*.jsonl')
    for path in glob.glob(pattern):
        with open(path, errors='ignore') as fh:
            for line in fh:
                try:
                    msg = json.loads(line)
                except ValueError:
                    continue
                branch, ts = msg.get('gitBranch'), msg.get('timestamp')
                if branch and ts and msg.get('type') in ('user', 'assistant'):
                    stamps[branch].append(dt.datetime.fromisoformat(ts.replace('Z', '+00:00')))
    return stamps


def summarize(times):
    times.sort()
    active = sum(g for g in ((b - a).total_seconds() for a, b in zip(times, times[1:])) if g < IDLE_GAP)
    return active / 3600, times[0].date(), times[-1].date(), len(times)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    repo, only = sys.argv[1], sys.argv[2:] or None
    rows = []
    for branch, times in collect(repo).items():
        if only and branch not in only:
            continue
        hours, first, last, count = summarize(times)
        rows.append((hours, branch, first, last, count))
    for hours, branch, first, last, count in sorted(rows, reverse=True)[:40]:
        print(f'{hours:6.1f} h  {first}..{last}  msgs={count:6d}  {branch}')


if __name__ == '__main__':
    main()
