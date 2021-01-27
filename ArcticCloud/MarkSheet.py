BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def Grader(score : int) -> str:
    if score >= 91:
        return "A+"
    if score >= 81 and score <= 90:
        return "A"
    if score >= 71 and score <= 80:
        return "B+"
    if score >= 61 and score <= 70:
        return "B"
    if score >= 51 and score <= 60:
        return "C"
    if score >= 41 and score <= 50:
        return "D"
    if score >= 31 and score <= 40:
        return "E"
    if score <= 30:
        return "Fail"


def banner_text(text : str , screen_width : int = 80, *args : str, orient : str = "center", border : str = " " ) -> None:
    if len(text) > (screen_width - 4):
        raise ValueError (f"String {text} is larger than specified width {screen_width}")
    if text == "=":
        color_effects = "".join(args)
        print(f"{color_effects}""=" * screen_width, f"{RESET}")
    else:
        if orient == "left":
            left_text = text.ljust(screen_width-4," ")
            color_effects = "".join(args)
            print(f"={color_effects} {left_text} {RESET}=")
            
        if orient == "right":
            right_text = text.rjust(screen_width-4," ")
            color_effects = "".join(args)
            print(f"={color_effects} {right_text} {RESET}=")
            
        if orient == "center":
            centered_text = text.center(screen_width-4, " ")
            color_effects = "".join(args)
            print(f"={color_effects} {centered_text} {RESET}=")


def PrintMarksheet(SchoolName : str, marks : list, data : list):
    list_container = marks

    sum = 0
    for val in list_container:
        num = int(val)
        sum = sum + num

    percent = (sum/600)*100
    x = Grader(percent)
    banner_text("=",80, RED, BOLD)
    banner_text(" ",80,border=RED)
    banner_text(f"{SchoolName}",80, CYAN, BOLD, border = RED)
    banner_text("REPORT CARD", 80, RED, BOLD, border = RED)
    banner_text(" ", 80)
    banner_text("=", 80, RED, BOLD)
    banner_text(f"NAME : {data[0]}                                              CLASS : XI", 80,YELLOW, orient ="left")
    banner_text(f"ROLL NO : {data[2]}                                                       SEC   : {data[1]}", 80,YELLOW, orient = "left")
    banner_text(" ",80)
    banner_text("------------------------------------",80, MAGENTA, BOLD)
    banner_text(" ", 80)
    banner_text("SUBJECTWISE MARKS", 80, CYAN)
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(f"English:         {list_container[0]}", 80,MAGENTA,BOLD, orient = "left")
    banner_text(f"Bengali:         {list_container[1]}", 80,MAGENTA,BOLD, orient = "left")
    banner_text(f"Physics:         {list_container[2]}", 80,MAGENTA,BOLD, orient = "left")
    banner_text(f"Chemistry:       {list_container[3]}", 80,MAGENTA,BOLD, orient = "left")
    banner_text(f"Biology:         {list_container[4]}", 80,MAGENTA,BOLD, orient = "left")
    banner_text(f"Computer:        {list_container[5]}", 80,MAGENTA,BOLD, orient = "left")
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text(f"The Total Marks is {sum}.", 80, BLUE, BOLD, orient = "center")
    if x == "Fail":
        banner_text(f"We are Sorry!, the Student has Failed.", 80, BLUE, BOLD, orient = "center")
    else:
        banner_text(f"The Grade Obtained is {x}", 80, BLUE, BOLD, orient = "center")
    banner_text(" ", 80)
    banner_text(" ", 80)
    banner_text("=", 80, RED, BOLD)
    
    
    
    
    
# if __name__ == "__main__":
#     main()