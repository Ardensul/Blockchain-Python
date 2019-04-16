import sys
from subprocess import run

## ATTENTION: Présentation de sale
def CheckDependencies():
    print("Checking dependencies")
    try:
        import pip
        print("pip found")
        # Import PyQt5
        try:
            import PyQt5
            print("PyQt5 found")
        except ImportError:
            print("PyQt5 not found")
            if run("pip install pyqt5") != 0:
                try:
                    from tkinter import messagebox
                    messagebox.showerror("Error", "pip could not install PyQt5 on your system.")
                except:
                    print("Error: pip could not install PyQt5 on your system.")
                return False

        return True
    except:
        print("pip not found")
        try:
            from tkinter import messagebox
            messagebox.showerror("Error", "This application requires pip to be installed on your system.")
        except ImportError:
            print("Error: This application requires pip to be installed on your system.")
        return False
