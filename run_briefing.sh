#!/bin/bash
cd /Users/nardusduplooy/Documents/navigator
source venv/bin/activate
python3 daily_briefing.py --briefing-only >> logs/scheduler.log 2>&1
echo "Briefing fired at $(date)" >> logs/scheduler.log
