#include "ClipboardXX\include\clipboardxx.hpp"
#include <iostream>

std::string get_text(std::string text)
{
    return text;
}
int main(int argc, char *argv[])
{
   
    std::cout << argv[1] << std::endl;
    clipboardxx::clipboard clipboard;
    std::string text = get_text(argv[1]);
    clipboard.copy(text);

    return 0;

}