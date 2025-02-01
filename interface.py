class Text:
    """Contains only constants of ANSI color codes."""
    RED: str = "\033[91m"
    LIGHT_RED: str = "\033[1;31m"
    YELLOW: str = "\033[93m"
    DARK_YELLOW: str = "\033[0;33m"
    BLUE: str = "\033[94m"
    LIGHT_BLUE: str = "\033[1;34m"
    CYAN: str = "\033[96m"
    GREEN: str = "\033[92m"
    LIGHT_WHITE: str = "\033[1;37m"

    BOLD: str = "\033[1m"
    ITALIC: str = "\033[3m"
    UNDERLINE: str = "\033[4m"
    CROSSED: str = "\033[9m"
    BLINK: str = "\033[5m"
    NEGATIVE: str = "\033[7m"
    SPACE: str = "\033c"
    END: str = "\033[0m"


class Interface:
    """Contains only constants of texts."""
    DIALOG_SEPARATOR: str = f"{Text.CROSSED}                                                            {Text.END}"
    INTERFACE_SEPARATOR: str = f"{Text.NEGATIVE}{Text.LIGHT_RED}/===============================================================================\\{Text.END}"
    EMPTY_CHARACTER: str = "✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕✕"
    LOGO: str = f"""{Text.BOLD}{Text.RED}
                                              @@@            @@@          @@     
                                            @@   @@        @@@@       @@@ @@@   
    @@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@ @@@          @@@@         @@@      
    @@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@@@@@@@    
    @@@@         @@@@                      @@@           @@@@@@@@@@@@@@@@@@@@    
    @@@@         @@@@                     @@@@          @@@@@      @@@@          
    @@@@         @@@@                    @@@@          @@@@@       @@@@          
    @@@@         @@@@                   @@@@@         @@@@        @@@@           
    @@@@         @@@@                  @@@@@            @        @@@@            
    @@@@         @@@@                @@@@@                      @@@@             
    @@@@@@@@@@@@@@@@@            @@@@@@@                      @@@@@              
    @@@@@@@@@@@@@@@@@         @@@@@@@@                       @@@@@               
    @@@@         @@@@         @@@                          @@@@                 



                           @@            @@@                                    
                         @@ @@           @@                   @@@               
                           @            @@                 @   @@               
                @@     @@               @@@@               @@  @                
               @@@      @@             @@ @@@@           @@   @@      @         
             @@@        @@@           @@    @@          @@   @@    @@           
           @@            @            @@               @     @@@@@              
         @                           @@              @      @@@                 
                                    @@                                          
    {Text.END}"""
