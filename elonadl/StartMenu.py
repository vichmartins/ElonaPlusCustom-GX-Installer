import os
import sys
import winshell
from win32com.client import Dispatch
from pathlib import Path

class StartMenu:
    """
    A class to manage Windows Start Menu shortcuts for Elona Plus Custom-GX.
    """
    
    def __init__(self, install_path):
        self.install_path = install_path
        self.program_data = os.environ.get('PROGRAMDATA')
        self.start_menu_path = Path(self.program_data) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs'
        self.folder_name = 'ElonaPlusCustom-GX'
        self.folder_path = self.start_menu_path / self.folder_name
        
    def create_directory(self):
        """Create the directory in the Start Menu Programs folder if it doesn't exist."""
        try:
            if not self.folder_path.exists():
                self.folder_path.mkdir(parents=True, exist_ok=True)
                print(f"Created directory: {self.folder_path}")
            else:
                print(f"Directory already exists: {self.folder_path}")
            return True
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    def create_shortcut(self, shortcut_name="Elona Plus Custom-GX"):
        """
        Create a shortcut to the install_path in the Start Menu folder.
        
        Args:
            shortcut_name: The name of the shortcut (without .lnk extension)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Check if install_path exists
            if not Path(self.install_path).exists():
                print(f"Error: Install path does not exist: {self.install_path}")
                return False
                
            # Create directory if it doesn't exist
            if not self.create_directory():
                return False
                
            # Create shortcut
            shortcut_path = self.folder_path / f"{shortcut_name}.lnk"
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(str(shortcut_path))
            shortcut.Targetpath = self.install_path
            shortcut.WorkingDirectory = str(Path(self.install_path).parent)
            shortcut.save()
            
            print(f"Created shortcut: {shortcut_path}")
            return True
        except Exception as e:
            print(f"Error creating shortcut: {e}")
            return False
    
    def remove_shortcut(self, shortcut_name="Elona Plus Custom-GX"):
        """
        Remove the shortcut from the Start Menu folder.
        
        Args:
            shortcut_name: The name of the shortcut (without .lnk extension)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            shortcut_path = self.folder_path / f"{shortcut_name}.lnk"
            if shortcut_path.exists():
                shortcut_path.unlink()
                print(f"Removed shortcut: {shortcut_path}")
                return True
            else:
                print(f"Shortcut does not exist: {shortcut_path}")
                return False
        except Exception as e:
            print(f"Error removing shortcut: {e}")
            return False
    
    def remove_directory(self):
        """
        Remove the directory from the Start Menu Programs folder.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if self.folder_path.exists():
                # Check if the directory is empty
                if any(self.folder_path.iterdir()):
                    print(f"Directory is not empty: {self.folder_path}")
                    return False
                
                self.folder_path.rmdir()
                print(f"Removed directory: {self.folder_path}")
                return True
            else:
                print(f"Directory does not exist: {self.folder_path}")
                return False
        except Exception as e:
            print(f"Error removing directory: {e}")
            return False