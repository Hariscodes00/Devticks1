# Write a script that:
# 1.checks if a folder called reports exists
# 2.if not, creates it
# 3.otherwise, prints “Folder already exists”

import os
folder = "report"
if not os.path.exists("report"):
    os.mkdir("report")
    print(f"The folder {folder} was created")
else :
    print("folder already exist")