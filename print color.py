text_colors = {'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purple':35,'cyan':36,'white':37}
bg_colors = {'black':40,'red':41,'green':42,'yellow':44,'blue':44,'purple':45,'cyan':46,'white':47}
styles = {'normal':0,'bold':1,'light':2,'italic':3}

def give_output(fg,bg,style):
    print(f'print("\\033[{styles[style]};{text_colors[fg]};{bg_colors[bg]}m Your text here")')
    
#fg color
fg = 30    
for x,y in text_colors.items():
    print(x)
    if x == "white":
        fg = input("\nwhich fg color? ")
      
#bg color
bg = 40    
for x,y in bg_colors.items():
    print(x)
    if x == "white":
        bg = input("\nwhich bg color? ")
        
#style
style = 0  
for x,y in styles.items():
    print(x)
    if x == "italic":
        style = input("\nwhich style? ")
        
try:
    give_output(fg,bg,style)
except:
    print("\n An error has occured, you may have given an invalid input")
        
    
