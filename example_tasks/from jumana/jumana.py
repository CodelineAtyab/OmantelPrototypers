"""
shutdown_manager.py

Handles machine shutdown / reboot for the kiosk.

Two ways to trigger a shutdown:
  1. Manually, from a menu option   -> shutdown_machine() / reboot_machine()
  2. Automatically, at closing time -> start_auto_shutdown()

Keep TEST_MODE = True while developing so nothing actually powers off.
Flip it to False only on the live terminal.
"""

import os
import platform
import threading
import time
from datetime import datetime, timedelta

# ---------- Configuration ----------
TEST_MODE = True              # True = print only, no real shutdown.
AUTO_SHUTDOWN_TIME = "22:00"  # 24h "HH:MM" closing time. Set to None to disable.


def _run_power_command(reboot=False):
    """Build and run the OS-specific power command."""
    system = platform.system()
    if system == "Windows":
        cmd = "shutdown /r /t 0" if reboot else "shutdown /s /t 0"
    elif system in ("Linux", "Darwin"):
        cmd = "shutdown -r now" if reboot else "shutdown -h now"
    else:
        raise OSError(f"Unsupported platform: {system}")

    action = "REBOOT" if reboot else "SHUTDOWN"
    if TEST_MODE:
        print(f"[TEST_MODE] Would {action} now -> {cmd}")
        return
    print(f"{action} -> {cmd}")
    os.system(cmd)


def shutdown_machine():
    _run_power_command(reboot=False)


def reboot_machine():
    _run_power_command(reboot=True)


# ---------- Auto shutdown at closing time ----------
def _seconds_until(target):
    now = datetime.now()
    target_dt = datetime.combine(now.date(), target)
    if target_dt <= now:                 # closing time already passed today
        target_dt += timedelta(days=1)   # schedule for tomorrow
    return (target_dt - now).total_seconds()


def _auto_shutdown_loop(target):
    while True:
        time.sleep(_seconds_until(target))
        shutdown_machine()
        time.sleep(60)  # roll past the trigger minute before re-scheduling


def start_auto_shutdown():
    """Start the background timer. Call once when the app launches."""
    if not AUTO_SHUTDOWN_TIME:
        return
    target = datetime.strptime(AUTO_SHUTDOWN_TIME, "%H:%M").time()
    threading.Thread(target=_auto_shutdown_loop, args=(target,), daemon=True).start()
    print(f"Auto-shutdown scheduled for {AUTO_SHUTDOWN_TIME} daily.")

start_auto_shutdown()