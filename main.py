from wox import Wox
# from wox import WoxAPI
import time

from ctypes import cdll

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


class HelloWorld(Wox):

    def query(self, query):
        results = []
        results.append({
            "Title": "Goto Desktop X",
            "SubTitle": "Goto Desktop: {}".format(query),
            "IcoPath": "Images/app.ico",
            "JsonRPCAction": {
                "method": "gotoDesktop", "parameters": [query, "trash"]
                }
        })

        return results

    def gotoDesktop(self, desktop, trash):
        try:
            vda = cdll.LoadLibrary("VirtualDesktopAccessor")
            desktopNumber = int(desktop)
            vda.GoToDesktopNumber(desktopNumber)
            time.sleep(1)
        except ValueError:
            pass
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
    HelloWorld()
