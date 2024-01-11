
# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

#import webrepl

#webrepl.start()
# import senko

# OTA = senko.Senko(
#   user="ocktokit", # Required
#   repo="octokit-iot", # Required
#   branch="master", # Optional: Defaults to "master"
#   working_dir="app", # Optional: Defaults to "app"
#   files = ["boot.py", "main.py"]
# )

# if OTA.update():
#     print("Updated to the latest version! Rebooting...")
#     machine.reset()

# if OTA.fetch():
#     print("A newer version is available!")
# else:
#     print("Up to date!")
