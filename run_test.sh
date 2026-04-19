#!/bin/bash
cd /Users/nardusduplooy/Documents/navigator
source venv/bin/activate
python3 daily_briefing.py --test-send >> logs/scheduler.log 2>&1
echo "Test fired at $(date)" >> logs/scheduler.log
