#include <WinUser.h>
#include <WinBase.h>
#include <Lmcons.h>
#include <windows.h>
#include <iostream>
int main()
{
    //HWND hwnd = FindWindowA(NULL, "Untitled - Notepad");
    //std::cout << hwnd << std::endl;
    // char username[UNLEN];
    // DWORD username_len = UNLEN+1;
    // bool name =  GetUserNameA(username, &username_len);
    // std::cout << name << username << std::endl;
    // //std::cout << UNLEN+1;
    DWORD all[UNLEN];
    DWORD q = UNLEN +1;
    bool reg = GetSystemRegistryQuota
    std::cout << all << "" << q <<std::endl;
    return 0;
}