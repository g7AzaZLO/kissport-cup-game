[app]

# (str) Title of your application
title = Cup Game

# (str) Package name
package.name = cupgame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py

# (str) Application entry point
source.main = android.py

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Supported platforms
platforms = android

# (list) Permissions
android.permissions = INTERNET

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Supported orientation
orientation = portrait
