from ctypes import cdll

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

import argparse
# may need to change dir/augment path to find the dll to call. In current config isn't
# needed
parser = argparse.ArgumentParser()
parser.add_argument('desktop', metavar='desktop', type=int, help='desktop number')
args = parser.parse_args()
vda = cdll.LoadLibrary("VirtualDesktopAccessor")
vda.GoToDesktopNumber(args.desktop)
print(f"Switching to desktop {args.desktop}")
