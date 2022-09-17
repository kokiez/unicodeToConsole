with open ("myascii.txt",encoding="utf-8") as fin:
    for line in fin:
        for char in line:
            if char == " ":
                save = 'std::cout << " ";'

            if char == "NULL":
                save = 'std::cout << (char)00;'
                
            if char == "SOH":
                save = 'std::cout << (char)01;'
                
            if char == "STX":
                save = 'std::cout << (char)02;'
                
            if char == "ETX":
                save = 'std::cout << (char)03;'
                
            if char == "EOT":
                save = 'std::cout << (char)04;'
                
            if char == "ENQ":
                save = 'std::cout << (char)05;'
                
            if char == "ACK":
                save = 'std::cout << (char)06;'
                
            if char == "BEL":
                save = 'std::cout << (char)07;'
                
            if char == "BS":
                save = 'std::cout << (char)08;'
                
            if char == "HT":
                save = 'std::cout << (char)09;'
                
            if char == "LF":
                save = 'std::cout << (char)10;'
                
            if char == "VT":
                save = 'std::cout << (char)11;'
                
            if char == "FF":
                save = 'std::cout << (char)12;'
                
            if char == "CR":
                save = 'std::cout << (char)13;'
                
            if char == "SO":
                save = 'std::cout << (char)14;'
                
            if char == "SI":
                save = 'std::cout << (char)15;'
                
            if char == "DLE":
                save = 'std::cout << (char)16;'
                
            if char == "DC1":
                save = 'std::cout << (char)17;'
                
            if char == "DC2":
                save = 'std::cout << (char)18;'
                
            if char == "DC3":
                save = 'std::cout << (char)19;'
                
            if char == "DC4":
                save = 'std::cout << (char)20;'
                
            if char == "NAK":
                save = 'std::cout << (char)21;'
                
            if char == "SYN":
                save = 'std::cout << (char)22;'
                
            if char == "ETB":
                save = 'std::cout << (char)23;'
                
            if char == "CAN":
                save = 'std::cout << (char)24;'
                
            if char == "EM":
                save = 'std::cout << (char)25;'
                
            if char == "SUB":
                save = 'std::cout << (char)26;'
                
            if char == "ESC":
                save = 'std::cout << (char)27;'
                
            if char == "FS":
                save = 'std::cout << (char)28;'
                
            if char == "GS":
                save = 'std::cout << (char)29;'
                
            if char == "RS":
                save = 'std::cout << (char)30;'
                
            if char == "US":
                save = 'std::cout << (char)31;'
                
            if char == "DEL":
                save = 'std::cout << (char)127;'
                
            if char == "space":
                save = 'std::cout << (char)32;'
                
            if char == "!":
                save = 'std::cout << (char)33;'
                
            if char == '"':
                save = 'std::cout << (char)34;'
                
            if char == "#":
                save = 'std::cout << (char)35;'
                
            if char == "$":
                save = 'std::cout << (char)36;'
                
            if char == "%":
                save = 'std::cout << (char)37;'
                
            if char == "&":
                save = 'std::cout << (char)38;'
                
            if char == "'":
                save = 'std::cout << (char)39;'
                
            if char == "(":
                save = 'std::cout << (char)40;'
                
            if char == ")":
                save = 'std::cout << (char)41;'
                
            if char == "*":
                save = 'std::cout << (char)42;'
                
            if char == "+":
                save = 'std::cout << (char)43;'
                
            if char == ",":
                save = 'std::cout << (char)44;'
                
            if char == "-":
                save = 'std::cout << (char)45;'
                
            if char == ".":
                save = 'std::cout << (char)46;'
                
            if char == "/":
                save = 'std::cout << (char)47;'
                
            if char == "0":
                save = 'std::cout << (char)48;'
                
            if char == "1":
                save = 'std::cout << (char)49;'
                
            if char == "2":
                save = 'std::cout << (char)50;'
                
            if char == "3":
                save = 'std::cout << (char)51;'
                
            if char == "4":
                save = 'std::cout << (char)52;'
                
            if char == "5":
                save = 'std::cout << (char)53;'
                
            if char == "6":
                save = 'std::cout << (char)54;'
                
            if char == "7":
                save = 'std::cout << (char)55;'
                
            if char == "8":
                save = 'std::cout << (char)56;'
                
            if char == "9":
                save = 'std::cout << (char)57;'
                
            if char == ":":
                save = 'std::cout << (char)58;'
                
            if char == ";":
                save = 'std::cout << (char)59;'
                
            if char == "<":
                save = 'std::cout << (char)60;'
                
            if char == "=":
                save = 'std::cout << (char)61;'
                
            if char == ">":
                save = 'std::cout << (char)62;'
                
            if char == "?":
                save = 'std::cout << (char)63;'
                
            if char == "@":
                save = 'std::cout << (char)64;'
                
            if char == "A":
                save = 'std::cout << (char)65;'
                
            if char == "B":
                save = 'std::cout << (char)66;'
                
            if char == "C":
                save = 'std::cout << (char)67;'
                
            if char == "D":
                save = 'std::cout << (char)68;'
                
            if char == "E":
                save = 'std::cout << (char)69;'
                
            if char == "F":
                save = 'std::cout << (char)70;'
                
            if char == "G":
                save = 'std::cout << (char)71;'
                
            if char == "H":
                save = 'std::cout << (char)72;'
                
            if char == "I":
                save = 'std::cout << (char)73;'
                
            if char == "J":
                save = 'std::cout << (char)74;'
                
            if char == "K":
                save = 'std::cout << (char)75;'
                
            if char == "L":
                save = 'std::cout << (char)76;'
                
            if char == "M":
                save = 'std::cout << (char)77;'
                
            if char == "N":
                save = 'std::cout << (char)78;'
                
            if char == "O":
                save = 'std::cout << (char)79;'
                
            if char == "P":
                save = 'std::cout << (char)80;'
                
            if char == "Q":
                save = 'std::cout << (char)81;'
                
            if char == "R":
                save = 'std::cout << (char)82;'
                
            if char == "S":
                save = 'std::cout << (char)83;'
                
            if char == "T":
                save = 'std::cout << (char)84;'
                
            if char == "U":
                save = 'std::cout << (char)85;'
                
            if char == "V":
                save = 'std::cout << (char)86;'
                
            if char == "W":
                save = 'std::cout << (char)87;'
                
            if char == "X":
                save = 'std::cout << (char)88;'
                
            if char == "Y":
                save = 'std::cout << (char)89;'
                
            if char == "Z":
                save = 'std::cout << (char)90;'
                
            if char == "[":
                save = 'std::cout << (char)91;'

            #python doc says use double slash which represents single slash.    
            if char == "\\":
                save = 'std::cout << (char)92;'
                
            if char == "]":
                save = 'std::cout << (char)93;'
                
            if char == "^":
                save = 'std::cout << (char)94;'
                
            if char == "_":
                save = 'std::cout << (char)95;'
                
            if char == "`":
                save = 'std::cout << (char)96;'
                
            if char == "a":
                save = 'std::cout << (char)97;'
                
            if char == "b":
                save = 'std::cout << (char)98;'
                
            if char == "c":
                save = 'std::cout << (char)99;'
                
            if char == "d":
                save = 'std::cout << (char)100;'
                
            if char == "e":
                save = 'std::cout << (char)101;'
                
            if char == "f":
                save = 'std::cout << (char)102;'
                
            if char == "g":
                save = 'std::cout << (char)103;'
                
            if char == "h":
                save = 'std::cout << (char)104;'
                
            if char == "i":
                save = 'std::cout << (char)105;'
                
            if char == "j":
                save = 'std::cout << (char)106;'
                
            if char == "k":
                save = 'std::cout << (char)107;'
                
            if char == "l":
                save = 'std::cout << (char)108;'
                
            if char == "m":
                save = 'std::cout << (char)109;'
                
            if char == "n":
                save = 'std::cout << (char)110;'
                
            if char == "o":
                save = 'std::cout << (char)111;'
                
            if char == "p":
                save = 'std::cout << (char)112;'
                
            if char == "q":
                save = 'std::cout << (char)113;'
                
            if char == "r":
                save = 'std::cout << (char)114;'
                
            if char == "s":
                save = 'std::cout << (char)115;'
                
            if char == "t":
                save = 'std::cout << (char)116;'
                
            if char == "u":
                save = 'std::cout << (char)117;'
                
            if char == "v":
                save = 'std::cout << (char)118;'
                
            if char == "w":
                save = 'std::cout << (char)119;'
                
            if char == "x":
                save = 'std::cout << (char)120;'
                
            if char == "y":
                save = 'std::cout << (char)121;'
                
            if char == "z":
                save = 'std::cout << (char)122;'
                
            if char == "{":
                save = 'std::cout << (char)123;'
                
            if char == "|":
                save = 'std::cout << (char)124;'
                
            if char == "}":
                save = 'std::cout << (char)125;'
                
            if char == "~":
                save = 'std::cout << (char)126;'
                
            if char == "Ç":
                save = 'std::cout << (char)128;'
                
            if char == "ü":
                save = 'std::cout << (char)129;'
                
            if char == "é":
                save = 'std::cout << (char)130;'
                
            if char == "â":
                save = 'std::cout << (char)131;'
                
            if char == "ä":
                save = 'std::cout << (char)132;'
                
            if char == "à":
                save = 'std::cout << (char)133;'
                
            if char == "å":
                save = 'std::cout << (char)134;'
                
            if char == "ç":
                save = 'std::cout << (char)135;'
                
            if char == "ê":
                save = 'std::cout << (char)136;'
                
            if char == "ë":
                save = 'std::cout << (char)137;'
                
            if char == "è":
                save = 'std::cout << (char)138;'
                
            if char == "ï":
                save = 'std::cout << (char)139;'
                
            if char == "î":
                save = 'std::cout << (char)140;'
                
            if char == "ì":
                save = 'std::cout << (char)141;'
                
            if char == "Ä":
                save = 'std::cout << (char)142;'
                
            if char == "Å":
                save = 'std::cout << (char)143;'
                
            if char == "É":
                save = 'std::cout << (char)144;'
                
            if char == "æ":
                save = 'std::cout << (char)145;'
                
            if char == "Æ":
                save = 'std::cout << (char)146;'
                
            if char == "ô":
                save = 'std::cout << (char)147;'
                
            if char == "ö":
                save = 'std::cout << (char)148;'
                
            if char == "ò":
                save = 'std::cout << (char)149;'
                
            if char == "û":
                save = 'std::cout << (char)150;'
                
            if char == "ù":
                save = 'std::cout << (char)151;'
                
            if char == "ÿ":
                save = 'std::cout << (char)152;'
                
            if char == "Ö":
                save = 'std::cout << (char)153;'
                
            if char == "Ü":
                save = 'std::cout << (char)154;'
                
            if char == "ø":
                save = 'std::cout << (char)155;'
                
            if char == "£":
                save = 'std::cout << (char)156;'
                
            if char == "Ø":
                save = 'std::cout << (char)157;'
                
            if char == "×":
                save = 'std::cout << (char)158;'
                
            if char == "ƒ":
                save = 'std::cout << (char)159;'
                
            if char == "á":
                save = 'std::cout << (char)160;'
                
            if char == "í":
                save = 'std::cout << (char)161;'
                
            if char == "ó":
                save = 'std::cout << (char)162;'
                
            if char == "ú":
                save = 'std::cout << (char)163;'
                
            if char == "ñ":
                save = 'std::cout << (char)164;'
                
            if char == "Ñ":
                save = 'std::cout << (char)165;'
                
            if char == "ª":
                save = 'std::cout << (char)166;'
                
            if char == "º":
                save = 'std::cout << (char)167;'
                
            if char == "¿":
                save = 'std::cout << (char)168;'
                
            if char == "®":
                save = 'std::cout << (char)169;'
                
            if char == "¬":
                save = 'std::cout << (char)170;'
                
            if char == "½":
                save = 'std::cout << (char)171;'
                
            if char == "¼":
                save = 'std::cout << (char)172;'
                
            if char == "¡":
                save = 'std::cout << (char)173;'
                
            if char == "«":
                save = 'std::cout << (char)174;'
                
            if char == "»":
                save = 'std::cout << (char)175;'
                
            if char == "░":
                save = 'std::cout << (char)176;'
                
            if char == "▒":
                save = 'std::cout << (char)177;'
                
            if char == "▓":
                save = 'std::cout << (char)178;'
                
            if char == "│":
                save = 'std::cout << (char)179;'
                
            if char == "┤":
                save = 'std::cout << (char)180;'
                
            if char == "Á":
                save = 'std::cout << (char)181;'
                
            if char == "Â":
                save = 'std::cout << (char)182;'
                
            if char == "À":
                save = 'std::cout << (char)183;'
                
            if char == "©":
                save = 'std::cout << (char)184;'
                
            if char == "╣":
                save = 'std::cout << (char)185;'
                
            if char == "║":
                save = 'std::cout << (char)186;'
                
            if char == "╗":
                save = 'std::cout << (char)187;'
                
            if char == "╝":
                save = 'std::cout << (char)188;'
                
            if char == "¢":
                save = 'std::cout << (char)189;'
                
            if char == "¥":
                save = 'std::cout << (char)190;'
                
            if char == "┐":
                save = 'std::cout << (char)191;'
                
            if char == "└":
                save = 'std::cout << (char)192;'
                
            if char == "┴":
                save = 'std::cout << (char)193;'
                
            if char == "┬":
                save = 'std::cout << (char)194;'
                
            if char == "├":
                save = 'std::cout << (char)195;'
                
            if char == "─":
                save = 'std::cout << (char)196;'
                
            if char == "┼":
                save = 'std::cout << (char)197;'
                
            if char == "ã":
                save = 'std::cout << (char)198;'
                
            if char == "Ã":
                save = 'std::cout << (char)199;'
                
            if char == "╚":
                save = 'std::cout << (char)200;'
                
            if char == "╔":
                save = 'std::cout << (char)201;'
                
            if char == "╩":
                save = 'std::cout << (char)202;'
                
            if char == "╦":
                save = 'std::cout << (char)203;'
                
            if char == "╠":
                save = 'std::cout << (char)204;'
                
            if char == "═":
                save = 'std::cout << (char)205;'
                
            if char == "╬":
                save = 'std::cout << (char)206;'
                
            if char == "¤":
                save = 'std::cout << (char)207;'
                
            if char == "ð":
                save = 'std::cout << (char)208;'
                
            if char == "Ð":
                save = 'std::cout << (char)209;'
                
            if char == "Ê":
                save = 'std::cout << (char)210;'
                
            if char == "Ë":
                save = 'std::cout << (char)211;'
                
            if char == "È":
                save = 'std::cout << (char)212;'
                
            if char == "ı":
                save = 'std::cout << (char)213;'
                
            if char == "Í":
                save = 'std::cout << (char)214;'
                
            if char == "Î":
                save = 'std::cout << (char)215;'
                
            if char == "Ï":
                save = 'std::cout << (char)216;'
                
            if char == "┘":
                save = 'std::cout << (char)217;'
                
            if char == "┌":
                save = 'std::cout << (char)218;'
                
            if char == "█":
                save = 'std::cout << (char)219;'
                
            if char == "▄":
                save = 'std::cout << (char)220;'
                
            if char == "¦":
                save = 'std::cout << (char)221;'
                
            if char == "Ì":
                save = 'std::cout << (char)222;'
                
            if char == "▀":
                save = 'std::cout << (char)223;'
                
            if char == "Ó":
                save = 'std::cout << (char)224;'
                
            if char == "ß":
                save = 'std::cout << (char)225;'
                
            if char == "Ô":
                save = 'std::cout << (char)226;'
                
            if char == "Ò":
                save = 'std::cout << (char)227;'
                
            if char == "õ":
                save = 'std::cout << (char)228;'
                
            if char == "Õ":
                save = 'std::cout << (char)229;'
                
            if char == "µ":
                save = 'std::cout << (char)230;'
                
            if char == "þ":
                save = 'std::cout << (char)231;'
                
            if char == "Þ":
                save = 'std::cout << (char)232;'
                
            if char == "Ú":
                save = 'std::cout << (char)233;'
                
            if char == "Û":
                save = 'std::cout << (char)234;'
                
            if char == "Ù":
                save = 'std::cout << (char)235;'
                
            if char == "ý":
                save = 'std::cout << (char)236;'
                
            if char == "Ý":
                save = 'std::cout << (char)237;'
                
            if char == "¯":
                save = 'std::cout << (char)238;'
                
            if char == "´":
                save = 'std::cout << (char)239;'
                
            if char == "≡":
                save = 'std::cout << (char)240;'
                
            if char == "±":
                save = 'std::cout << (char)241;'
                
            if char == "‗":
                save = 'std::cout << (char)242;'
                
            if char == "¾":
                save = 'std::cout << (char)243;'
                
            if char == "¶":
                save = 'std::cout << (char)244;'
                
            if char == "§":
                save = 'std::cout << (char)245;'
                
            if char == "÷":
                save = 'std::cout << (char)246;'
                
            if char == "¸":
                save = 'std::cout << (char)247;'
                
            if char == "°":
                save = 'std::cout << (char)248;'
                
            if char == "¨":
                save = 'std::cout << (char)249;'
                
            if char == "·":
                save = 'std::cout << (char)250;'
                
            if char == "¹":
                save = 'std::cout << (char)251;'
                
            if char == "³":
                save = 'std::cout << (char)252;'
                
            if char == "²":
                save = 'std::cout << (char)253;'
                
            if char == "■":
                save = 'std::cout << (char)254;'
                
            if char == "nbsp":
                save = 'std::cout << (char)255;'
                



#the end
            elif char == "\n":
                save = 'std::cout << "" << endl;'
                
            with open("code.txt", "a+", encoding="utf-8") as file_object:
                        file_object.seek(0)
                        data = file_object.read(100)
                        if len(data) > 0 :
                            file_object.write("\n")
                        file_object.write(save)
print("Data Saved\n")
