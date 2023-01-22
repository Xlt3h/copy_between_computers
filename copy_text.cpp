#include "ClipboardXX\include\clipboardxx.hpp"
#include <iostream>

int main(int argc, char *argv[])
{
    std::string arguments = "";
    for (int i = 1; i < argc; i++)
    {
        arguments += argv[i];
        arguments += " ";
    }
    
    
    clipboardxx::clipboard clipboard;
    std::string text = arguments;
    
    clipboard.copy(text);

    return 0;

}