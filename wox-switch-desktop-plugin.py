from wox import Wox
# from wox import WoxAPI
# import time
import subprocess


# from wox import Wox

''' VirtualDesktopAccessorAPI
    * int GetCurrentDesktopNumber()
    * int GetDesktopCount()
    // Returns zeroed GUID with invalid number found
    * GUID GetDesktopIdByNumber(int number)
    * int GetDesktopNumber(IVirtualDesktop *pDesktop)
    * int GetDesktopNumberById(GUID desktopId)
    * GUID GetWindowDesktopId(HWND window)
    * int GetWindowDesktopNumber(HWND window)
    * int IsWindowOnCurrentVirtualDesktop(HWND window)
    * BOOL MoveWindowToDesktopNumber(HWND window, int number)
    * void GoToDesktopNumber(int number)
    * void RegisterPostMessageHook(HWND listener, int messageOffset)
    * void UnregisterPostMessageHook(HWND hwnd)

    // Returns 1 if pinned, 0 if not pinned, -1 if not valid
    * int IsPinnedWindow(HWND hwnd)
    * void PinWindow(HWND hwnd)
    * void UnPinWindow(HWND hwnd)

    // Returns 1 if pinned, 0 if not pinned, -1 if not valid
    * int IsPinnedApp(HWND hwnd)
    * void PinApp(HWND hwnd)
    * void UnPinApp(HWND hwnd)
    * int IsWindowOnDesktopNumber(HWND window, int number) /
    * void RestartVirtualDesktopAccessor() // Call this during taskbar created message

    * void EnableKeepMinimized() // Deprecated, does nothing
    * void RestoreMinimized() // Deprecated, does nothing
'''


class SwitchDesktop(Wox):

    def query(self, query):
        results = []
        results.append({
            "Title": "Goto Desktop Z",
            "SubTitle": f"Goto Desktop: {query}",
            "IcoPath": "Images/app.ico",
            "JsonRPCAction": {
                "method": "gotoDesktop", "parameters": [query]
                }
        })

        return results

    def gotoDesktop(self, desktop):
        # The following code will crash wox, so executing it via a sub process call
        # Instead.
        '''
        try:
            from ctypes import cdll
            vda = cdll.LoadLibrary("VirtualDesktopAccessor")
            desktopNumber = int(desktop)
            vda.GoToDesktopNumber(desktopNumber)
        except:
            pass
        '''
        subprocess.call(f'python cli-switch-desktop.py {desktop}')

        return

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath": "Images/app.ico"
        })
        return results


if __name__ == "__main__":
    SwitchDesktop()
