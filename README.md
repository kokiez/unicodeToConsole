# Clear content inside codes.txt and myascii.txt before running python file. <No requirements needed for python>

  
# unicodeToConsole

This code will help providing you the cout << charblabla; statements.
If you are printing extended chars in console. You might either get ? mark or you will have to import an external library. which burdens your project. You might get tons of errors, headaches and so on. So, here i introduce a simple python code. 

By entering your ascii blocks or bloody art in myascii.txt and upon running python file. Codes will be generated in codes.txt which you can copy paste into your cpp file and run your c++ file no matter in linux or VS22, VS19, it will work as shown below in image.
  
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



## EXAMPLE C++ EDIT:
>
>int main() {
>
>	SetConsoleCP(258);
>	
>	SetConsoleOutputCP(258);
>	
>	std::cout << (char)223;
>	
>	}
