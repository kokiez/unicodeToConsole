# unicodeToConsole
Converting unicode character to a c++ code e.g cout &lt;&lt; char(219).

![My Image](ascii2cpp.png)


## You can find ASCII character codes from this site.
https://theasciicode.com.ar/extended-ascii-code/box-drawings-single-line-vertical-right-character-ascii-code-195.html

### steps:
1. Add your ascii art into myascii.txt
2. Edit the python code, try finding the blocks code in the site.
3. It will take you max 5 or 10 minutes to edit this python code if else statements.
4. After you are done. run the python file, cout << (char)219; like codes will be generated in *codes.txt* file.

If you didnt understand anything, hit me up. Create an issue. 

If you could fork this project and add all the ascii codes, that would help a ton of people.

Thanks

## EXAMPLE C++ EDIT:
>HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
>
>int main() {
>
>	SetConsoleCP(2588);
>	
>	SetConsoleOutputCP(2588);
>	
>	std::cout << (char)223;
>	
>	}
