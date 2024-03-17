#!/bin/zsh

# Check if there are any existing tmux sessions
if tmux ls 2>&1 | grep -q "no server running"; then
    # If no sessions exist, start a new one
    tmux
else
    # If sessions exist, attach to the first one
    tmux attach-session
fi
